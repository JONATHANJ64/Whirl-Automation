from functools import partial

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QCheckBox

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_pallet_init import Ui_PalletInitDialog


class PalletInitDialog(WhirlDialogBase):

    sig_confirm = Signal(dict)

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_PalletInitDialog()
        self.ui.setupUi(self)
        self.pallets = app.pallets
        for sn, p in self.pallets.items():
            if p.get('pos') == 'lift_locate':
                index = p['index']
                getattr(self.ui, f"ll_{index}").setEnabled(True)
                for chk in getattr(self.ui, f"ll_{index}").findChildren(QCheckBox):
                    name = chk.objectName()
                    chk.setChecked(p.get(name, False))
                    chk.stateChanged.connect(partial(self._on_chk_changed, sn, name))
                getattr(self.ui, f"pallet_{index}").setText(f"Pallet {sn}")
            if p.get('count') is not None:      # finished part
                self.ui.lower_housing.setEnabled(False)

        self.ui.btn_confirm.released.connect(self._on_btn_confirm)

    def _on_chk_changed(self, sn, name, val):
        self.pallets[sn][name] = bool(val)

    def _on_btn_confirm(self):
        getattr(self, 'sig_confirm').emit(self.pallets)
        self.close()
