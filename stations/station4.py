import time
from functools import partial

from PySide2.QtWidgets import QMessageBox

from routines.hopper_conveyor import HopperConveyorRoutine
from routines.pneumatic_slide.station4_right_handle_fixture_pick_slide import Station4RightHandleFixturePickSlide
from routines.pneumatic_slide.station4_right_handle_rotary_slide import Station4RightHandleRotarySlide
from settings import R_HOPPER_PICKED, R_REQUEST_AIR1_OFF, R_REQUEST_AIR1_ON, R_ACK_AIR1_OFF, R_ACK_AIR1_ON, \
    R_REQUEST_FIXTURE_OPEN, R_REQUEST_FIXTURE_CLOSE, R_REQUEST_FIXTURE_ROTATE_0, \
    R_REQUEST_FIXTURE_ROTATE_180
from stations.base import BaseStation
from utils.cognex import CognexVisionController
from utils.common import get_config
from utils.logger import logger


FEEDERS = ['right_handle', 'hopper', 'agitator']

FINAL_VISION_CHECKS = {
    'left_handle_assembly': {
        'trigger_open': 0,
        'dial_open': 1,
        'support_arm_open': 6
    },
    'final_vision': {
        'pinion_final': 2,
        'dial_final': 3,
        'handle_gaps_final': 8,
        'support_arm_final': 7,
        'hopper_final': 4,
        'trigger_final': 5
    }
}


class Station4(BaseStation):

    def __init__(self, app):
        super().__init__(app, conf=get_config()['station4'], feeders=FEEDERS, name="Station4", p_index=6,
                         prefetch_parts=['right_handle'])
        self.feeders['hopper'] = HopperConveyorRoutine(app=app, root=self)
        self.feeders['right_handle'].set_reversed_flag(True)
        self.feeders['right_handle'].set_reversed_cognex_offset(3)
        self._fv_cognex = None
        self._fv_bypass = False

    def initialize(self):
        if self._fv_cognex is None:
            self._fv_cognex = CognexVisionController(host=get_config()['final_vision']['cognex'])
            if not self._fv_cognex.connect():
                self._fv_cognex = None
                self._add_init_alarm(msg="Station4:: Cognex Final Vision is offline!")
                return False
            # Read data without backlight to clear the old values
            self._fv_cognex.read_data()
        return super().initialize()

    def get_ready_feeder(self):
        for name, ff in self.feeders.items():
            if not self._finished_feeders.get(name) and ff.is_finished():
                if name == 'hopper' and not self._finished_feeders.get('right_handle'):
                    logger.warning(f"{self.name}: {ff.name} is ready, but Right Handle is not yet finished!")
                    continue
                if name == 'agitator':
                    if not self._finished_feeders.get('right_handle'):
                        logger.warning(
                            f"{self.name}: FlexFeeder({name}) is ready, but Right Handle should be finished first!")
                        continue
                    if not self._finished_feeders.get('hopper'):
                        logger.warning(
                            f"{self.name}: FlexFeeder({name}) is ready, but Hopper should be finished first!")
                        continue
                return name

    def _check_final_vision(self, c_type='left_handle_assembly'):
        if self._fv_bypass and c_type == 'left_handle_assembly':
            return []
        conf = get_config()['final_vision']
        data = self._fv_cognex.read_data()
        invalid_ones = [n for n, addr in FINAL_VISION_CHECKS[c_type].items() if conf[n] and not data[addr]]
        return invalid_ones

    def fsm(self):
        if self.state == 'idle' and self._fv_bypass is True:
            self._fv_bypass = False
        if self._cur_ff is not None and self._cur_ff.name == 'hopper':
            if self.state == 'set_position':
                self.state = 'check_robot_task_ready'
                return
            if self.state == 'check_robot_pick':
                self.state = 'check_robot_result'
                return
            elif self.state == 'check_robot_result':
                if self.robot.read_variable(var_name=R_HOPPER_PICKED) == 1:
                    if self._cur_ff.is_present():
                        self.app.add_alarm(dict(
                            msg="Hopper removal from conveyor was not detected. "
                                "Please inspect robot 4 and choose how to proceed.",
                            level='critical',
                            buttons=QMessageBox.Retry | QMessageBox.Abort,
                            default_button=QMessageBox.Retry,
                            callback=partial(self._on_alarm_closed, self.state)))
                        self.state = 'error'
                        return
        elif self._cur_ff is not None and self._cur_ff.name == 'right_handle':
            if self.state == 'check_robot_result':
                if self.robot.read_variable(var_name=R_REQUEST_AIR1_OFF) == 1:
                    self.write_wago_output(name='robot4_air1_toggle', val=1)
                    time.sleep(1.0)
                    while self.read_wago_output(name='robot4_air1_toggle') is False:
                        time.sleep(.01)
                    self.robot.write_variable(R_REQUEST_AIR1_OFF, 0)
                    self.robot.write_variable(R_ACK_AIR1_OFF, 1)
                elif self.robot.read_variable(var_name=R_REQUEST_AIR1_ON) == 1:
                    self.write_wago_output(name='robot4_air1_toggle', val=0)
                    time.sleep(0.5)
                    while self.read_wago_output(name='robot4_air1_toggle') is True:
                        time.sleep(.01)
                    self.robot.write_variable(R_REQUEST_AIR1_ON, 0)
                    self.robot.write_variable(R_ACK_AIR1_ON, 1)
            if len(self._part_pos) == 4 and self._part_pos[3]:  # Reversed
                if self.state in {'check_robot_pick', 'check_robot_result'}:
                    if self.robot.read_variable(var_name=R_REQUEST_FIXTURE_OPEN) == 1:
                        logger.debug(f"{self.name} :: Opening Rotary Slide...")
                        if self._move_slide(s_type='rotary', action='open'):
                            self.robot.write_variable(var_name=R_REQUEST_FIXTURE_OPEN, value=0)
                        else:
                            return
                    elif self.robot.read_variable(var_name=R_REQUEST_FIXTURE_CLOSE) == 1:
                        logger.debug(f"{self.name} :: Closing Rotary Slide...")
                        if self._move_slide(s_type='rotary', action='close'):
                            self.robot.write_variable(var_name=R_REQUEST_FIXTURE_CLOSE, value=0)
                        else:
                            return
                    elif self.robot.read_variable(var_name=R_REQUEST_FIXTURE_ROTATE_0) == 1:
                        logger.debug(f"{self.name} :: Fixture slide - orienting to PLACE...")
                        if self._move_slide(s_type='fixture', action='place'):
                            self.robot.write_variable(var_name=R_REQUEST_FIXTURE_ROTATE_0, value=0)
                        else:
                            return
                    elif self.robot.read_variable(var_name=R_REQUEST_FIXTURE_ROTATE_180) == 1:
                        logger.debug(f"{self.name} :: Fixture slide - orienting to PICK...")
                        if self._move_slide(s_type='fixture', action='pick'):
                            self.robot.write_variable(var_name=R_REQUEST_FIXTURE_ROTATE_180, value=0)
                        else:
                            return

        if (self.state == 'has_pallet') or \
                (self._is_prefetch and self._pallet.pallet_ready() and self.state != 'warning'):
            if not self.app.is_flush:
                if 'right_handle' not in self._finished_feeders and not self._fv_bypass:
                    invalid = self._check_final_vision(c_type='left_handle_assembly')
                    if invalid:
                        self.add_alarm(dict(
                            msg=f"{','.join(invalid)} placement error detected, please correct and resume operation.",
                            level='critical',
                            buttons=['Retry', 'Bypass'],
                            callback=partial(self._on_station_alarm_closed, self.state)))
                        self.state = 'warning'
                        return

        return super(Station4, self).fsm()

    def _move_slide(self, s_type='rotary', action='open'):
        slide = Station4RightHandleRotarySlide(root=self, action=action) if s_type == 'rotary' else \
            Station4RightHandleFixturePickSlide(root=self, action=action)
        slide.start()
        s_time = time.time()
        while not slide.is_finished():
            if time.time() - s_time > slide.timeout:
                self.add_alarm(dict(
                    msg=f"Station4 :: Right Handle {s_type.capitalize()} Slide: TIMEOUT!",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return False
            time.sleep(.1)
        return True

    def _perform_finished_part(self):
        if self._cur_ff is not None and self._cur_ff.name == 'agitator':
            invalid = self._check_final_vision(c_type='final_vision')
            if invalid:
                logger.warning(f"failed parts: {invalid}")
                self._pallet.update_pallet_state(state={'final_vision': False})
        return super()._perform_finished_part()

    def _get_robot_park_i10_value(self):
        # Station4 has 4 parts with reversed ones
        return 5

    def _on_station_alarm_closed(self, *args):
        state, action = args[:2]
        if action == 'retry':
            self.state = state
        elif action == 'ignore':
            self.state = 'idle'
        elif action == 'bypass':
            self._fv_bypass = True
            self.state = state

    def on_paused(self):
        self.feeders['hopper'].pause()
        super(Station4, self).on_paused()

    def on_resumed(self):
        self.feeders['hopper'].resume()
        super(Station4, self).on_resumed()

    def on_stopped(self):
        self.feeders['hopper'].stop()
        super(Station4, self).on_stopped()
