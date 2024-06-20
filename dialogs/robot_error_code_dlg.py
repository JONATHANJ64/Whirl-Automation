import threading

from PySide2.QtCore import Signal

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_robot_error_code import Ui_RobotErrorCodeDialog
from widgets.message import show_message
from widgets.spinner import QtSpinner
import time


class RobotErrorCodeDialog(WhirlDialogBase):

    sig_error = Signal(object)

    def __init__(self, app, index, err):
        super().__init__(app)
        self.ui = Ui_RobotErrorCodeDialog()
        self.ui.setupUi(self)
        self.app = app
        self.index = index
        self.ui.label.setText(err or "")
        self.ui.btn_clear.released.connect(self._on_btn)
        self.ui.btn_cancel.released.connect(self.close)
        self.spinner = QtSpinner(parent=self)
        getattr(self, 'sig_error').connect(self._on_error_result)

    def _on_btn(self):
        if not self.app.stations[f"station{self.index}"].robot.is_connected():
            show_message(msg_type='Error', msg=f"Robot{self.index} is currently not connected!")
            return
        self.spinner.start()
        threading.Thread(target=self._clear_error).start()
        self.setDisabled(True)

    def _clear_error(self):
        robot = self.app.stations[f"station{self.index}"].robot
        robot.clear_cont_error()
        for i in range(80, 93):
            robot.write_variable(var_name=f"I{i}", value=0)
            time.sleep(0.05)
        getattr(self, 'sig_error').emit(robot.get_cont_error())

    def _on_error_result(self, error):
        self.spinner.close()
        if error:
            self.setDisabled(False)
            self.ui.label.setText(error)
        else:
            self.close()
