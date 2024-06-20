import threading
import time

from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException

from settings import WAGO_VERBOSE
from utils.logger import logger


class WagoController(threading.Thread):

    def __init__(self, host=None, port=502, timeout=1000, verbose=WAGO_VERBOSE):
        super().__init__()
        self._client = None
        self.host = host
        self.port = port
        self.timeout = timeout
        self.verbose = verbose
        self._b_stop = threading.Event()
        self._b_stop.clear()
        self._lock = threading.Lock()
        self.in_values = None
        self.out_values = None
        self.connected = False

    def set_host(self, host):
        self.host = host

    def connect(self):
        try:
            self._client = ModbusTcpClient(host=self.host, port=self.port, timeout=self.timeout)
            time.sleep(1)   # Adding this seems to have stopped wago from occasionally returning old values
            result = self._client.connect()
            time.sleep(1)
            if result:
                logger.info(f"Wago: Connected to the modbus server({self.host}), result: {result}")
            self.connected = result
            return result
        except Exception as e:
            logger.error(f"Wago: Failed to connect to the coupler - {e}")
            self._client = None
            self.connected = False

    def run(self) -> None:
        while not self._b_stop.is_set():
            self.in_values = self.read_coils(address=0, count=32)
            time.sleep(.001)
            self.out_values = self.read_coils(address=0x200, count=24)
            time.sleep(.001)

    def read_holding_registers(self, address, count=1, unit=1):
        if self._client is not None or self.connect():
            with self._lock:
                try:
                    r = self._client.read_holding_registers(address=address, count=count, unit=unit)
                except Exception as e:
                    logger.error(f"Wago: Failed to read holding registers - {e}")
                    self._client = None
                    r = None
            if not isinstance(r, ModbusException) and r is not None:
                if self.verbose:
                    logger.debug(
                        f"Wago: Read holding registers from {address} to {address + count}, result: {r.registers}")
                return r.registers
            else:
                logger.error(f"Wago: Failed to read holding registers - {r}")

    def write_register(self, address, data):
        if self._client is not None or self.connect():
            with self._lock:
                try:
                    r = self._client.write_register(address, data)
                except Exception as e:
                    logger.error(f"Wago: Failed to write register - {e}")
                    self._client = None
                    r = None
            if not isinstance(r, ModbusException) and r is not None:
                if self.verbose:
                    logger.debug(f"Wago: Wrote {data} to register {address}, result: {not r.isError()}")
                return not r.isError()
            else:
                logger.error(f"Wago: Failed to write holding register - {r}")

    def read_coils(self, address, count):
        if self._client is not None or self.connect():
            with self._lock:
                try:
                    r = self._client.read_coils(address=address, count=count)
                except Exception as e:
                    logger.error(f"Wago: Failed to read coils - {e}")
                    self._client = None
                    r = None
            if not isinstance(r, ModbusException) and r is not None:
                if self.verbose:
                    logger.debug(f"Wago: Read coils from {address} to {address + count}, result: {r.bits}")
                return r.bits
            else:
                logger.error(f"Wago: Failed to read coils - {r}")

    def write_coil(self, address, value):
        if self._client is not None or self.connect():
            with self._lock:
                try:
                    r = self._client.write_coil(address, value)
                except Exception as e:
                    logger.error(f"Wago: Failed to write coil - {e}")
                    self._client = None
                    r = None
            if not isinstance(r, ModbusException) and r is not None:
                if self.verbose:
                    logger.debug(f"Wago: Wrote {value} to coil {address}, result: {not r.isError()}")
                return not r.isError()
            else:
                logger.error(f"Wago: Failed to write coil - {r}")

    def write_coils(self, address, values):
        if self._client is not None or self.connect():
            with self._lock:
                try:
                    r = self._client.write_coils(address, values)
                except Exception as e:
                    logger.error(f"Wago: Failed to write coils - {e}")
                    self._client = None
                    r = None
            if not isinstance(r, ModbusException) and r is not None:
                if self.verbose:
                    logger.debug(f"Wago: Wrote {values} to coil starting from {address}, result: {not r.isError()}")
                return not r.isError()
            else:
                logger.error(f"Wago: Failed to write coils - {r}")

    def read_input(self, channel):
        if self.in_values is not None:
            return self.in_values[channel - 1]

    def read_output(self, channel):
        if self.out_values is not None:
            return self.out_values[channel - 1]

    def write_output(self, channel, val):
        self.write_coil(address=channel - 1, value=1 if val else 0)

    def close(self, close=True):
        self._b_stop.set()
        if self._client is not None and close:
            logger.debug("Closing Wago Client...")
            self._client.close()
            self._client = None
