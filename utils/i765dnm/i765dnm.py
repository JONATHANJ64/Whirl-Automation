"""
    Python wrapper of the I-7565-DNM DeviceNet-USB Converter.

    https://www.icpdas-usa.com/i_7565_dnm.html

"""

import ctypes
import os
import sys
import time
from ctypes import *
from ctypes import wintypes
import serial.tools.list_ports

from utils.i765dnm.error_code import ERROR_CODE

_cur_dir = os.path.dirname(os.path.realpath(__file__))
lib = cdll.LoadLibrary(os.path.join(_cur_dir, 'I7565DNM.dll'))


def parse_result(code: wintypes.DWORD) -> tuple:
    """
    Parse the return code from I765-DNM module.
    :param code:
    :return:
    """
    if code == 0:
        return True, None
    else:
        msg = ERROR_CODE.get(code, {})
        return False, f"{msg.get('name', 'Unknown')}({msg.get('description', '')})"


def get_dll_version() -> wintypes.DWORD:
    """
    Obtain the version information of I7565DNM.DLL.
    :return: For example: If 100(hex) is return, it means DLL version is 1.00.
             If 123(hex) is return, it means DLL version is 1.23.
    """
    return lib.I7565DNM_GetDLLVersion()


def scan_available_ports() -> list:
    """
    Scan available COM ports
    :return: List of COM port numbers
    """
    ports = serial.tools.list_ports.comports()
    return [int(p.name[3:]) for p in ports if 'I-756x' in p.description]


def get_firmware_version(port: int) -> wintypes.DWORD:
    """
    Obtain the version information of the firmware inside the I-7565-DNM module.
    :param port:
    :return: For example: If 100(hex) is return, it means DLL version is 1.00.
             If 123(hex) is return, it means DLL version is 1.23.
    """
    return lib.I7565DNM_GetFirmwareVersion(port)


def reset_firmware(port: int) -> tuple:
    """
    Reset the I-7565-DNM firmware.
    When users have changed the baud rate of CAN bus or changed the Master’s MAC ID,  function must be called
    to make change enable.
    After calling this function, users should wait for 1 or 2 seconds to make firmware boot up completely.
    :param port:
    :return:
    """
    return parse_result(lib.I7565DNM_ResetFirmware(port))


def activate_module(port: int) -> tuple:
    """
    Activate I-7565-DNM module.
    It must be called once before using the other functions of I-7565-DNM APIs.
    :param port:
    :return:
    """
    return parse_result(lib.I7565DNM_ActiveModule(port))


def clear_config(port: int) -> tuple:
    """
    Clear all configurations in EEPROM of the I-7565-DNM.
    :param port:
    :return:
    """
    return parse_result(lib.I7565DNM_ClearAllConfig(port))


def get_master_mac_id(port: int) -> wintypes.DWORD:
    """
    Get MAC ID of the DeviceNet master (I-7565-DNM).
    :param port:
    :return:
    """
    return lib.I7565DNM_GetMasterMACID(port)


def set_master_mac_id(port: int, mac_id: c_byte) -> tuple:
    """
    Set MAC ID of the DeviceNet master (I-7565-DNM).
    After calling this function, users must call reset_firmware() to make change enabled.
    It will save the information in EEPROM of the I-7565-DNM.
    :param port:
    :param mac_id: New MAC ID of the master. (0 ~ 63)
    :return:
    """
    return parse_result(lib.I7565DNM_SetMasterMACID(port, mac_id))


def get_master_status(port: int) -> tuple:
    """
    Obtain the firmware status inside the I-7565-DNM.
    Users can call this function to make sure that the DeviceNet master is online successfully.
    :param port:
    :return:
    """
    return parse_result(lib.I7565DNM_GetMasterStatus(port))


def get_baudrate(port: int):
    """
    Get DeviceNet baud rate information of I-7565-DNM.
    :param port:
    :return: baud rate in Kbps
    """
    val = lib.I7565DNM_GetBaudRate(port)
    return {0: 125, 1: 250, 2: 500}.get(val)


def set_baudrate(port: int, baudrate: int) -> tuple:
    """
    Set DeviceNet baud rate of the I-7565-DNM.
    After calling this function, you must call reset_firmware() to reset the firmware to make change enabled.
    :param port:
    :param baudrate: 125, 250, 500
    :return:
    """
    val = {125: 0, 250: 1, 500: 2}[baudrate]
    return parse_result(lib.I7565DNM_SetBaudRate(port, val))


def get_slave_status(port: int, slave_id: int) -> tuple:
    """
    Get remote slave device’s communication status.
    :param port:
    :param slave_id: Remote slave’s MAC ID. (0~63)
    :return:
    """
    return parse_result(lib.I7565DNM_GetSlaveStatus(port, slave_id))


def add_slave_device(port: int, slave_id: int) -> tuple:
    """
    Add slave devices into the ScanList of the I-7565-DNM and save information into the EEPROM.
    Before communicating with any slave devices, users should call this function to add these devices.
    Explicit_EPR(The Expected Packet Rate) value is set as 2500.
    :param port:
    :param slave_id: Remote slave device’s MAC ID (0~63)
    :return:
    """
    return parse_result(lib.I7565DNM_AddDevice(port, slave_id, 2500))


def remove_slave_device(port: int, slave_id: int) -> tuple:
    """
    Remove the specified slave device from the ScanList in the I-7565-DNM.
    And information of the device in EEPROM is erased at the same time.
    :param port:
    :param slave_id: Remote slave device’s MAC ID (0~63)
    :return:
    """
    return parse_result(lib.I7565DNM_RemoveDevice(port, slave_id))


def start_slave_device(port: int, slave_id: int) -> tuple:
    """
    Start communication with the specific device that users applying to.
    :param port:
    :param slave_id: Remote slave’s MAC ID. (0~63)
    :return:
    """
    return parse_result(lib.I7565DNM_StartDevice(port, slave_id))


def add_slave_io_connection(port: int, slave_id: int, con_type: int,
                            input_len: int, output_len: int, epr: int) -> tuple:
    """
    Configure the I/O connection of the specific MAC ID device.
    I-7565-DNM can get/set the data via connection, which connects to the specific slave,
    according to the produced / consumed connection path of this slave device.
    This configuration data will be saved into EEPROM within the I-7565-DNM.
    :param port:
    :param slave_id: Remote slave device’s MAC ID (0~63)
    :param con_type: Remote slave device’s I/O connection type
                     1 : Poll connection type
                     2 : Bit-Strobe connection type
                     3 : COS connection type
                     4 : Cyclic connection type
    :param input_len: Remote slave device’s input length. (Byte)
    :param output_len: Remote slave device’s output length. (Byte)
    :param epr: Expected packet rate. (mSec)
    :return:
    """
    return parse_result(lib.I7565DNM_AddIOConnection(port, slave_id, con_type, input_len, output_len, epr))


def remove_slave_io_connection(port: int, slave_id: int, con_type: int):
    """
    Remove IO connection
    :param port:
    :param slave_id:
    :param con_type: Remote slave's I/O connection type.
    :return:
    """
    return parse_result(lib.I7565DNM_RemoveIOConnection(port, slave_id, con_type))


def read_output_data(port: int, slave_id: int, con_type: int = 1, length: int = 2):
    """
    Read data according with the consumed connection path of the specific MAC ID device via I/O connection
    :param port:
    :param slave_id:
    :param con_type: Remote slave's I/O connection type.
    :param length: Length(bytes) of the IO ports to be read.
    :return:
    """
    read_buf = (ctypes.c_byte * 512)()
    p_buf = ctypes.cast(read_buf, ctypes.POINTER(ctypes.c_byte))
    read_len = (ctypes.c_long * 32)()
    p_len = ctypes.cast(read_len, ctypes.POINTER(ctypes.c_long))
    r = lib.I7565DNM_ReadbackOutputData(port, slave_id, con_type, byref(p_len), byref(p_buf))
    if r == 0:
        return bytearray(p_buf)[:length]


def write_output_data(port: int, slave_id: int, con_type: int = 1, data: bytearray = bytearray()):
    """
    Set data according with the consumed connection path of the specific MAC ID device via I/O connection.
    :param port:
    :param slave_id:
    :param con_type: Remote slave's I/O connection type.
    :param data:
    :return:
    """
    b_array = ctypes.c_byte * len(data)
    return parse_result(lib.I7565DNM_WriteOutputData(port, slave_id, con_type, len(data), b_array.from_buffer(data)))


def stop_slave_device(port: int, slave_id: int) -> tuple:
    """
    Stop communication with the destination device that users appointed to.
    :param port:
    :param slave_id: Remote slave device’s MAC ID (0~63)
    :return:
    """
    return parse_result(lib.I7565DNM_StopDevice(port, slave_id))


def stop_all_devices(port: int) -> tuple:
    """
    Stop communication with all slave devices that users appointed to.
    :param port:
    :return:
    """
    return parse_result(lib.I7565DNM_StopAllDevice(port))


def close_module(port: int) -> tuple:
    """
    Stop and close the USB driver.
    This must be called once before exiting the user’s application program.
    :param port:
    :return:
    """
    return parse_result(lib.I7565DNM_CloseModule(port))


if __name__ == '__main__':

    print(f"DLL version: {get_dll_version()}")

    all_ports = scan_available_ports()
    if not all_ports:
        print("No device found!")
        sys.exit(-1)

    _port = all_ports[0]
    print(f"Found I-756x devices: {all_ports}, using COM{_port} now...")

    print(f"Firmware version: {get_firmware_version(_port)}")

    print(f"Activation: {activate_module(_port)}")

    print(f"Baudrate: {get_baudrate(port=_port)} kbps")

    print(f"Master MAC ID: {get_master_mac_id(_port)}")

    print(f"Master status: {get_master_status(_port)}")

    sid = 1

    print(f"Slave({sid}) status: {get_slave_status(_port, sid)}")

    print(f"Start slave({sid}) device: {start_slave_device(_port, sid)}")

    cnt = 0
    while True:
        try:
            buf = bytearray([0x10, 0x00])
            print(f"Write data({buf}): {write_output_data(_port, sid, 1, buf)}")
            time.sleep(1)
            buf = bytearray([0x00, 0x00])
            print(f"Write data({buf}): {write_output_data(_port, sid, 1, buf)}")
            time.sleep(1)
            _data = read_output_data(_port, sid)
            print(cnt, _data)
            cnt += 1
            time.sleep(1)
            if _data is None:
                break
        except KeyboardInterrupt:
            break

    # for v in [0xAA, 0x0F, 0xF0, 0xFF]:
    #     buf = bytearray([v])
    #     buf.append(0)
    #     print(f"Write data({v:02x}): {write_output_data(_port, slave_id, 1, buf)}")
    #     time.sleep(1)
    #     read_val = read_output_data(port=_port, slave_id=slave_id, con_type=1)
    #     print(f"\tReading back: {read_val}")
    #     time.sleep(1)

    print(f"Stop slave({sid}) device: {stop_slave_device(_port, sid)}")

    print(f"Closing module - {close_module(port=_port)}")
