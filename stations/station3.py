import time
from functools import partial

from PySide2.QtWidgets import QMessageBox

from routines.pneumatic_slide.station3_part_flip_nest_slide import Station3PartFlipNestSlide
from settings import R_REQUEST_FIXTURE_OPEN, R_REQUEST_FIXTURE_CLOSE
from stations.base import BaseStation
from utils.common import get_config
from utils.logger import logger


FEEDERS = ['left_handle', 'support_arm', 'dial', 'trigger']


class Station3(BaseStation):

    def __init__(self, app):
        self._laser_error = False
        super().__init__(app, conf=get_config()['station3'], feeders=FEEDERS, name="Station3", p_index=5,
                         prefetch_parts=['left_handle'])
        for name, f in self.feeders.items():
            if name != 'dial':
                f.set_reversed_flag(True)
                f.set_reversed_cognex_offset(4)

    def get_ready_feeder(self):
        for i, name in enumerate(self.feeder_names):
            if not self._finished_feeders.get(name) and self.feeders[name].is_finished():
                if any([not self._finished_feeders.get(self.feeder_names[n]) for n in range(i)]):
                    logger.warning(f"{self.name}: FlexFeeder({name}) is ready, but previous one is not yet finished!")
                    continue
                return name

    def set_product_type(self, p_type):
        super().set_product_type(p_type)
        if "Whirl" not in p_type:       # Sta-Green or ACE
            self.feeders.pop('support_arm')
            self.feeder_names.remove('support_arm')

    def fsm(self):
        if self.state == 'has_pallet' or \
                (self._is_prefetch and self._pallet.pallet_ready() and self.state != 'warning'):
            if (self.read_wago_input(name='laser_sensor_dial') or self.read_wago_input(
                    name='laser_sensor_left_handle')) and 'left_handle' not in self._finished_feeders:
                self.add_alarm(dict(
                    msg="Station3: Unexpected object detected on the pallet, please remove and then continue!",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return
        if self._cur_ff is not None and self._cur_ff.name != 'dial':
            if len(self._part_pos) == 4 and self._part_pos[3]:      # Reversed
                if self.state in {'check_robot_pick', 'check_robot_result'}:
                    if self.robot.read_variable(var_name=R_REQUEST_FIXTURE_OPEN) == 1:
                        logger.debug(f"{self.name} :: Opening Fixture Slide...")
                        if self._flip_nest_slide(action='open'):
                            self.robot.write_variable(var_name=R_REQUEST_FIXTURE_OPEN, value=0)
                        else:
                            return
                    elif self.robot.read_variable(var_name=R_REQUEST_FIXTURE_CLOSE) == 1:
                        logger.debug(f"{self.name} :: Closing Fixture Slide...")
                        if self._flip_nest_slide(action='close'):
                            self.robot.write_variable(var_name=R_REQUEST_FIXTURE_CLOSE, value=0)
                        else:
                            return
        if self._cur_ff is not None and self._cur_ff.name in {'left_handle', 'dial'} and \
                self.state == 'check_robot_result':
            if self._is_prefetch:
                return super(Station3, self).fsm()
            if self.robot.read_variable(var_name=f"I4{self._cur_ff.index}") == 1:
                time.sleep(1)       # Give some time to let part settle into pallet
                if not self.read_wago_input(name=f'laser_sensor_{self._cur_ff.name}'):
                    self._laser_error = True
                    self.app.btn_build(force='Pause')
                    time.sleep(2)
                    self.app.call_action_door()
                    self.app.add_alarm(dict(
                        msg=f"{self._cur_ff.name} was not detected after placement!"
                            f"\nPlease add part manually and continue.",
                        level='critical',
                        buttons=QMessageBox.Retry,
                        default_button=QMessageBox.Retry,
                        callback=partial(self._on_alarm_closed, self.state)))
                    self.state = 'warning'
                else:
                    return super(Station3, self).fsm()
            time.sleep(0.1)
            return

        return super(Station3, self).fsm()

    def _flip_nest_slide(self, action):
        slide = Station3PartFlipNestSlide(root=self, action=action)
        slide.start()
        s_time = time.time()
        while not slide.is_finished():
            if time.time() - s_time > slide.timeout:
                self.add_alarm(dict(
                    msg="Station3 :: Flip Nest Slide Timeout!",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return False
            time.sleep(.1)
        return True

    def _get_robot_park_i10_value(self):
        # Station3 has 8 parts with reversed ones
        return 9

    def _on_alarm_closed(self, *args):
        state, action = args[:2]
        if self._laser_error:
            self._laser_error = False
            self.state = 'check_robot_result'
            return
        if state == 'has_pallet':
            self.state = 'has_pallet'
        return super()._on_alarm_closed(*args)
