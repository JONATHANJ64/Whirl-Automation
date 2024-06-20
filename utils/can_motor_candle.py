"""
    GYEMS RMD-L-50 Motor Driver

    Sample Values:

        Angle Kp:       100
        Angle Ki:       10

        Speed Kp:       250
        Speed Ki:       50

        Torque Kp:      20
        Torque Ki:      20


"""
import threading
import candle_driver
import time
import traceback
from settings import CANBUS_BITRATE, MOTOR_RETRY_CNT
from utils.logger import logger


ID_OFFSET = 0x140


class PyCanMotor(object):

    def __init__(self, bitrate=CANBUS_BITRATE):
        self.bitrate = bitrate
        self._device = None
        self._opened = False
        self._lock = threading.Lock()
        self._ch = None

    def open(self) -> bool:
        if not self._opened:
            devices = candle_driver.list_devices()
            if devices:
                self._device = devices[0]
                self._device.open()
                logger.debug(f"Found a candle adapter, name: {self._device.name()}, path: {self._device.path()}")
                self._ch = self._device.channel(0)
                self._ch.set_bitrate(self.bitrate)
                self._ch.stop()
                self._device.close()
                self._device.open()
                self._ch.start()
                self._opened = True
                return True
            else:
                logger.error("No Motor Adaptor Found!")

    def lock_motor_positions(self) -> list:
        results = []
        for i in [2, ]:     # TODO: Add more motors
            cur_pos = self.read_multi_turns_angle(arb_id=i)
            if cur_pos is not None:
                if cur_pos > 360 * 1000:
                    raise ValueError(f"Invalid angle from the motor {i} - {cur_pos} !")
                logger.debug(f"Current position of the motor {i}: {cur_pos}, fixing now...")
                self.set_position_multi_turn(arb_id=i, pos=cur_pos, speed_limit=1)
                results.append(True)
            else:
                results.append(False)
        return results

    def reset_all_motors(self):
        for i in [2, ]:  # TODO: Add more motors
            self.turn_motor_off(arb_id=i)

    def lock_current_position(self, arb_id=1):
        cur_pos = self.read_multi_turns_angle(arb_id)
        if cur_pos is not None:
            if cur_pos > 360 * 1000:
                raise ValueError(f"Invalid angle from the motor {arb_id} - {cur_pos} !")
            logger.debug(f"Current position of the motor {arb_id}: {cur_pos}, fixing now...")
            self.set_position_multi_turn(arb_id=arb_id, pos=cur_pos, speed_limit=1)

    def get_device_info(self):
        if self._opened:
            return {'name': self._device.name(), 'path': self._device.path()}

    def is_opened(self):
        return self._opened

    def read_pid_parameters(self, arb_id=1):
        msg = self._handshake_msg(arb_id=arb_id, msg=[0x30])
        if msg:
            return dict(
                angle_kp=msg[2],
                angle_ki=msg[3],
                speed_kp=msg[4],
                speed_ki=msg[5],
                torque_kp=msg[6],
                torque_ki=msg[7]
            )

    def read_multi_turns_angle(self, arb_id=1):
        """
        Read motor angle value. Positive value indicates clockwise cumulative angle, negative value
        indicates counterclockwise cumulative angle, unit 0.01 ° / LSB.
        """
        msg = self._handshake_msg(arb_id=arb_id, msg=[0x92])
        if msg:
            return round(int.from_bytes(msg[::-1][:-1], byteorder='big', signed=True) / 100, 1)

    def read_single_circle_angle(self, arb_id=1):
        """
        CircleAngle, starting from the encoder zero point, increased by clockwise rotation
        and returning to zero when it reaches zero again, the unit is 0.01°/LSB.
        """
        msg = self._handshake_msg(arb_id=arb_id, msg=[0x94])
        if msg:
            return round((msg[6] + (msg[7] << 8)) * .01, 1)

    def read_acceleration_data(self, arb_id=1):
        msg = self._handshake_msg(arb_id=arb_id, msg=[0x33])
        if msg:
            return dict(
                position_loop_p=msg[2],
                position_loop_i=msg[3],
                speed_loop_p=msg[4],
                speed_loop_i=msg[5],
                torque_loop_p=msg[6],
                torque_loop_i=msg[7]
            )

    def read_encoder_data(self, arb_id=1):
        msg = self._handshake_msg(arb_id=arb_id, msg=[0x90])
        if msg:
            return dict(
                cur_pos=msg[2] + (msg[3] << 8),
                orig_pos=msg[4] + (msg[5] << 8),
                offset=msg[6] + (msg[7] << 8),
            )

    def read_motor_status_1(self, arb_id=1):
        """
            Motor temperature（1°C/LSB)
            Voltage（0.1V/LSB)
            Error State（dict）
        """
        return self._send_motor_status_1_cmd(arb_id=arb_id, cmd=0x9A)

    def read_motor_status_2(self, arb_id=1):
        """
        Motor temperature（1°C/LSB）
        Motor torque current(Iq)（Range:-2048 ~ 2048, real torque current range:-33A ~ 33A）
        Motor speed（1dps/LSB）
        Encoder position value（14bit encoder value range 0 ~ 16383）
        """
        msg = self._handshake_msg(arb_id=arb_id, msg=[0x9C])
        return self._parse_motor_status(msg)

    def read_motor_status_3(self, arb_id=1):
        """
        Actual phase current is 1A/64LSB
        """
        msg = self._handshake_msg(arb_id=arb_id, msg=[0x9D])
        if msg:
            return dict(
                current_a=(msg[2] + (msg[3] << 8)) / 64.,
                current_b=(msg[4] + (msg[5] << 8)) / 64.,
                current_c=(msg[6] + (msg[7] << 8)) / 64.,
            )

    def write_pid_parameters(self, arb_id=1, to_rom=True, angle_kp=0, angle_ki=0, speed_kp=0, speed_ki=0,
                             torque_kp=0, torque_ki=0):
        msg = [0x32 if to_rom else 0x31, 0x00, angle_kp, angle_ki, speed_kp, speed_ki, torque_kp, torque_ki]
        return bytes(msg) == self._handshake_msg(arb_id=arb_id, msg=msg)

    def write_encoder_offset(self, arb_id=1, offset=0):
        msg = [0x91, 0, 0, 0, 0, 0, offset & 0xFF, (offset & 0xFF00) >> 8]
        return bytes(msg) == self._handshake_msg(arb_id=arb_id, msg=msg)

    def set_zero_position_rom(self, arb_id=1):
        """
            This command needs to be powered on again to take effect.
            This command will write the zero position to ROM. Multiple writes will affect the chip life.
            So not recommended to use it frequently.
        """
        reply = self._handshake_msg(arb_id=arb_id, msg=[0x19])
        if reply:
            return reply[6] + (reply[7] << 8)

    def clear_motor_error_flag(self, arb_id=1):
        return self._send_motor_status_1_cmd(arb_id=arb_id, cmd=0x9B)

    def set_torque_current(self, arb_id=1, torque=0):
        """
        Iq Control is the value range: -2000 ~ 2000, corresponding to the actual torque current range -32A ~ 32A.
        Iq Control in this command is not limited by the Max Torque Current value in the host computer.
        """
        int_torque = int(torque / 32 * 2000)
        b_value = int_torque.to_bytes(length=2, byteorder='big', signed=True)
        reply = self._handshake_msg(arb_id=arb_id, msg=[0xA1, 0, 0, 0, b_value[1], b_value[0]])
        return self._parse_motor_status(reply)

    def set_speed(self, arb_id=1, speed=0):
        """
        Set speed. unit: dps

         The maximum torque current under this command is limited by the Max Torque Current value in the host computer.
         The maximum acceleration of the motor is limited by the Max Acceleration value in the host computer.
        """
        s = int(speed * 100)     # 0xA2 command requires 0.01dps/LSB
        reply = self._handshake_msg(arb_id=arb_id,
                                    msg=[0xA2, 0, 0, 0, s & 0xFF, (s >> 8) & 0xFF, (s >> 16) & 0xFF, (s >> 24) & 0xFF])
        return self._parse_motor_status(reply)

    def move_multi_turn(self, arb_id=1, offset=0, speed_limit=None):
        cur_angle = self.read_multi_turns_angle(arb_id=arb_id)
        self.set_position_multi_turn(arb_id=arb_id, pos=cur_angle + offset, speed_limit=speed_limit)

    def set_position_multi_turn(self, arb_id=1, pos=0., speed_limit=None):
        """
        Set position of the motor (multi-turn angle)
        """
        p = int(pos * 100)  # 0xA3/0xA4 command requires 0.01degree/LSB
        msg = [0xA3 if speed_limit is None else 0xA4, 0,
               0 if speed_limit is None else speed_limit & 0xFF,
               0 if speed_limit is None else (speed_limit >> 8) & 0xFF,
               p & 0xFF, (p >> 8) & 0xFF, (p >> 16) & 0xFF, (p >> 24) & 0xFF]
        reply = self._handshake_msg(arb_id=arb_id, msg=msg)
        return self._parse_motor_status(reply)

    def set_position_single_turn(self, arb_id=1, angle=0., direction='clockwise', speed_limit=None):
        """
        The host sends this command to control the position of the motor (single-turn angle).
        The actual angle range is 0° ~ 359.99°
        """
        angle = self.normalize_angle(angle)
        ang = int(angle * 100)  # 0xA5/0xA6 command requires 0.01degree/LSB
        reply = self._handshake_msg(
            arb_id=arb_id,
            msg=[0xA5 if speed_limit is None else 0xA6,
                 0x00 if direction == 'clockwise' else 0x01,
                 0 if speed_limit is None else speed_limit & 0xFF,
                 0 if speed_limit is None else (speed_limit >> 8) & 0xFF,
                 ang & 0xFF,
                 (ang >> 8) & 0xFF]
        )
        return self._parse_motor_status(reply)

    def turn_motor_off(self, arb_id=1):
        msg = [0x80, 0, 0, 0, 0, 0, 0, 0]
        return bytes(msg) == self._handshake_msg(arb_id=arb_id, msg=msg)

    def stop_motor(self, arb_id=1):
        msg = [0x81, 0, 0, 0, 0, 0, 0, 0]
        return bytes(msg) == self._handshake_msg(arb_id=arb_id, msg=msg)

    def resume_motor(self, arb_id=1):
        msg = [0x88, 0, 0, 0, 0, 0, 0, 0]
        return bytes(msg) == self._handshake_msg(arb_id=arb_id, msg=msg)

    def _handshake_msg(self, arb_id=1, msg=None, timeout=1000):
        msg = msg or []
        msg.extend([0x00] * max(8 - len(msg), 0))
        retry_cnt = 0
        with self._lock:
            while retry_cnt < MOTOR_RETRY_CNT:
                if self._opened or self.open():
                    self._ch.write(ID_OFFSET + arb_id, bytes(msg))
                    try:
                        # Why do we have to read first? It returns the original message first!
                        self._ch.read(timeout)
                        # Read the response now.
                        s_time = time.time()
                        while True:
                            frame_type, can_id, can_data, extended, ts = self._ch.read(timeout)
                            if can_data[0] == msg[0]:
                                return can_data
                            elif time.time() - s_time > timeout:
                                break
                            else:
                                time.sleep(.001)
                    except TimeoutError:
                        logger.error(f"CAN: Failed to read data from motor {arb_id}!")
                        logger.debug(f"Stack: \n{''.join(traceback.format_stack())}")
                self.close()
                time.sleep(.2)
                retry_cnt += 1

    def _send_motor_status_1_cmd(self, arb_id=1, cmd=None):
        msg = self._handshake_msg(arb_id=arb_id, msg=[cmd])
        if msg:
            return dict(
                temperature=msg[1],
                voltage=round((msg[3] + (msg[4] << 8)) * .1, 2),
                error_state=dict(
                    low_voltage_protection=msg[7] & 1,
                    over_temperature_protection=(msg[7] >> 3) & 1
                )
            )

    @staticmethod
    def _parse_motor_status(msg):
        if msg:
            r_torque = round(int.from_bytes(msg[2:3], byteorder='little', signed=True) / 2048. * 33, 2)
            speed = msg[4] + (msg[5] << 8)
            return dict(
                temperature=msg[1],
                torque=r_torque,
                speed=speed if speed < 32768 else (speed - 65536),
                encoder_position=msg[6] + (msg[7] << 8),
            )

    @staticmethod
    def normalize_angle(angle):
        if angle < 0:
            angle += 360
        if angle >= 360:
            angle -= 360
        return angle

    def get_near_direction(self, cur_angle, target_angle):
        cur_angle = self.normalize_angle(cur_angle)
        target_angle = self.normalize_angle(target_angle)
        if target_angle > cur_angle:
            return 'clockwise' if target_angle - cur_angle < 180 else 'counterclockwise'
        else:
            return 'counterclockwise' if cur_angle - target_angle <= 180 else 'clockwise'

    def wait_motion_complete(self, target_angle, tolerance, timeout, arb_id):
        ts = time.time()
        while time.time() - ts < timeout:
            if self.read_multi_turns_angle(arb_id=arb_id) - target_angle < tolerance:
                return True
            time.sleep(.01)
        return False

    def motor_stalled(self, arb_id, prog_speed, tolerance):        # tolerance is a percentage of prog_speed (0% - 100%)
        motor_status = self.read_motor_status_2(arb_id)
        cur_speed = motor_status['speed']
        if abs(abs(cur_speed) - prog_speed) > (tolerance / 100) * abs(prog_speed):
            return True
        else:
            return False

    def close(self, close=True):
        logger.debug("Closing motor connection...")
        if self._ch is not None and close:
            self._ch.stop()
        self._ch = None
        if self._device is not None and close:
            self._device.close()
        self._device = None
        self._opened = False


if __name__ == '__main__':

    m = PyCanMotor()
    m.open()
    # print(m.read_pid_parameters(arb_id=2))

    print(m.read_multi_turns_angle())

    def thread_a():
        while True:
            s_time = time.time()
            print(m.read_multi_turns_angle())
            print("A: ", s_time, time.time() - s_time)
            time.sleep(1 - time.time() + s_time)

    def thread_b():
        while True:
            s_time = time.time()
            print(m.read_pid_parameters())
            print("\tB: ", s_time, time.time() - s_time)
            time.sleep(1 - time.time() + s_time)

    threading.Thread(target=thread_a).start()
    # time.sleep(.5)
    threading.Thread(target=thread_b).start()
