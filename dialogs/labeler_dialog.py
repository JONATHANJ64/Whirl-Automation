from functools import partial

from PySide2.QtCore import QTimer

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_labeler import Ui_LabelerDialog


class LabelerDialog(WhirlDialogBase):

    def __init__(self, app):
        super().__init__(app)
        self._labeler = app.stations['station5'].labeler
        self.ui = Ui_LabelerDialog()
        self.ui.setupUi(self)
        for k in {'feed', 'unlock', 'clear'}:
            getattr(self.ui, f"btn_{k}").released.connect(partial(self._on_btn, k))
        self._timer = QTimer()
        self._timer.timeout.connect(self._update_state)
        self._timer.start(100)

    def _on_btn(self, k):
        if k == 'feed':
            self._labeler.state = 'start'
        elif k == 'unlock':
            self._labeler.unlock_motor()
        elif k == 'clear':
            self._labeler.clear_error()

    def _update_state(self):
        self.ui.btn_feed.setEnabled(self.app.is_building)
        err_msg = self._labeler.read_current_state().get('msg', '')
        self.ui.btn_clear.setEnabled(bool(err_msg))
        self.ui.error.setText(err_msg)
        self.ui.state.setText(self._labeler.state)
        self.ui.label_sensor.setStyleSheet(f"border-radius:12px;background-color:#"
                                           f"{'00aa00' if self._labeler.is_label_applied() else 'aa0000'};")

    def close(self) -> bool:
        self._timer.stop()
        return super(LabelerDialog, self).close()
