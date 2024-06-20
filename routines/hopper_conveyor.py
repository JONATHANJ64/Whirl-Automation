import time
from routines.base import RoutineBase
from utils.common import get_config
from utils.logger import logger


class HopperConveyorRoutine(RoutineBase):

    def __init__(self, app, root, index=1):
        super().__init__(app, conf=get_config()['station4'])
        self.root = root
        self.err_msg = ''
        self._stopped = False
        self.name = 'hopper'
        self.index = index
        self.target_angle = None
        self.m_conf = get_config()['station4']['motor']
        self.motor_id = self.m_conf['address'] + 1
        self.h_conf = get_config()['station4']['hopper_conveyor']
        self.initialized = False
        self.wago = root.wago

    def initialize(self):
        self.motor.turn_motor_off(self.motor_id)
        if not self.wago.connect():
            self._add_init_alarm(msg="Wago Module of Station 4 is offline!")
            return False

        # CCW is decreasing
        if not self.is_indexed():
            self.motor.move_multi_turn(arb_id=self.motor_id, offset=-1260, speed_limit=self.h_conf['index_speed'])
            s_time = time.time()
            while not self.is_indexed():
                if time.time() - s_time > (1260 / self.h_conf['index_speed']) + 2:
                    self.motor.stop_motor(arb_id=self.motor_id)
                    self._add_init_alarm(
                        msg="Station 4: Hopper conveyor homing procedure failed: Indexing sensor was not detected")
                    return False
                time.sleep(.25)

        # self.motor.set_speed(arb_id=self.motor_id, speed=self.h_conf['homing_speed'])
        # while self.is_indexed():
        #     time.sleep(.1)
        self.motor.stop_motor(arb_id=self.motor_id)
        cur_angle = self.motor.read_multi_turns_angle(arb_id=self.motor_id)
        logger.debug(f"Hopper Conveyor: current angle: {cur_angle}")
        time.sleep(0.1)
        self.motor.set_position_multi_turn(arb_id=self.motor_id, pos=cur_angle + 180,
                                           speed_limit=self.h_conf['index_speed'])
        s_time = time.time()
        while (cur_angle + 180) - self.motor.read_multi_turns_angle(arb_id=self.motor_id) >= .5:
            time.sleep(0.25)
            if time.time() - s_time > (180 / self.h_conf['index_speed']) + 2:
                self.motor.stop_motor(arb_id=self.motor_id)
                self._add_init_alarm(
                    msg="Station 4: Hopper conveyor homing procedure failed: "
                        "Hopper conveyor motor did not reach commanded position")
                return False
        if self.is_indexed():
            self._add_init_alarm(
                msg="Station 4: Hopper conveyor homing procedure failed: Indexing sensor should be off")
            return False

        cur_angle = self.motor.read_multi_turns_angle(arb_id=self.motor_id)
        s_time = time.time()
        self.motor.set_speed(arb_id=self.motor_id, speed=-self.h_conf['homing_speed'])
        while not self.is_indexed():
            if time.time() - s_time > 12:
                self.motor.stop_motor(arb_id=self.motor_id)
                self._add_init_alarm(msg="Station 4: Hopper conveyor homing procedure failed: "
                                         "Hopper conveyor motor did not reach commanded position")
                return False
            if cur_angle - self.motor.read_multi_turns_angle(arb_id=self.motor_id) > 540:
                self.motor.stop_motor(arb_id=self.motor_id)
                self._add_init_alarm(msg="Station 4: Hopper conveyor homing procedure failed: "
                                         "Indexing sensor was not detected")
                return False
            time.sleep(.01)
        self.motor.stop_motor(arb_id=self.motor_id)

        if self.h_conf['home_offset'] > 0:
            self.motor.move_multi_turn(arb_id=self.motor_id, offset=self.h_conf['home_offset'],
                                       speed_limit=self.h_conf['index_speed'])

        self.initialized = True

    def fsm(self):
        if self._stopped:
            time.sleep(0.1)
            return
        if self.state == 'idle':
            if self.is_indexed() and self.is_present():
                self.motor.stop_motor(arb_id=self.motor_id)
                self.motor.lock_current_position(self.motor_id)
                self.state = 'finished'
            else:
                self.target_angle = None
                self.state = 'move_conveyor'
        elif self.state == 'move_conveyor':
            # if self.is_present():
            # self.err_msg = "Cannot index hopper conveyor - A hopper is still present at the pick point."
            # self.motor.stop_motor(arb_id=self.motor_id)
            # self.state = 'error'
            # else:
            if self.target_angle is None:
                if self.is_present():
                    self.err_msg = "Please remove hopper from front of conveyor and clear error."
                    self.state = 'error'
                    return
                else:
                    self.target_angle = self.motor.read_multi_turns_angle(
                        arb_id=self.motor_id) - (self.h_conf['index_length'] - 50)
            logger.debug(f"Hopper Conveyor: target angle: {self.target_angle}")
            self.motor.set_position_multi_turn(arb_id=self.motor_id, pos=self.target_angle,
                                               speed_limit=self.h_conf['index_speed'])
            if self.motor.wait_motion_complete(target_angle=self.target_angle, tolerance=1.0,
                                               timeout=self.h_conf['index_length'] / self.h_conf['index_speed'] + 2,
                                               arb_id=self.motor_id):
                self.state = 'slow_approach'
            elif not self._stopped:
                self.err_msg = "Hopper conveyor motor did not reach commanded position"
                self.motor.stop_motor(arb_id=self.motor_id)
                self.state = 'error'
        elif self.state == 'slow_approach':
            self.motor.set_position_multi_turn(arb_id=self.motor_id, pos=self.target_angle - 50,
                                               speed_limit=self.h_conf['homing_speed'])
            self._tick = time.time()
            self.state = 'check_index'
        elif self.state == 'check_index':
            if self.is_indexed():
                self.motor.stop_motor(arb_id=self.motor_id)
                self.motor.lock_current_position(arb_id=self.motor_id)
                self.target_angle = None
                self.state = 'check_presence'
            elif time.time() - self._tick > self.h_conf['index_length'] / self.h_conf['index_speed']:
                self.motor.stop_motor(arb_id=self.motor_id)
                self.err_msg = 'Indexing sensor is not active during anticipated conveyor indexing positions'
                self.state = 'error'
        elif self.state == 'check_presence':
            if self.is_present():
                self.motor.stop_motor(arb_id=self.motor_id)
                self.motor.lock_current_position(arb_id=self.motor_id)
                self.state = 'finished'
            elif not self.is_present():
                time.sleep(0.5)
                self.state = 'move_conveyor'
            # elif time.time() - self._tick > self.h_conf['index_length'] / self.h_conf['index_speed']:
            #    self.motor.stop_motor(arb_id=self.motor_id)
            #    self.app.add_alarm(dict(
            #        msg="Presence sensor is not active during anticipated conveyor indexing positions!",
            #        level='critical',
            #        buttons=QMessageBox.Retry | QMessageBox.Abort,
            #        default_button=QMessageBox.Retry,
            #        callback=self._on_alarm_closed))
            #    self.state = 'error'
            time.sleep(.01)
        elif self.state == 'finished':
            pass

    def is_finished(self):
        return self.state == 'finished'

    def restart_feed(self):
        self.state = 'idle'

    def do_index(self, clear_error=False):
        self._stopped = False
        if clear_error:
            self.err_msg = ''
        self.state = 'idle'

    @staticmethod
    def is_feeder_online():
        return True

    def stop_state(self):
        self.motor.stop_motor(arb_id=self.motor_id)
        self._stopped = True

    def read_current_state(self):
        return {'state': self.state, 'msg': self.err_msg, 'stopped': self._stopped, 'indexed': self.is_indexed(),
                'present': self.is_present()}

    def _on_alarm_closed(self, *args):
        ret = args[1]
        if ret == 'retry':
            self.state = "idle"
        elif ret == 'abort':
            pass

    def on_stopped(self):
        self.motor.stop_motor(arb_id=self.motor_id)

    def on_resumed(self):
        if self.state == 'check_index':
            self._tick = time.time()
            self.state = 'slow_approach'

    def on_paused(self):
        self.motor.stop_motor(arb_id=self.motor_id)
        self.motor.lock_current_position(self.motor_id)

    def is_indexed(self):
        if self.read_wago_input(name='hopper_conveyor_indexing'):  # Double check sensor in the case of a false positive
            time.sleep(0.05)
        return self.read_wago_input(name='hopper_conveyor_indexing')

    def is_present(self):
        return self.read_wago_input(name='hopper_conveyor_part_detection')
