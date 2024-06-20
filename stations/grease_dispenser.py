import time
from functools import partial

from PySide2.QtWidgets import QMessageBox

from routines.base import RoutineBase
from utils.common import get_config, get_valve_bit_value
from utils.logger import logger


class GreaseDispenser(RoutineBase):

    def __init__(self, app):
        super().__init__(app, conf=get_config()['station1'], name='grease_dispenser')
        self._is_purge = False
        self._is_normal = True
        self._pallet = app.pallet_handlers[2]
        self.station_alarms = []

    def initialize(self):
        self.wago = self.app.stations['station1'].wago
        self._pallet.init_conf(self)
        if not self._reset_valves():
            self._add_init_alarm(msg="Grease Dispenser: Cannot read Valve status!")
            return False
        if not self._pallet.is_started():
            self._pallet.start()
        while not self._pallet.initialized:
            if self._pallet.initialized is False:
                return False
            time.sleep(.01)

    def set_product_type(self, p_type):
        pass

    def _reset_valves(self):
        cur_state = self.valve.read_data(slave_id=self.slave_id)
        if cur_state is None:
            return False
        for name, ch in self.conf['valve'].items():
            if name.startswith('grease_') and get_valve_bit_value(cur_state, ch):
                logger.debug(f"Grease Dispenser: Turning valve({self.slave_id}) off - {name}({ch})")
                self.valve.write_bit(slave_id=self.slave_id, pos=ch, val=False)
        return True

    def old_fsm(self):  # This version draws back excess grease after application, but cannot be pre-charged
        # Normal Operation
        if self.state == 'idle':
            if self.read_wago_input(name='reservoir_empty'):
                self._tick = time.time()
                self.state = 'wait_reservoir_empty'
            elif self.has_finished_pallet():
                logger.debug("Grease dispenser: Already has a finished pallet, skipping...")
                if self._is_normal:
                    self._pallet.update_pallet_state(state={'grease': True})
                self.state = 'finished'
            else:
                self.app.publish_station_state(data={'type': 'current', 'target': 'grease', 'value': 'pre-charge'})
                self._is_normal = True
                self.state = 'wait_for_pallet'
        elif self.state == 'wait_reservoir_empty':
            if not self.read_wago_input(name='reservoir_empty'):
                self.state = 'idle'
            elif time.time() - self._tick > .5:
                self.app.add_alarm(dict(
                    msg="The grease reservoir is almost empty, OK to refill?",
                    level='warning',
                    buttons=QMessageBox.Yes | QMessageBox.No,
                    default_button=QMessageBox.Yes,
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'

        # Refill start
        elif self.state == 'refill':
            self.write_wago_output(name='electrovalve_to_alemite_ram', val=True)
            self._tick = time.time()
            self.state = 'check_reservoir_full'
        elif self.state == 'check_reservoir_full':
            if self.read_wago_input(name='reservoir_full'):
                self._tick = time.time()
                self.state = 'confirm_reservoir_full'
            elif time.time() - self._tick > self.conf['grease_dispenser']['grease_reservoir_timeout']:
                self.write_wago_output(name='electrovalve_to_alemite_ram', val=False)
                self.app.add_alarm(dict(
                    msg="Warning: Grease reservoir fill action timed out. "
                        "The grease drum may be empty. "
                        "Please replace the drum and/or inspect the grease reservoir, and then press APPLY.",
                    level='warning',
                    buttons=QMessageBox.Apply | QMessageBox.Close,
                    default_button=QMessageBox.Close,
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
        elif self.state == 'confirm_reservoir_full':
            if not self.read_wago_input(name='reservoir_full'):
                self.state = 'check_reservoir_full'
            elif time.time() - self._tick > .25:
                self.write_wago_output(name='electrovalve_to_alemite_ram', val=False)
                self.state = 'idle'

        # Inject Start
        elif self.state == 'wait_for_pallet':  # Waiting for the pallet to be arrived here....
            if self.has_finished_pallet():
                logger.debug("Grease dispenser: Already has a finished pallet, skipping...")
                if self._is_normal:
                    self._pallet.update_pallet_state(state={'grease': True})
                self.state = 'finished'
            elif self._pallet.pallet_ready():
                self.app.publish_station_state(data={'type': 'current', 'target': 'grease', 'value': 'greasing...'})
                self.state = 'lower_greaser_block'
        elif self.state == 'lift_pallet':
            self._is_normal = False
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['lift_locate_up_2'], val=True)
            self._tick = time.time()
            self.state = 'wait_lift_extended'
        elif self.state == 'wait_lift_extended':
            if self.read_wago_input(name='lift_locate_extended_2'):
                self.state = 'lower_greaser_block'
            elif time.time() - self._tick > self.conf['grease_dispenser']['sensor_timeout']:
                self.app.add_alarm(dict(
                    msg="Grease Dispenser: lift_locate_extended_2 sensor timeout!",
                    level='critical',
                    buttons=QMessageBox.Retry | QMessageBox.Abort,
                    default_button=QMessageBox.Retry,
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
        elif self.state == 'lower_greaser_block':
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_lower_grease_block'],
                                 val=True)
            self._tick = time.time()
            self.state = 'wait_grease_slide_extended'
        elif self.state == 'wait_grease_slide_extended':
            if self.read_wago_input(name='grease_slide_extended'):
                self._pallet.update_pallet_state(state={'grease': False})
                self.state = 'apply_grease_dispenser_advance_ejector_piston_1'
            elif time.time() - self._tick > self.conf['grease_dispenser']['sensor_timeout']:
                self.app.add_alarm(dict(
                    msg="Grease Dispenser: grease_slide_extended sensor timeout!",
                    level='critical',
                    buttons=QMessageBox.Retry | QMessageBox.Abort,
                    default_button=QMessageBox.Retry,
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
            elif self.read_wago_input(name='reservoir_empty'):
                self._tick = time.time()
                self.state = 'wait_reservoir_empty'
        elif self.state == 'apply_grease_dispenser_advance_ejector_piston_1':
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_advance_ejector_piston'],
                                 val=True)
            self.state = 'inject_delay_1'
        elif self.state == 'inject_delay_1':
            time.sleep(self.conf['grease_dispenser']['inject_delay'])
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_advance_ejector_piston'],
                                 val=False)
            self.state = 'close_spool_valve'
        elif self.state == 'close_spool_valve':
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_spool_valve'], val=False)
            time.sleep(self.conf['grease_dispenser']['open_spool_valve_delay'])
            self.state = 'apply_grease_canister_back_pressure'
        elif self.state == 'apply_grease_canister_back_pressure':
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_canister_back_pressure'],
                                 val=True)
            self.state = 'reservoir_back_pressure_delay'
        elif self.state == 'reservoir_back_pressure_delay':
            time.sleep(self.conf['grease_dispenser']['reservoir_back_pressure_delay'])
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=True)
            self.state = 'shot_chamber_filling_delay'
        elif self.state == 'shot_chamber_filling_delay':
            time.sleep(self.conf['grease_dispenser']['shot_chamber_filling_delay'])
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_canister_back_pressure'],
                                 val=False)
            time.sleep(0.25)
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'],
                                 val=False)
            self.state = 'depressurize_delay'
        elif self.state == 'depressurize_delay':
            time.sleep(self.conf['grease_dispenser']['depressurize_delay'])
            self.state = 'open_spool_valve'
        elif self.state == 'open_spool_valve':
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_spool_valve'], val=True)
            self.state = 'open_spool_valve_delay'
        elif self.state == 'open_spool_valve_delay':
            time.sleep(self.conf['grease_dispenser']['open_spool_valve_delay'])
            self.state = 'apply_grease_dispenser_advance_ejector_piston_2'
        elif self.state == 'apply_grease_dispenser_advance_ejector_piston_2':
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_advance_ejector_piston'],
                                 val=True)
            self.state = 'inject_delay_2'
        elif self.state == 'inject_delay_2':
            time.sleep(self.conf['grease_dispenser']['inject_delay'])
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_advance_ejector_piston'],
                                 val=False)
            if self._is_normal:
                self._pallet.update_pallet_state(state={'grease': True})
            self.state = 'ejector_pullback'
        elif self.state == 'ejector_pullback':
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=True)
            time.sleep(self.conf['grease_dispenser']['shot_chamber_filling_delay'])
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=False)
            self.state = 'raise_greaser_block'
        elif self.state == 'raise_greaser_block':
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_lower_grease_block'],
                                 val=False)
            self._tick = time.time()
            self.state = 'wait_grease_slide_retracted'
        elif self.state == 'wait_grease_slide_retracted':
            if self.read_wago_input(name='grease_slide_retracted'):
                self.state = 'finished'
            elif time.time() - self._tick > self.conf['grease_dispenser']['sensor_timeout']:
                self.app.add_alarm(dict(
                    msg="Grease Dispenser: grease_slide_retracted sensor timeout!",
                    level='critical',
                    buttons=QMessageBox.Retry | QMessageBox.Abort,
                    default_button=QMessageBox.Retry,
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
        elif self.state == 'finished':
            if self._is_normal:
                if self.read_wago_input(name='grease_slide_retracted'):
                    self._pallet.release_pallet()
                    self.state = 'check_pallet_released'
            elif self._is_purge:
                self.state = 'apply_grease_canister_back_pressure'
        elif self.state == 'check_pallet_released':
            if self._pallet.released:
                self.state = 'idle'
        elif self.state == 'purge':
            if self._is_purge:
                self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_spool_valve'], val=True)
                time.sleep(0.5)
                self.valve.write_bit(slave_id=self.slave_id,
                                     pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=True)
                time.sleep(0.5)
                self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_canister_back_pressure'],
                                     val=True)
                self._is_purge = False
            if time.time() - self._tick > 3.0:
                self.stop_purge()

        # TODO Active fsm starts here...

    def fsm(self):  # This version pre-charges the greaser before pallet arrives, but leaks onto main conveyor
        # Normal Operation
        if self.state == 'idle':
            if self.read_wago_input(name='reservoir_empty'):
                self._tick = time.time()
                self.state = 'wait_reservoir_empty'
            elif self.has_finished_pallet():
                logger.debug("Grease dispenser: Already has a finished pallet, skipping...")
                if self._is_normal:
                    self._pallet.update_pallet_state(state={'grease': True})
                    self._reset_valves()
                self.state = 'finished'
            else:
                self.app.publish_station_state(data={'type': 'current', 'target': 'grease', 'value': 'pre-charge'})
                self._is_normal = True
                self.state = 'apply_grease_canister_back_pressure'
        elif self.state == 'wait_reservoir_empty':
            if not self.read_wago_input(name='reservoir_empty'):
                self.state = 'idle'
            elif time.time() - self._tick > .5:
                self.add_alarm(dict(
                    msg="The grease reservoir is almost empty, OK to refill?",
                    level='warning',
                    buttons=['Yes', 'No'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'

        # Refill start
        elif self.state == 'refill':
            self.write_wago_output(name='electrovalve_to_alemite_ram', val=True)
            self._tick = time.time()
            self.state = 'check_reservoir_full'
        elif self.state == 'check_reservoir_full':
            if self.read_wago_input(name='reservoir_full'):
                self._tick = time.time()
                self.state = 'confirm_reservoir_full'
            elif time.time() - self._tick > self.conf['grease_dispenser']['grease_reservoir_timeout']:
                self.add_alarm(dict(
                    msg="Warning: Grease reservoir fill action timed out. "
                        "The grease drum may be empty. "
                        "Please replace the drum and/or inspect the grease reservoir, and then press APPLY.",
                    level='warning',
                    buttons=['Apply', 'Close'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.write_wago_output(name='electrovalve_to_alemite_ram', val=False)
                self.state = 'warning'
        elif self.state == 'confirm_reservoir_full':
            if not self.read_wago_input(name='reservoir_full'):
                self.state = 'check_reservoir_full'
            elif time.time() - self._tick > .25:
                self.write_wago_output(name='electrovalve_to_alemite_ram', val=False)
                self.state = 'idle'

        # Inject Start
        elif self.state == 'lift_pallet':
            self._is_normal = False
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['lift_locate_up_2'], val=True)
            self._tick = time.time()
            self.state = 'wait_lift_extended'
        elif self.state == 'wait_lift_extended':
            if self.read_wago_input(name='lift_locate_extended_2'):
                self.state = 'apply_grease_canister_back_pressure'
            elif time.time() - self._tick > self.conf['grease_dispenser']['sensor_timeout']:
                self.app.add_alarm(dict(
                    msg="Grease Dispenser: lift_locate_extended_2 sensor timeout!",
                    level='critical',
                    buttons=QMessageBox.Retry | QMessageBox.Abort,
                    default_button=QMessageBox.Retry,
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
        elif self.state == 'apply_grease_canister_back_pressure':
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_canister_back_pressure'],
                                 val=True)
            self.state = 'reservoir_back_pressure_delay'
        elif self.state == 'reservoir_back_pressure_delay':
            time.sleep(self.conf['grease_dispenser']['reservoir_back_pressure_delay'])
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=True)
            self.state = 'shot_chamber_filling_delay'
        elif self.state == 'shot_chamber_filling_delay':
            time.sleep(self.conf['grease_dispenser']['shot_chamber_filling_delay'])
            self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_canister_back_pressure'],
                                 val=False)
            time.sleep(0.25)
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'],
                                 val=False)
            self.state = 'depressurize_delay'
        elif self.state == 'depressurize_delay':
            time.sleep(self.conf['grease_dispenser']['depressurize_delay'])
            self.app.publish_station_state(data={'type': 'current', 'target': 'grease', 'value': 'wait...'})
            self.state = 'wait_for_pallet'
        elif self.state == 'wait_for_pallet':  # Waiting for the pallet to be arrived here....
            if self._pallet.pallet_ready():
                self.app.publish_station_state(data={'type': 'current', 'target': 'grease', 'value': 'greasing...'})
                self.state = 'lower_greaser_block'
        elif self.state == 'lower_greaser_block':
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_lower_grease_block'],
                                 val=True)
            self._tick = time.time()
            self.state = 'wait_grease_slide_extended'
        elif self.state == 'wait_grease_slide_extended':
            if self.read_wago_input(name='grease_slide_extended'):
                self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_spool_valve'], val=True)
                self._pallet.update_pallet_state(state={'grease': False})
                self.state = 'open_spool_valve_delay'
            elif time.time() - self._tick > self.conf['grease_dispenser']['sensor_timeout']:
                self.add_alarm(dict(
                    msg="Grease Dispenser: grease_slide_extended sensor timeout!",
                    level='critical',
                    buttons=['Retry'],
                    callback=partial(self._on_alarm_closed, self.state)))
                self.state = 'warning'
            elif self.read_wago_input(name='reservoir_empty'):
                self._tick = time.time()
                self.state = 'wait_reservoir_empty'
        elif self.state == 'open_spool_valve_delay':
            time.sleep(self.conf['grease_dispenser']['open_spool_valve_delay'])
            self.state = 'apply_grease_dispenser_advance_ejector_piston'
        elif self.state == 'apply_grease_dispenser_advance_ejector_piston':
            self.valve.write_bit(slave_id=self.slave_id,
                                 pos=self.conf['valve']['grease_dispenser_advance_ejector_piston'],
                                 val=True)
            self.state = 'inject_delay'
        elif self.state == 'inject_delay':
            time.sleep(self.conf['grease_dispenser']['inject_delay'])
            self._reset_valves()
            if self._is_normal:
                self._pallet.update_pallet_state(state={'grease': True})
            self.state = 'finished'
        elif self.state == 'finished':
            if self._is_normal:
                if self.read_wago_input(name='grease_slide_retracted') and self._pallet.pallet_ready():
                    self._pallet.release_pallet()
                    self.state = 'check_pallet_released'
            elif self._is_purge:
                self.state = 'apply_grease_canister_back_pressure'
        elif self.state == 'check_pallet_released':
            if self._pallet.released:
                time.sleep(.5)       # give some delay so that we don't check state of the current one!
                self.state = 'idle'

    def refill(self):
        self.state = 'refill'

    def clear_error(self):
        self.state = 'idle'

    def do_action(self, k):
        if k == 'inject':
            self._is_purge = False
            self.state = 'lower_greaser_block'
        elif k == 'purge':
            self._tick = time.time()
            self._is_purge = True
            self.state = 'purge'
        else:  # refill or clear_error
            self.app.set_grease_error(None)
            getattr(self, k)()

    def stop_purge(self):
        self._is_purge = False
        self.valve.write_bit(slave_id=self.slave_id, pos=self.conf['valve']['grease_canister_back_pressure'],
                             val=False)
        time.sleep(3.0)
        self.valve.write_bit(slave_id=self.slave_id,
                             pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=False)
        time.sleep(0.5)
        self.valve.write_bit(slave_id=self.slave_id,
                             pos=self.conf['valve']['grease_dispenser_advance_ejector_piston'],
                             val=True)
        time.sleep(0.5)
        self.valve.write_bit(slave_id=self.slave_id,
                             pos=self.conf['valve']['grease_dispenser_advance_ejector_piston'],
                             val=False)
        time.sleep(0.5)
        self.valve.write_bit(slave_id=self.slave_id,
                             pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=True)
        time.sleep(0.5)
        self.valve.write_bit(slave_id=self.slave_id,
                             pos=self.conf['valve']['grease_dispenser_retract_ejector_piston'], val=False)
        self.state = 'idle'

    def read_state(self):
        return {'pallet': self._pallet.state, 'station': self.state}

    def read_robot_error(self):
        return

    def check_already_finished_pallet(self, code):
        return self.app.pallets[code].get('grease')

    def has_finished_pallet(self):
        for sn, p in self.app.pallets.items():
            # Find currently placed pallet
            if p.get('pos') == 'lift_locate' and p.get('index') == self._pallet.index and not p.get('state'):
                return p.get('grease')

    def apply_finished_parts(self):
        pass

    def reject_pallet(self):
        self._reset_valves()
        self.state = 'finished'

    def add_alarm(self, alarm):
        logger.warning(f"Grease dispenser alarm::: {alarm.get('msg', '')}")
        self.station_alarms.append(alarm)

    def remove_first_alarm(self):
        if self.station_alarms:
            self.station_alarms = self.station_alarms[1:]

    def _on_alarm_closed(self, *args):
        state, action = args[:2]
        if state == 'wait_reservoir_empty':
            if action == 'yes':
                self.refill()
            elif action == 'no':
                self.app.set_grease_error('empty')
        elif state == 'check_reservoir_full':
            if action == 'apply':
                self.clear_error()
            elif action == 'close':
                self.app.set_grease_error('timeout')
        elif state == 'wait_grease_slide_extended':
            if action == 'retry':
                self.state = 'lower_greaser_block'
        elif action == 'retry':
            self._tick = time.time()
            self.state = state
        elif action == 'abort':
            self._reset_valves()
            self.state = 'idle'

    def on_stopped(self):
        self._pallet.stop()

    def on_resumed(self):
        self._pallet.resume()

    def on_paused(self):
        if self.state in {'refill', 'check_reservoir_full', 'confirm_reservoir_full'}:
            self.state = 'idle'
        self.write_wago_output(name='electrovalve_to_alemite_ram', val=False)
        self._pallet.pause()
