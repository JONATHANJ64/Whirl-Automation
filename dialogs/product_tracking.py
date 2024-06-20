from functools import partial

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QPushButton, QMessageBox

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_product_tracking import Ui_ProductTrackingDialog
from utils.common import get_config, update_config_file


names = [k for k in get_config().get('tracking', {}).keys() if '_time' not in k]


class ProductTrackingDialog(WhirlDialogBase):

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_ProductTrackingDialog()
        self.ui.setupUi(self)
        self._timer = QTimer()
        self._timer.timeout.connect(self._update_tracking_info)
        self._update_tracking_info()
        self._timer.start(1000)
        for btn in self.findChildren(QPushButton):
            btn.released.connect(partial(self._on_btn_reset, btn.objectName()[10:]))

    def _update_tracking_info(self):
        info = get_config().get('tracking', {})
        for name in names:
            getattr(self.ui, name).setText(str(info.get(name, 0)))
        self.ui.parts_count.setText(str(self.app.get_current_part_count_in_box() or 0))

    def _on_btn_reset(self, k):
        txt = getattr(self.ui, f"lb_{k}").text() if k != 'all' else 'ALL'
        ret = QMessageBox.question(self, 'Whirl', f"Are you sure you want to reset \"{txt}\"?",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.No:
            return
        if k == 'all':
            update_config_file({'tracking': {name: 0 for name in names}})
        else:
            update_config_file({'tracking': {k: 0}})
        self._update_tracking_info()

    def closeEvent(self, event):
        self._timer.stop()
        super().closeEvent(event)
