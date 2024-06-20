import os
from functools import partial
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import QToolButton, QMenu, QAction, QMessageBox

from utils.logger import logger
from widgets.message import show_message

FEEDERS = {
    1: ['lower_housing', ],
    2: ['grease', ],
    3: ['cross_gear', 'ring_gear', 'pinion', 'crank_handle'],
    4: ['upper_housing', 'crank_arm', 'rotor'],
    5: ['left_handle', 'dial', 'support_arm', 'trigger'],
    6: ['right_handle', 'hopper', 'agitator'],
}
_cur_dir = os.path.dirname(os.path.realpath(__file__))


class PalletWidget(QToolButton):

    def __init__(self, parent, app, sn=''):
        super().__init__(parent)
        self.app = app
        self.sn = sn
        self.setText("")
        self.setFixedSize(QSize(78, 48))
        self.setToolTipDuration(5000)
        self.set_icon(name="pallet_0_0")

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
        self.pop_menu = QMenu(self)
        self.action_reject = QAction('Reject', self)
        icon_reject = QIcon()
        icon_reject.addFile(":/img/img/reject.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_reject.setIcon(icon_reject)
        self.action_reject.triggered.connect(partial(self._on_action, 'reject'))
        self.pop_menu.addAction(self.action_reject)
        self.pop_menu.addSeparator()
        self.action_remove = QAction('Remove', self)
        icon_delete = QIcon()
        icon_delete.addFile(":/img/img/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_remove.setIcon(icon_delete)
        self.action_remove.triggered.connect(partial(self._on_action, 'remove'))
        self.pop_menu.addAction(self.action_remove)
        self.pop_menu.addSeparator()
        self.action_edit_parts = QAction('Edit Parts', self)
        icon_edit_part = QIcon()
        icon_edit_part.addFile(":/img/img/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_edit_parts.setIcon(icon_edit_part)
        self.action_edit_parts.triggered.connect(partial(self.app.on_edit_pallet_state_triggered, sn))
        self.pop_menu.addAction(self.action_edit_parts)

        self.action_manual_unload = QAction('Unload Manually', self)
        icon_manual_unload = QIcon()
        icon_manual_unload.addFile(":/img/img/grab.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_manual_unload.setIcon(icon_manual_unload)
        self.action_manual_unload.triggered.connect(partial(self._on_action, 'manual_unload'))
        self.pop_menu.addAction(self.action_manual_unload)
        self.action_manual_unload.setVisible(False)

        self.update_state(show_log=False)

    def set_icon(self, name):
        if not os.path.exists(os.path.join(_cur_dir, os.pardir, 'ui', 'img', f"{name}.png")):
            if not name.endswith('_0'):
                logger.warning(f"No such icon - {name}")
            return
        icon = QIcon()
        icon.addFile(f":/img/img/{name}.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QSize(78, 48))

    def update_state(self, show_log=True):
        state = self.app.pallets[self.sn]
        index = state.get('index', 0)
        if show_log:
            logger.debug(f"Pallet{self.sn}: updating state - {state}")
        if state.get('pos') == 'lift_locate':
            finished = [f for f in FEEDERS.get(index, []) if state.get(f)]
            self.set_icon(name=f"pallet_{index}_{len(finished)}")

        # self.action_remove.setEnabled(state.get('pos') == 'transit') < disabled 'remove', has bugs.
        self.action_manual_unload.setVisible(state.get('pos') == 'lift_locate' and index == 1)
        self.action_reject.setDisabled(state.get('state') == 'reject')

        tooltip = f"<center><h3><b>Pallet{self.sn}</b></h3></center><hr/>"
        for k in range(1, 7):
            for name in FEEDERS.get(k, []):
                if state.get(name):
                    tooltip += f"✔{name}<br/>"
                elif state.get(name) is False:
                    tooltip += f"⠀ <b>{name}</b><br/>"
                elif k == index:
                    tooltip += f"⠀ <tt>{name}</tt><br/>"
        if state.get('count') is not None:
            tooltip += f"Final Test Count: {state.get('count')}</br>"
        self.setToolTip(tooltip)
        self.setStyleSheet("border: 2px solid red;background-color:#e1e1e1" if state.get('state') == 'reject' else '')

    def on_context_menu(self, point):
        self.pop_menu.exec_(self.mapToGlobal(point))

    def _on_action(self, action):
        ret = QMessageBox.question(self, 'Whirl', f"{action.capitalize()} this pallet?",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.No:
            return
        if action == 'reject':
            state = self.app.pallets[self.sn]
            # No need to check robot for Grease Dispenser and Final Assembly Check
            if state['index'] not in {2, 7} and state['pos'] in 'lift_locate':
                if 'state_num' in state and \
                        not self.app.stations[f"station{state['state_num']}"].robot.check_paused_and_parked():
                    show_message(msg_type="Error", msg="Please park robot before rejecting pallet!")
                    return
            if state.get('state_num') == 5 and state['index'] == 1 and state['pos'] == 'lift_locate':
                show_message(msg_type="Error", msg="Cannot reject pallet, please use unload manually instead.")
                return
            if state['index'] not in {2, 7}:
                if state['pos'] in 'lift_locate':
                    self.app.pallet_handlers[state['index']].root.reject_pallet()
            else:
                if state['index'] == 2:
                    if state['pos'] in 'lift_locate':
                        self.app.stations['grease'].reject_pallet()
                elif state['index'] == 7:
                    if state['pos'] in 'lift_locate':
                        show_message(msg_type='Error', msg="Cannot reject pallet at final test station.")
                        return

        if action == 'manual_unload':
            station = self.app.stations['station5']
            if not station.robot.check_paused_and_parked():
                show_message(msg_type="Error", msg="Robot is not paused and parked!")
                return
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Whirl")
            msgbox.setText('Please unload the pallet from the "Lift & Locate 1" and press CONTINUE')
            msgbox.addButton('CONTINUE', QMessageBox.YesRole)
            msgbox.exec_()
            station.unload_manually()
            return
        if action == 'remove':
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Whirl")
            msgbox.setText('Please remove the pallet from conveyor and press CONTINUE')
            msgbox.addButton('CONTINUE', QMessageBox.YesRole)
            msgbox.exec_()
        self.app.publish_pallet_state(sn=self.sn, state={'state': action})
