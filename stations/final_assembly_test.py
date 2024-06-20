import time
from routines.base import RoutineBase
from utils.common import get_config
from utils.logger import logger


class FinalAssemblyTestRoutine(RoutineBase):

    def __init__(self, app):
        super().__init__(app, conf=get_config()['station3'], name='final_assembly_test')
        self._cnt = 0
        self._cur_sensor_val = False
        self._is_normal = True
        self._pallet = app.pallet_handlers[7]
        self.station_alarms = []

    def initialize(self):
        self.wago = self.app.stations['station3'].wago
        self._pallet.init_conf(self)
        if not self._pallet.is_started():
            self._pallet.start()
        while not self._pallet.initialized:
            if self._pallet.initialized is False:
                return False
            time.sleep(.01)

    def read_state(self):
        return {'pallet': self._pallet.state, 'station': self.state}

    def read_robot_error(self):
        return

    def set_product_type(self, p_type):
        pass

    def fsm(self):
        if self.state == 'idle':
            if self._pallet.pallet_ready():
                self._is_normal = True
                if self._pallet.get_current_pallet_state().get('final_vision') is False:
                    logger.warning("Final Assembly: Bypassing the pallet since the final vision was failed!")
                    self._pallet.update_pallet_state(state={'count': 0})
                    self.state = 'finished'
                    return
                self._pallet.update_pallet_state(state={'final_test': False})
                self.state = 'start'
        elif self.state == 'start':
            self._cnt = 0
            self.app.publish_station_state(
                data={'type': 'current', 'target': 'final_test', 'value': f'count: {self._cnt}'})
            self.turn_air_jet(True)
            self._pallet.update_pallet_state(state={'count': 0})
            self._tick = time.time()
            self.state = 'wait_delay'
        elif self.state == 'wait_delay':
            if time.time() - self._tick > self.conf['test']['startup_delay']:
                self._tick = time.time()
                self._cur_sensor_val = self.read_sensor_value()
                self.state = 'count'
        elif self.state == 'count':
            if time.time() - self._tick > self.conf['test']['duration']:
                self.turn_air_jet(False)
                logger.info(f">>> Count on the final assembly test: {self._cnt}")
                self.state = 'finished'
            else:
                val = self.read_sensor_value()
                if self._cur_sensor_val != val and val:
                    self._cnt += 1
                    self._pallet.update_pallet_state(state={'count': self._cnt})
                    self.app.publish_station_state(
                        data={'type': 'current', 'target': 'final_test', 'value': f'count: {self._cnt}'})
                self._cur_sensor_val = val
        elif self.state == 'finished':
            if self._is_normal:
                self._pallet.update_pallet_state(state={'final_test': True})
                self._pallet.release_pallet()
                self.app.publish_station_state(data={'type': 'current', 'target': 'final_test', 'value': 'wait...'})
                self.state = 'idle'

    def add_alarm(self, alarm):
        logger.warning(f"Final test station alarm::: {alarm.get('msg', '')}")
        self.station_alarms.append(alarm)

    def remove_first_alarm(self):
        if self.station_alarms:
            self.station_alarms = self.station_alarms[1:]

    def _on_alarm_closed(self, *args):
        state, action = args[:2]
        if action == 'retry':
            self.state = state
        elif action == 'ignore':
            self.state = 'idle'

    def check_already_finished_pallet(self, code):
        return self.app.pallets[code].get('final_test')

    def start_count(self, is_normal=True):
        self._is_normal = is_normal
        self.state = 'start'

    def turn_air_jet(self, val):
        self.turn_valve(name='lift_locate_final_assembly_test_air_7', val=val)

    def read_sensor_value(self):
        return self.read_wago_input(name='rotary_test')

    def get_count(self):
        return self._cnt

    def get_sensor_value(self):
        return self._cur_sensor_val

    def is_finished(self):
        return self.state == 'finished'

    def apply_finished_parts(self):
        pass

    def on_stopped(self):
        if self.app.main_power:
            self.turn_air_jet(False)
        self._pallet.stop()

    def on_resumed(self):
        self._pallet.resume()
        # Restart from scratch again on the same part
        self.state = 'idle'

    def on_paused(self):
        self.turn_air_jet(False)
        self._pallet.pause()
