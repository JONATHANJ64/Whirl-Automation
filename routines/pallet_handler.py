import time
from functools import partial

# from PySide2.QtWidgets import QMessageBox

from routines.base import RoutineBase
from routines.pneumatic_slide.pallet_handler_lift_and_locate_slide import PalletHandlerLiftAndLocateSlide
from utils.cognex import CognexBarcodeReader
from utils.common import get_config
from utils.logger import logger


class PalletHandlerRoutine(RoutineBase):

    def __init__(self, app, index=0):
        super().__init__(app, name=f"LL{index}")
        self.index = index
        self.root = None
        self.barcode_reader = None
        self._has_pallet = False
        self.p_conf = get_config()['pallet']
        self._cur_sn = None
        self.part_state = {}
        self.cnt = 0
        self.released = True
        self._cycle_finished = False
        self._next_cycle = False
        self._is_initialized = None

    def init_conf(self, root):
        self.root = root
        self.wago = root.wago
        self.conf = root.conf

    def initialize(self):
        if self.barcode_reader is None:
            self.barcode_reader = CognexBarcodeReader(host=self.conf[f'barcode_{self.index}'])
            if not self.barcode_reader.connect():
                self.initialized = False
                self.barcode_reader = None
                self._add_init_alarm(msg=f"Barcode reader of Lift & Locate {self.index} is offline!")
                return False
        time.sleep(self.p_conf['startup_timeout'])
        # When lift is up, pallet is away from the sensor. So we need to down the lift in advance to check main sensor.
        self._move_slide(action='down', check_current=False, check_target=False)
        if self.index == 6:  # Disengage clamp prior to lift, so movement does not disturb pallet during lift.
            self.turn_valve(name='lift_locate_upper_housing_pallet_clamp_6', val=False)
            time.sleep(1)  # Give some time to allow clamp to fully open.
        self._has_pallet = self.read_wago_sensor(name='main')
        if self._has_pallet:
            self._move_slide(action='up', check_current=False, check_target=False)
            for sn, st in self.app.pallets.items():
                if st.get('pos') == 'lift_locate' and st.get('index') == self.index:
                    logger.debug(f"L&L{self.index} - Current pallet state found - {st}")
                    self._cur_sn = sn
                    self.part_state = st
                    # if st.get('pos') not in 'lift_locate':  # In case pallet arrives during init for previous session
                    #    self.update_pallet_state(state={'pos': 'lift_locate'})
                    break
            if self._cur_sn is None:
                self._move_slide(action='down', check_current=False, check_target=False)
                self._has_pallet = False
                # self._add_init_alarm(msg=f"Unknown pallet found on Lift & Locate {self.index}!")
                # return False      - set back to true to reject unknown pallets on init instead of accepting them

        if self.index == 6:     # Upper Housing Clamp
            self.turn_valve(name='lift_locate_upper_housing_pallet_clamp_6', val=False)
            s_time = time.time()
            while not self.read_wago_input(name='upper_housing_clamp_open'):
                if time.time() - s_time > 5:
                    self._add_init_alarm(msg="Upper Housing Clamp isn't opened after turning on the valve!")
                    return False
                time.sleep(.1)
        if self._move_slide(action='down', check_current=False, check_target=False):
            self._is_initialized = True     # added this so pallet is not released before next station is initialized
            return True

    def fsm(self):
        if self.state == 'idle':
            if self._has_pallet:
                if self._move_slide(action='up'):
                    if self.index == 6:
                        self.turn_valve(name='lift_locate_upper_housing_pallet_clamp_6', val=True)
                    self.released = False
                    self.state = 'pallet_ready'
            else:
                if self.index == 3:     # Lift & Locate 3 doesn't have pre sensor/actuator
                    self.state = 'wait_main_sensor'
                else:
                    if self.app.cycle_ts is not None and \
                            time.time() - self.app.cycle_ts > get_config().get('single_cycle_pallet_timeout', 20):
                        # No pallet arrived
                        self._cycle_finished = True
                        return

                    if self.read_wago_sensor(name='main'):
                        self.state = 'activate_slide'
                        return

                    if self.read_wago_sensor(name='pre'):
                        if self.index == 1 and self.app.is_flush and \
                                all([s.get('flushed') for s in self.app.pallets.values()]):
                            logger.warning("All pallets are blank! Finished flush!")
                            self.app.cancel_all_prefetched_parts()
                            self.app.emit_finished_signal(sig_type='flush')
                            self.state = 'flushed'
                            return
                        self._next_cycle = False
                        logger.debug(f"A pallet has arrived at Lift & Locate {self.index} pre-gate")
                        self._cycle_finished = False
                        self.state = 'actuate_pre_gate'
                    else:
                        time.sleep(.05)
        elif self.state == 'actuate_pre_gate':
            self.write_valve(name='pre', val=True)
            time.sleep(self.p_conf['gate_actuation_time'])
            self.write_valve(name='pre', val=False)
            logger.debug(f"LL{self.index}: Actuated pre-gate, waiting for the main sensor...")
            if not self.read_wago_sensor(name='pre'):
                self.state = 'wait_main_sensor'
            else:
                self.root.add_alarm(dict(
                    msg=f"Lift & Locate {self.index}: Pre-Gate sensor isn't turned off after actuation!",
                    level='critical',
                    buttons=['Retry', 'Abort'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
        elif self.state == 'wait_main_sensor':
            if self.index == 3:     # Doesn't have pre-gate, so check here...
                if self.app.cycle_ts is not None and \
                        time.time() - self.app.cycle_ts > get_config().get('single_cycle_pallet_timeout', 20):
                    # No pallet arrived
                    self._cycle_finished = True
                    return
            if self.read_wago_sensor(name='main'):
                self._next_cycle = False
                self._cycle_finished = False
                logger.debug(f"Lift & Locate {self.index}: A pallet has arrived to the main gate")
                time.sleep(self.p_conf['main_gate_on_delay'])
                self.state = 'activate_slide'
            else:
                time.sleep(.05)
        elif self.state == 'activate_slide':
            self.cnt = 0
            if self._move_slide(action='up'):
                time.sleep(.05)  # Give some delay to stabilize the barcode reader
                if self.index == 6:
                    self.turn_valve(name='lift_locate_upper_housing_pallet_clamp_6', val=True)
                    self.state = 'check_clamp_closed'
                else:
                    self.state = 'scan_barcode'
        elif self.state == 'check_clamp_closed':
            if self.read_wago_input(name='upper_housing_clamp_closed'):
                self.state = 'scan_barcode'
        elif self.state == 'scan_barcode':
            self.released = False
            s_time = time.time()
            code = self.barcode_reader.read_barcode()
            logger.debug(f"Read pallet barcode on Lift & Locate #{self.index}: `{code}`, {time.time() - s_time}")
            if bool(code):
                if code in self.app.pallets:
                    clear_old = False
                    self._cur_sn = code
                    self._has_pallet = True
                    if self.app.is_flush and self.app.pallets[code].get('flushed'):
                        logger.debug(f"Blank pallet has arrived to LL{self.index} during the flush, bypassing...")
                        self.state = 'ready_for_release'
                        return
                    elif self.app.pallets[code].get('is_new'):
                        if self.index == 1:
                            logger.debug(f"Starting a new pallet({code}) from LL1...")
                            clear_old = True    # Set this value True so that `is_new` field is removed
                        else:         # bypass this pallet until LL1
                            self.state = 'ready_for_release'
                            return
                    else:
                        state = self.app.pallets[code].get('state')
                        if state == 'remove':
                            self.root.add_alarm(dict(
                                msg=f"Pallet({code}) is no longer valid, please remove it from conveyor and press Ok ",
                                level='critical',
                                buttons=['Continue'],
                                callback=partial(self._on_alarm_closed, 'ask_remove_pallet')))
                            self.state = 'warning'
                            return
                        elif state == 'reject':
                            if self.index == 7:
                                self.root.add_alarm(dict(
                                    msg=f"Pallet({code}) was rejected, please clear any components from the pallet "
                                        f"and then press Continue",
                                    level='critical',
                                    buttons=['Continue'],
                                    callback=partial(self._on_alarm_closed, 'ask_reject_pallet')))
                                self.state = 'warning'
                            else:
                                logger.debug(f"LL #{self.index}: Pallet {code} is rejected, bypassing...")
                                self.state = 'ready_for_release'
                            return
                        elif self.root.check_already_finished_pallet(code):
                            logger.warning(f"All feeders of {self.root.name} are already finished, bypassing...")
                            self.state = 'ready_for_release'
                            return

                    self.update_pallet_state(state={'pos': 'lift_locate', 'index': self.index, 'ts': time.time(),
                                                    'state_num': self.root.index if hasattr(self.root, 'index') else 0},
                                             clear_old=clear_old)
                    self.state = 'pallet_ready'
                else:
                    if len(self.app.pallets.keys()) < get_config()['pallet'].get('count', 20):
                        self._cur_sn = code
                        self._on_alarm_closed('ask_new_pallet', 'yes')
                        # self.app.add_alarm(dict(
                        #     msg=f"A new pallet({code}) has appeared on Lift & Locate {self.index}, add this?",
                        #     level='critical',
                        #     buttons=QMessageBox.Yes | QMessageBox.No,
                        #     default_button=QMessageBox.No,
                        #     callback=partial(self._on_alarm_closed, 'ask_new_pallet')))
                    else:
                        self.root.add_alarm(dict(
                            msg=f"A new pallet({code}) has appeared on Lift & Locate {self.index}, but no space left!",
                            level='critical',
                            buttons=['Ok'],
                            callback=partial(self._on_alarm_closed, 'new_pallet_no_space')))
                        self.state = 'warning'
            elif self.cnt < 3:
                self.cnt += 1
                time.sleep(1)
            else:
                self.root.add_alarm(dict(
                    msg=f"Barcode scanner at Lift and Locate {self.index}: failed to read valid data",
                    level='critical',
                    buttons=['Retry', 'Abort'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
                # self._move_slide(action='down')
                # TODO: Add action when pallet is invalid here.
        elif self.state == 'pallet_ready':    # The station is working here.
            pass
        elif self.state == 'ready_for_release':
            if self.app.cycle_ts is not None and not self._next_cycle:
                self._cycle_finished = True
                return
            if self.can_release():
                self._next_cycle = False
                if self.index == 6:
                    self.turn_valve(name='lift_locate_upper_housing_pallet_clamp_6', val=False)
                    self.state = 'check_clamp_open'
                else:
                    if self._move_slide(action='down'):
                        self.state = 'actuate_main_gate'
            else:
                time.sleep(.1)
        elif self.state == 'check_clamp_open':
            if self.read_wago_input(name='upper_housing_clamp_open'):
                if self._move_slide(action='down'):
                    self.state = 'actuate_main_gate'
        elif self.state == 'actuate_main_gate':
            time.sleep(self.p_conf['release_delay'][str(self.index)])
            self.write_valve(name='main', val=True)
            time.sleep(self.p_conf['gate_actuation_time'])
            self.write_valve(name='main', val=False)
            time.sleep(1.0)
            if self.read_wago_sensor(name='main'):  # Make sure pallet is really gone before updating state
                self.root.add_alarm(dict(
                    msg=f"Pallet was not released from lift and locate {self.index}",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
                return
            self.update_pallet_state(
                state={'pos': 'transit', 'index': (self.index + 1) if self.index < 7 else 1, 'ts': time.time()}
            )
            self._has_pallet = False
            time.sleep(.5)
            self._cur_sn = None
            self.released = True
            self._cycle_finished = False
            self.state = 'idle'

    def get_station_alarms(self):
        if hasattr(self.root, 'station_alarms'):
            return self.root.station_alarms
        else:
            return []

    def is_finished_one_cycle(self):
        return self._cycle_finished

    def cycle_one(self):
        self._next_cycle = True
        self._cycle_finished = False

    def update_pallet_state(self, state, clear_old=False):
        self.app.publish_pallet_state(sn=self._cur_sn, state=state, clear_old=clear_old)

    def get_current_pallet_state(self):
        return self.app.pallets.get(self._cur_sn, {})

    def can_release(self):
        next_index = (self.index + 1) if self.index < 7 else 1
        spacing = self.p_conf["spacing"][str(self.index)]
        if spacing > 0:
            return len([p for p in self.app.pallets.values()
                        if p.get('pos') == 'transit' and p.get('index') == next_index]) < spacing
        else:
            return self.app.pallet_handlers[self.index].can_accept_next_pallet() and \
               not self.app.pallet_handlers[next_index].has_pallet() and \
               self.app.pallet_handlers[next_index].is_initialized()

    def _move_slide(self, action='up', check_current=False, check_target=False):
        slide = PalletHandlerLiftAndLocateSlide(pallet=self, action=action, check_current=check_current,
                                                check_target=check_target, timeout=4)
        slide.start()
        s_time = time.time()
        while not slide.is_finished():
            if time.time() - s_time >= slide.timeout:
                self.root.add_alarm(dict(
                    msg=f"Lift & Locate{self.index} :: Slide({action}) Timeout!",
                    level='critical',
                    buttons=['Retry', 'Ignore'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
                return False
            time.sleep(.1)
        return True

    def can_accept_next_pallet(self):
        return self._has_pallet and self.initialized

    def is_initialized(self):
        return self._is_initialized

    def pallet_ready(self):
        return self.state == 'pallet_ready'

    def has_pallet(self):
        return self._has_pallet

    def release_pallet(self):
        self.state = 'ready_for_release'

    def read_wago_sensor(self, name):
        return self.read_wago_input(name=f"lift_locate_{name}_{self.index}")

    def write_valve(self, name, val):
        self.turn_valve(name=f'lift_locate_{name}_{self.index}', val=val)

    def get_current_pallet_sn(self):
        return self._cur_sn

    def _on_alarm_closed(self, *args):
        state, action = args[:2]
        if state == 'ask_new_pallet':
            if action == 'yes':   # Add a new pallet
                if self.index == 1:
                    self._has_pallet = True
                    self.update_pallet_state(state={'pos': 'lift_locate', 'index': self.index, 'ts': time.time()})
                    self.state = 'pallet_ready'
                else:
                    self.update_pallet_state(
                        state={'pos': 'lift_locate', 'index': self.index, 'ts': time.time(), 'is_new': True})
                    self.state = 'ready_for_release'
            elif action == 'no':    # Remove this pallet
                self._cur_sn = None
                self.root.add_alarm(dict(
                    msg=f"Please remove the pallet from Lift & Locate {self.index} and press OK",
                    level='critical',
                    buttons=['Ok'],
                    callback=partial(self._on_alarm_closed, 'remove_pallet')))
        elif state == 'new_pallet_no_space':
            self.root.add_alarm(dict(
                msg=f"Please remove the pallet from Lift & Locate {self.index} and press OK",
                level='critical',
                buttons=['Ok'],
                callback=partial(self._on_alarm_closed, 'remove_pallet')))
        elif state == 'actuate_pre_gate':
            if action == 'retry':
                self.state = state
            else:
                self.state = 'idle'
        elif state == 'remove_pallet':
            self.state = 'idle'
        elif state == 'scan_barcode':
            if action == 'retry':
                self.cnt = 0
                self.state = 'scan_barcode'
            else:
                self.state = 'idle'
        elif state in {'ask_reject_pallet', 'ask_remove_pallet'}:
            if action == 'continue':
                self.update_pallet_state(state={'state': None}, clear_old=True)
                self.state = 'ready_for_release'
        elif state == 'actuate_main_gate':
            if action == 'retry':
                self.state = 'actuate_main_gate'
        else:
            if action == 'retry':
                self.state = state
            elif action == 'ignore':
                self.state = 'idle'

    def on_stopped(self):
        pass

    def on_resumed(self):
        if self.state == 'flushed':
            self.state = 'idle'

    def on_paused(self):
        pass
