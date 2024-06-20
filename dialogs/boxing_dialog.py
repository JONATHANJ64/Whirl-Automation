from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_boxing import Ui_BoxingDialog


class BoxingDialog(WhirlDialogBase):

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_BoxingDialog()
        self.ui.setupUi(self)
        self.station = app.stations['station5']
        cur_cnt = self.station.get_current_part_count_in_box()
        if cur_cnt is None:
            self.ui.spin_cnt.setDisabled(True)
        else:
            self.ui.spin_cnt.setValue(cur_cnt)
            self.ui.spin_cnt.valueChanged.connect(self._on_counter_changed)
        self.ui.btn_restart.released.connect(self._on_btn_restart)

    def _on_counter_changed(self):
        self.station.update_current_part_count_in_box(self.ui.spin_cnt.value())

    def _on_btn_restart(self):
        self.station.restart_boxing_final()
        self.close()
