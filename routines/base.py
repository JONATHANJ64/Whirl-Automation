import threading
import time
from abc import abstractmethod
from functools import partial

from PySide2.QtWidgets import QMessageBox

from utils.common import get_config
from utils.logger import logger


class RoutineBase(threading.Thread):

    def __init__(self, app, conf=None, name=None):
        super(RoutineBase, self).__init__(name=name)
        self.conf = conf or {}
        self.app = app
        self.motor = self.app.motor
        self._b_stop = threading.Event()
        self._b_pause = threading.Event()
        self._b_pause.set()
        self.state = "init"
        self._is_started = False
        self.initialized = None
        self.cognex = None
        self.robot = None
        self.wago = None
        self.valve = app.valve
        self.slave_id = self.conf.get('valve', {}).get('slave_id', 0)
        self._tick = 0

    @abstractmethod
    def initialize(self):
        """
        :return: False if not successful
        """
        raise NotImplementedError("initialize function should be implemented")

    def run(self) -> None:
        logger.info(f"=== Starting {self.__class__.__name__} routine...")
        self._is_started = True
        paused = True
        while not self._b_stop.is_set():
            if self.state == 'init_error':
                pass
            elif self.state == 'stopped':
                pass
            elif self.state == 'init':
                self.initialized = None
                # Update config from the file before starting...
                new_conf = get_config().get(self.name.lower())
                if new_conf:
                    self.conf = new_conf

                time.sleep(.5)
                if self.initialize() is not False:
                    logger.info(f"=== Initialized {self.__class__.__name__}({self.name})...")
                    self._b_pause.clear()
                    self.initialized = True
                    self.state = 'idle'
            else:
                if not self._b_pause.is_set():
                    self.fsm()
                    paused = False
                elif not paused:
                    self.on_paused()
                    paused = True
            time.sleep(.001)

    def is_started(self):
        return self._is_started

    def _add_init_alarm(self, msg):
        self.app.add_alarm(dict(
            msg=msg,
            level='critical',
            buttons=QMessageBox.Retry | QMessageBox.Abort,
            default_button=QMessageBox.Retry,
            callback=self._on_init_alarm_closed))
        self.state = 'init_error'

    def _on_init_alarm_closed(self, *args):
        ret = args[0]
        if ret == 'retry':
            self.state = 'init'
        elif ret == 'abort':
            pass

    @abstractmethod
    def on_paused(self):
        """
        Customize this function to do post actions once paused.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def on_resumed(self):
        """
        Customize this function to do post actions once resumed.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def on_stopped(self):
        """
        Customize this function to do post actions once stopped.
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def fsm(self):
        raise NotImplementedError()

    @abstractmethod
    def _on_alarm_closed(self, *args):
        pass

    def _add_motor_error(self, motor_id, msg):
        self.motor.turn_motor_off(arb_id=motor_id)
        self.app.add_alarm(dict(
            msg=msg,
            level='critical',
            buttons=QMessageBox.Retry | QMessageBox.Abort,
            default_button=QMessageBox.Retry,
            callback=partial(self._on_alarm_closed, self.state)))
        self.state = 'error'

    def read_wago_input(self, name):
        if self.wago is not None:
            return self.wago.read_input(channel=self.conf['io'][name])

    def read_wago_output(self, name):
        if self.wago is not None:
            return self.wago.read_output(channel=self.conf['io'][name])

    def write_wago_output(self, name, val):
        if self.wago is not None:
            return self.wago.write_output(channel=self.conf['io'][name], val=val)

    def turn_valve(self, name="", val=False):
        slave_id = self.conf['valve']['slave_id']
        pos = self.conf['valve'][name]
        logger.debug(f"{self.name}: Turning Valve({slave_id}) - '{name}'({pos}) {'ON' if val else 'OFF'}")
        self.valve.write_bit(slave_id=slave_id, pos=pos, val=val)

    def stop(self):
        logger.info(f"=== Stopping {self.__class__.__name__}, state is `{self.state}` ...")
        self.state = 'stopped'
        self._b_stop.set()
        self.on_stopped()
        try:
            self.join(.1)
        except RuntimeError:
            pass

    def pause(self, show_log=True):
        if show_log:
            logger.info(f"=== Pausing {self.__class__.__name__}...")
        self._b_pause.set()

    def resume(self):
        if self._b_pause.is_set():
            logger.info(f"=== Resuming {self.__class__.__name__}...")
            self._b_pause.clear()
            self.on_resumed()
