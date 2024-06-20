import time
from functools import partial

from PySide2.QtWidgets import QMessageBox

from routines.base import RoutineBase
from utils.common import get_config
from utils.logger import logger


class Labeler(RoutineBase):

    def __init__(self, app, root):
        super().__init__(app, conf=get_config()['station5']['labeler'])
        self.name = "Labeler"
        self.root = root
        self.m_conf = get_config()['station5']['motor']
        self.motor_id = self.m_conf['address'] + 1
        self.v_conf = get_config()['station5']['valve']
        self._tick = 0
        self._err_msg = ''
        self._target_pos = None
        self._air_on = False
        self.wago = root.wago

    def initialize(self):
        self.motor.turn_motor_off(self.motor_id)
        if not self.wago.connect():
            self._add_init_alarm(msg="Wago Module of the Station5 is offline!")
            return False

        if self.is_label_applied():                           # Push old label off if detected
            cur_angle = self.motor.read_multi_turns_angle(arb_id=self.motor_id)
            self.motor.set_position_multi_turn(arb_id=self.motor_id, pos=cur_angle - 1080, speed_limit=90)
            while self.is_label_applied():
                time.sleep(.02)
            # Give some time to make sure label is fully removed before beginning init
            time.sleep(1.5)
            self.motor.stop_motor(arb_id=self.motor_id)
            time.sleep(0.25)

        self.air_toggle(True)
        cur_angle = self.motor.read_multi_turns_angle(arb_id=self.motor_id)
        self.motor.set_position_multi_turn(arb_id=self.motor_id, pos=cur_angle - 1080, speed_limit=30)
        s_time = time.time()
        while True:
            if self.is_label_applied():
                self.air_toggle(False)
                self.motor.stop_motor(arb_id=self.motor_id)
                time.sleep(0.1)
                self.move_motor(offset=self.conf['home_offset'], speed=None)
                break
            elif time.time() - s_time > 108:
                self._add_init_alarm(msg="Cannot find the home position of the labeler!")
                return False
            time.sleep(.02)

    def fsm(self):
        if self.state == 'idle':
            # Label is ready for pick... already did in init function
            self._tick = time.time()
            self.state = 'check_sensor'
        elif self.state == "start":
            if self.is_label_applied():  # Push old label off if detected
                cur_angle = self.motor.read_multi_turns_angle(arb_id=self.motor_id)
                self.motor.set_position_multi_turn(arb_id=self.motor_id, pos=cur_angle - 1080, speed_limit=90)
                while self.is_label_applied():
                    time.sleep(.02)
                # Give some time to make sure label is fully removed before beginning init
                time.sleep(1.5)
                self.motor.stop_motor(arb_id=self.motor_id)
                time.sleep(0.25)
            offset = self.conf['label_pitch'] / self.conf['rot_per_revolution'] * 360. - self.conf['sensor_offset']
            self.air_toggle(True)
            if self.move_motor(offset=offset, speed=None):
                self._tick = time.time()
                self.state = "check_sensor"
        elif self.state == 'check_sensor':
            if self.is_label_applied():
                self.air_toggle(False)
                self.motor.stop_motor(arb_id=self.motor_id)
                # if abs(self.motor.read_multi_turns_angle(arb_id=self.motor_id) - self._target_pos) < .2:
                logger.debug('Label edge found...')
                self._target_pos = None
                self.state = 'move_offset'
            elif time.time() - self._tick > self.conf['sensor_timeout']:
                self.air_toggle(False)
                self.root.add_alarm(dict(
                    msg=f"No Label after {self.conf['sensor_timeout']} sec.! Missing label or end of spool?",
                    level='warning',
                    buttons=['Retry'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
        elif self.state == 'move_offset':
            cur_angle = self.motor.read_multi_turns_angle(arb_id=self.motor_id)
            final_angle = cur_angle - self.conf['sensor_offset']
            if self.move_motor(offset=self.conf['sensor_offset'], speed=self.m_conf['offset_speed']):
                while self.motor.wait_motion_complete(target_angle=final_angle, tolerance=5.0, timeout=50,
                                                      arb_id=self.motor_id) is False:
                    time.sleep(.1)
                self.state = 'ready'
        elif self.state == 'ready':
            self._err_msg = ''

        elif self.state == 'wait':
            pass

    def read_current_state(self):
        return {'state': self.state, 'msg': self._err_msg}

    def is_label_applied(self):
        return self.read_wago_input('label_applicator')

    def unlock_motor(self):
        self.motor.stop_motor(arb_id=self.motor_id)
        if self.state != 'init':
            self.state = 'wait'

    def clear_error(self):
        self._err_msg = ''
        if self.state != 'init':
            self.state = 'wait'

    def move_motor(self, offset, speed):
        cur_angle = self.motor.read_multi_turns_angle(arb_id=self.motor_id)
        self._target_pos = cur_angle - offset
        status = self.motor.set_position_multi_turn(
            arb_id=self.motor_id,
            pos=self._target_pos,
            speed_limit=self.m_conf['speed_limit'] if speed is None else speed
        )
        if status is None:
            self._err_msg = f"Failed to move({offset}) of the Labeler motor!"
            self._add_motor_error(motor_id=self.motor_id, msg=self._err_msg)
            return False
        return True

    def start_labeler(self):
        self.state = 'start'

    def is_ready(self):
        return self.state == 'ready'

    def air_toggle(self, state):
        self.valve.write_bit(slave_id=self.v_conf['slave_id'], pos=self.v_conf['label_air'], val=state)
        self._air_on = state

    def _on_alarm_closed(self, *args):
        ret = args[1]
        if ret == 'retry':
            self.state = "start"
        elif ret == 'abort':
            pass
        if self.state == 'check_sensor':
            if ret == 'retry':
                self.state = 'start'
        self._err_msg = ''

    def on_stopped(self):
        self.air_toggle(False)
        self.motor.stop_motor(arb_id=self.motor_id)

    def on_resumed(self):
        # Continue moving to the position
        if self._air_on:
            self.air_toggle(True)
        if self._target_pos is not None:
            self.motor.set_position_multi_turn(
                arb_id=self.motor_id,
                pos=self._target_pos,
                speed_limit=self.m_conf['speed_limit']
            )
        self._target_pos = None
        if self.state == 'check_sensor':
            self._tick = time.time()

    def on_paused(self):
        self.air_toggle(False)
        self.motor.stop_motor(arb_id=self.motor_id)
