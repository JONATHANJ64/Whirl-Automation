import struct
import threading
import time

from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
from utils.logger import logger


# Control registers of the vision controller
VISION_ENABLE_EXTERNAL_TRIGGER = 0
VISION_TRIGGER = 1
VISION_BUFFER_RESULTS_ENABLE = 2
VISION_INSPECTION_RESULTS_ACK = 3
VISION_EXECUTE_COMMAND = 4
VISION_SET_OFFLINE = 7
VISION_CLEAR_ERROR = 18
SOFT_EVENT_0 = 24           # Event action set in cognex spreadsheet, used to clear old values from results buffer

# Control registers of the barcode reader


class CognexBase:

    def __init__(self, host=None, port=502, timeout=300, keep_alive=15):
        super().__init__()
        self._client = None
        self.host = host
        self.port = port
        self.timeout = timeout
        self.keep_alive = keep_alive
        self._last_read_time = 0
        self._lock = threading.Lock()
        self._connected = False

    def connect(self, init=True):
        pass

    def is_connected(self):
        return self._connected

    def close(self):
        if self._client is not None:
            self._client.close()
        self._client = None


class CognexVisionController(CognexBase):

    """
    https://support.cognex.com/docs/is_574/web/EN/ise/Content/Communications_Reference/ModbusTCP_5x.htm
    """

    def connect(self, init=True):
        try:
            self._client = ModbusTcpClient(host=self.host, port=self.port, timeout=self.timeout)
            result = self._client.connect()
            if result:
                logger.debug(f"Cognex: Connected to the server({self.host}), result: {result}")
                self.clear_offline()
                if init:
                    return self._init_vision_sensor()
                else:
                    self._connected = True
                    return True
        except Exception as e:
            logger.error(f"Cognex: Failed to connect to the server - {e}")
            self._client = None

    def _init_vision_sensor(self):
        """
        - Check `Online`                            Status Byte 0, bit 7
        - Set `Execute Command`                     Byte 0, bit 4
        - Set `Trigger Enable`                      Byte 0, bit 0
        - Set `Buffer Results Enable`               Byte 0, bit 2
        """
        if not self.is_online():
            logger.error("Cognex is offline!")
            return False

        # Execute command
        self._client.write_coil(address=VISION_EXECUTE_COMMAND, value=True)
        # Enable external trigger
        self._client.write_coil(address=VISION_ENABLE_EXTERNAL_TRIGGER, value=True)
        # Set Buffer Results Enable
        self._client.write_coil(address=VISION_BUFFER_RESULTS_ENABLE, value=True)
        self._connected = True
        return True

    def set_offline(self):
        logger.debug(f"Setting Cognex at {self.host} offline...")
        self._client.write_coil(VISION_SET_OFFLINE, True)
        while self.is_online() is True:
            time.sleep(0.05)

    def clear_offline(self):
        logger.debug(f"Setting Cognex at {self.host} online...")
        self._client.write_coil(VISION_SET_OFFLINE, False)
        while self.is_online() is False:
            time.sleep(0.05)

    def is_result_valid(self):
        di = self._client.read_discrete_inputs(address=0, count=24)
        if not isinstance(di, ModbusException):
            return di.bits[11]

    def is_online(self):
        di = self._client.read_discrete_inputs(address=0, count=8)
        if not isinstance(di, ModbusException):
            return di.bits[7]

    def read_data(self, reg_count=32):
        """
        - Check `Trigger Ready`                     Status Byte 0, bit 0
        - Unset `Inspection Results Ack`            Byte 0, bit 3
        - Set `Trigger`                             Byte 0, bit 1
        - Check `Trigger Ack`                       Status Byte 0, bit 1
        - Check `Results Valid`                     Status Byte 1, bit 3
        - Read holding register
        - Set `Inspection Results Ack`              Byte 0, bit 3
        - Unset `Trigger`                           Byte 0, bit 1
        """
        if self._client is None:
            return
        elif time.time() - self._last_read_time > self.keep_alive:
            # Close and open the connection again.
            self.close()
            if not self.connect(init=False):
                return

        # trigger_ready = self._client.read_discrete_inputs(address=0, count=8)
        # if isinstance(trigger_ready, ModbusException) or not trigger_ready.bits[0]:
        #     logger.error(f"Cognex: Not ready for the trigger! - {trigger_ready}")
        #     return

        self._client.write_coil(VISION_INSPECTION_RESULTS_ACK, False)

        s_time = time.time()
        # pop previous results from the buffer
        while self.is_result_valid():
            self._client.write_coil(VISION_INSPECTION_RESULTS_ACK, True)
            time.sleep(.01)
            self._client.write_coil(VISION_INSPECTION_RESULTS_ACK, False)
            time.sleep(.01)
            if time.time() - s_time > 3:
                logger.error("Cognex: Failed to pop previous results! Timeout!")
                break

        self._client.write_coil(VISION_TRIGGER, True)
        s_time = time.time()
        result_valid = False
        while True:
            di = self._client.read_discrete_inputs(8, 8)
            if not isinstance(di, ModbusException):
                result_valid = di.bits[3]
            if result_valid:
                break
            elif time.time() - s_time > 5:
                logger.error("No result valid after 5 sec! giving up...")
                break
            else:
                time.sleep(.025)

        r = None
        if result_valid:
            hr = self._client.read_holding_registers(address=7005, count=reg_count, unit=2)
            if not isinstance(hr, ModbusException):
                r = hr.registers
        self._client.write_coil(VISION_INSPECTION_RESULTS_ACK, True)
        self._client.write_coil(VISION_TRIGGER, False)
        self._last_read_time = time.time()
        return r

    def read_position_data(self, index, check_reversed=False, r_offset=4):
        with self._lock:
            values = self.read_data(reg_count=64 if check_reversed else 32)
        if values is not None:
            b_val = [v.to_bytes(2, 'big') for v in values]
            x = round(struct.unpack('!f', b''.join([b_val[6 * index + 1], b_val[6 * index]]))[0], 1)
            y = round(struct.unpack('!f', b''.join([b_val[6 * index + 3], b_val[6 * index + 2]]))[0], 1)
            z = round(struct.unpack('!f', b''.join([b_val[6 * index + 5], b_val[6 * index + 4]]))[0], 1)
            if check_reversed and (x == 9999.0 or y == 9999.0 or z == 9999.0):
                logger.debug(f"Cognex: Trying to read reversed ones")
                index += r_offset
                x = round(struct.unpack('!f', b''.join([b_val[6 * index + 1], b_val[6 * index]]))[0], 1)
                y = round(struct.unpack('!f', b''.join([b_val[6 * index + 3], b_val[6 * index + 2]]))[0], 1)
                z = round(struct.unpack('!f', b''.join([b_val[6 * index + 5], b_val[6 * index + 4]]))[0], 1)
                return x, y, z, True
            return x, y, z

    def clear_results_buffer(self):
        with self._lock:
            if self._client is None:
                return
            elif time.time() - self._last_read_time > self.keep_alive:
                # Close and open the connection again.
                self.close()
                if not self.connect(init=False):
                    return
            self._client.write_coil(address=SOFT_EVENT_0, value=True)
            while self._client.read_coils(24).bits[0] is False:         # Waiting for soft event ack.
                time.sleep(.001)
            self._client.write_coil(address=SOFT_EVENT_0, value=False)
            while self._client.read_coils(24).bits[0]:
                time.sleep(.001)

    def clear_error(self):
        self._client.write_coil(address=VISION_CLEAR_ERROR, value=True)
        while int(self._client.read_holding_registers(7000, 2).registers[1]) != 0:
            time.sleep(0.05)
        self._client.write_coil(address=VISION_CLEAR_ERROR, value=False)
        return True

    def job_change(self, job_id: int):
        with self._lock:
            if self._client is None:
                return
            elif time.time() - self._last_read_time > self.keep_alive:
                # Close and open the connection again.
                self.close()
                if not self.connect(init=False):
                    return
            self.set_offline()
            self._client.write_registers(2000, values=[job_id, 0])
            while int(self._client.read_holding_registers(2000, 1).registers[0]) != job_id:
                time.sleep(0.05)
            self.clear_error()                               # clear any current errors from initial job load
            self._client.write_coil(address=VISION_EXECUTE_COMMAND, value=False)  # make sure execute is not already on
            time.sleep(.1)
            logger.debug(f"Changing job to program {job_id}...")
            self._client.write_coil(address=VISION_EXECUTE_COMMAND, value=True)
            while int(self._client.read_holding_registers(7000, 1).registers[0]) != job_id:
                time.sleep(0.5)
            self._client.write_coil(address=VISION_EXECUTE_COMMAND, value=False)
            time.sleep(0.1)
            self.clear_offline()
            logger.debug("Job change complete")
            return True


CODE_TRIGGER_ENABLE = 0
CODE_TRIGGER = 1
CODE_BUFFER_RESULT_ENABLE = 2
CODE_RESULTS_ACK = 3
CODE_TRIGGER_READY = 0
CODE_TRIGGER_ACK = 1
CODE_DECODE_COMPLETE = 9
CODE_RESULT_BUFFER_OVERRUN = 10
CODE_RESULT_AVAIL = 11


class CognexBarcodeReader(CognexBase):
    """
    https://support.cognex.com/docs/dmst_616SR2/web/EN/Industrial_Protocols_Manual/Content/Topics/PDF/DMCAP/ModbusTCP.htm
    """

    def __init__(self, host=None, port=502, timeout=300, keep_alive=3500):
        super().__init__(host, port, timeout, keep_alive)
        self._track_id = None

    def connect(self, init=True):
        try:
            self._client = ModbusTcpClient(host=self.host, port=self.port, timeout=self.timeout)
            result = self._client.connect()
            if result:
                logger.debug(f"Cognex: Connected to the server({self.host}), result: {result}")
                if init:
                    self._client.write_coil(CODE_BUFFER_RESULT_ENABLE, True)
                    self._client.write_coil(CODE_TRIGGER_ENABLE, True)
                self._connected = True
                return True
        except Exception as e:
            logger.error(f"Cognex: Failed to connect to the cognex barcode server - {e}")
            self._client = None

    def read(self):
        if self._client is None and not self.connect():
            return
        elif time.time() - self._last_read_time > self.keep_alive:
            # Close and open the connection again.
            self.close()
            if not self.connect(init=False):
                return
        # Wait for TriggerReady status from the reader
        if not self._wait_for_status(pin=CODE_TRIGGER_READY, name="TriggerReady"):
            logger.error("Barcode reader - TriggerReady is not available")
            return ''

        self._client.write_coil(CODE_TRIGGER, True)

        if not self._wait_for_status(pin=CODE_TRIGGER_ACK, name="TriggerAck"):
            logger.error("Barcode reader - TriggerAck is not available")
            return ''
        self._client.write_coil(CODE_TRIGGER, False)

        if not self._wait_for_status(pin=CODE_DECODE_COMPLETE, name="DecodeComplete", timeout=3):
            logger.error("Barcode reader - DecodeComplete is not available")
            return ''

        r = ""
        di_status = self._client.read_discrete_inputs(0, 32)
        if hasattr(di_status, 'bits'):
            if di_status.bits[CODE_RESULT_BUFFER_OVERRUN]:
                logger.warning("Barcode buffer overrun!")
            elif di_status.bits[CODE_RESULT_AVAIL]:
                hr = self._client.read_input_registers(address=2000, count=64, unit=2)
                if not isinstance(hr, ModbusException):
                    bits = hr.registers
                    if self._track_id is None:
                        self._track_id = bits[1]
                    elif bits[2] == self._track_id:
                        length = bits[4]
                        for i in range(length // 2 + 1):
                            r += chr(bits[5 + i] % 256)
                            r += chr(bits[5 + i] // 256)
                        r = r[:length]
                        self._track_id = bits[1]
        else:
            logger.warning("Decoded, but no result available")

        self._client.write_coil(CODE_RESULTS_ACK, True)
        time.sleep(.05)
        self._client.write_coil(CODE_RESULTS_ACK, False)
        self._last_read_time = time.time()

        return r

    def read_barcode(self):
        s_time = time.time()
        while time.time() - s_time < 1.5:
            c = self.read()
            time.sleep(.01)
            if c:
                return c
        return ''

    def _wait_for_status(self, pin=0, timeout=2, name=""):
        # Wait for TriggerReady status from the reader
        s_time = time.time()
        while True:
            try:
                di = self._client.read_discrete_inputs(0, 32)
            except Exception as e:
                logger.error(f"Failed to read DI - {e}")
                return
            if not isinstance(di, ModbusException):
                if di.bits[pin]:
                    return True
            if time.time() - s_time > timeout:
                logger.error(f"{name} is not set, giving up...")
                if hasattr(di, 'bits'):
                    logger.error(f"Status - {di.bits}")
                return False
            time.sleep(.01)


if __name__ == '__main__':

    # c = CognexVisionController(host='192.168.1.235')
    # c.connect()
    #
    # while True:
    #     try:
    #         val = c.read_data(reg_count=16)
    #         if val:
    #             print(["%02X" % v for v in val])
    #         time.sleep(1)
    #     except KeyboardInterrupt:
    #         break
    #
    # c.close()

    b = CognexBarcodeReader(host='192.168.100.17')
    b.connect()

    while True:
        try:
            _s_time = time.time()
            code = b.read_barcode()
            if code:
                print(f"Read `{code}`, elapsed: {time.time() - _s_time}")
        except KeyboardInterrupt:
            break
    b.close()
