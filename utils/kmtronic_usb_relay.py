"""

Turn ON:        FF 01 01
Turn OFF:       FF 01 00
Status:         FF 01 03         00: OFF, 01: ON

"""
import serial.tools.list_ports

from settings import KMTRONIC_USB_VID, KMTRONIC_USB_PID
from utils.logger import logger


class KMTronicUSBRelay(object):

    def __init__(self):
        self._ser = None

    def open(self):
        for c in serial.tools.list_ports.comports():
            if c.vid == KMTRONIC_USB_VID and c.pid == KMTRONIC_USB_PID:
                print(f"Found a relay adapter - {c.device} - {c.description}")
                try:
                    self._ser = serial.Serial(port=c.device, timeout=1)
                    return True
                except Exception as e:
                    logger.error(f"Failed to open the relay - {e}")

    def get_status(self):
        if self._ser is not None or self.open():
            try:
                self._ser.write(b'\xFF\x01\x03')
                r = self._ser.readline()
                return r == b'\xFF\x01\x01'
            except Exception as e:
                logger.error(f"KMTronic Relay: Failed to get status - {e}")
                self._ser = None

    def turn_relay(self, val):
        if self._ser is not None or self.open():
            logger.info(f"KMTronic Relay: Turning Main Power {'ON' if val else 'OFF'}")
            try:
                written = self._ser.write(b'\xFF\x01\x01' if val else b'\xFF\x01\x00')
                return written == 3
            except Exception as e:
                logger.error(f"KMTronic Relay: Failed to turn relay on/off - {e}")
                self._ser = None

    def close(self):
        if self._ser is not None:
            self._ser.close()
            self._ser = None


if __name__ == '__main__':

    import time

    _relay = KMTronicUSBRelay()
    print(_relay.open())

    print("Status: ", _relay.get_status())
    print("Turning ON: ", _relay.turn_relay(True))
    time.sleep(2)
    print("Turning OFF: ", _relay.turn_relay(False))
