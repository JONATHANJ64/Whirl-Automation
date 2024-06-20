from functools import partial

from PySide2.QtGui import QFont
from PySide2.QtWidgets import QPushButton, QSizePolicy

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_lift_locate import Ui_LiftLocateDialog


class LiftLocateDialog(WhirlDialogBase):

    def __init__(self, parent, index):
        super().__init__(parent)
        self.ui = Ui_LiftLocateDialog()
        self.ui.setupUi(self)
        self.app = parent
        self.index = index
        self._pallet = self.app.pallet_handlers[index]
        self.station = self._pallet.root
        self.setWindowTitle(f"{self.station.name} Errors")
        self.alarms = self._pallet.get_station_alarms()
        self.a_idx = 0
        self._show_alarm()

    def _show_alarm(self):
        # Clear layout
        for i in reversed(range(self.ui.layout_buttons.count())):
            item = self.ui.layout_buttons.itemAt(i)
            if item.widget() is not None:
                item.widget().deleteLater()

        alarm = self.alarms[self.a_idx]
        self.ui.error.setText(alarm.get('msg', ''))
        if alarm.get('level') != 'init-box-detected':
            self.ui.widget_others.hide()
        for txt in alarm.get('buttons', []):
            btn = QPushButton(self.ui.box)
            btn.setText(txt)
            sp = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
            sp.setHorizontalStretch(0)
            sp.setVerticalStretch(0)
            sp.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
            btn.setSizePolicy(sp)
            font = QFont()
            font.setPointSize(12)
            btn.setFont(font)
            btn.released.connect(partial(self._on_btn, txt, alarm))
            self.ui.layout_buttons.addWidget(btn)

    def _on_btn(self, action, alarm):
        if hasattr(self.station, 'remove_first_alarm'):
            self.station.remove_first_alarm()

        if alarm.get('level') == 'init-box-detected':
            alarm['callback'](action.lower(), self.ui.spin_cnt.value())
        elif callable(alarm.get('callback')):
            alarm['callback'](action.lower())

        if self.a_idx < len(self.alarms) - 1:
            self.a_idx += 1
            self._show_alarm()
        elif action not in alarm.get('keep_actions', []):
            self.close()
