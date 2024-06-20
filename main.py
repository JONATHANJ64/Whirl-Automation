import os
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

import glob
import threading
import time
import sys
from functools import partial
import traceback
from settings import DEBUG, COGNEX_JOBS
from utils.can_motor_candle import PyCanMotor
from utils.common import get_config, get_pallet_state, update_pallet_state, set_pallet_state_exclusive, \
    clear_pallet_state, update_config_file
from utils.valve import I765DNMValveController
from PySide2.QtGui import QIcon, Qt
from PySide2.QtCore import Signal, QTimer, QSize, QObject, QEvent
from PySide2 import QtGui
from dialogs.boxing_dialog import BoxingDialog
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QSizePolicy, QAction, QInputDialog
from PySide2.QtGui import QFont
from utils.logger import logger
from utils.kmtronic_usb_relay import KMTronicUSBRelay
from utils.wago import WagoController
from stations.station1 import Station1
from stations.station2 import Station2
from stations.station3 import Station3
from stations.station4 import Station4
from stations.station5 import Station5
from stations.final_assembly_test import FinalAssemblyTestRoutine
from stations.grease_dispenser import GreaseDispenser
from ui.ui_whirl import Ui_Whirl
from dialogs.flex_feeder_dlg import FlexFeederDialog
from dialogs.product_tracking import ProductTrackingDialog
from dialogs.labeler_dialog import LabelerDialog
from dialogs.pallet_edit_dialog import PalletEditDialog
from dialogs.hopper_dialog import HopperDialog
from widgets.touch_observer import TouchObserver
from widgets.spinner import QtSpinner
from widgets.message import show_message
from routines.pallet_handler import PalletHandlerRoutine
from dialogs.test_dlg import TestDialog
from dialogs.settings_dialog import SettingsDialog
from dialogs.pallet_init_dialog import PalletInitDialog
from dialogs.station_dialog import StationDialog
from dialogs.robot_error_dlg import RobotErrorDialog
from dialogs.robot_home_confirm_dlg import RobotHomeConfirmDialog


_cur_dir = os.path.dirname(os.path.realpath(__file__))


class WhirlApp(QMainWindow):

    ui = Ui_Whirl()
    alarms = []
    pallets = get_pallet_state()
    alarm_level = None
    conf = get_config()
    motor = PyCanMotor()
    km_relay = KMTronicUSBRelay()
    main_power = False
    _power_checked = False
    _conn_msg = None
    valve = I765DNMValveController()

    sig_alarm_added = Signal()
    grease_error = None
    _b_stop = threading.Event()
    _dialogs = {}
    _lock = threading.Lock()
    is_building = False
    is_stopped = False
    is_flush = False
    sig_pallet_state = Signal(tuple)
    sig_station_state = Signal(dict)
    sig_main_power = Signal(bool)
    sig_door_state = Signal(dict)
    sig_finished = Signal(str)
    robot_paused = {}
    cycle_ts = None
    cur_circuit_broken = False
    circuit_was_broken = False
    _timer_cycle = QTimer()
    _timer_robot_motor_check = QTimer()
    _ts_start = 0
    product_type = None
    _ever_built = False

    def __init__(self):
        super().__init__()
        # ========== Basic UI setup ==========
        self.ui.setupUi(self)
        # Add horizontal spacer before the main power tool button
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred))
        self.ui.toolBar.addWidget(spacer)
        self.action_main_power = QAction(self)
        self.ui.toolBar.addAction(self.action_main_power)
        self.action_main_power.triggered.connect(self._on_main_power_action)
        getattr(self, "sig_alarm_added").connect(self.show_alarms)
        for k in {'test', 'settings', 'station'}:
            getattr(self.ui, f"action{k.capitalize()}").triggered.connect(partial(self._open_dialog, k))
        self.ui.actionProductTracking.triggered.connect(partial(self._open_dialog, 'tracking'))
        self.ui.actionDoor.triggered.connect(self._on_action_door)

        self.ui.btn_build.released.connect(self.btn_build)
        self.ui.btn_clear_pallet_state.released.connect(self._on_btn_clear_pallet_state)
        self.ui.btn_stop.released.connect(self._on_btn_stop)
        self.ui.btn_flush.released.connect(self._on_btn_flush)
        getattr(self, 'sig_pallet_state').connect(self._on_pallet_state_changed)
        getattr(self, 'sig_station_state').connect(self._on_station_state_changed)
        getattr(self, 'sig_main_power').connect(self._on_main_power_status)
        getattr(self, 'sig_finished').connect(self._on_finished_signal)
        self.ui.mode.currentTextChanged.connect(self._on_mode_changed)
        self.ui.btn_flush.setDisabled(True)
        self.ui.mode.setDisabled(True)
        self.ui.btn_build.setStyleSheet("background-color: red; color: black;")

        self._timer_cycle.timeout.connect(self._check_cycle_finished)
        self._timer_robot_motor_check.timeout.connect(self._check_robot_motor_state)

        self._tr_peripheral = threading.Thread(target=self._monitor_door_and_leds)
        getattr(self, 'sig_door_state').connect(self._on_door_state)

        self.spinner = QtSpinner(parent=self)
        self.ui.btn_build.setEnabled(False)
        self._on_main_power_status()

        self.pallet_handlers = {index: PalletHandlerRoutine(app=self, index=index) for index in range(1, 8)}
        self.wago_peripheral = WagoController(host=self.conf['peripheral']['wago'])
        self.stations = {
            'station1': Station1(app=self),
            'station2': Station2(app=self),
            'station3': Station3(app=self),
            'station4': Station4(app=self),
            'station5': Station5(app=self),
            'grease': GreaseDispenser(app=self),
            'final_test': FinalAssemblyTestRoutine(app=self),
        }

        self._tr_main_power = threading.Thread(target=self._monitor_main_power)
        self._tr_main_power.start()
        for name in self.pallets:
            self.pallets[name]['flushed'] = False

        self.ui.board.set_app(self)

    def _open_dialog(self, name):
        if self._dialogs.get(name) is not None:
            return
        if name == 'test':
            self._dialogs[name] = TestDialog(app=self)
        elif name == 'settings':
            if not DEBUG and not self._power_checked:
                show_message(msg_type="Warning", msg="Not ALL peripheral devices are online now. Try again later.")
                return
            self._dialogs[name] = SettingsDialog(app=self)
        elif name == 'station':
            self._dialogs[name] = StationDialog(app=self)
        elif name == 'tracking':
            self._dialogs[name] = ProductTrackingDialog(app=self)
        self._dialogs[name].closed.connect(partial(self._on_dialog_closed, name))
        self._dialogs[name].show()

    def _on_dialog_closed(self, name):
        if name == 'settings':
            if self._dialogs[name].changed_settings:
                self.ui.statusbar.showMessage("System Settings Changed. Please launch the program again.")
        self._dialogs[name] = None

    def add_alarm(self, alarm):
        logger.error(f"Alarm({alarm.get('level')}): {alarm['msg']}")
        with self._lock:
            self.alarms.append(alarm)
        getattr(self, "sig_alarm_added").emit()

    def open_motors(self):
        if not self.motor.is_opened():
            if not self.motor.open():
                show_message(msg="No Motor Adapter Found!", msg_type='Critical')
                return
            try:
                self.motor.reset_all_motors()
            except Exception as e:
                logger.error(f"Failed to reset all motors - {e}")
                return False
            locked = self.motor.lock_motor_positions()
            if not all(locked):
                invalid_indexes = [i for i, r in enumerate(locked) if not r]
                names = []
                for i in invalid_indexes:
                    for m, st in self.conf.items():
                        if st['motor']['address'] == i:
                            names.append(m)
                            break
                show_message(
                    msg=f"Motor of {', '.join(names)} {' is' if len(names) < 2 else 's are'}"
                        f" not connected!", msg_type='Critical')
                return
        return True

    def show_alarms(self):
        if self.alarm_level is not None:
            return
        while self.alarms:
            with self._lock:
                alarm = self.alarms.pop(-1)
            self.alarm_level = alarm['level']
            if alarm.get('type') == 'robot_error':
                dlg = RobotErrorDialog(app=self, msg=alarm['msg'])
                dlg.sig_action.connect(partial(self._on_robot_action, alarm))
                dlg.exec_()
            elif alarm.get('type') == 'robot_home_confirm':
                dlg = RobotHomeConfirmDialog(app=self, msg=alarm['msg'])
                dlg.sig_action.connect(partial(self._on_robot_action, alarm))
                dlg.exec_()
            else:
                ret = getattr(QMessageBox, alarm['level'])(
                    self, 'Whirl', alarm['msg'],
                    alarm.get('buttons', QMessageBox.Retry | QMessageBox.Abort),
                    alarm.get('default_button', QMessageBox.Retry))
                if callable(alarm.get('callback')):
                    try:
                        r_val = ret.name.decode().lower()
                    except AttributeError:
                        r_val = None
                    alarm['callback'](r_val)
            time.sleep(.1)
        self.alarm_level = None

    def _on_robot_action(self, alarm, action):
        if callable(alarm.get('callback')):
            alarm['callback'](action)
        self.alarm_level = None

    def pause_station_robot_button(self, index):
        self.ui.board.update_robot_button(idx=index, state='pause')

    def on_touch_released(self):
        pass

    def get_current_part_count_in_box(self):
        return self.stations['station5'].get_current_part_count_in_box()

    def set_grease_error(self, error):
        self.grease_error = error
        if error:
            self.ui.statusbar.showMessage(
                {
                    'empty': 'Warning: Grease reservoir level low!',
                    'timeout': 'Warning: Grease filling timeout!'
                }[error])
        else:
            self.ui.statusbar.clearMessage()

    def btn_build(self, force=None):
        txt = force or self.ui.btn_build.text()
        if txt == 'Run':
            if any([not self.stations[f"station{i}"].can_robot_start() for i in range(1, 6)]):
                show_message(msg_type="Warning", msg="All robots are not ready to run!")
                return
        if txt in {"Start", 'Run'} and self._door_safety_circuit_broken():
            ret = QMessageBox.question(self, 'Whirl', "A machine door is still open, please close and try again",
                                       QMessageBox.Retry | QMessageBox.Cancel)
            if ret == QMessageBox.Retry:
                QTimer.singleShot(10, self.btn_build)
            return

        if txt == 'Pause':
            self.ui.btn_clear_pallet_state.setEnabled(True)
            self.ui.btn_build.setText("Run")
            self._write_peripheral_output(name='main_conveyor', val=False)
            for st in self.stations.values():
                st.pause()
            for i in range(1, 6):
                self.pause_robot(i)
            self.ui.board.set_robot_buttons(False)
            self.is_building = False
            self.ui.btn_build.setStyleSheet("background-color: red; color: black;")
            self.ui.btn_build.setFont(QFont('MS Shell Dlg 2', 12))
        elif 'cycle' in txt.lower():
            self.cycle_ts = time.time()
            for p in self.pallet_handlers.values():
                p.cycle_one()
            self.ui.btn_build.setText("Pause")
        else:       # Start or Run
            en_labeler = get_config().get('station5', {}).get('labeler', {}).get('enabled', False)
            if not self._ever_built:       # Very first build
                p_type, ok = QInputDialog().getItem(self, "Select Product Type",
                                                    "Product Type:", list(COGNEX_JOBS.keys()), 0, False)
                if ok:
                    logger.info(f">>> Selected product type: '{p_type}'")
                    self.product_type = p_type
                    self.ui.lb_product_type.setText(f"Product Type: {p_type}")
                    for st in self.stations.values():
                        threading.Thread(target=st.set_product_type, args=(p_type, )).start()
                    if 'Whirl' not in p_type:
                        self.ui.board.disable_support_arm()
                # if QMessageBox.question(self, 'Whirl',
                #                        f"Labeler is {'en' if en_labeler else 'dis'}abled, start building?",
                #                        QMessageBox.Yes | QMessageBox.Cancel
                #                        ) == QMessageBox.Cancel:
                #    return
                # Clear current production status
                update_config_file(data={'tracking': {'total_current': 0, 'rejected_current': 0}})

                if any([p.get('pos') == 'lift_locate' and not p.get('is_new') for p in self.pallets.values()]):
                    pallet_init_dlg = PalletInitDialog(app=self)
                    pallet_init_dlg.sig_confirm.connect(self._on_pallet_init_confirmed)
                    pallet_init_dlg.exec_()
                    self.ui.btn_build.setStyleSheet("background-color: green; color: black;")
                    self.ui.btn_build.setFont(QFont('MS Shell Dlg 2', 12))
                    return
            self.ui.btn_build.setStyleSheet("background-color: green; color: black;")
            self.ui.btn_build.setFont(QFont('MS Shell Dlg 2', 12))
            self._start_build()

    def _on_pallet_init_confirmed(self, pallets):
        self.pallets = pallets
        update_pallet_state(pallets)
        self.ui.board.update_pallet_widgets()
        for st in self.stations.values():
            st.apply_finished_parts()
        self._start_build()

    def _check_robot_motor_state(self):
        if all([self.stations[f"station{i}"].robot.get_motor_status() for i in range(1, 6)]):
            logger.info("All robot motors are turned ON.")
            self._timer_robot_motor_check.stop()
            self.circuit_was_broken = False
            self.spinner.stop()
            self._start_build()
            return
        if time.time() - self._ts_start > 5:
            not_running = [str(i) for i in range(1, 6) if not self.stations[f"station{i}"].robot.get_motor_status()]
            show_message(msg_type="Error", msg=f"Motor of Robot {','.join(not_running)} are still not ON!\n"
                                               f"Please try again later!")
            self._timer_robot_motor_check.stop()
            self.ui.btn_build.setStyleSheet("background-color: red; color: black;")
            self.ui.btn_build.setFont(QFont('MS Shell Dlg 2', 12))
            self.spinner.stop()

    def _start_build(self):
        if self.circuit_was_broken:
            self._ts_start = time.time()
            for i in range(1, 6):
                threading.Thread(target=self.stations[f"station{i}"].robot.turn_motor, args=(True, )).start()
            self._timer_robot_motor_check.start(200)
            self.spinner.start()
            return

        for name in self.pallets:
            self.pallets[name]['flushed'] = False

        self.circuit_was_broken = False
        self.ui.board.set_robot_buttons(True)
        if self.ui.mode.currentIndex() == 1:
            self.cycle_ts = time.time()
        self.ui.btn_clear_pallet_state.setEnabled(False)
        self.ui.btn_build.setText("Pause")
        self._write_peripheral_output(name='main_conveyor', val=True)
        for st in self.stations.values():
            if st.is_started():
                st.resume()
            else:
                st.start()
        self.is_building = True
        # self.ui.btn_stop.setEnabled(True)
        # self.ui.btn_flush.setEnabled(True)
        self._ever_built = True

        # WIP
        # init_p_handlers = []
        # while True:
        #    for st in self.stations.keys():
        #        if self.stations[f'{st}'].are_pallet_handlers_initialized():
        #            init_p_handlers.append(st)
        #    if len(init_p_handlers) == len(self.stations):
        #        break
        #    time.sleep(0.25)

        self.ui.statusbar.showMessage("Build started...", 5000)

    def _on_mode_changed(self, val):
        if self.is_building:
            ret = QMessageBox.question(self, 'Whirl', f"Change mode to {val}?", QMessageBox.Yes | QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                return
            if self.ui.mode.currentIndex() == 0:    # Continuous
                self.cycle_ts = None
            else:
                self.cycle_ts = time.time()

    def _check_cycle_finished(self):
        if self.cycle_ts is not None and self.is_building and self.ui.mode.currentIndex() == 1:
            if all([p.is_finished_one_cycle() for p in self.pallet_handlers.values()]):
                logger.debug(f"All Lift & Locates finished one cycle!")
                self.ui.btn_build.setText("Cycle One")

    def on_flex_feeder_btn(self, ff):
        if ff == 'hopper':
            HopperDialog(app=self).exec_()
        elif ff == 'labeler':
            LabelerDialog(app=self).exec_()
        elif ff == 'boxing':
            if self.robot_paused.get('station5', True) is True:
                BoxingDialog(app=self).exec_()
            else:
                self.ui.statusbar.showMessage("Please pause & park the robot 5 to edit boxing...", 3000)
        else:
            for i in range(1, 6):
                if ff in self.stations[f"station{i}"].feeders:
                    feeder = self.stations[f"station{i}"].feeders[ff]
                    if feeder.is_feeder_online():
                        FlexFeederDialog(app=self, name=ff).exec_()
                    else:
                        show_message(msg_type="Warning", msg=f"{ff.capitalize()} Feeder is Offline!")

    def _write_peripheral_output(self, name, val):
        try:
            self.wago_peripheral.write_output(channel=self.conf['peripheral']['io'][name], val=val)
        except Exception as e:
            logger.error(f"Failed to write to peripheral WAGO - {e}")

    def pause_robot(self, idx):
        self.ui.board.pause_robot(idx)

    def turn_led(self, color='green', val=True):
        self._write_peripheral_output(name=f"led_{color}", val=val)

    def publish_pallet_state(self, sn, state, clear_old=False):
        getattr(self, 'sig_pallet_state').emit((sn, state, clear_old))

    def publish_station_state(self, data):
        getattr(self, 'sig_station_state').emit(data)

    def _on_pallet_state_changed(self, data):
        sn, state, clear_old = data
        if sn is None:
            logger.error(f"Invalid pallet state - {state}")
            return
        if sn not in self.pallets:
            self.pallets[sn] = {}
        if state == {'state': 'remove'}:
            self.ui.board.remove_pallet_widget(sn)
            return 
        if clear_old:
            set_pallet_state_exclusive(sn=sn, pallet_state=state)
            self.pallets[sn] = state
        else:
            update_pallet_state({sn: state})
            self.pallets[sn].update(**state)
        self.ui.board.update_pallet_widget_pos(sn)

    def _on_station_state_changed(self, state):
        self.ui.board.update_station_state(state)

    def _on_btn_clear_pallet_state(self):
        ret = QMessageBox.question(self, 'Whirl',
                                   "Clear state of all pallets? If so, please take out ALL pallets and press YES",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.No:
            return
        self.pallets = {}
        clear_pallet_state()
        self.ui.board.clear_pallets()

    def _on_btn_stop(self):
        # if not self.is_building or self.is_flush:
        #     return
        ret = QMessageBox.question(self, 'Whirl', "STOP current operation?", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.No:
            return
        self.ui.btn_build.setDisabled(True)
        self.is_stopped = True
        self.ui.btn_stop.setEnabled(False)
        self._write_peripheral_output(name='main_conveyor', val=False)
        self._stop_whole_machine()
        self.ui.statusbar.showMessage("Stopping the whole machine...")

    def _on_btn_flush(self):
        if not self.is_building or self.is_stopped:
            return
        ret = QMessageBox.question(self, 'Whirl',
                                   "Flush? This will clean all pallets and completely empty the line!",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.No:
            return
        self.ui.statusbar.showMessage("Flushing the whole machine...")
        self.is_flush = True
        self.ui.btn_flush.setEnabled(False)

    def cancel_all_prefetched_parts(self):
        for i in range(1, 6):
            self.stations[f"station{i}"].cancel_prefetched_part()

    def emit_finished_signal(self, sig_type):
        getattr(self, 'sig_finished').emit(sig_type)

    def _on_finished_signal(self, sig_type):
        if sig_type == 'flush':
            self.ui.statusbar.showMessage("Whole machine is flushed...")

    def on_edit_pallet_state_triggered(self, sn):
        PalletEditDialog(app=self, sn=sn).exec_()

    def apply_manual_pallet_state(self, sn, new_state):
        for st, _ in new_state.items():
            for i in range(1, 6):
                self.stations[f"station{i}"].mark_part_as_done(st)
        self.pallets[sn].update(**new_state)
        update_pallet_state({sn: self.pallets[sn]})

    def call_action_door(self):
        self._on_action_door(query=False)

    def _door_safety_circuit_broken(self):
        return not self.wago_peripheral.read_input(channel=self.conf['peripheral']['io']['door_safety_circuit'])

    def _monitor_door_and_leds(self):
        while not self._b_stop.is_set():
            broken = self._door_safety_circuit_broken()
            opened = self.wago_peripheral.read_output(channel=self.conf['peripheral']['io']['door_lock'])
            getattr(self, 'sig_door_state').emit({'broken': broken, 'opened': opened})
            # Manage LEDs
            self.turn_led(color='green', val=self.is_building)
            self.turn_led(color='red', val=not self.is_building)
            # self.turn_led(
            #    color='orange',
            #    val=(self.alarms or any([v.station_alarms for v in self.stations.values()]) or self.grease_error))
            # time.sleep(.1)

            # WIP - will replace line above when finished
            self.turn_led(
                color='orange',
                val=(self.alarms or any(self.ui.board.robot_cont_errors.values())
                     or any(self.ui.board.robot_pp_errors.values()) or
                     any(self.ui.board.f_errors.values()) or
                     any([v.station_alarms for v in self.stations.values()]) or self.grease_error))
            time.sleep(0.1)

    def _on_door_state(self, state):
        broken = state['broken']
        self.ui.door_circuit.setStyleSheet(f"border-radius:12px;background-color:#{'aa0000' if broken else '00aa00'};")
        icon = QIcon()
        icon.addFile(
            f":/img/img/door_{'opened' if state['opened'] else 'closed'}.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.actionDoor.setIcon(icon)
        self.cur_circuit_broken = broken
        if broken and self.circuit_was_broken != broken:
            logger.warning("Current Safety Circuit Broken!")
            self.ui.statusbar.showMessage("Current Safety Circuit Broken!", 5000)
            self.btn_build(force='Pause')
            self.circuit_was_broken = broken

    def _on_action_door(self, query=True):
        ch = self.conf['peripheral']['io']['door_lock']
        opened = self.wago_peripheral.read_output(channel=ch)
        if query:
            ret = QMessageBox.question(self, 'Whirl', f"{'Close' if opened else 'Open'} the door?",
                                       QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.No:
                return
        if not opened:
            for i in range(1, 6):
                if not self.stations[f"station{i}"].can_robot_start():
                    show_message(msg_type='Warning', msg=f"Robot{i} is still running!\nPlease try again once finished!")
                    return
        self._write_peripheral_output(name='door_lock', val=not opened)

    def _on_main_power_action(self):
        ret = QMessageBox.question(self, 'Whirl',
                                   f"Are you sure you want to power o{'ff' if self.main_power else 'n'}?",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.No:
            return
        logger.debug(f"Turning main power O{'FF' if self.main_power else 'N'}")
        self.km_relay.turn_relay(not self.main_power)

    def _check_all_peripherals(self):
        if not self.motor.is_opened() and not self.open_motors():
            self._conn_msg = "Motors are not connected!"
            return False
        time.sleep(2)

        if not self.wago_peripheral.connected and not self.wago_peripheral.connect():
            self._conn_msg = "Wago Peripheral is not connected!"
            return False

        for i in range(1, 6):
            r, msg = self.stations[f"station{i}"].check_peripherals()
            if not r:
                self._conn_msg = f"Station{i}:: {msg}"
                return False

        if not self.valve.is_connected() and not self.valve.connect():
            self._conn_msg = "I765DNM valve adapter is not connected!"
            return False
        else:
            self.valve.reset_device()
            time.sleep(4)
            logger.debug("Activating all DeviceNet slave devices...")
            for i in range(1, 5):
                self.valve.start_slave_device(slave_id=self.conf[f"station{i}"]['valve']['slave_id'])
        return True

    def _monitor_main_power(self):
        while not self._b_stop.is_set():
            status = self.km_relay.get_status()
            if status:
                if not self.main_power:
                    logger.debug("Main power is just turned on...")
                    try:
                        self.wago_peripheral.start()
                    except RuntimeError:        # Already started?
                        pass
                    for i in range(1, 6):
                        try:
                            self.stations[f"station{i}"].wago.start()
                        except RuntimeError:    # Already started?
                            pass
                if not self._power_checked:
                    if self._check_all_peripherals():
                        self._write_peripheral_output(name='main_air', val=True)
                        self._write_peripheral_output(name='aux_air', val=True)
                        self.circuit_was_broken = self._door_safety_circuit_broken()
                        self._power_checked = True
            getattr(self, 'sig_main_power').emit(status)
            time.sleep(1)

    def _on_main_power_status(self, val=False):
        self.action_main_power.setToolTip(f'Power/Lights/Air - {"OFF" if val else "ON"}')
        icon = QIcon()
        icon.addFile(f":/img/img/main_power_{'off' if val else 'on'}.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_main_power.setIcon(icon)
        self.ui.btn_build.setEnabled(self._power_checked)
        if val:
            if not self.main_power:
                self._timer_cycle.start(100)
                self._tr_peripheral.start()
            if not self._power_checked:
                self.ui.statusbar.showMessage(self._conn_msg)
            else:
                self.ui.board.start_background_jobs()
                self.ui.statusbar.clearMessage()
        else:
            self.ui.statusbar.showMessage("Turn the MAIN power ON")
        self.main_power = val

    def _stop_whole_machine(self):
        self.ui.board.close()
        self._timer_cycle.stop()
        self._b_stop.set()
        try:
            self._tr_main_power.join(.3)
        except RuntimeError:
            logger.error("Failed to join the main power thread!")
        try:
            self._tr_peripheral.join(.3)
        except RuntimeError:
            logger.error("Failed to join the door monitoring thread!")
        self.valve.close(close=self.main_power)
        for st in self.stations.values():
            try:
                st.stop()
            except RuntimeError:
                pass
        self.wago_peripheral.close(close=self.main_power)
        self.motor.close(close=self.main_power)
        for p in self.pallet_handlers.values():
            p.stop()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.MouseButtonPress and event.buttons() == Qt.RightButton:
            obj_name = watched.objectName()
            if obj_name.startswith('btn_ff'):
                self.ui.board.on_ff_right_click(obj_name[7:])
        return super().eventFilter(watched, event)

    def closeEvent(self, event) -> None:
        ret = QMessageBox.question(self, 'Whirl', "Are you sure to close the app?", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.No:
            event.ignore()
            return
        if self.km_relay.get_status() is False:
            event.accept()
            return
        for i in range(1, 6):
            if not self.stations[f"station{i}"].ready_for_close():
                show_message(msg_type='Error', msg=f"Station{i} is still running! Please stop and try again!")
                event.ignore()
                return
        self._stop_whole_machine()
        event.accept()


if __name__ == '__main__':

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, exc_tb):
        logger.error(f'!!! Crashed! Exctype: {exctype}, Value: {value}, Traceback: {traceback.format_tb(exc_tb)}')
        getattr(sys, "_excepthook")(exctype, value, exc_tb)
        sys.exit(1)

    sys.excepthook = exception_hook

    logger.info("========== Starting Whirl GUI App ==========")
    app = QApplication(sys.argv)

    for font in glob.glob(os.path.join(_cur_dir, 'fonts', '*.ttf')):
        QtGui.QFontDatabase.addApplicationFont(font)

    whirl_app = WhirlApp()
    app.installEventFilter(whirl_app)
    whirl_app.show()
    touch_observer = TouchObserver(whirl_app.window().windowHandle())
    touch_observer.released.connect(lambda pos: whirl_app.on_touch_released())

    sys.exit(app.exec_())
