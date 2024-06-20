import threading
import time
from functools import partial

from utils.logger import logger


class PneumaticSlideBase(threading.Thread):

    def __init__(self, root, wago, name="", conf=None, cur_sensor='', target_sensor='', output_name='', timeout=5,
                 action='extend', check_current=True, check_target=True, alarm_on_timeout=False):
        super().__init__(name=name)
        self.root = root
        self.app = root.app
        self.wago = wago
        self.conf = conf
        self.cur_sensor = cur_sensor
        self.target_sensor = target_sensor
        self.output_name = output_name
        self.timeout = timeout
        self.action = action
        self.check_current = check_current
        self.check_target = check_target
        self.alarm_on_timeout = alarm_on_timeout
        self._b_stop = threading.Event()
        self._b_stop.clear()
        self._state = 'init'
        self._start_time = 0
        self._is_finished = False

    def run(self) -> None:
        s_time = time.time()
        while not self._b_stop.is_set():
            if self._state == 'init':
                while self.wago.in_values is None or self.wago.out_values is None:
                    if time.time() - s_time > 3:
                        self.root.add_alarm(dict(
                            msg=f"{self.name}: Failed to connect to Wago!",
                            level='critical',
                            buttons=['Retry'],
                            callback=partial(self._on_alarm_closed, 'init')))
                        self._state = 'warning'
                    else:
                        time.sleep(.01)
                self._state = 'idle'
            elif self._state == 'idle':
                if not self.check_current and not self.check_target:
                    if self.read_target_sensor():
                        self._is_finished = True
                        break
                    else:
                        self._state = 'start_output'
                elif not self.check_current or self.read_cur_sensor():   # Check current sensor status
                    self._state = 'check_target'
                else:
                    self.root.add_alarm(dict(
                        msg=self._compose_error_message(current=True),
                        level='warning',
                        buttons=['Ignore', 'Retry'],
                        callback=partial(self._on_alarm_closed, 'idle')))
                    self._state = 'warning'
            elif self._state == 'check_target':     # Check target sensor status
                if not self.check_target or not self.read_target_sensor():
                    self._state = 'start_output'
                else:
                    self.root.add_alarm(dict(
                        msg=self._compose_error_message(current=False),
                        level='warning',
                        buttons=['Ignore', 'Retry'],
                        callback=partial(self._on_alarm_closed, 'check_target')))
                    self._state = 'warning'
            elif self._state == 'start_output':
                logger.debug(f"{self.name}: {self.action}ing...")
                self._start_time = time.time()
                self.write_output()
                self._state = 'running'
            elif self._state == 'running':
                if self.read_target_sensor():
                    logger.debug(f"{self.name}: Finished, sensor is on...")
                    self._is_finished = True
                    break
                elif time.time() - self._start_time > self.timeout:
                    if self.alarm_on_timeout:
                        self.root.add_alarm(dict(
                            msg=f"{self.name}: {self.action.capitalize()} Timeout!",
                            level='warning',
                            buttons=['Ignore', 'Retry'],
                            callback=partial(self._on_alarm_closed, 'idle')))
                    self._state = 'warning'
            time.sleep(.01)
        self.stop()

    def _compose_error_message(self, current=True):
        name = self.cur_sensor if current else self.target_sensor
        msg = f"{self.name} {' '.join([v.capitalize() for v in name.split('_')])} " \
              f"should be on to {self.action}!"
        return msg

    def write_output(self):
        val = self.action in {'activate', 'on', 'up', 'close', 'pick', 'rotate', 'engage'}
        logger.debug(f"{self.name} : Turning {self.output_name} valve '{val}'")
        self.app.valve.write_bit(slave_id=self.conf['valve']['slave_id'], pos=self.conf['valve'][self.output_name],
                                 val=val)

    def read_cur_sensor(self):
        return self.wago.read_input(self.conf['io'][self.cur_sensor])

    def read_target_sensor(self):
        try:
            return self.wago.read_input(self.conf['io'][self.target_sensor])
        except KeyError:
            print(self)

    def _on_alarm_closed(self, *args):
        state, ret = args[:2]
        if ret == 'retry':
            self._state = state
        elif ret == 'ignore':
            if state == 'idle':
                self._state = 'check_target'
            elif state == 'check_target':
                self._state = 'start_output'
            elif state == 'running':
                self._is_finished = True
                self._state = state

    def is_finished(self):
        return self._is_finished

    def stop(self):
        self._b_stop.set()
        try:
            self.join(.1)
        except RuntimeError:
            pass
