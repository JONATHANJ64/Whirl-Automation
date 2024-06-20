from functools import partial
from PySide2.QtCore import QTimer
from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_station import Ui_StationDialog


class StationDialog(WhirlDialogBase):

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_StationDialog()
        self.ui.setupUi(self)
        self._timers = {}
        for i in range(1, 6):
            self._start_station_timer(f"station{i}")
        self._start_station_timer('grease')
        self._start_station_timer('final_test')

    def _start_station_timer(self, st):
        timer = QTimer()
        timer.timeout.connect(partial(self._update_station_state, st))
        timer.start(500)
        self._timers[st] = timer

    def _update_station_state(self, st):
        state = self.app.stations[st].read_state()
        getattr(self.ui, f"state_{st}").setText(', '.join([f"{k}: {v}" for k, v in state.items()]))
        getattr(self.ui, f"error_{st}").setText(self.app.stations[st].read_robot_error() or '')

    def close(self) -> bool:
        for t in self._timers.values():
            t.stop()
        return super(StationDialog, self).close()
