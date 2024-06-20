import threading

from utils.common import change_bit_of_byte
from utils.i765dnm.i765dnm import *
from utils.logger import logger


class I765DNMValveController:

    def __init__(self):
        self._port = None
        self._connected = False
        self._lock = threading.Lock()
        self._bit_lock = threading.Lock()

    def connect(self):
        ports = scan_available_ports()
        if not ports:
            logger.warning("I765DNM: No Device Found!")
            self._port = None
            return False
        else:
            self._port = ports[0]
            logger.debug(f"I765DNM: Found device at COM{self._port}, trying to activate...")
            try:
                self._connected, msg = activate_module(self._port)
                logger.debug(f"I765DNM: activation result - {self._connected}")
                return self._connected
            except Exception as e:
                logger.error(f"Failed to activate I765DNM: {e}")
                return False

    def is_connected(self):
        return self._connected

    def activate(self):
        if self._port is not None or self.connect():
            return activate_module(self._port)

    def get_information(self):
        if self._port is not None or self.connect():
            return {
                "port": f"COM{self._port}",
                "DLL Version": get_dll_version(),
                "Firmware Version": get_firmware_version(self._port),
                "Baudrate": get_baudrate(self._port),
                "Master MAC ID": get_master_mac_id(self._port),
                "Master status": get_master_status(self._port)[1]
            }

    def start_slave_device(self, slave_id):
        r, msg = start_slave_device(port=self._port, slave_id=slave_id)
        if r:
            logger.debug(f"I765DNM: Started slave device({slave_id}), status: {get_slave_status(self._port, slave_id)}")
        else:
            logger.error(f"I765DNM: Failed to start slave device - {msg}")
        return r, msg

    def read_data(self, slave_id):
        data = None
        with self._lock:
            if self._port is not None or self.connect():
                try:
                    data = read_output_data(port=self._port, slave_id=slave_id)
                except Exception as e:
                    logger.error(f"Failed to read data from valve! - {e}")
                    self._connected = False
                    self._port = None
        if data is not None:
            return bytearray([data[1], data[0]])

    def write_bit(self, slave_id, pos: int, val):
        with self._bit_lock:
            logger.debug(f"Trying to write bit({val}) to position({pos}) of {slave_id}")
            data = self.read_data(slave_id=slave_id)
            if data is not None:
                logger.debug(f"Reading bits from {slave_id}: {bin(int(data.hex(), 16))}")
                if pos < 9:
                    data = bytearray([data[0], change_bit_of_byte(data[1], pos - 1, val)])
                else:
                    data = bytearray([change_bit_of_byte(data[0], pos - 9, val), data[1]])
                self.write_data(slave_id=slave_id, data=bytearray([data[1], data[0]]))
                logger.debug(f"writing bits: {bin(int(data.hex(), 16))}")
            if data is None:
                logger.error(f"Valve: Failed to write bit({val}) to ({pos}), slave_id: {slave_id}")
        return data is not None

    def write_data(self, slave_id, data: bytearray):
        try:
            with self._lock:
                reply = write_output_data(port=self._port, slave_id=slave_id, con_type=1, data=data)
            return reply
        except Exception as e:
            logger.error(f"Failed to write data({data}) to slave device({slave_id}) - {e}")

    def reset_device(self):
        return reset_firmware(port=self._port)

    def stop_slave_device(self, slave_id):
        try:
            return stop_slave_device(port=self._port, slave_id=slave_id)
        except Exception as e:
            logger.error(f"Failed to stop slave device - {e}")

    def close(self, close=True):
        if close:
            close_module(self._port)
        self._port = None
        self._connected = False


if __name__ == '__main__':

    _valve = I765DNMValveController()
    print(_valve.get_information())
    cnt = 0
    while True:
        try:
            # buf = bytearray([0x10, 0x00])
            # v.write_data(1, buf)
            # v.write_bit(1, 5, True)
            print(_valve.read_data(1))
            time.sleep(1)
            cnt += 1
            # buf = bytearray([0x00, 0x00])
            # v.write_data(1, buf)
            # v.write_bit(1, 5, False)
            print(cnt, _valve.read_data(1))
            # time.sleep(1)
        except KeyboardInterrupt:
            break
    # v.stop_slave_device(2)
    _valve.close()
