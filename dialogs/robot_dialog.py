from functools import partial
from PySide2.QtCore import QSize, QTimer
from PySide2.QtWidgets import QCheckBox

from dialogs.base import WhirlDialogBase
from settings import R_INK_JET_VERTICAL_ADJUST, R_DISABLE_COLLISION_DETECTION
from ui.dialogs.ui_dlg_robot import Ui_RobotDialog


class RobotDialog(WhirlDialogBase):

    def __init__(self, app, root=None, index=1, error="", park_enable=True):
        super().__init__(app)
        self.index = index
        self.station = self.app.stations[f"station{index}"]
        self.robot = self.station.robot
        self.ui = Ui_RobotDialog()
        self.ui.setupUi(self)
        self.root = root
        self.error = error
        self.ui.error.setText(error)
        self.setWindowTitle(f"Control Robot {index}")

        # Speed adjustment
        speed = self.robot.get_ext_speed()
        if speed:
            self.ui.speed.setValue(speed)

        self.ui.chk_dcd.setChecked(self.robot.read_variable(var_name=R_DISABLE_COLLISION_DETECTION))
        self.ui.chk_dcd.stateChanged.connect(self._on_dcd_changed)

        # Picker & Placer of Robot 4
        if self.index == 4:
            self.ui.btn_picker.released.connect(partial(self._on_btn_action, 'picker'))
            self.ui.btn_placer.released.connect(partial(self._on_btn_action, 'placer'))
        else:
            self.ui.group_picker.hide()
            self.ui.group_placer.hide()
            if self.index != 2:
                self.setFixedSize(QSize(self.width() - 300, self.height()))

        # Vacuum of Robot 3 & 4
        if self.index in {3, 4}:
            self._update_vacuum_state()
            self.ui.btn_vacuum.released.connect(partial(self._on_btn_action, 'vacuum'))
        else:
            self.ui.group_vacuum.hide()

        # Sensor Check Skipping
        self.ui.stack_sensor_check_skip.setCurrentWidget(getattr(self.ui, f"page_{index}"))
        for chk in getattr(self.ui, f"page_{index}").findChildren(QCheckBox):
            num = int(chk.objectName().split('_')[-1])
            chk.setChecked(bool(self.robot.read_variable(var_name=f"I{num}")))
            chk.stateChanged.connect(partial(self._on_sensor_check_skip_changed, chk))
        if index == 2:
            cur_adj = self.robot.read_variable(R_INK_JET_VERTICAL_ADJUST)
            self.ui.inkjet_adjust.setMinimum(cur_adj - 10)
            self.ui.inkjet_adjust.setMaximum(cur_adj + 10)
            self.ui.inkjet_adjust.valueChanged.connect(self._on_inkjet_changed)

        # Bind buttons
        for k in {'hand', 'park', 'set_speed'}:
            getattr(self.ui, f"btn_{k}").released.connect(partial(self._on_btn_action, k))
        self.ui.btn_park.setEnabled(park_enable)

        if self.app.robot_paused.get(f"station{index}"):
            self._update_status()
        else:
            self.ui.widget_action.setEnabled(False)
            self.ui.btn_park.setEnabled(False)

    def _update_status(self):  # Old
        for k, v in self.robot.read_io_state().items():
            state = ('opened' if v else 'closed') if k == 'hand' else ('retracted' if v else 'extended')
            getattr(self.ui, f"state_{k}").setText(state.upper())
            getattr(self.ui, f"btn_{k}").setText(
                {'opened': 'CLOSE', 'closed': 'OPEN', 'retracted': 'EXTEND', 'extended': 'RETRACT'}[state]
            )

    # def _update_status(self):  # New
    #    for k, v in self.robot.read_io_state().items():
    #        state = v
    #        getattr(self.ui, f"state_{k}").setText(state.upper())
    #        getattr(self.ui, f"btn_{k}").setText(
    #            {'opened': 'CLOSE', 'closed': 'OPEN', 'retracted': 'EXTEND', 'extended': 'RETRACT'}[state]
    #        )

    def _on_sensor_check_skip_changed(self, chk, val):
        num = int(chk.objectName().split('_')[-1])
        self.robot.write_variable(var_name=f"I{num}", value=0 if val == 0 else 1)

    def _on_inkjet_changed(self):
        self.robot.write_variable(var_name=R_INK_JET_VERTICAL_ADJUST, value=self.ui.inkjet_adjust.value())

    def _on_btn_action(self, k):
        if k == 'park':
            # ret = QMessageBox.question(
            #    self, 'Whirl',
            #    f"Are you sure you want to send the robot{self.index} to the home position?\n"
            #    f"Any currently running robot task will be aborted, please ensure there are no parts being \n"
            #    f"held by the robot hand before continuing.",
            #    QMessageBox.Yes | QMessageBox.Cancel)
            # if ret == QMessageBox.Yes:
            self.ui.error.setText("")
            self.root.park_robot(idx=self.index)
            self.close()
        elif k == 'set_speed':
            self.robot.set_speed(speed=self.ui.speed.value())
        elif k == 'vacuum':
            self.robot.set_vacuum_state(index=self.index, val="ON" in self.ui.btn_vacuum.text())
            self._update_vacuum_state()
        elif k in ['hand', 'picker', 'placer']:
            closed_extended = getattr(self.ui, f"state_{k}").text() in {'CLOSED', 'EXTENDED'}
            self.robot.write_io_state(k, closed_extended)
            self.ui.widget_action.setEnabled(False)
            QTimer.singleShot(1000 if self.index == 4 else 200, self._read_state_and_update)

    def _on_dcd_changed(self, val):
        self.robot.write_variable(var_name=R_DISABLE_COLLISION_DETECTION, value=1 if val else 0)

    def _update_vacuum_state(self):
        state = self.robot.read_vacuum_state(self.index)
        self.ui.state_vacuum.setText('ON' if state else 'OFF')
        self.ui.btn_vacuum.setText("Turn OFF" if state else 'Turn ON')

    def _read_state_and_update(self):
        self._update_status()
        self.ui.widget_action.setEnabled(True)

    def enable_park_btn(self):
        """Use Outside"""
        self.ui.btn_park.setEnabled(True)
