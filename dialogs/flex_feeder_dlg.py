import threading
import time
from functools import partial

from PySide2.QtCore import Signal, QSize
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QComboBox

from dialogs.base import WhirlDialogBase
from ui.dialogs.ui_dlg_flex_feeder import Ui_FlexFeederDialog
from utils.logger import logger
from widgets.common import widget_to_setter, widget_to_signal, widget_to_getter
from widgets.message import show_message


class FlexFeederDialog(WhirlDialogBase):

    sig_state = Signal(dict)

    def __init__(self, app, name):
        super().__init__(app)
        self.name = name
        self.ui = Ui_FlexFeederDialog()
        self.ui.setupUi(self)
        self.ui.img.setPixmap(QPixmap(f":/img/img/components/{name}.png"))
        ff_name = ' '.join([v.upper() for v in name.split('_')])
        self.setWindowTitle(f"Flex Feeder Dialog({ff_name})")
        self.ui.name.setText(ff_name)
        self.state = {}
        self.ui.btn_close.released.connect(self.close)
        for i in range(1, 6):
            if name in self.app.stations[f"station{i}"].feeders:
                self.station = self.app.stations[f"station{i}"]
                self.robot = self.station.robot
                self.feeder = self.station.feeders[name]
                self.conf = self.feeder.get_feeder_config()
                break

        if not self.conf:
            show_message(msg_type="Critical", msg="Failed to connect to the feeder!")
            self.close()
            return
        self.ui.type.setText(f"Type: {self.conf['type']}")
        if not self.conf.get('is_dial'):
            self.ui.group_dial.setParent(None)
            self.ui.btn_dial_lift.hide()
        else:
            self.ui.btn_dial_lift.released.connect(partial(self._on_btn, 'dial_lift'))
        self.ui.stack_other.setCurrentWidget(getattr(self.ui, f"page_{self.conf.get('type', 'Recirculating').lower()}"))
        self._preload_widgets(conf=self.conf)
        self._on_type_changed(self.conf['type'])
        self._feeder_state = None
        getattr(self, 'sig_state').connect(self._on_feeder_state)
        self._tr = threading.Event()
        self._thread = threading.Thread(target=self._poll_feeder_state)
        self._thread.start()
        for k in {'start_feed', 'backlight', 'clear_error', 'conveyor_lift', 're_acquire', 'pause_resume'}:
            getattr(self.ui, f"btn_{k}").released.connect(partial(self._on_btn, k))
        for k in {'main_forward', 'main_backward', 'feeder_forward', 'return_forward', 'return_backward'}:
            getattr(self.ui, f"btn_{k}").released.connect(partial(self._on_btn_conveyor, k))

    def _preload_widgets(self, prefix="", conf=None):
        for k, c in conf.items():
            wid_id = f'{prefix}_{k}' if prefix else k
            if type(c) == dict:
                self._preload_widgets(prefix=wid_id, conf=c)
            elif hasattr(self.ui, wid_id):
                wid = getattr(self.ui, wid_id)
                if isinstance(wid, QComboBox):
                    c = str(c)
                getattr(wid, widget_to_setter(wid))(c)
                signal_name = widget_to_signal(wid)
                if signal_name:
                    getattr(wid, signal_name).connect(partial(self._on_widget_changed, wid, wid_id))

    def _on_widget_changed(self, widget, key: str, *args):

        def _update_conf(c_key: str, data: dict, value):
            for k in data.keys():
                if k == c_key:
                    if isinstance(widget, QComboBox) and 'frequency' in widget.objectName():
                        value = int(value)
                    data[k] = value
                    return
                elif c_key.startswith(k):
                    _update_conf(c_key=c_key[len(k) + 1:], data=data[k], value=value)
                    return

        new_val = getattr(widget, widget_to_getter(widget))()
        logger.debug(f"Setting: `{key} changed to `{new_val}`")
        _update_conf(c_key=key, data=self.conf, value=new_val)
        if not self.feeder.update_feeder_config(self.conf):
            show_message(msg_type="Critical", msg="Failed to update feeder config!")

    def _on_type_changed(self, f_type):
        self.ui.stack_other.setCurrentWidget(getattr(self.ui, f"page_{f_type.lower()}"))
        getattr(self.ui.group_return, 'show' if f_type == 'Recirculating' else 'hide')()
        if f_type == 'Recirculating':
            self.ui.btn_conveyor_lift.hide()
        self.ui.reverse_time.setEnabled(f_type != 'Recirculating')
        self.ui.pre_check_timeout.setEnabled(f_type != 'Recirculating')
        self.ui.part_presence_timeout.setEnabled(f_type != 'Recirculating')
        self.ui.feeder_idle_timeout.setEnabled(f_type == 'Recirculating')

    def _on_btn(self, k):
        if k == 'start_feed':
            txt = self.ui.btn_start_feed.text().lower()
            if 'restart' in txt:
                if self.robot.check_paused_and_parked():
                    logger.debug(f"{self.robot} is parked, restarting(rejecting) flex feeder({self.name}) now...")
                    self.station.disregard_feeder_pos(name=self.name, reject=True)
                else:
                    show_message(msg_type="Error", msg="Please pause & park the robot!")
            else:
                self.feeder.stop_feed()
            self._all_conveyor_off()
        elif k == 're_acquire':
            if self.robot.check_paused_and_parked():
                logger.debug(f"{self.name}: Re-Acquiring feeder...")
                self.station.disregard_feeder_pos(name=self.name, reject=False)
            else:
                show_message(msg_type="Error", msg="Please pause & park the robot!")
        elif k == 'backlight':
            self.feeder.turn_backlight(val='ON' in self.ui.btn_backlight.text())
        elif k == 'clear_error':
            self.feeder.reject_part()
        elif k == 'dial_lift':
            self.feeder.turn_ev0(val=True if 'UP' in self.ui.btn_dial_lift.text() else False)  # - New
            # self.feeder.lift_slide(action='lift' if 'UP' in self.ui.btn_dial_lift.text() else 'down') - Old,  Broken
            self.ui.btn_dial_lift.setText(f"Dial Lift {'DOWN' if 'UP' in self.ui.btn_dial_lift.text() else 'UP'}")
        elif k == 'conveyor_lift':
            self.feeder.lift_slide(action='lift' if 'UP' in self.ui.btn_conveyor_lift.text() else 'down')
            self.ui.btn_conveyor_lift.setText(
                f"Conveyor Lift {'DOWN' if 'UP' in self.ui.btn_conveyor_lift.text() else 'UP'}")
        elif k == 'pause_resume':
            if self.ui.btn_pause_resume.text() == "Resume":
                self.feeder.resume_feed()
            else:
                self.feeder.pause_feed()

    def _all_conveyor_off(self):
        self.feeder.turn_backlight(val=False)
        self.feeder.stop_motor(name='feeder')
        self.feeder.stop_motor(name='main')
        if self.ui.type.text() == 'Recirculating':
            self.feeder.stop_motor(name='return')

    def _on_btn_conveyor(self, k):
        name, d = k.split('_')
        if self.ui.type.text() == 'Reciprocating' and name == 'return':
            return
        if self._feeder_state != 'idle':
            show_message(msg_type="Warning",
                         msg="The component feeder should be stopped before attempting to move the conveyor!")
            return
        btn = getattr(self.ui, f"btn_{k}")
        other_d = f"btn_{name}_{'backward' if d == 'forward' else 'forward'}"
        other_btn = getattr(self.ui, other_d) if hasattr(self.ui, other_d) else None
        if btn.text() == 'X':
            self.feeder.stop_motor(name=name)
            btn.setText('>>' if d == 'forward' else '<<')
            if other_btn is not None:
                other_btn.setEnabled(True)
        else:
            if not self.robot.check_paused_and_parked():
                show_message(msg_type="Error", msg="Please pause & park the robot!")
                return
            self.feeder.action_motor(name=name, action='speed', direction=d)
            btn.setText('X')
            if other_btn is not None:
                other_btn.setEnabled(False)
            self.feeder.ignore_pos()

    def _poll_feeder_state(self):
        while not self._b_stop.is_set():
            state = self.feeder.read_current_state()
            state['robot_parked'] = self.robot.check_paused_and_parked()
            state['online'] = self.feeder.is_feeder_online()
            getattr(self, 'sig_state').emit(state)
            time.sleep(.4)

    def _on_feeder_state(self, state):
        if not state.get('online') and self.state.get('online'):
            show_message(msg_type="Warning", msg=f"{self.name.capitalize()} Feeder became offline!")
            self.close()
            return
        self.ui.lb_paused.setText("Paused: YES" if state.get('paused') else "Paused: NO")
        self.ui.btn_pause_resume.setText("Resume" if state.get('paused') else "Pause")
        self._feeder_state = state.get('state', 'N/A')
        feeder_stopped = state.get('stopped_feeder')
        self.ui.lb_state.setText(self._feeder_state)

        self.ui.btn_start_feed.setText(
            "Restart Feed" if self._feeder_state in {'idle', 'ready'} or feeder_stopped else 'Stop Feed')
        self.ui.btn_re_acquire.setEnabled(self._feeder_state in {'idle', 'ready'})
        self.ui.lb_robot_paused_parked.setText(
            f"<html><head/><body><p>Robot Paused &amp; Parked: <span style=\"font-weight:600;\">"
            f"{'YES' if state.get('robot_parked') else 'NO'}</span></p></body></html>")

        for k in {'main_forward', 'main_backward', 'feeder_forward', 'return_forward', 'return_backward'}:
            getattr(self.ui, f"btn_{k}").setEnabled(state.get('robot_parked'))

        bl = state.get('backlight', False)
        icon = QIcon()
        icon.addFile(f":/img/img/{'green' if bl else 'gray'}-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_backlight.setIcon(icon)
        self.ui.btn_backlight.setText(f" Turn Backlight {'OFF' if bl else 'ON'}")
        self.ui.lb_error.setText(state.get('msg') or '')
        self.ui.group_buttons.setDisabled(bool(state.get('msg')))
        self.ui.group_conveyor.setDisabled(bool(state.get('msg')))
        getattr(self.ui.btn_clear_error, "show" if bool(state.get('msg')) else "hide")()
        self.state = state

    def closeEvent(self, event):
        self._b_stop.set()
        self._thread.join(.5)
        return super(FlexFeederDialog, self).closeEvent(event)
