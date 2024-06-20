from PySide2.QtWidgets import QCheckBox, QMessageBox

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_pallet_edit import Ui_PalletEditDialog
from utils.logger import logger
from widgets.message import show_message


class PalletEditDialog(WhirlDialogBase):

    def __init__(self, app, sn):
        super().__init__(app)
        self.sn = sn
        self.ui = Ui_PalletEditDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Edit Pallet {sn}")
        self.ui.btn_close.released.connect(self.close)
        self.ui.btn_apply.released.connect(self._on_btn_apply)
        self.state = self.app.pallets.get(sn, {})
        for name, st in self.state.items():
            if hasattr(self.ui, name) and isinstance(getattr(self.ui, name), QCheckBox):
                if st:
                    getattr(self.ui, name).setChecked(True)
                    getattr(self.ui, name).setEnabled(False)
                elif st is False:       # Currently working part
                    if self.state.get(f"{name}_parked"):
                        getattr(self.ui, name).setEnabled(True)
                    else:
                        getattr(self.ui, name).setEnabled(False)
                        logger.info(f"Currently processing {name}, "
                                    f"but robot was never parked.. disabling manual checkbox...")
        for i in range(1, 6):
            for chk in getattr(self.ui, f"station_{i}").findChildren(QCheckBox):
                chk.stateChanged.connect(self._on_chk_changed)

    def _on_chk_changed(self):
        self.ui.btn_apply.setEnabled(True)

    def _on_btn_apply(self):
        state = {}
        for i in range(1, 6):
            for chk in getattr(self.ui, f"station_{i}").findChildren(QCheckBox):
                state[chk.objectName()] = chk.isChecked()
        changed_parts = [name for name, st in state.items() if st and not self.state.get(name)]
        if changed_parts:
            ret = QMessageBox.question(self, 'Whirl', f"Mark {','.join(changed_parts)} as DONE?",
                                       QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.Yes:
                logger.debug(f"{changed_parts} {'is' if len(changed_parts) == 1 else 'are'} "
                             f"marked as DONE manually, updating...")
                self.app.apply_manual_pallet_state(self.sn, {name: True for name in changed_parts})
                self.close()
        else:
            show_message(msg_type="Information", msg="Nothing Changed!")
