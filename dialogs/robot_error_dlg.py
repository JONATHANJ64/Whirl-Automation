from functools import partial

from PySide2.QtCore import Signal

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_robot_error import Ui_RobotErrorDialog


class RobotErrorDialog(WhirlDialogBase):

    sig_action = Signal(str)

    def __init__(self, app, msg):
        super().__init__(app)
        self.ui = Ui_RobotErrorDialog()
        self.ui.setupUi(self)
        self.ui.msg.setText(msg)
        for k in {'retry', 'new_part', 'cancel'}:
            getattr(self.ui, f"btn_{k}").released.connect(partial(self._on_btn, k))

    def _on_btn(self, k):
        getattr(self, 'sig_action').emit(k)
        self.close()
