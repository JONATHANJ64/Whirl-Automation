import threading
import time
from functools import partial

from PySide2 import QtGui
from PySide2.QtCore import Qt, QSize, QTimer, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QMessageBox, QToolButton, QMenu, QAction

from dialogs.lift_locate_dialog import LiftLocateDialog
from dialogs.robot_dialog import RobotDialog
from dialogs.robot_error_code_dlg import RobotErrorCodeDialog
from settings import ROBOT_COMMON_EVENTS, ROBOT_EXTRA_EVENTS
from ui.ui_board import Ui_BoardWidget
from utils.logger import logger
from widgets.pallet import PalletWidget


class BoardWidget(QWidget):

    sig_feeder_state = Signal(dict)
    sig_park_complete = Signal(int)
    sig_robot_cont_error = Signal(dict)
    sig_robot_pp_error = Signal(dict)

    _feeder_state = {}

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_BoardWidget()
        self.ui.setupUi(self)
        self.app = None
        self._pallets = {}
        self.ui.layout_queue_1.setAlignment(Qt.AlignLeft)
        self.ui.layout_queue_5.setAlignment(Qt.AlignRight)
        self.ui.layout_queue_6.setAlignment(Qt.AlignBottom)
        self.ui.layout_queue_7.setAlignment(Qt.AlignLeft)
        self.robot_io_state = {}
        self.robot_cont_errors = {}
        self.robot_pp_errors = {}
        self.f_errors = {}
        self._robot_error_timers = {}
        for i in range(1, 6):
            self.get_robot_btn(i).released.connect(partial(self.on_btn_robot_play, i))
            getattr(self.ui, f"btn_robot_more_{i}").released.connect(partial(self._on_btn_robot_more, i))
            getattr(self.ui, f"btn_robot_error_{i}").setVisible(False)
            getattr(self.ui, f"btn_robot_error_{i}").released.connect(partial(self._on_btn_robot_error, i))
            timer = QTimer()
            timer.timeout.connect(partial(self._execute_robot_error_timer, i))
            timer.start(250)
            self._robot_error_timers[i] = timer
        self._b_stop = threading.Event()
        self.ui.btn_pause_all_robots.released.connect(self._on_btn_pause_all_robots)
        self._robot_dlg = None
        self._tr_robot_parking = {}
        self._b_stop_park = {i: threading.Event() for i in range(7)}
        getattr(self, 'sig_feeder_state').connect(self._on_feeder_state)
        getattr(self, 'sig_park_complete').connect(self._on_park_completed)
        getattr(self, 'sig_robot_cont_error').connect(self._on_robot_cont_error)
        getattr(self, 'sig_robot_pp_error').connect(self._on_robot_pp_error)
        for i in range(1, 8):
            getattr(self.ui, f"groupBox_{i}").sig_clicked.connect(partial(self._on_ll_clicked, i))
        self._station_alarm_timer = QTimer()
        self._station_alarm_timer.timeout.connect(self._check_station_alarms)
        self._background_jobs_started = False

    def set_app(self, app):
        self.app = app
        for sn, state in app.pallets.items():
            self._pallets[sn] = PalletWidget(parent=self, app=app, sn=sn)
            self.update_pallet_widget_pos(sn)
        for btn in self.ui.board.findChildren(QToolButton):
            name = btn.objectName()
            if name.startswith("btn_ff"):
                btn.released.connect(partial(self.app.on_flex_feeder_btn, name[7:]))
        self._station_alarm_timer.start(100)
        # Pause all robots at the beginning
        for i in range(1, 6):
            self.on_btn_robot_play(i)

    def start_background_jobs(self):
        if not self._background_jobs_started:
            threading.Thread(target=self._monitor_feeder_errors).start()
            threading.Thread(target=self._check_robot_error).start()
            self._background_jobs_started = True

    def update_pallet_widgets(self):
        for sn in self.app.pallets:
            self.update_pallet_widget_pos(sn)

    def update_pallet_widget_pos(self, sn):
        if sn not in self._pallets:
            self._pallets[sn] = PalletWidget(parent=self, app=self.app, sn=sn)

        state = self.app.pallets[sn]
        if state.get('state') == 'remove':
            return
        wid = self._pallets[sn]
        wid.update_state()
        if state.get('pos') == 'transit':
            index = [w.get('ts', 0) for w in self.app.pallets.values()
                     if w.get('pos') == 'transit' and w.get('index') == state.get('index')].index(
                state.get('ts', 0))
            layout = f"layout_queue_{state['index']}"
            if hasattr(self.ui, layout):        # LL3 doesn't have queue...
                getattr(self.ui, layout).insertWidget(index, wid)
        elif state.get('pos') == 'lift_locate':
            getattr(self.ui, f"layout_pallet_{state['index']}").insertWidget(0, wid)

    def remove_pallet_widget(self, sn):
        if sn in self._pallets:
            self._pallets[sn].deleteLater()
            self._pallets.pop(sn, None)

    def clear_pallets(self):
        for sn in self._pallets:
            self._pallets[sn].deleteLater()
        self._pallets = {}

    def update_station_state(self, data):
        if data.get('type') == 'current':
            getattr(self.ui, f"current_{data['target']}").setText(data['value'])
        elif data.get('type') == 'error':
            wid = getattr(self.ui, f"error_{data['target']}")
            wid.setText(data.get('value'))
            wid.setStyleSheet(f"color: rgb({'170, 0, 0' if data.get('value') else '0, 170, 0'})")

    def get_robot_btn(self, idx):
        return getattr(self.ui, f"btn_robot_play_{idx}")

    def set_robot_buttons(self, val):
        for i in range(1, 6):
            self.get_robot_btn(i).setEnabled(val)
        self.ui.btn_pause_all_robots.setEnabled(val)
        self.ui.btn_pause_all_robots.setText("Resume ALL robots")

    def on_btn_robot_play(self, idx):
        if self.get_robot_btn(idx).text() == 'pause':
            self.pause_robot(idx)
        else:
            self.start_robot(idx)

    def pause_robot(self, idx):
        """Used outside"""
        name = f"station{idx}"
        robot = self.app.stations[name].robot
        if self._tr_robot_parking.get(idx) is not None:
            logger.info(f"Pausing {robot} parking...")
            self._b_stop_park[idx].set()
            self._tr_robot_parking[idx].join(.5)
            self._tr_robot_parking[idx] = None
            self.app.robot_paused[name] = 'park'
        else:
            if robot.is_connected():
                self.robot_io_state[name] = robot.read_io_state()  # save IO state
                logger.info(f"Pausing robot{idx}, IO state - {self.robot_io_state[name]}")
                self.app.robot_paused[name] = 'interrupted' if robot.get_task_status() == 'RUN' else True
            else:
                self.app.robot_paused[name] = True
        robot.pause()
        self.update_robot_button(idx=idx, state='start')
        return True

    def start_robot(self, idx):
        """Used outside"""
        self.app.stations[f"station{idx}"].mark_robot_parked(val=False)
        name = f"station{idx}"
        if idx == 5 and self.app.stations[name].state == 'bin_full':
            ret = QMessageBox.question(
                self, 'Whirl', "Product bin was full, did you empty and reset the counter?",
                QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.No:
                return
            self.app.stations[name].restart_after_bin_full()

        robot = self.app.stations[name].robot
        if self.robot_io_state.get(name) and robot.read_io_state() != self.robot_io_state[name]:
            ret = QMessageBox.question(
                self, 'Whirl',
                f"Robot{idx} hand must be set back to initial state before continuing. YES to proceed?",
                QMessageBox.Yes | QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                return
            logger.debug(f"IO state of robot{idx} is changed, applying old one - {self.robot_io_state[name]}")
            for k, v in self.robot_io_state[name].items():
                robot.write_io_state(k, v)

        paused_reason = self.app.robot_paused.get(name)
        if paused_reason == 'interrupted':
            logger.debug(f"Robot{idx} was interrupted, starting task with 1...")
            robot.start_task()
        elif paused_reason == 'park':
            self.park_robot(idx)
            return True
        elif paused_reason in {'other', True}:
            logger.debug(f"Robot{idx} was paused in idle, continue task...")
            robot.continue_task()
        self.app.robot_paused[name] = False
        self.robot_io_state[name] = {}
        self.update_robot_button(idx=idx, state='pause')
        return True

    def update_robot_button(self, idx, state):
        """Used Outside"""
        logger.debug(f"Setting robot button({idx}) as {state}")
        btn = self.get_robot_btn(idx)
        btn.setText(state)
        icon = QIcon()
        icon.addFile(f":/img/img/{state}.png", QSize(), QIcon.Normal, QIcon.Off)
        btn.setIcon(icon)

    def _on_btn_robot_more(self, idx):
        self._robot_dlg = RobotDialog(
            app=self.app, root=self, index=idx, error=self.robot_pp_errors.get(idx, ""),
            park_enable=self._tr_robot_parking.get(idx) is None and not self.app.cur_circuit_broken)
        self._robot_dlg.closed.connect(self._on_robot_dlg_closed)
        self._robot_dlg.exec_()

    def _on_robot_dlg_closed(self):
        self._robot_dlg = None

    def park_robot(self, idx):
        """Used Outside"""
        self.app.stations[f"station{idx}"].mark_robot_parked(val=True)
        self.app.robot_paused[f"station{idx}"] = False
        self.robot_io_state[f"station{idx}"] = {}
        self._b_stop_park[idx].clear()
        self._tr_robot_parking[idx] = threading.Thread(target=self._park_robot, args=(idx, ))
        self._tr_robot_parking[idx].start()
        self.update_robot_button(idx=idx, state='pause')

    def _park_robot(self, idx):
        robot = self.app.stations[f"station{idx}"].robot
        for i in range(80, 91):
            robot.write_variable(var_name=f"I{i}", value=0)
            time.sleep(0.05)
        self.app.stations[f"station{idx}"].robot_go_home(stop_flag=self._b_stop_park[idx],
                                                         sig_finish=self.sig_park_complete)

    def _on_park_completed(self, idx):
        self._tr_robot_parking[idx] = None
        if self._robot_dlg is not None:
            self._robot_dlg.enable_park_btn()
        self.app.robot_paused[f"station{idx}"] = True
        self.update_robot_button(idx=idx, state='start')

    def _on_btn_robot_error(self, idx):
        error = self.robot_cont_errors.get(idx) or self.robot_pp_errors.get(idx)
        RobotErrorCodeDialog(app=self.app, index=idx, err=error).exec_()

    def _check_robot_error(self):
        while not self._b_stop.is_set():
            # Continuous Error
            for i in range(1, 6):
                robot = self.app.stations[f"station{i}"].robot
                error = robot.get_cont_error()
                if not robot.is_connected() or '8700' in str(error) or 'blackout' in str(error)\
                        or '11271' in str(error) or 'Communication error with Teach' in str(error):
                    error = f'Lost connection with Robot {i}, attempting to reestablish...'
                if 'Enable Auto signal ON' in str(error):
                    error = f'Teach pendant key not set to auto mode'
                self.robot_cont_errors[i] = error
                getattr(self, 'sig_robot_cont_error').emit({'index': i, 'error': error})
            # Pick & Place Error
            for num in range(1, 6):
                if not self.app.stations[f"station{num}"].robot.is_connected():
                    continue
                pp_err = ""
                for i in range(80, 93):
                    val = self.app.stations[f"station{num}"].robot.read_variable(var_name=f"I{i}")
                    if val is not None and val > 0:
                        self.pause_robot(num)
                        logger.error(f"Pick & Place Error(I{i}) on robot {num}!")
                        if i < 83:
                            pp_err = ROBOT_COMMON_EVENTS[i].format(
                                num=num, part=self.app.stations[f"station{num}"].get_current_feeder_name())
                        else:
                            pp_err = ROBOT_EXTRA_EVENTS.get(num, {}).get(i, '')
                getattr(self, 'sig_robot_pp_error').emit({'num': num, 'err': pp_err})
            time.sleep(.1)

    def _on_robot_pp_error(self, data):
        self.robot_pp_errors[data['num']] = data['err']

    def _on_robot_cont_error(self, data):
        i = data['index']
        error = data['error']
        getattr(self.ui, f"btn_robot_play_{i}").setEnabled(not error and not self.app.cur_circuit_broken)
        getattr(self.ui, f"btn_robot_more_{i}").setEnabled(not error)

    def _monitor_feeder_errors(self):
        while not self._b_stop.is_set():
            state = {}
            for i in range(1, 6):
                for name, feeder in self.app.stations[f"station{i}"].feeders.items():
                    state[name] = feeder.read_current_state()
            state['labeler'] = self.app.stations['station5'].read_labeler_state()
            getattr(self, 'sig_feeder_state').emit(state)
            time.sleep(1)

    def _on_feeder_state(self, state):
        self._feeder_state = state
        for name, st in state.items():
            btn = getattr(self.ui, f"btn_ff_{name}")
            self.f_errors[name] = st.get('msg')
            if st.get('msg'):
                logger.error(f"Error on the feeder({name}) - {st}")
                btn.setStyleSheet(
                    """QToolButton{
                        border: 2px solid #BB0000;
                        background-color: #E1E1E1;
                        color: #BB0000;
                    }
                    QToolButton::hover {
                      border: 2px solid #FF0000;
                      background-color: #E5F1FB;
                      color: #FF0000;
                    }
                    """
                )
            else:
                btn.setStyleSheet('')
                self.feeder_errors = None
            btn.setToolTip(st.get('msg') or '')

    def on_ff_right_click(self, name):
        if self._feeder_state.get(name, {}).get('msg'):
            menu = QMenu()
            action_clear = QAction("Clear Error")
            icon = QIcon()
            icon.addFile(u":/img/img/clean.png", QSize(), QIcon.Normal, QIcon.Off)
            action_clear.setIcon(icon)
            menu.addAction(action_clear)
            action = menu.exec_(QtGui.QCursor.pos())
            menu.close()
            if action is not None:
                for i in range(1, 6):
                    if name in self.app.stations[f"station{i}"].feeders:
                        feeder = self.app.stations[f"station{i}"].feeders[name]
                        feeder.reject_part()

    def _execute_robot_error_timer(self, idx):
        error = self.robot_cont_errors.get(idx, "") or self.robot_pp_errors.get(idx, "")
        btn = getattr(self.ui, f"btn_robot_error_{idx}")
        btn.setEnabled(bool(error))
        btn.setToolTip(error)
        btn.setVisible(bool(error))  # and int(time.time() * 10) % 4 != 0) <--- causes icon to flash

    def _on_btn_pause_all_robots(self):
        if "pause" in self.ui.btn_pause_all_robots.text().lower():
            logger.debug("Pausing ALL robots...")
            for i in range(1, 6):
                self.pause_robot(i)
                time.sleep(0.05)
            self.ui.btn_pause_all_robots.setText("Resume ALL robots")
        else:
            logger.debug("Resuming ALL robots...")
            for i in range(1, 6):
                self.start_robot(i)
                time.sleep(0.05)
            self.ui.btn_pause_all_robots.setText("Pause ALL robots")

    def _on_ll_clicked(self, idx):
        if self.app.pallet_handlers[idx].get_station_alarms():
            LiftLocateDialog(parent=self.app, index=idx).exec_()
        else:
            logger.warning(f"No station error on Station{idx}")

    def _check_station_alarms(self):
        for i in range(1, 8):
            alarms = self.app.pallet_handlers[i].get_station_alarms()
            box = getattr(self.ui, f"groupBox_{i}")
            if alarms:
                box.setStyleSheet("ClickableGroupBox {color:#0000C8; border:1px solid #C80000;} \n"
                                  "ClickableGroupBox:hover {color:#0000C8; cursor:pointer; border:1px solid #C80000;}\n"
                                  "QToolTip {color:red;}")
                box.setToolTip(alarms[0].get('msg', ''))
            else:
                box.setStyleSheet("ClickableGroupBox {color: #0000C8;}")
                box.setToolTip('')

    def disable_support_arm(self):
        self.ui.btn_ff_support_arm.setEnabled(False)

    def close(self):
        self._station_alarm_timer.stop()
        self._b_stop.set()
        for t in self._robot_error_timers.values():
            t.stop()
