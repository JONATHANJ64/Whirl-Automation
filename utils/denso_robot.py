import threading

from settings import ROBOT_IO_HAND, ROBOT_IO_AGITATOR, R_MOVING_TO_PARK, R_VACUUM_ACTUATOR
from utils.bCAPClient.bcapclient import BCAPClient
from utils.logger import logger
from ctypes import *


class DensoRobot(object):

    def __init__(self, host='192.168.100.8', robot_type='rc7', index=1, port=5007, timeout=5.0):
        self.host = host
        self.port = port
        self.index = index
        self.timeout = timeout
        self._client = None
        self._handle = None
        self._h_robot = None
        self._h_cur_pos = None
        self._cur_task = None
        self.robot_type = robot_type
        self._connected = False
        self._home_pos = [0, 0, 0]
        self._lock = threading.Lock()

    def __str__(self):
        return f"Robot{self.index}({self.host})"

    def connect(self):
        try:
            self._client = BCAPClient(host=self.host, port=self.port, timeout=self.timeout)
            logger.info(f"{self}: Opened connection")
            self._client.service_start("")
            if self.robot_type == 'rc7':
                self._handle = self._client.controller_connect(name="", provider="CaoProv.DENSO.NetwoRC",
                                                               machine="localhost", option="")
            else:
                self._handle = self._client.controller_connect(name="", provider="CaoProv.DENSO.VRC",
                                                               machine="localhost", option="")
            self._connected = True
            self._home_pos = self.read_variable("P99")
            return True
        except Exception as e:
            logger.error(f"{self}: Failed to connect to the Denso Robot - {e}")
            self.clear_handles()

    def read_variable(self, var_name: str):
        if self._client is not None or self.connect():
            try:
                with self._lock:
                    handle = self._client.controller_getvariable(handle=self._handle, name=var_name, option="")
                    val = self._client.variable_getvalue(handle=handle)
                    if handle != 0:
                        self._client.variable_release(handle=handle)
                return val
            except Exception as e:
                logger.error(f"{self}: Failed to read variable({var_name}) - {e}")
                self.clear_handles()

    def write_variable(self, var_name: str, value, check_result=True):
        if self._client is not None or self.connect():
            try:
                with self._lock:
                    handle = self._client.controller_getvariable(handle=self._handle, name=var_name, option="")
                    self._client.variable_putvalue(handle=handle, newval=value)
                    if handle != 0:
                        self._client.variable_release(handle=handle)
                return not check_result or value == self.read_variable(var_name)
            except Exception as e:
                logger.error(f"{self}: Failed to write variable - {e}")
                self.clear_handles()

    # def move(self, pos, motion="@E"):
    #     """
    #     :param pos: 7-axis position value - [x, y, z, Rx, Ry, Rz, Fig]
    #     :param motion: Reach Motion. Can be "@P", "@0", "@E"
    #     :return:
    #     """
    #     if self._client is not None or self.connect():
    #         try:
    #             if self._h_robot is None:
    #                 self._h_robot = self._client.controller_getrobot(handle=self._handle, name="Arm", option="")
    #             return self._client.robot_move(self._h_robot, 1, [pos, "P", motion], "")
    #         except Exception as e:
    #             logger.error(f"{self}: Failed to move robot arm - {e}")

    def get_current_position(self):
        if self._client is not None or self.connect():
            try:
                if self._h_robot is None:
                    self._h_robot = self._client.controller_getrobot(handle=self._handle, name="Arm", option="")
                if self._h_cur_pos is None:
                    self._h_cur_pos = self._client.robot_getvariable(self._h_robot, "@CURRENT_POSITION")
                pos = self._client.variable_getvalue(self._h_cur_pos)
                return pos
            except Exception as e:
                logger.error(f"{self}: Failed to get current position - {e}")
                self.clear_handles()

    def turn_motor(self, val: bool):
        if self._client is not None or self.connect():
            c_val = c_short(val)
            try:
                if self._h_robot is None:
                    self._h_robot = self._client.controller_getrobot(handle=self._handle, name="Arm", option="")
                return self._client.robot_execute(handle=self._h_robot, command="Motor", param=c_val)
            except Exception as e:
                logger.error(f"{self}: Failed to turn motor {'ON' if val else 'OFF'} - {e}")
                self.clear_handles()

    def set_speed(self, speed, accel=None, decel=None):
        if accel is None:
            accel = max(min(int(speed * speed / 100.), 100), 1)
        if decel is None:
            decel = max(min(int(speed * speed / 100.), 100), 1)
        logger.debug(f"{self}: Setting robot speed: {speed}, accel: {accel}, decel: {decel}")
        c_speed = c_float(speed)            # RC7 requires ctypes for float values
        c_accel = c_float(accel)
        c_decel = c_float(decel)
        if self._client is not None or self.connect():
            try:
                if self._h_robot is None:
                    self._h_robot = self._client.controller_getrobot(handle=self._handle, name="Arm", option="")
                return self._client.robot_execute(self._h_robot, "ExtSpeed", [c_speed, c_accel, c_decel])
            except Exception as e:
                logger.error(f"{self}: Failed to set robot speed - {e}")
                self.clear_handles()

    def get_ext_speed(self):
        if self._client is not None or self.connect():
            try:
                if self._h_robot is None:
                    self._h_robot = self._client.controller_getrobot(self._handle, "")
                hspeed = self._client.robot_getvariable(self._h_robot, '@EXTSPEED', "")
                speed = self._client.variable_getvalue(hspeed)
                self._client.variable_release(hspeed)
                return round(speed)
            except Exception as e:
                logger.error(f"{self}: Could not acquire current robot external speed - {e}")
                self.clear_handles()

    def get_motor_status(self):
        if self._client is not None or self.connect():
            try:
                if self._h_robot is None:
                    self._h_robot = self._client.controller_getrobot(self._handle, "")
                h_motor = self._client.robot_getvariable(self._h_robot, '@SERVO_ON', "")
                motor_status = self._client.variable_getvalue(h_motor)
                self._client.variable_release(h_motor)
                return motor_status
            except Exception as e:
                logger.error(f"{self}: Could not acquire current motor status - {e}")
                self.clear_handles()

    # def get_auto_status(self):
    #     if self._client is not None or self.connect():
    #         try:
    #             h_status = self._client.controller_getvariable(handle=self._handle, name="@AUTO_ENABLE", option="")
    #             auto_status = self._client.variable_getvalue(handle=h_status)
    #             if h_status != 0:
    #                 self._client.variable_release(handle=h_status)
    #             return auto_status
    #         except Exception as e:
    #             logger.error(f"{self}: Failed to get auto status - {e}")

    def get_io(self, num):
        return self.read_variable(f"IO{num}")

    def set_io(self, num, val):
        return self.write_variable(f"IO{num}", val)

    # def take_arm(self):
    #     try:
    #         if self._h_robot is None:
    #             self._h_robot = self._client.controller_getrobot(handle=self._handle, name="Arm", option="")
    #         return self._client.robot_execute(self._h_robot, "TakeArm", [0, 0])
    #     except Exception as e:
    #         logger.error(f"{self}: Failed to take arm - {e}")

    # def give_arm(self):
    #     try:
    #         if self._h_robot is None:
    #             self._h_robot = self._client.controller_getrobot(handle=self._handle, name="Arm", option="")
    #         return self._client.robot_execute(self._h_robot, "GiveArm", None)
    #     except Exception as e:
    #         logger.error(f"{self}: Failed to give arm - {e}")

    def start_task(self, task_name: str = 'pro1', mode: int = 1):
        """
        :param task_name: Program name
        :param mode:
            1: One Cycle Execution
            2: Continuous Execution
            3: Step Forward
        :return: task handle.
        """
        if self._client is not None or self.connect():
            try:
                if self._cur_task is None:
                    self._cur_task = self._client.controller_gettask(handle=self._handle, name=task_name, option="")
                if self.get_task_status('pro1') != 'RUN':
                    c_mode = c_long(mode)
                    self._client.task_start(handle=self._cur_task, mode=c_mode, option="")
            except Exception as e:
                logger.error(f"{self}: Failed to start task - {e}")

    def get_task_status(self, task_name: str = 'pro1'):
        if self._client is not None or self.connect():
            try:
                if self._cur_task is None:
                    self._cur_task = self._client.controller_gettask(handle=self._handle, name=task_name, option="")
                if self.robot_type == 'rc7':
                    h_status = self._client.task_getvariable(self._cur_task, "@STATUS", '')
                    status = self._client.variable_getvalue(h_status)
                else:
                    status = self._client.task_execute(handle=self._cur_task, command="GetStatus")
                if status is not None:
                    if self.robot_type == 'rc7':
                        return ["1", "READY", "DORMANT", "4", "RUN", "6", "SUSPENDED"][status]
                    else:
                        return ["NON_EXISTENT", "DORMANT", "READY", "RUN", "WAIT", "SUSPENDED"][status]
            except Exception as e:
                logger.error(f"{self}: Failed to get task status - {e}")
                self.clear_handles()

    def continue_task(self, task_name: str = 'pro1', mode: int = 1):
        if self._client is not None or self.connect():
            try:
                if self._cur_task is None:
                    self._cur_task = self._client.controller_gettask(handle=self._handle, name=task_name, option="")
                status = self.get_task_status(task_name)
                if (status in {"DORMANT", "SUSPENDED", "WAIT"}) and self.read_variable("I50") == 0:
                    self.start_task(task_name, mode)
                else:
                    logger.debug(f"{self}: Current robot task is not in a continuable state.")
            except Exception as e:
                logger.error(f"{self}: Could not continue running task - {e}")
                self.clear_handles()

    def get_cont_error(self):
        if self._client is not None or self.connect():
            c_error_msg = self.read_variable("@ERROR_DESCRIPTION") or ''
            c_error_code = self.read_variable("@ERROR_CODE") or ''
            clear_msgs = ['21F3', '21FC', 'Enable-auto signal turned OFF', 'Enable Auto signal OFF', 'Enable Auto OFF',
                          'Enable-auto signal turned ON']
            if any([m in c_error_msg for m in clear_msgs]):
                self.clear_cont_error()
            if "Undefined error" not in c_error_msg and "The operation completed successfully." not in c_error_msg \
                    and c_error_code:
                return f"{c_error_msg} ({c_error_code})"

    def clear_cont_error(self):
        if self._client is not None or self.connect():
            try:
                result = self._client.controller_execute(self._handle, "ClearError", 0)
                return result
            except Exception as e:
                logger.error(f'Failed to clear cont error - {e}')
                self.clear_handles()

    # def set_auto_mode(self, mode):
    #     """
    #     param mode: 1: Internal Auto, 2: External Auto
    #     """
    #     if self._client is not None or self.connect():
    #         c_mode = c_short(mode)
    #         self._client.controller_execute(self._handle, "PutAutoMode", c_mode)

    def stop_task(self, mode: int = 0, task_handle=None):
        """
        Stop the currently running task
        :param task_handle:
        :param mode:  0: Default stop, 1: Instant stop, 2: Step stop, 3: Cycle stop, 4: Reset
        :return:
        """
        if self._client is not None or self.connect():
            if self.get_task_status() is not None and self.get_task_status() != "READY":
                try:
                    self._client.task_stop(task_handle or self._cur_task, c_long(mode), "")
                except Exception as e:
                    logger.error(f"{self}: Failed to stop task - {e}")
                    self.clear_handles()
            elif self.get_task_status() == "READY":
                logger.debug(f"{self} task is already on halt")
            else:
                logger.debug(f"{self} task in an unknown state")

    # def release_task(self, task_handle):
    #     if task_handle != 0:
    #         try:
    #             self._client.task_release(task_handle)
    #         except Exception as e:
    #             logger.error(f"{self}: Failed to release task - {e}")

    # def is_moved_to_position(self, num):
    #     # P0~P9 are matched to P90~P99.
    #     target_p = self.read_variable(f"P{num if num >= 10 else (90 + num)}")
    #     _p = self.get_current_position()
    #     if _p is not None:
    #         if sum([(_p[k] - target_p[k]) ** 2 for k in range(len(target_p))]) < .1:
    #             return True

    def read_io_state(self):  # Old
        state = {'hand': self.get_io(ROBOT_IO_HAND['in'][self.index])}
        if self.index == 4:
            state['picker'] = self.get_io(ROBOT_IO_AGITATOR['picker']['in'])
            state['placer'] = self.get_io(ROBOT_IO_AGITATOR['placer']['in'])
        return state

    # def read_io_state(self):  # New
    #    def open_closed(hand_device):
    #        hand_st = {'hand': 'opened'} if hand_device['hand'][0] else {'hand': 'closed'}
    #        if 'picker' in hand_device.keys():
    #            hand_st['picker'] = 'retracted' if hand_device['picker'][0] is True else 'extended'
    #            hand_st['placer'] = 'retracted' if hand_device['placer'][0] is True else 'extended'
    #        return hand_st

    #    io_state = {'hand': [None, None]}
    #    for io_hand in range(0, 2):
    #        io_state['hand'][io_hand] = self.get_io(ROBOT_IO_HAND['out'][self.index][io_hand])
    #    if self.index == 4:
    #        io_state['picker'] = [None, None]
    #        io_state['placer'] = [None, None]
    #        for io_picker in range(0, 2):
    #            io_state['picker'][io_picker] = self.get_io(ROBOT_IO_AGITATOR['picker']['out'][io_picker])
    #        for io_placer in range(0, 2):
    #            io_state['placer'][io_placer] = self.get_io(ROBOT_IO_AGITATOR['placer']['out'][io_placer])
    #    hand_state = open_closed(io_state)
    #    return hand_state

    def read_vacuum_state(self, index):
        return self.get_io(num=R_VACUUM_ACTUATOR.get(index))

    def set_vacuum_state(self, index, val):
        return self.set_io(num=R_VACUUM_ACTUATOR.get(index), val=val)

    def write_io_state(self, name, val):
        port = ROBOT_IO_HAND['out'][self.index] if name == 'hand' else ROBOT_IO_AGITATOR[name]['out']
        self.set_io(num=port[0], val=val)
        self.set_io(num=port[1], val=not val)

    def is_connected(self):
        return self._connected

    def clear_handles(self):
        self._client = None
        self._handle = None
        self._h_robot = None
        self._h_cur_pos = None
        self._cur_task = None
        self._connected = False

    def check_paused_and_parked(self):
        def _get_offset(offset):
            val = offset % 360
            return val if val < 180 else 360 - val
        _p = self.get_current_position()
        if _p is not None:
            if all([_get_offset(abs(_p[i] - self._home_pos[i])) < 0.5 for i in range(len(self._home_pos))]):
                return self.get_task_status() == 'READY'
        return False

    def pause(self):
        if self.is_connected():
            self.stop_task(mode=0 if self.read_variable(var_name=R_MOVING_TO_PARK) else 2)

    def close(self):
        if self._client is not None:
            try:
                if self._cur_task is not None:
                    self._cur_task = None
                if self._h_robot:
                    self._client.robot_release(self._h_robot)
                if self._handle != 0:
                    self._client.controller_disconnect(self._handle)
                self._client.service_stop()
            except Exception as e:
                logger.error(f"{self}: Failed to close - {e}")
            self.clear_handles()


if __name__ == '__main__':

    import ctypes

    def get_key(key):
        return bool(ctypes.windll.user32.GetAsyncKeyState(key) & 0x8000)

    ESC = 0x1B  # [ESC] virtual key code

    a = 0
    while True:
        a = a + 100000

    # cur_pos = d.get_current_position()
    # print(f"Current Position: {cur_pos}")

    # d.start_task(task_name='pro1', mode=1)
    # d.get_task_status(task_name='pro1')
    # d.set_speed(speed=50, accel=100, decel=100)

    # for i in range(1, 7):
    #     p = d.read_variable(f"P{i}")
    #     print(f"P{i}: {p}")
    #
    # i1 = d.read_variable('I1')
    # print(f"I1: {i1}")
    # d.write_variable('I1', i1 + 1)
    # print(f"New I1: {d.read_variable('I1')}")
    #
    # print("Starting task...")
    # _handle = d.start_task(task_name='pro99', mode=1)
    #
    # while True:
    #     try:
    #         if get_key(ESC):
    #             print("ESC is pressed! Stopping task instantly.")
    #             d.stop_task(task_handle=_handle, mode=1)
    #             break
    #     except KeyboardInterrupt:
    #         break
    #
    # print("Releasing task...")
    # d.release_task(task_handle=_handle)

