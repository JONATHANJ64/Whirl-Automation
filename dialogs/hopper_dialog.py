import threading
import time

from PySide2.QtCore import Signal

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_hopper import Ui_HopperDialog


class HopperDialog(WhirlDialogBase):

    sig_state = Signal(dict)

    def __init__(self, app):
        super().__init__(app)
        self._hopper = app.stations['station4'].feeders['hopper']
        self.ui = Ui_HopperDialog()
        self.ui.setupUi(self)
        self.ui.btn_close.released.connect(self.close)
        self.ui.btn_index.released.connect(self._on_btn_index)
        self.ui.btn_stop.released.connect(self._on_btn_stop)
        getattr(self, 'sig_state').connect(self._on_feeder_state)
        self._b_stop = threading.Event()
        self._thread = threading.Thread(target=self._poll_feeder_state)
        self._thread.start()

    def _on_btn_index(self):
        if self.ui.btn_index.text() == 'Index':
            self._hopper.do_index()
        else:
            self._hopper.do_index(clear_error=True)

    def _on_btn_stop(self):
        self._hopper.stop_state()

    def _on_feeder_state(self, state):
        self.ui.msg.setText(state.get('msg', ''))
        self.ui.btn_stop.setDisabled(state.get('state') == 'error' or state.get('stopped'))
        self.ui.btn_index.setText('Clear Error' if state.get('state') == 'error' else 'Index')
        self.ui.btn_index.setDisabled(state.get('state') != 'error' and not state.get('stopped'))
        self.ui.indexed.setStyleSheet(
            f"background-color: #{'00ff00' if state['indexed'] else 'aa0000'};border-radius: 12px;")
        self.ui.present.setStyleSheet(
            f"background-color: #{'00ff00' if state['present'] else 'aa0000'};border-radius: 12px;")

    def _poll_feeder_state(self):
        while not self._b_stop.is_set():
            getattr(self, 'sig_state').emit(self._hopper.read_current_state())
            time.sleep(.1)

    def close(self) -> bool:
        self._b_stop.set()
        self._thread.join(.2)
        return super().close()
