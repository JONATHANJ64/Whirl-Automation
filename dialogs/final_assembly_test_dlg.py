from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap

from dialogs.base import WhirlDialogBase
from stations.final_assembly_test import FinalAssemblyTestRoutine
from ui.dialogs.ui_dlg_final_assembly import Ui_FinalAssemblyTestDialog
from utils.common import get_config
from widgets.message import show_message


class FinalAssemblyTestDialog(WhirlDialogBase):

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_FinalAssemblyTestDialog()
        self.ui.setupUi(self)
        self._tester = FinalAssemblyTestRoutine(app=self.app)
        self._tester.start()
        self.ui.btn.released.connect(self._on_btn)
        self._timer = QTimer()
        self._timer.timeout.connect(self._update_state)

    def _on_btn(self):
        if self.ui.btn.text() == 'Start':
            self.ui.btn.setText("Stop")
            self._tester.start_count(is_normal=False)
            self._timer.start(20)
        else:
            self._tester.pause()
            self._timer.stop()
            self.ui.btn.setText("Start")

    def _update_state(self):
        self.ui.rpm.setText(f"{self._tester.get_count()}")
        self.ui.sensor.setPixmap(
            QPixmap(f":/img/img/{'green' if self._tester.get_sensor_value() else 'gray'}-circle.png"))
        if self._tester.is_finished():
            self._on_btn()
            conf = get_config()['station3']['test']
            if conf['low_pass'] <= self._tester.get_count() <= conf['high_pass']:
                show_message(msg_type="Info", msg="Success!")
            else:
                show_message(msg_type="Error", msg="Failed!")

    def close(self) -> bool:
        self._timer.stop()
        self._tester.stop()
        return super(FinalAssemblyTestDialog, self).close()
