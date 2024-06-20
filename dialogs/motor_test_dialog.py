import threading
import time
from functools import partial

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_motor_test import Ui_MotorTestDialog
from utils.common import update_config_file, get_config


class MotorTestDialog(WhirlDialogBase):

    motor_status = Signal(dict)

    def __init__(self, parent, name):
        super().__init__(parent)
        self.ui = Ui_MotorTestDialog()
        self.ui.setupUi(self)
        # This dialog is opened from the settings dialog!
        self.app = parent.app
        self.motor = self.app.motor
        self.name = name

        self.ui.btnClose.released.connect(self.close)
        self.ui.btnSetPID.released.connect(self._on_btn_set_pid)
        self.ui.btnTestAngle.released.connect(partial(self._on_btn_test, 'Angle'))
        self.ui.btnTestSpeed.released.connect(partial(self._on_btn_test, 'Speed'))
        self.ui.btnTestTorque.released.connect(partial(self._on_btn_test, 'Torque'))
        self.conf = get_config()[name]['motor']
        self.motor_id = self.conf['address'] + 1
        self.setWindowTitle(f"{name.capitalize()} Motor Configuration")

        self._is_running = False

        # Preload values from config
        for k, v in self.conf.items():
            if k == 'address':
                self.ui.address.setText(str(v))
            elif hasattr(self.ui, k):
                getattr(self.ui, k).setValue(v)

        getattr(self, 'motor_status').connect(self._on_motor_status_updated)
        self._tr_motor = threading.Thread(target=self._loop_motor_status)
        self._tr_motor.start()

        if not self.motor.is_opened():
            if not self.motor.open():
                self.app.add_alarm(dict(
                    msg="Motor Adaptor Not Found!",
                    level='critical',
                    buttons=QMessageBox.Retry | QMessageBox.Abort,
                    default_button=QMessageBox.Retry,
                    callback=self._on_msg_closed))

        self._on_btn_set_pid()

    def _on_msg_closed(self, ret):
        pass
        # if not self.motor.is_opened():
        #     if not self.motor.open():
        #         self.app.add_alarm(
        #         dict(msg="Motor Adaptor Not Found!", level='critical', callback=self._on_msg_closed))

    def _read_pid_params(self):
        pid_params = self.motor.read_pid_parameters(arb_id=self.motor_id)
        # Sometimes the motor returns ALL zero as the PID parameters.
        if pid_params and all([v > 0 for v in pid_params.values()]):
            self.ui.PIDBox.setEnabled(True)
            self.ui.OpBox.setEnabled(True)
            for k, v in pid_params.items():
                getattr(self.ui, k).setValue(v)
            return True
        else:
            self.ui.PIDBox.setEnabled(False)
            self.ui.OpBox.setEnabled(False)

    def _loop_motor_status(self):
        while not self._b_stop.is_set():
            status = dict(
                single_turn_angle=self.motor.read_single_circle_angle(arb_id=self.motor_id),
                multi_turn_angle=self.motor.read_multi_turns_angle(arb_id=self.motor_id),
            )
            encoder_data = self.motor.read_encoder_data(arb_id=self.motor_id) or {}
            for k in {'cur_pos', 'orig_pos', 'offset'}:
                status[f'encoder_{k}'] = encoder_data.get(k)
            status1 = self.motor.read_motor_status_1(arb_id=self.motor_id) or {}
            for k in {'temperature', 'voltage'}:
                status[k] = status1.get(k)
            status2 = self.motor.read_motor_status_2(arb_id=self.motor_id) or {}
            for k in {'torque', 'speed'}:
                status[k] = status2.get(k)
            getattr(self, 'motor_status').emit(status)
            time.sleep(.2)

    def _on_motor_status_updated(self, status):
        for k, v in status.items():
            if v is not None:
                getattr(self.ui, k).setEnabled(True)
                getattr(self.ui, k).setText(str(v))
            else:
                getattr(self.ui, k).setEnabled(False)

    def _on_btn_set_pid(self):
        self.motor.write_pid_parameters(
            arb_id=self.motor_id,
            to_rom=self.ui.chkPIDROM.isChecked(),
            angle_kp=self.ui.angle_kp.value(),
            angle_ki=self.ui.angle_ki.value(),
            speed_kp=self.ui.speed_kp.value(),
            speed_ki=self.ui.speed_ki.value(),
            torque_kp=self.ui.torque_kp.value(),
            torque_ki=self.ui.torque_ki.value()
        )
        self._read_pid_params()
        for k in {'angle_kp', 'angle_ki', 'speed_kp', 'speed_ki', 'torque_kp', 'torque_ki'}:
            self.app.conf[self.name]['motor'][k] = getattr(self.ui, k).value()
        update_config_file(self.app.conf)

    def _on_btn_test(self, t_type='Angle'):
        if self._is_running:
            for t in {'Angle', 'Speed', 'Torque'}:
                getattr(self.ui, f"btnTest{t}").setEnabled(True)
                getattr(self.ui, f"btnTest{t}").setText('Start')
            self.motor.stop_motor(self.motor_id)
            self._is_running = False
        else:
            getattr(self.ui, f"btnTest{t_type}").setText('Stop')
            if t_type == 'Angle':
                self.ui.btnTestSpeed.setEnabled(False)
                self.ui.btnTestTorque.setEnabled(False)
                speed_limit = self.ui.target_angle_speed_limit.value()
                if self.ui.radio_single.isChecked():
                    direction = 'clockwise' if self.ui.comboAngleDirection.currentIndex() == 0 else 'counterclockwise'
                    self.motor.set_position_single_turn(arb_id=self.motor_id, angle=self.ui.target_angle.value(),
                                                        direction=direction, speed_limit=speed_limit)
                else:
                    self.motor.set_position_multi_turn(arb_id=self.motor_id, pos=self.ui.target_angle.value(),
                                                       speed_limit=speed_limit)
            elif t_type == 'Speed':
                self.ui.btnTestAngle.setEnabled(False)
                self.ui.btnTestTorque.setEnabled(False)
                self.motor.set_speed(arb_id=self.motor_id, speed=self.ui.target_speed.value())
            else:
                self.ui.btnTestAngle.setEnabled(False)
                self.ui.btnTestSpeed.setEnabled(False)
                self.motor.set_torque_current(arb_id=self.motor_id, torque=self.ui.target_torque.value() / 1000.)
            self._is_running = True

    def close(self):
        self._b_stop.set()
        self._tr_motor.join(.5)
        return super(MotorTestDialog, self).close()
