import time
from abc import abstractmethod

from PySide2.QtWidgets import QMessageBox

from routines.base import RoutineBase
from routines.feeder import FlexFeederRoutine
from settings import R_PART_TO_PICK, R_ABORT_SENSOR_CHECK, R_CAMERA_NOT_BLOCKED, \
    R_PARK_COMPLETE, R_DO_PREFETCH, R_PREFETCH_FINISHED, R_WAITING, R_PART_IN_FIXTURE, COGNEX_JOBS
from utils.cognex import CognexVisionController
from utils.denso_robot import DensoRobot
from utils.logger import logger
from utils.wago import WagoController


class BaseStation(RoutineBase):

    def __init__(self, app, conf, feeders, name, p_index, prefetch_parts=None):
        super().__init__(app, conf=conf, name=name)
        self._cur_ff = None
        self.index = int(name[-1])
        self._finished_feeders = {}
        self._robot_error_action = None
        self.feeder_names = feeders
        self.feeders = {f: FlexFeederRoutine(name=f, app=app, root=self, host=self.conf['feeders'].get(f), index=i)
                        for i, f in enumerate(feeders)}
        self.robot = DensoRobot(host=self.conf['robot'], robot_type=self.conf['robot_type'], index=self.index)
        self.wago = WagoController(host=self.conf['wago'])
        self._pallet = app.pallet_handlers[p_index]
        self._pallet.init_conf(self)
        self._part_pos = []
        self._prefetch_parts = prefetch_parts or []
        self._is_prefetch = False
        self.station_alarms = []

    def check_peripherals(self):
        self.cognex = CognexVisionController(host=self.conf['cognex'])
        if not self.cognex.connect():
            self.cognex = None
            return False, "Connecting to Cognex Vision..."

        if not self.wago.connected and not self.wago.connect():
            return False, "Connecting to Wago I/O..."

        for f in self.feeders.values():
            if not f.is_feeder_online():
                return False, f"Feeder({f.name}) is offline!"

        if not self.robot.is_connected() and not self.robot.connect():
            return False, "Connecting to Robot Contoller..."
        if self.robot.get_task_status() != 'READY':
            logger.warning(f"Robot connected and stopping the old program...")
            self.robot.stop_task(mode=4)
        return True, None

    def read_feeder_state(self):
        return {name: f.state for name, f in self.feeders.items()}

    def read_state(self):
        r = {n: f.state for n, f in self.feeders.items()}
        r['pallet'] = self._pallet.state
        r['station'] = self.state
        return r

    def initialize(self):

        if self.cognex is None:
            self.cognex = CognexVisionController(host=self.conf['cognex'])
            if not self.cognex.connect():
                self.cognex = None
                self._add_init_alarm(msg=f"Cognex Vision of the {self.name} is offline!")
                return False
            # Read data without backlight to clear the old values
            self.cognex.read_data()

        if not self.robot.is_connected():
            if not self.robot.connect():
                self._add_init_alarm(msg=f"Robot of the {self.name} is offline!")
                return False
            if self.robot.get_task_status() != 'READY':
                logger.warning(f"Robot connected and stopping the old program...")
                self.robot.stop_task(mode=4)
            self.robot.set_speed(100)
            self.robot_go_home()
        else:
            self.robot.set_speed(100)
            # self.robot.set_io(num=64 if self.index != 4 else 65, val=True)
            # if self.index == 4:
            #    self.robot.set_io(num=68, val=True)
            #    self.robot.set_io(num=70, val=True)
            self.robot_go_home()

        for f in self.feeders.values():
            if not f.is_started():
                f.start()
        s_time = time.time()
        while not all([f.initialized for f in self.feeders.values()]):
            if time.time() - s_time > 20:
                feeders = [f.name for f in self.feeders.values() if not f.initialized]
                logger.error(f"{self.name}: Failed to initialize feeder(s) - {','.join(feeders)}")
                return False
            time.sleep(.1)

        if not self._pallet.is_started():
            self._pallet.start()
        while not self._pallet.initialized:
            if self._pallet.initialized is False:
                return False
            time.sleep(.01)
        self._finished_feeders = {f: True for f in self.feeders.keys() if self._pallet.part_state.get(f)}

    def set_product_type(self, p_type):
        self.cognex.job_change(COGNEX_JOBS[p_type])

    def fsm(self):
        if self.state == "idle":
            if self.robot.read_variable(var_name=R_PARK_COMPLETE) > 0:
                logger.warning(f"{self.robot} is waiting for PARK_COMPLETE...")
                self.robot.write_variable(var_name=R_PARK_COMPLETE, value=0)
            if self.robot.read_variable(var_name=R_PART_IN_FIXTURE) > 0:
                self.add_alarm(dict(
                    type='fixture_error',
                    msg=f'A part may still be placed in its nest at station {self.index}!\n'
                        f'Please remove and then continue.',
                    level='critical',
                    buttons=(['Open', 'Close'] if self.index in {3, 4} else []) + ['Continue'],
                    keep_actions=['Open', 'Close'],
                    callback=self._on_fixture_alarm_closed))
                self.state = 'error'
            for p in self._prefetch_parts:
                if not self._finished_feeders.get(p) and self.feeders[p].is_finished():
                    logger.debug(f"{self.name}:: {p} is available before pallet... pre-fetching...")
                    self._cur_ff = self.feeders[p]
                    self._is_prefetch = True
                    self.app.publish_station_state(
                        data={'type': 'current', 'target': self.name[-1], 'value': self._cur_ff.name})
                    self.state = 'set_position'
                    return
            if not self.app.is_stopped and self._pallet.pallet_ready():
                self.state = 'has_pallet'
        elif self.state == 'has_pallet':
            if self._is_all_parts_marked_done():
                return
            if self.check_robot_paused():
                return
            state = self.robot.get_task_status()
            if state == 'READY':
                self.clear_robot_variables()
                self._move_robot_home()
                self.state = "check_feeder"
            elif state == "DORMANT":
                self.robot.stop_task(mode=4)
                time.sleep(1)
        elif self.state == "check_feeder":
            if self._is_all_parts_marked_done():
                return
            if self.check_robot_paused():
                return
            for name in self.feeders.keys():
                if self._pallet.get_current_pallet_state().get(name) and not self._finished_feeders.get(name):
                    logger.warning(f"{self.name}: {name} is marked as DONE manually!")
                    self._finished_feeders[name] = True
            ready_feeder_name = self.get_ready_feeder()
            if ready_feeder_name:
                logger.info(f"{self.name}: FlexFeeder({ready_feeder_name}) is ready for pick...")
                self._cur_ff = self.feeders[ready_feeder_name]
                self.app.publish_station_state(
                    data={'type': 'current', 'target': self.name[-1], 'value': ready_feeder_name})
                self._pallet.update_pallet_state(state={self._cur_ff.name: False})
                self.state = 'set_position'
            else:
                time.sleep(.5)
        elif self.state == 'set_position':
            self._part_pos = self._cur_ff.read_data()
            logger.debug(f">>> {self.name}: position of {self._cur_ff.name}: {self._part_pos}")
            for j, p in enumerate(self._part_pos[:3]):
                self.robot.write_variable(var_name=f"D{self._cur_ff.index + 1}{j}", value=p)
            self.state = "check_robot_task_ready"
        elif self.state == "check_robot_task_ready":
            if self._cur_ff is None:
                logger.warning(f"{self.name}:: Looks like current feeder is marked as done")
                self._perform_finished_part()
                return
            if self.check_robot_paused():
                return
            # When reversed, we add more offset values to the I10 variable.
            offset = len(self.feeders.keys()) if (len(self._part_pos) == 4 and self._part_pos[3]) else 0
            if self.robot.get_task_status() == 'READY':
                self.robot.write_variable(var_name=R_PART_TO_PICK, value=self._cur_ff.index + 1 + offset)
                if self._is_prefetch:
                    self.robot.write_variable(var_name=R_DO_PREFETCH, value=1)
                else:
                    if self.robot.read_variable(var_name=f"I6{self._cur_ff.index}") == 1:
                        logger.warning(f"{self.robot} - PICKED already set! clearing...")
                        self.robot.write_variable(var_name=f"I6{self._cur_ff.index}", value=0)
                self.robot.start_task()
                logger.warning(f'station {self.index} starting robot...')
                time.sleep(1)       # Give some delay before checking PICKED variable
                self.state = 'check_robot_pick'
        elif self.state == 'check_robot_pick':      # Robot is picking the part here
            if self._cur_ff is None:
                logger.warning(f"{self.name}:: Looks like current feeder is marked as done")
                self._perform_finished_part()
                return
            if self.robot.read_variable(var_name=f"I6{self._cur_ff.index}") == 1:
                logger.warning(f"Picked a part({self._cur_ff.name}) by robot, restarting feed...")
                self._cur_ff.restart_feed()
                time.sleep(1)       # Give some delay before checking PLACED variable
                self.state = 'check_robot_result'
        elif self.state == 'check_robot_result':    # Robot is placing part here
            if self._cur_ff is None:
                logger.warning(f"{self.name}:: Looks like current feeder is marked as done")
                self._perform_finished_part()
                return
            if self._is_prefetch:
                if self.app.is_stopped:
                    logger.debug(f"Station{self.index}: Canceling pre-fetched part because we are stopping!")
                    self.cancel_prefetched_part()
                    self.state = 'stopped'
                    return
                if self._pallet.pallet_ready():
                    self.robot.write_variable(var_name=R_DO_PREFETCH, value=0)
                    self._pallet.update_pallet_state(state={self._cur_ff.name: False})
                    self._is_prefetch = False
                return
            if self.robot.read_variable(var_name=f"I4{self._cur_ff.index}") == 1:
                if self._cur_ff.name == 'hopper':
                    self._cur_ff.restart_feed()
                logger.info(f"{self.name}: finished Pick & Place of {self._cur_ff.name}!")
                self._pallet.update_pallet_state(state={self._cur_ff.name: True})
                self._perform_finished_part()
            time.sleep(.05)
        elif self.state == 'wait_5s':
            if time.time() - self._tick > 5:
                self.robot.continue_task()
                self.state = 'idle'
        elif self.state == 'finished':
            self._pallet.release_pallet()
            self._finished_feeders = {}
            self.state = 'idle'

    def _perform_finished_part(self):
        if self._cur_ff is not None:
            self._finished_feeders[self._cur_ff.name] = True
        self._cur_ff = None
        self._part_pos = []
        if self.app.is_stopped:
            self.state = 'stopped'
        elif all([self._finished_feeders.get(f) for f in self.feeders.keys()]):
            logger.info(f"{self.name}: finished ALL feeders!")
            self.clear_robot_variables()
            self.app.publish_station_state(data={'type': 'current', 'target': self.name[-1], 'value': 'wait'})
            self.state = 'finished'
        else:
            self.state = 'check_feeder'

    def _is_all_parts_marked_done(self):
        if all([self._finished_feeders.get(f) for f in self.feeders.keys()]):
            logger.debug(f"{self.name}:: Looks like ALL feeders are marked as DONE...")
            self.clear_robot_variables()
            self.app.publish_station_state(data={'type': 'current', 'target': self.name[-1], 'value': 'wait'})
            self.state = 'finished'
            return True

    def get_current_feeder_name(self):
        if self._cur_ff:
            return self._cur_ff.name

    def clear_finished_feeders(self):
        self._finished_feeders = {}

    def mark_robot_parked(self, val=True):
        """Used from outside"""
        if self._cur_ff and self._pallet.get_current_pallet_sn():
            self._pallet.update_pallet_state(state={f"{self._cur_ff.name}_parked": val})

    def mark_part_as_done(self, part_name):
        if self._cur_ff and self._cur_ff.name == part_name:
            if self.state == 'check_robot_pick' or part_name == 'hopper':
                self._cur_ff.restart_feed()
            self._perform_finished_part()
        elif part_name in self.feeders:
            self._finished_feeders[part_name] = True

    def disregard_feeder_pos(self, name='', reject=True):
        """User from the FlexFeeder Dialog"""
        ff = self.feeders[name]
        logger.warning(f"{'Rejecting' if reject else 'Disregarding'} the currently picking & placing "
                       f"part({ff.name})...")
        if self.index in (3, 4):                    # Clear flip nest timeout error if part is re-acquired or restarted
            for index in range(len(self.station_alarms)):
                errmsg = [self.station_alarms[index]['msg']]
                search_string = ['Station3 :: Flip Nest Slide Timeout!', 'Slide: TIMEOUT!']
                for msg in errmsg:
                    if any([m in msg for m in search_string]):
                        self.station_alarms.pop(index)
                        break
        if reject:
            ff.reject_part()
        else:
            ff.re_acquire()
        self._cur_ff = None
        self.state = 'idle' if self._is_prefetch else 'has_pallet'

    def check_robot_paused(self):
        return self.app.robot_paused.get(self.name.lower())

    def apply_finished_parts(self):
        for sn, p in self.app.pallets.items():
            # Find currently placed pallet
            if p.get('pos') == 'lift_locate' and p.get('index') == self._pallet.index and not p.get('state'):
                for feeder_name in [f.name for f in self.feeders.values()]:
                    if p.get(feeder_name):
                        self._finished_feeders[feeder_name] = True
                break

    def can_robot_start(self):
        return self.robot.get_task_status() != 'RUN' or self.robot.read_variable(var_name=R_PREFETCH_FINISHED) or \
                                self.robot.read_variable(var_name=R_WAITING)

    def add_alarm(self, alarm):
        logger.warning(f"Station{self.index} alarm::: {alarm.get('msg', '')}")
        self.station_alarms.append(alarm)

    def remove_first_alarm(self):
        if self.station_alarms:
            self.station_alarms = self.station_alarms[1:]

    def _on_station_alarm_closed(self, *args):
        state, action = args[:2]
        if action == 'retry':
            self.state = state
        elif action == 'ignore':
            self.state = 'idle'

    def ready_for_close(self):
        allowed_states = {'stopped', 'idle', 'check_robot_task_ready', 'check_feeder', 'init',
                          'check_robot_task_ready', 'check_robot_unload_finished'}
        return self.state in allowed_states or (self._is_prefetch and self.state == 'check_robot_result')

    def _on_alarm_closed(self, *args):
        state, action = args[:2]
        self._robot_error_action = action
        if action == "retry":
            self.robot.continue_task()
            time.sleep(.5)
            self.state = state
        elif action == "new_part":
            self._cur_ff.restart_feed()
            self._cur_ff = None
            self.robot.write_variable(R_ABORT_SENSOR_CHECK, 1)
            self.robot.continue_task()
            time.sleep(.5)
        elif action == 'cancel':
            self._cur_ff.restart_feed()
            self._cur_ff = None
            self.robot.write_variable(R_ABORT_SENSOR_CHECK, 1)
            self.robot_go_home()
            time.sleep(.5)
        elif action == 'ok':
            self.state = state

    def check_already_finished_pallet(self, code):
        return all([self.app.pallets[code].get(name) for name in self.feeders])

    @abstractmethod
    def get_ready_feeder(self):
        raise NotImplementedError()

    def continue_robot(self):
        self.robot.continue_task()

    def _on_fixture_alarm_closed(self, action):
        if action == 'open':
            self.turn_valve(name='flip_nest_gripper_open' if self.index == 3 else 'right_handle_rotator_slide_close',
                            val=False)
        elif action == 'close':
            self.turn_valve(name='flip_nest_gripper_open' if self.index == 3 else 'right_handle_rotator_slide_close',
                            val=True)
        elif action == 'continue':
            self.state = 'idle'

    def _on_robot_home_confirm_closed(self, *args):
        action = args[0]
        if action == 'yes':
            time.sleep(.5)
            if self._robot_error_action == 'cancel':
                self.state = 'finished'
            else:
                self.robot.continue_task()
                self.state = 'idle'
        elif action == 'pendant':
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Whirl")
            msgbox.setText(f'{self.name}: Plug in teach pendant and manually jog robot to a clear path to home '
                           f'position, remove teach pendant, and then press continue…')
            msgbox.addButton('Continue', QMessageBox.YesRole)
            msgbox.exec_()
            self.robot.turn_motor(True)
            self._tick = time.time()
            self.state = 'wait_5s'

    def read_cognex_position(self, index, ignore_i22=False, check_reversed=False, r_offset=4):
        not_blocked = self.robot.read_variable(var_name=R_CAMERA_NOT_BLOCKED) == 1
        if (not_blocked or ignore_i22) and self.cognex is not None:
            return self.cognex.read_position_data(index, check_reversed=check_reversed, r_offset=r_offset)

    def clear_cognex_results(self):
        self.cognex.clear_results_buffer()

    def reject_pallet(self):
        self.state = 'finished'

    def on_resumed(self):
        if self.state == 'stopped':
            self.state = 'idle'
        self._pallet.resume()
        # if self.robot.get_task_status() != 'READY':
        #     self.robot.continue_task()
        for ff in self.feeders.values():
            ff.resume()

    def on_paused(self):
        self.robot.pause()
        self._pallet.pause()
        for ff in self.feeders.values():
            ff.pause()

    def on_stopped(self):
        if self.app.main_power and self.robot.is_connected():
            self.robot.stop_task()
            self.clear_robot_variables()
        self._pallet.stop()
        for ff in self.feeders.values():
            ff.stop()
        if self.app.main_power and self.cognex is not None and self.cognex.is_connected():
            self.cognex.close()
        self.wago.close(close=self.app.main_power)

    def _get_robot_park_i10_value(self):
        return len(self.feeders.keys()) + 1

    def cancel_prefetched_part(self):
        self.robot.stop_task(mode=4)
        self._move_robot_home()

    def are_pallet_handlers_initialized(self):
        return self._pallet.initialized

    def _move_robot_home(self, stop_flag=None, sig_finish=None):
        if not self.robot.check_paused_and_parked():
            self.robot.write_variable(var_name=R_PART_TO_PICK, value=self._get_robot_park_i10_value())
            time.sleep(.1)
            self.robot.start_task()
            self._wait_until_robot_parked(stop_flag=stop_flag, sig_finish=sig_finish)

            """auto re-acquiring part here in case robot is parked during prefetch"""
            if self._cur_ff is not None:
                name = [self._cur_ff.name]
                if self.index in [1, 3, 4] and self._is_prefetch and any([n in name for n in self._prefetch_parts]):
                    self.disregard_feeder_pos(name=self._cur_ff.name, reject=False)

        else:
            logger.debug('Robot already at home position')
            self.robot.write_variable(var_name=R_CAMERA_NOT_BLOCKED, value=1)
            if self.robot.write_variable(var_name=R_PARK_COMPLETE, value=0):
                if sig_finish is not None:
                    sig_finish.emit(self.index)

    def _wait_until_robot_parked(self, stop_flag=None, sig_finish=None):
        while not self._b_stop.is_set():
            if stop_flag is not None and stop_flag.is_set():
                logger.info(f"{self.robot}: Canceling park...")
                return
            if self.robot.read_variable(var_name=R_PARK_COMPLETE) == 1:
                logger.debug(f"Parking of {self.robot} is finished.")
                if self.robot.write_variable(var_name=R_PARK_COMPLETE, value=0):
                    if sig_finish is not None:
                        sig_finish.emit(self.index)
                    return
            time.sleep(.5)

    # ========== External Functions of Robot ==========
    def read_robot_error(self):
        if self.robot is not None:
            return self.robot.get_cont_error()

    def clear_robot_error(self):
        if self.robot is not None:
            self.robot.clear_cont_error()

    def robot_go_home(self, stop_flag=None, sig_finish=None):
        self.robot.stop_task(mode=4)
        self._move_robot_home(stop_flag=stop_flag, sig_finish=sig_finish)

    def robot_pause(self):
        if self.robot is not None:
            # Set task into "DORMANT" state, which can be continued afterwards.
            self.robot.stop_task(mode=1)

    def set_robot_speed(self, val):
        if self.robot is not None:
            self.robot.set_speed(val)

    def robot_abort_senor_check(self):
        """
        If robot didn't find the part by the sensor(so cannot pick), it stuck while checking sensor value.
        Set I13 as 1 to escape this loop
        """
        self.robot.write_variable(R_ABORT_SENSOR_CHECK, 1)

    def clear_robot_variables(self):
        for v in {'D10', 'D11', 'D12', 'D20', 'D21', 'D22', 'D30', 'D31', 'D32', 'D40', 'D41', 'D42'}:
            self.robot.write_variable(var_name=v, value=999.0)
        for v in {'I40', 'I41', 'I42', 'I43'}:
            self.robot.write_variable(var_name=v, value=0)
