from PySide2.QtCore import QTimer

from ui.dialogs.ui_dlg_motor_state import Ui_MotorStateDialog

from dialogs.base import WhirlDialogBase


class MotorStateDialog(WhirlDialogBase):

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_MotorStateDialog()
        self.ui.setupUi(self)
        self._s_timer = QTimer()
        self._s_timer.timeout.connect(self._update_state)
        self._s_timer.start(500)

    def _update_state(self):
        for motor_id, status in self.app.motor_status.items():
            for k, m in self.app.conf['motor'].items():
                if m['address'] == motor_id - 1:
                    txt = f"Temp: {status['temperature']} °C\t Speed: {status['speed']} DPS\t " \
                          f"Torque: {status['torque']} A"
                    getattr(self.ui, f"motor_status_{k}").setText(txt)

    def closeEvent(self, event):
        self._s_timer.stop()
        super(MotorStateDialog, self).closeEvent(event)
