import time
from routines.base import RoutineBase
from utils.flex_feeder import FlexFeeder
from utils.logger import logger


BACKLIGHT_DELAY = 0.25
ERROR_MESSAGES = {
    'feeding_timeout': "Part feeding time out!",
    'part_presence_timeout': "{name} is detected at conveyor entrance but failed to reach front of the conveyor!"
}


class FlexFeederRoutine(RoutineBase):

    def __init__(self, name, app, root, host, index=0):
        super().__init__(app)
        self.root = root
        self.name = name
        self.index = index
        self._pos = None
        self._feeder = FlexFeeder(name=name, host=host)
        self._has_part = False
        self._init_error = False
        self._en_reversed = False       # Check reversed position from cognex or not
        self._r_offset = 4              # Offset value in case of reversed postion from cognex

    def initialize(self):
        if not self._feeder.is_alive():
            if not self._init_error:
                self._add_init_alarm(msg=f"FlexFeeder({self.name}) is not alive!")
                self._init_error = True
            return False
        # Try to read position to avoid replacing current available parts
        self.root.clear_cognex_results()
        time.sleep(0.25)
        self._feeder.turn_backlight(True)
        time.sleep(BACKLIGHT_DELAY)
        pos = self.root.read_cognex_position(index=self.index, ignore_i22=True)
        if pos is not None and not any([p in {0, 9999.} for p in pos]):
            logger.debug(f"Position of {self.name} is valid, just setting up...")
            self._pos = pos
            self._has_part = True
        else:
            self._feeder.reset_feed()
        self._feeder.turn_backlight(False)

    def fsm(self):
        if self.state == 'idle':
            if self._has_part:
                self.state = 'finished'
            else:
                self._pos = None
                # Read data from cognex without turning backlight on, so that previous value is cleared...
                self.root.clear_cognex_results()
                # self.root.read_cognex_position(index=self.index, ignore_i22=True)
                self._feeder.start_feed()
                self.state = 'check_feeder'
        elif self.state == 'check_feeder':
            st = self._feeder.get_ready_status()
            if st.get('finished'):
                self._feeder.turn_backlight(True)
                time.sleep(BACKLIGHT_DELAY)  # Give some delay so that backlight is enough for cognex!
                if self.name in {'cross_gear', 'pinion'}:
                    time.sleep(3.5)
                elif self.name in {'dial'}:
                    time.sleep(1.0)
                self.state = 'get_position'
            # elif st.get('error'):
            #     err_msg = st.get('msg', '')
            #     self.app.add_alarm(dict(
            #         msg=ERROR_MESSAGES.get(err_msg, '{name} Flex Feeder Error! Retry?').format(name=self.name),
            #         level='warning',
            #         buttons=QMessageBox.Retry | QMessageBox.Ignore,
            #         default_button=QMessageBox.Retry,
            #         callback=self._on_alarm_closed))
            #     self.state = 'warning'
            time.sleep(.1)
        elif self.state == 'get_position':
            pos = self.root.read_cognex_position(index=self.index, check_reversed=self._en_reversed,
                                                 r_offset=self._r_offset)
            if pos is not None:
                if any([p in {0, 9999.} for p in pos[:3]]):
                    logger.warning(f"{self.name}: Invalid position data, restarting...")
                    self._feeder.turn_backlight(False)
                    self._feeder.reject_part()
                    self._has_part = False
                    time.sleep(1)
                    self.state = 'idle'
                else:
                    logger.debug(f"{self.name}: Read position data from cognex - {pos}")
                    self._feeder.turn_backlight(False)
                    self._pos = pos
                    self.state = 'finished'
            time.sleep(.01)
        elif self.state == 'finished':
            pass

    def re_acquire(self):
        self._pos = None
        self.state = 'check_feeder'

    def ignore_pos(self):
        # Ignore the currently acquired position
        self._pos = None

    def set_reversed_flag(self, val):
        self._en_reversed = val

    def set_reversed_cognex_offset(self, val):
        self._r_offset = val

    def is_feeder_online(self):
        return self._feeder.is_alive()

    def is_finished(self):
        return self.state == 'finished' and self.is_feeder_online() and self._pos is not None

    def read_data(self):
        return self._pos

    def turn_ev0(self, val):
        return self._feeder.turn_ev0(val)

    def read_current_state(self):
        return self._feeder.get_current_state()

    def resume_feed(self):
        return self._feeder.resume_feed()

    def pause_feed(self):
        return self._feeder.pause_feed()

    def reset_feed(self):
        return self._feeder.reset_feed()

    def stop_feed(self):
        return self._feeder.stop_feed()

    def set_state(self, state):
        return self._feeder.set_state(state)

    def lift_slide(self, action='up'):
        self._feeder.lift_slide(action=action)

    def action_motor(self, name, action, direction=None):
        return self._feeder.action_motor(name, action, direction)

    def stop_motor(self, name):
        return self._feeder.stop_motor(name=name)

    def turn_backlight(self, val):
        return self._feeder.turn_backlight(val)

    def _on_alarm_closed(self, *args):
        pass
    #     state, action = args[:2]
    #     if action == 'retry':
    #         self._feeder.reject_part()
    #         time.sleep(.1)
    #         self.state = 'check_feeder'

    def reject_part(self):
        self._feeder.reject_part()
        self.state = 'check_feeder'

    def restart_feed(self):
        logger.debug(f"Restarting {self.name} feeder, has part: {self._has_part}")
        if self._has_part:
            self._has_part = False
            self._feeder.reset_feed()
        self.state = 'idle'

    def get_feeder_config(self):
        return self._feeder.get_config()

    def update_feeder_config(self, data):
        return self._feeder.update_config(data=data)

    def on_stopped(self):
        if self.app.main_power:
            self._feeder.turn_backlight(False)
            self._feeder.pause_feed()

    def on_resumed(self):
        self._feeder.resume_feed()
        if self.state == 'get_position':
            self._feeder.turn_backlight(True)

    def on_paused(self):
        self._feeder.pause_feed()
        self._feeder.turn_backlight(False)
