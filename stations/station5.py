import copy
import time
from functools import partial

from PySide2.QtWidgets import QMessageBox

from routines.pneumatic_slide.station5_box_clamp import Station5BoxClamp
from routines.pneumatic_slide.station5_box_cylinder import Station5BoxCylinder
from routines.pneumatic_slide.station5_rotary_fixture import Station5RotaryFixture
from settings import R_TASK_COMPLETED, R_PART_TO_PICK, R_UNLOAD_FINISHED, \
    R_UNLOAD_MODE, R_UNLOAD_DIRECTION, R_UNLOAD_PLACE_POINT, R_UNLOAD_ROTARY_HOME, R_UNLOAD_ROTARY_180, R_BOXING_MODE, \
    R_BOXING_FINISHED, R_BOXING_START_WAIT_SENSOR3, R_BOX_PULLED, PRODUCT_BARCODES
from stations.base import BaseStation
from routines.labeler import Labeler
from utils.cognex import CognexBarcodeReader
from utils.common import get_config, update_config_file
from utils.logger import logger


class Station5(BaseStation):

    def __init__(self, app):
        super().__init__(app, conf=get_config()['station5'], feeders=['lower_housing', ], name='Station5', p_index=1)
        self.barcode_reader = None
        self.labeler = Labeler(app=app, root=self)
        self._barcode_cnt = 0
        self._label_fails = 0
        self._parts_cnt = None
        self._has_box = False
        self._manually_unloaded = False
        self._final_passed = False

    def get_ready_feeder(self):
        if self.feeders['lower_housing'].is_finished():
            return 'lower_housing'

    def initialize(self):
        en_labeler = self.conf.get('labeler', {}).get('enabled')
        if en_labeler:
            if not self.labeler.is_started():
                self.labeler.start()
            s_time = time.time()
            while not self.labeler.initialized:
                if time.time() - s_time > 2:
                    return False
                time.sleep(.001)

        if self.barcode_reader is None:
            self.barcode_reader = CognexBarcodeReader(host=self.conf['barcode_labeler'])
            if not self.barcode_reader.connect():
                self.barcode_reader = None
                self._add_init_alarm(msg="Barcode reader of the Station5 is offline!")
                return False

        if self.conf['unload_mode'] == 'boxing' and not self._init_boxing_situation():
            return False

        val = super(Station5, self).initialize()
        if val is not False:
            self.robot.write_variable(var_name="I58", value=0 if en_labeler else 1)
        return val

    def _init_boxing_situation(self):
        # Boxing initialization
        if not self._slide_box_clamp(action='engage'):
            return False
        if not self._actuate_box_cylinder(action='retract', check_target=False):
            return False

        self._has_box = self.read_wago_input(name='boxing_sensor_2')
        if not self._slide_box_clamp(action='retract'):
            return False
        if self._has_box:
            if self._parts_cnt is None:
                self.add_alarm(dict(
                    msg="Box detected in the loading area, "
                        "please confirm number of parts in current box before continuing!",
                    level='init-box-detected',
                    buttons=['Confirm'],
                    callback=partial(self._on_station_alarm_closed, "init-box-detected")))
                self.state = 'warning'
                return False
            else:   # Engage the clamp so that we can continue working
                if not self._slide_box_clamp(action='engage'):
                    return False
        else:
            if self._parts_cnt is not None:
                self.add_alarm(dict(
                    msg="Previously detected box no longer present, OK to feed a new box?",
                    level='critical',
                    buttons=['OK'],
                    callback=partial(self._on_station_alarm_closed, "init-box-disappeared")))
                self.state = 'warning'
                return False
        return True

    def read_state(self):
        r = {n: f.state for n, f in self.feeders.items()}
        r['labeler'] = self.labeler.state
        r['pallet'] = self._pallet.state
        r['station'] = self.state
        return r

    def read_labeler_state(self):
        return self.labeler.read_current_state()

    def _is_all_parts_marked_done(self):
        if self._pallet.get_current_pallet_state().get('count') is None:  # Ignore finished parts
            return super(Station5, self)._is_all_parts_marked_done()

    def fsm(self):
        if self.state == "idle":
            if self._parts_cnt == 7:
                # Box is in the boxing platform and we have already 6 finished parts.. let's just send it to the sealer.
                self.state = 'start_move_box_away_to_sealer'
                self._parts_cnt = 1
                return
            if self._has_box:
                if self.read_wago_input(name='boxing_sensor_2') and self.read_wago_input(name='box_clamp_retracted'):
                    self._slide_box_clamp(action='engage')  # Need this in case user resets boxing routine
                if not self.read_wago_input(name='boxing_sensor_2'):
                    logger.warning(f"Station5:: Something is wrong.. I don't have any box now!")
                    self._has_box = False
            else:
                if self.read_wago_input(name='boxing_sensor_2'):
                    self.add_alarm(dict(
                        msg="Box detected in the loading area, "
                            "please confirm number of parts in current box before continuing!",
                        level='init-box-detected',
                        buttons=['Confirm', 'Back'],
                        callback=partial(self._on_station_alarm_closed, "box-detected-abnormally")))
                    self.state = 'warning'
                    return
                if self.read_wago_input(name='boxing_sensor_1'):
                    logger.debug(f"Station5:: New blank box is available from erector, pulling it now...")
                    self.state = 'pull_box_from_erector'
                    return
            super(Station5, self).fsm()
        elif self.state == 'check_feeder':
            if self.check_robot_paused():
                return
            count = self._pallet.get_current_pallet_state().get('count')
            if count is not None:       # Finished part...
                logger.debug(f"Station5: A finished part has arrived, count: {count}")
                conf = get_config()['station3']['test']
                self._final_passed = conf['low_pass'] <= count <= conf['high_pass']
                self.state = f"start_unload_{self.conf['unload_mode']}"
            else:                       # Blank part...
                if self.app.is_flush:
                    logger.debug("Station5: bypassing the unloaded pallet...")
                    self._pallet.update_pallet_state(state={"flushed": True})
                    self.state = 'finished'
                else:
                    self._pallet.update_pallet_state(state={"start_ts": time.time()})
                    super(Station5, self).fsm()

        # ===================== Unloading =====================
        elif self.state == 'start_unload_binning':          # Binning
            self.robot.write_variable(var_name=R_UNLOAD_MODE, value=0)
            self.robot.write_variable(var_name=R_UNLOAD_DIRECTION, value=0)
            self.robot.write_variable(var_name=R_UNLOAD_PLACE_POINT, value=0)
            self.state = 'check_robot_binning_unload_task_ready'
        elif self.state == "check_robot_binning_unload_task_ready":
            if self.check_robot_paused():
                return
            if self.robot.get_task_status() == 'READY':
                self.robot.write_variable(var_name=R_PART_TO_PICK, value=2 if self._final_passed else 3)
                if self._final_passed:
                    if self.read_wago_input('product_exit_conveyor'):
                        self.add_alarm(dict(
                            msg="Object detected on the exit conveyor, "
                                "please remove object to continue current operation.",
                            level='critical',
                            buttons=['Retry'],
                            callback=partial(self._on_station_alarm_closed, self.state)))
                        self.state = 'warning'
                        return
                else:
                    if self.read_wago_input('reject_conveyor_sensor'):
                        self.add_alarm(dict(
                            msg="Object detected on the reject conveyor, "
                                "please remove object to continue current operation.",
                            level='critical',
                            buttons=['Retry'],
                            callback=partial(self._on_station_alarm_closed, self.state)))
                        self.state = 'warning'
                        return
                self.robot.start_task()
                self.state = 'check_robot_unload_finished'

        elif self.state == 'start_unload_boxing':           # Boxing
            if not self._has_box:
                self.state = 'idle'
                return
            if self._parts_cnt is None or self._parts_cnt == 0:
                self._parts_cnt = 1
            self.robot.write_variable(var_name=R_UNLOAD_MODE, value=1)
            self.robot.write_variable(var_name=R_UNLOAD_DIRECTION, value=1 if self._parts_cnt <= 3 else 0)
            self.robot.write_variable(var_name=R_UNLOAD_PLACE_POINT, value=self._parts_cnt)
            self.state = 'check_robot_boxing_unload_task_ready'
        elif self.state == 'check_robot_boxing_unload_task_ready':
            if self.check_robot_paused():
                return
            if self.robot.get_task_status() == 'READY':
                self.robot.write_variable(var_name=R_PART_TO_PICK, value=2 if self._final_passed else 3)
                if not self._final_passed:
                    if self.read_wago_input('reject_conveyor_sensor'):
                        self.add_alarm(dict(
                            msg="Object detected on the reject conveyor, "
                                "please remove object to continue current operation.",
                            level='critical',
                            buttons=['Retry'],
                            callback=partial(self._on_station_alarm_closed, self.state)))
                        self.state = 'warning'
                        return
                self.robot.start_task()
                self.state = 'unload_boxing_home' if self._final_passed else 'check_robot_unload_finished'
        elif self.state == 'unload_boxing_home':
            if self.robot.read_variable(var_name=R_UNLOAD_ROTARY_HOME) > 0:
                logger.debug(f"{self.name}: Moving rotary fixture HOME")
                if self.read_wago_input(name='whirl_rotator_part_presence'):
                    self.add_alarm(dict(
                        msg="Whirl detected in rotator, please remove from fixture manually and press RETRY.",
                        level='warning',
                        buttons=['Retry'],
                        default_button=QMessageBox.Retry,
                        callback=partial(self._on_alarm_closed, "unload_boxing_home")))
                    self.state = 'warning'
                else:
                    if self._rotary_fixture_slide(action='home'):
                        if self.robot.write_variable(var_name=R_UNLOAD_ROTARY_HOME, value=0):
                            self.state = 'unload_boxing_180' if self._parts_cnt <= 3 else 'check_robot_unload_finished'
        elif self.state == 'unload_boxing_180':
            if self.robot.read_variable(var_name=R_UNLOAD_ROTARY_180) > 0:
                logger.debug(f"{self.name}: Moving rotary fixture 180")
                if not self.read_wago_input(name='whirl_rotator_part_presence'):
                    self.add_alarm(dict(
                        msg="Whirl NOT detected in rotator, please place in fixture manually and press RETRY.",
                        level='warning',
                        buttons=['Retry'],
                        callback=partial(self._on_alarm_closed, "unload_boxing_180")))
                    self.state = 'warning'
                else:
                    if self._rotary_fixture_slide(action='rotate'):
                        if self.robot.write_variable(var_name=R_UNLOAD_ROTARY_180, value=0):
                            self.state = 'check_robot_unload_finished'
        elif self.state == 'check_robot_unload_finished':
            if self.robot.read_variable(var_name=R_UNLOAD_ROTARY_HOME) > 0:
                self.robot.write_variable(var_name=R_UNLOAD_ROTARY_HOME, value=0)
            if self.robot.read_variable(var_name=R_UNLOAD_FINISHED):
                logger.debug(f"Station5: Finished unloading...")
                self.robot.write_variable(var_name=R_UNLOAD_FINISHED, value=0)
                self.state = 'finish_unloading'
        elif self.state == 'finish_unloading':
            self._update_tracking_status()
            # Finished unloading here and we clear the pallet state
            self._pallet.update_pallet_state(state={"pos": "lift_locate", 'index': 1, 'state_num': 5}, clear_old=True)
            if self.conf['unload_mode'] == 'binning':
                conf = get_config()['station5']
                unload_num = conf.get('unload_num', 1)
                new_num = copy.deepcopy(unload_num)
                if self._final_passed and not self._manually_unloaded:
                    new_num = unload_num + 1
                    update_config_file({'station5': {'unload_num': new_num}})
                self._manually_unloaded = False
                if conf['en_binning_track'] and new_num >= conf['bin_full_count']:
                    time.sleep(.5)
                    self.app.pause_robot(self.index)
                    self.add_alarm(dict(
                        msg=f"Product bin is full({conf['bin_full_count']}), please empty and reset counter.",
                        level='critical',
                        buttons=['Reset'],
                        callback=partial(self._on_station_alarm_closed, 'check_feeder')))
                    self.state = 'bin_full'
                    return
            else:       # boxing mode
                box_full = self._parts_cnt == 6 and self._final_passed
                if self._final_passed and not self._manually_unloaded:
                    self._parts_cnt = 1 if self._parts_cnt == 6 else (self._parts_cnt + 1)
                self._manually_unloaded = False
                if box_full:
                    logger.debug("Box is full in boxing mode.")
                    self.state = 'start_move_box_away_to_sealer'
                    return
            super(Station5, self).clear_finished_feeders()
            time.sleep(1)  # Give some delay so that state is cleared enough.
            self.state = 'check_feeder'

        elif self.state == 'pause_robot':
            self.robot.stop_task(mode=4)
            time.sleep(2)
            self.robot_go_home()
            self.state = 'robot_paused'
        elif self.state == 'robot_paused':
            pass

        elif self.state == 'pull_box_from_erector':
            if not self._slide_box_clamp(action='retract'):
                return
            if self.check_robot_paused():
                return
            if self.read_wago_input(name='boxing_sensor_3'):
                self.add_alarm(dict(
                    msg="Obstruction detected at sensor 3 (box sealer entrance), "
                        "please remove obstruction before continuing!",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, "blockage-at-sensor3")))
                self.state = 'warning'
                return
            self.robot.write_variable(var_name=R_PART_TO_PICK, value=4)
            self.robot.write_variable(var_name=R_BOXING_MODE, value=2)
            while self.robot.get_task_status() != 'READY':
                time.sleep(0.1)
            self.robot.start_task()
            while self.robot.read_variable(var_name=R_BOXING_FINISHED):    # waiting for this var to be set back to 0
                time.sleep(0.1)
            self.state = 'wait_for_pull_from_erector'
        elif self.state == 'wait_for_pull_from_erector':
            if self.robot.read_variable(var_name=R_BOX_PULLED):
                logger.debug("Station5: Robot has finished pulling from the erector.")
                self.state = 'engage_clamp_to_check_sensor_2'
        elif self.state == 'engage_clamp_to_check_sensor_2':
            if self._slide_box_clamp(action='engage'):
                if self.read_wago_input(name='boxing_sensor_2'):
                    logger.info("Station5: Box has arrived to the platform!")
                    self._has_box = True
                    self.state = 'idle'

        # Boxing Final...
        elif self.state == 'start_move_box_away_to_sealer':
            if self.read_wago_input(name='boxing_sensor_3'):
                self.add_alarm(dict(
                        msg="Cannot load current box into box sealer, obstruction on loading platform detected.",
                        level='critical',
                        buttons=['Retry'],
                        callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return
            if not self.read_wago_input(name='box_cylinder_retracted'):
                self.add_alarm(dict(
                    msg="Box pusher retract was not detected, please retract the pusher, and press RETRY",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return
            if not self._slide_box_clamp(action='retract'):
                return
            if self.check_robot_paused():
                return
            self.robot.write_variable(var_name=R_PART_TO_PICK, value=4)
            self.robot.write_variable(var_name=R_BOXING_MODE, value=1)
            self.robot.write_variable(var_name=R_BOXING_START_WAIT_SENSOR3, value=0)
            self.robot.start_task()
            self.state = 'box_seal_wait_robot_i13'
        elif self.state == 'box_seal_wait_robot_i13':
            self._has_box = self.read_wago_input(name='boxing_sensor_2')
            if self.robot.read_variable(var_name=R_BOXING_START_WAIT_SENSOR3):
                if self.read_wago_input(name='boxing_sensor_3'):
                    self.robot.write_variable(var_name=R_BOXING_START_WAIT_SENSOR3, value=0)
                    self.state = 'box_extend_cylinder'
                else:
                    self.app.pause_robot(self.index)
                    self.add_alarm(dict(
                        msg="Box arrival not detected at the box sealer entrance, "
                            "please park robot 5 and manually remove the box.",
                        level='critical',
                        buttons=['Retry'],
                        callback=partial(self._on_station_alarm_closed, 'warning')))
                    self.state = 'warning'
        elif self.state == 'box_extend_cylinder':
            if not self._actuate_box_cylinder(action='extend'):
                self.app.pause_robot(self.index)
                return
            if self.read_wago_input(name='boxing_sensor_3'):
                self.app.pause_robot(self.index)
                self.add_alarm(dict(
                    msg="Box still detected at the box sealer entrance, "
                        "please park robot 5 and manually remove the box.",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, 'warning')))
                self.state = 'warning'
                return
            if not self._actuate_box_cylinder(action='retract', check_target=False):
                return
            self.state = 'idle'

        # ===================== Labeling =====================
        elif self.state == 'check_robot_result':
            if not get_config()['station5'].get('labeler', {}).get('enabled'):
                super(Station5, self).fsm()
                return
            self.robot.write_variable(var_name="I57", value=0)      # Clear the variable
            if self.robot.read_variable(var_name="I53") == 1:
                logger.debug("Station5: picked lower housing and ready to apply label")
                self.state = 'check_labeler'
            time.sleep(.5)
        elif self.state == 'check_labeler':
            if not get_config()['station5'].get('labeler', {}).get('enabled') or self.labeler.is_ready():
                logger.debug("Station5: Labeler is ready... applying now..")
                self.robot.write_variable(var_name="I54", value=1)
                self.state = 'check_ready_for_barcode'
        elif self.state == 'check_ready_for_barcode':
            if self.robot.read_variable(var_name="I55"):
                self.robot.write_variable(var_name="I54", value=0)
                logger.debug("Station5: reading barcode...")
                self._barcode_cnt = 0
                self.state = 'read_barcode'
            else:
                time.sleep(.3)
        elif self.state == 'read_barcode':
            code = self.barcode_reader.read_barcode()
            if PRODUCT_BARCODES[self.app.product_type] in code:
                logger.debug("Station5: correct barcode... placing it on the pallet")
                self.robot.write_variable(var_name="I56", value=1)
                self._label_fails = 0
                self._barcode_cnt = 0
                self.labeler.start_labeler()
                self.state = 'check_robot_placement_result'
            else:
                if self._barcode_cnt < 2:
                    self._barcode_cnt += 1
                    time.sleep(0.5)
                else:
                    self.state = 'reject_lower_housing'
        elif self.state == 'reject_lower_housing':
            if self.check_robot_paused():
                return
            if self.read_wago_input('reject_conveyor_sensor'):
                self.add_alarm(dict(
                    msg="Object detected on the reject conveyor, "
                        "please remove object to continue current operation.",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return
            self.robot.write_variable(var_name="I57", value=1)
            self.state = 'check_robot_labeling_completed'
            if self._label_fails < 3:
                self._label_fails += 1
            else:
                self._label_fails = 0
                self.add_alarm(dict(
                    msg="Multiple failed label applications (3) detected, please inspect labeler before continuing.",
                    level='warning',
                    buttons=['Close'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
        elif self.state == 'check_robot_placement_result':
            if self.robot.read_variable(var_name="I40") == 1:
                logger.info("Station5: finished Place of lower housing!")
                self.robot.write_variable(var_name="I56", value=0)
                self._pallet.update_pallet_state(state={'lower_housing': True})
                # self._move_robot_home() - Redundant
                self._cur_ff = None
                self.state = 'finished'
            time.sleep(.5)
        elif self.state == "check_robot_labeling_completed":
            if self.robot.read_variable(var_name=R_TASK_COMPLETED):
                self.labeler.start_labeler()
                logger.debug("Station5: Robot has finished labeling task, returning home...")
                self.state = 'finished' if self._barcode_cnt == 0 else 'idle'
            else:
                time.sleep(.5)
        else:
            super(Station5, self).fsm()

    def _update_tracking_status(self):
        t_info = get_config().get('tracking', {})
        total_time = t_info.get('total', 0) * t_info.get('avg_build_time', 0)
        reject_time = t_info.get('rejected', 0) * t_info.get('avg_reject_time', 0)
        elapsed = time.time() - self._pallet.get_current_pallet_state().get('start_ts', 0)
        if self._final_passed:
            t_info['total'] = t_info.get('total', 0) + 1
            t_info['total_current'] = t_info.get('total_current', 0) + 1
            t_info['avg_build_time'] = (total_time + elapsed) / t_info['total']
        else:
            t_info['rejected'] = t_info.get('rejected', 0) + 1
            t_info['rejected_current'] = t_info.get('rejected_current', 0) + 1
            t_info['avg_reject_time'] = (reject_time + elapsed) / t_info['rejected']
        update_config_file(data={'tracking': t_info})

    def _rotary_fixture_slide(self, action):
        slide = Station5RotaryFixture(root=self, action=action)
        slide.start()
        s_time = time.time()
        while not slide.is_finished():
            if time.time() - s_time > slide.timeout:
                self.add_alarm(dict(
                    msg="Station5 :: Rotary Fixture Slide Timeout!",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return False
            time.sleep(.1)
        return True

    def _slide_box_clamp(self, action='engage'):
        slide = Station5BoxClamp(root=self, action=action)
        slide.start()
        s_time = time.time()
        while not slide.is_finished():
            if time.time() - s_time > slide.timeout:
                self.add_alarm(dict(
                    msg=f"Station5 :: Box Clamp {action.capitalize()} Timeout!",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return False
            time.sleep(.1)
        return True

    def _actuate_box_cylinder(self, action='extend', check_target=False):
        slide = Station5BoxCylinder(root=self, action=action, check_target=check_target)
        slide.start()
        s_time = time.time()
        while not slide.is_finished():
            if time.time() - s_time > slide.timeout:
                msg = 'Station5 :: Box Cylinder Retract Timeout!' if action != 'extend' else \
                    'Box pusher retract was not detected once pushed the cylinder!\nRetract the pusher, and press RETRY'
                self.add_alarm(dict(
                    msg=msg,
                    level='critical',
                    buttons=['Retry'] if action != 'extend' else ['Retry'],
                    callback=partial(self._on_station_alarm_closed, self.state)))
                self.state = 'warning'
                return False
            time.sleep(.1)
        return True

    def check_already_finished_pallet(self, code):
        # For Robot 5, finished parts(with `count` value) shouldn't be marked as finished.
        state = self.app.pallets[code]
        return state.get('count') is None and all([state.get(name) for name in self.feeders])

    def unload_manually(self):
        self._manually_unloaded = True
        self.state = 'finish_unloading'

    def restart_after_bin_full(self):
        self.state = 'check_feeder'

    def get_current_part_count_in_box(self):
        if self._has_box:
            if self._parts_cnt == 0:
                return 0
            else:
                return self._parts_cnt - 1

    def update_current_part_count_in_box(self, val):
        self._parts_cnt = val + 1   # parts count in box starts at 0, self._parts_cnt start at 1

    def restart_boxing_final(self):
        self.state = 'idle'

    def _on_station_alarm_closed(self, *args):
        state, action = args[:2]
        if state == 'init-box-detected':
            self._parts_cnt = args[2] + 1
            logger.info(f">>> Station5 :: Initial part counter in the detected box - {self._parts_cnt}")
            self.state = 'init'
        elif state == 'box-detected-abnormally':
            self._parts_cnt = args[2] + 1
            logger.info(f">>> Station5 :: Recovered box count from the abnormal situation - {self._parts_cnt}")
            self._has_box = True
            self.state = 'idle'
        elif state == 'init-box-disappeared':
            self._parts_cnt = None      # Clear the parts counter because the box has disappeared! :)
            self.state = 'init'
        elif state == 'unload_boxing_180':
            if action == 'retry':
                self.state = 'unload_boxing_180'
        elif state == 'unload_boxing_home':
            if action == 'retry':
                self.state = 'unload_boxing_home'
        elif state == 'check_robot_labeling_completed':
            if action == 'close':
                self.state = state
        elif state == "blockage-at-sensor3":
            if action == 'retry':
                self.state = 'idle'
        elif state in 'reject_lower_housing' or 'check_robot_labeling_completed' \
                or 'check_robot_binning_unload_task_ready' or 'check_robot_boxing_unload_task_ready':
            if action == 'retry':
                self.state = state
        else:
            return super()._on_station_alarm_closed(*args)

    def _on_alarm_closed(self, *args):
        state, action = args[:2]
        if state == 'finished' and action == 'retry':
            logger.info("Restarting the whole flow...")
            self._pallet.release_pallet()
            self.state = 'idle'
        elif state in {'unload_boxing_home', 'unload_boxing_180'}:
            if action.lower() == 'retry':
                self.state = state
            else:
                logger.warning(f"Station5 - aborted unloading(boxing) {'BEFORE' if 'home' in state else 'AFTER'} "
                               f"rotary HOME...")
                self.state = 'pause_robot'
                self.app.robot_paused['station5'] = 'other'
                self.app.pause_station_robot_button(index=5)
        else:
            return super(Station5, self)._on_alarm_closed(args)

    def _get_robot_park_i10_value(self):
        return 5

    def on_paused(self):
        self.labeler.pause()
        super(Station5, self).on_paused()

    def on_resumed(self):
        self.labeler.resume()
        super(Station5, self).on_resumed()

    def on_stopped(self):
        self.labeler.stop()
        super(Station5, self).on_stopped()
