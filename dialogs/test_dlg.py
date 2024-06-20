import struct
import time
from functools import partial

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_test import Ui_TestDialog
from utils.cognex import CognexVisionController
from utils.denso_robot import DensoRobot
from utils.wago import WagoController
from widgets.message import show_message
from utils.logger import logger


class TestDialog(WhirlDialogBase):

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_TestDialog()
        self.ui.setupUi(self)
        self.station = None
        self.wago = None
        self.cognex = None
        self.robot = None
        for k in {'cognex', 'wago', 'robot'}:
            getattr(self.ui, f"btn_{k}_connect").released.connect(partial(self._on_btn_connect, k))
        self.ui.btn_wago_read.released.connect(self._on_btn_wago_read)
        self.ui.btn_wago.released.connect(self._on_btn_wago_turn)
        self.ui.btn_transfer.released.connect(self._on_btn_transfer)

    def _on_btn_connect(self, k):
        if k == 'cognex':
            if self.cognex is None:
                self.cognex = CognexVisionController(host=self.ui.cognex_host.text())
                if self.cognex.connect():
                    if self.robot is not None:
                        self.ui.btn_transfer.setEnabled(True)
                else:
                    show_message(msg="Failed to connect!", msg_type="Error")
                    self.cognex = None
            else:
                show_message(msg="Already connected!", msg_type="Warning")
        elif k == 'wago':
            if self.wago is None:
                self.wago = WagoController(host=self.ui.wago_host.text())
                if self.wago.connect():
                    self.wago.start()
                    self.ui.wago_address.setEnabled(True)
                    self.ui.btn_wago_read.setEnabled(True)
                    self.ui.btn_wago.setEnabled(True)
                else:
                    show_message(msg="Failed to connect!", msg_type="Error")
                    self.wago = None
            else:
                show_message(msg="Already connected!", msg_type="Warning")
        elif k == 'robot':
            robotnum = self.ui.robot_host.text()
            logger.debug(robotnum[0])
            self.station = self.app.stations[f"station{robotnum[0]}"]
            self.robot = self.station.robot
            self.ui.btn_transfer.setEnabled(True)


    def _on_btn_wago_read(self):
        self.ui.wago_status.setText('ON' if self.wago.out_values[self.ui.wago_address.value()] else 'OFF')

    def _on_btn_wago_turn(self):
        val = "ON" in self.ui.btn_wago.text()
        if self.wago.write_coil(address=self.ui.wago_address.value(), value=val):
            self.ui.btn_wago.setText(f"Turn {'OFF' if val else 'ON'}")
            time.sleep(.2)
            self._on_btn_wago_read()

    def _on_btn_transfer(self):
        values = self.cognex.read_data()
        b_val = [v.to_bytes(2, 'big') for v in values]
        x1 = struct.unpack('!f', b''.join([b_val[1], b_val[0]]))[0]
        y1 = struct.unpack('!f', b''.join([b_val[3], b_val[2]]))[0]
        r1 = struct.unpack('!f', b''.join([b_val[5], b_val[4]]))[0]
        x2 = struct.unpack('!f', b''.join([b_val[7], b_val[6]]))[0]
        y2 = struct.unpack('!f', b''.join([b_val[9], b_val[8]]))[0]
        r2 = struct.unpack('!f', b''.join([b_val[11], b_val[10]]))[0]
        x3 = struct.unpack('!f', b''.join([b_val[13], b_val[12]]))[0]
        y3 = struct.unpack('!f', b''.join([b_val[15], b_val[14]]))[0]
        r3 = struct.unpack('!f', b''.join([b_val[17], b_val[16]]))[0]
        x4 = struct.unpack('!f', b''.join([b_val[19], b_val[18]]))[0]
        y4 = struct.unpack('!f', b''.join([b_val[21], b_val[20]]))[0]
        r4 = struct.unpack('!f', b''.join([b_val[23], b_val[22]]))[0]

        self.ui.cognex_x.setText(f"X1: {round(x1, 1)} X2: {round(x2, 1)} X3: {round(x3, 1)} X4: {round(x4, 1)}")
        self.ui.cognex_y.setText(f"Y1: {round(y1, 1)} Y2: {round(y2, 1)} Y3: {round(y3, 1)} Y4: {round(y4, 1)}")
        self.ui.cognex_r.setText(f"R1: {round(r1, 1)} R2: {round(r2, 1)} R3: {round(r3, 1)} R4: {round(r4, 1)}")

        self.robot.write_variable('D10', x1)
        self.robot.write_variable('D11', y1)
        self.robot.write_variable('D12', r1)

        self.robot.write_variable('D20', x2)
        self.robot.write_variable('D21', y2)
        self.robot.write_variable('D22', r2)

        self.robot.write_variable('D30', x3)
        self.robot.write_variable('D31', y3)
        self.robot.write_variable('D32', r3)

        self.robot.write_variable('D40', x4)
        self.robot.write_variable('D41', y4)
        self.robot.write_variable('D42', r4)

    def closeEvent(self, event):
        super(TestDialog, self).closeEvent(event)
        if self.wago is not None:
            self.wago.close()
        if self.cognex is not None:
            self.cognex.close()
        if self.robot is not None:
            self.robot.close()
