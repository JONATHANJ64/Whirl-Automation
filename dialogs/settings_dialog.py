import threading
import time
from functools import partial

from PySide2.QtCore import QTimer, Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QToolButton, QPushButton, QLabel

from dialogs.base import WhirlDialogBase
from dialogs.final_assembly_test_dlg import FinalAssemblyTestDialog
from dialogs.motor_test_dialog import MotorTestDialog
from settings import DEBUG
from ui.dialogs.ui_dlg_settings import Ui_SettingsDialog
from utils.cognex import CognexVisionController, CognexBarcodeReader
from utils.common import logger, update_config_file, get_valve_bit_value, get_config
from utils.denso_robot import DensoRobot
from utils.flex_feeder import FlexFeeder
from utils.wago import WagoController
from widgets.common import widget_to_setter, widget_to_signal, widget_to_getter
from widgets.message import show_message


WAGO_OUTPUTS = ['alemite_ram', 'air1_toggle', 'main_air', 'main_conveyor', 'aux_air', 'box_cylinder_actuate']


class SettingsDialog(WhirlDialogBase):

    sig_valve_data = Signal(bytearray)

    def __init__(self, app):
        super().__init__(app)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.conf = get_config()
        self._cur_valve_slave_id = 0

        self._preload_widgets(conf=self.conf)

        self._feeders = {}
        self._timers = {}

        self._valve = app.valve

        getattr(self, 'sig_valve_data').connect(self._on_valve_data)
        self._b_stop = threading.Event()
        self._tr_valve = threading.Thread(target=self._read_valve_state)
        self._tr_valve.start()

        self._timer_wago = QTimer()
        self._timer_wago.timeout.connect(self._read_wago_state)
        self._timer_wago.start(200)

        self.ui.tabWidget.setCurrentIndex(0)
        self.changed_settings = False

        # Bind release events of the valve test output buttons
        for btn in self.ui.tabWidget.findChildren(QToolButton):
            name = btn.objectName()
            if name.endswith('_btn'):
                btn.released.connect(partial(self._on_btn_valve_test, btn, name[:-4]))

        # Bind release events of the test module buttons
        for btn in self.ui.tabWidget.findChildren(QPushButton):
            name = btn.objectName()
            if name.startswith('btn_') and name.endswith('_test'):
                btn.released.connect(partial(self._on_btn_module_test, btn, name[4:-5]))

        # Bind other buttons
        self.ui.btn_test_final_assembly.released.connect(lambda: FinalAssemblyTestDialog(app=app).exec_())
        for k in {'inject', 'purge', 'refill', 'clear_error'}:
            getattr(self.ui, f"btn_grease_{k}").released.connect(partial(self._on_grease_btn, k))
        self.ui.btn_grease_refill.setEnabled(self.app.grease_error == 'empty')
        self.ui.btn_grease_clear_error.setEnabled(self.app.grease_error == 'timeout')
        self.grease_dispenser = self.app.stations['grease']
        if not DEBUG and not self.grease_dispenser.is_started():
            self.grease_dispenser.start()
        self._timer_grease = QTimer()
        self._timer_grease.timeout.connect(self._read_grease_state)
        self._timer_grease.start(100)
        getattr(self.ui, f"radio_unload_{get_config()['station5']['unload_mode']}").setChecked(True)
        for k in {'boxing', 'binning'}:
            getattr(self.ui, f"radio_unload_{k}").toggled.connect(self._on_unload_mode_changed)
        self.ui.btn_reset_counter.released.connect(self._on_btn_reset_counter)
        self.ui.station5_en_binning_track.stateChanged.connect(self._on_en_binning_track)

        self._on_unload_mode_changed()

    def initialize(self):
        if not self._valve.is_connected() and not self._valve.connect():
            show_message(msg_type="Warning", msg="I765DNM valve adapter is not connected!")
        else:
            try:
                info = self._valve.get_information()
                logger.debug(f"Valve info: {info}")
            except OSError:
                show_message(msg_type="Warning", msg="I765DNM info error! Please restart the APP!")

    def _read_wago_state(self):
        idx = self.ui.tabWidget.currentIndex()
        if idx <= 5:
            wago = self.app.stations[f"station{idx}"].wago if idx > 0 else self.app.wago_peripheral
            if wago.in_values is not None and wago.out_values is not None:
                cur_st = f"station{self.ui.tabWidget.currentIndex()}" if idx > 0 else 'peripheral'
                self._update_wago_digital_ios(conf=self.conf[cur_st],
                                              values={'in': wago.in_values, 'out': wago.out_values},
                                              prefix=cur_st)

    @staticmethod
    def _is_wago_output(name):
        return any([v in name for v in WAGO_OUTPUTS])

    def _update_wago_digital_ios(self, prefix="", conf=None, values=None):
        for k, c in conf.items():
            wid_id = f'{prefix}_{k}' if prefix else k
            if k == 'io':
                for lb, ch in c.items():
                    try:
                        label = getattr(self.ui, f"{wid_id}_{lb}_state")
                    except AttributeError:
                        continue
                    val = values['out' if self._is_wago_output(lb) else 'in'][ch - 1]
                    if 'reverse' in lb:
                        color = 'gray' if val else 'green'
                    else:
                        color = 'green' if val else 'gray'
                    label.setPixmap(QPixmap(f":/img/img/{color}-circle.png"))
                    if self._is_wago_output(lb):
                        try:
                            getattr(self.ui, f"{wid_id}_{lb}_btn").setText('OFF' if val else 'ON')
                        except AttributeError:
                            pass
            elif type(c) == dict:
                self._update_wago_digital_ios(prefix=wid_id, conf=c, values=values)

    def _read_valve_state(self):
        while not self._b_stop.is_set():
            cur_idx = self.ui.tabWidget.currentIndex()
            if 0 < cur_idx < 6:
                slave_id = self.conf[f"station{cur_idx}"]['valve']['slave_id']
                data = self._valve.read_data(slave_id=slave_id)
                getattr(self, 'sig_valve_data').emit(data)
            time.sleep(1)

    def _on_valve_data(self, data):
        cur_idx = self.ui.tabWidget.currentIndex()
        if 0 < cur_idx < 6:
            if data is not None:
                getattr(self.ui, f"group_valve_{cur_idx}").setEnabled(True)
                cur_st = f"station{cur_idx}"
                self._update_valve_widgets(conf=self.conf[cur_st], data=data, prefix=cur_st)
            else:
                getattr(self.ui, f"group_valve_{cur_idx}").setEnabled(False)

    def _update_valve_widgets(self, prefix="", conf=None, data=None):
        for k, c in conf.items():
            wid_id = f'{prefix}_{k}' if prefix else k
            if k == 'valve':
                for lb, ch in c.items():
                    if lb != 'slave_id':
                        try:
                            label = getattr(self.ui, f"{wid_id}_{lb}_state")
                            val = get_valve_bit_value(data, ch)
                            label.setPixmap(QPixmap(f":/img/img/{'green' if val else 'gray'}-circle.png"))
                            getattr(self.ui, f"{wid_id}_{lb}_btn").setText('OFF' if val else 'ON')
                        except AttributeError:
                            pass
            elif type(c) == dict:
                self._update_valve_widgets(prefix=wid_id, conf=c, data=data)

    def _preload_widgets(self, prefix="", conf=None):
        for k, c in conf.items():
            wid_id = f'{prefix}_{k}' if prefix else k
            if type(c) == dict:
                self._preload_widgets(prefix=wid_id, conf=c)
            elif hasattr(self.ui, wid_id):
                wid = getattr(self.ui, wid_id)
                if isinstance(wid, QLabel):
                    c = str(c)
                getattr(wid, widget_to_setter(wid))(c)
                signal_name = widget_to_signal(wid)
                if signal_name:
                    getattr(wid, signal_name).connect(partial(self._on_widget_changed, wid, wid_id))

    def _on_widget_changed(self, widget, key: str, *args):

        def _update_conf(c_key: str, data: dict, value):
            for k in data.keys():
                if k == c_key:
                    data[k] = value
                    return
                elif c_key.startswith(k):
                    _update_conf(c_key=c_key[len(k) + 1:], data=data[k], value=value)
                    return

        new_val = getattr(widget, widget_to_getter(widget))()
        logger.debug(f"Setting: `{key} changed to `{new_val}`")
        _update_conf(c_key=key, data=self.conf, value=new_val)
        update_config_file(self.conf)
        self.changed_settings = True

    def _on_flex_feeder_state_update(self, station, k):
        state = self._feeders[f"{station}_{k}"].get_ready_status()
        getattr(self.ui, f"{station}_feeder_{k}_state").setText('Ready' if state.get('finished') else state.get('msg'))

    def _on_btn_valve_test(self, btn, key):
        output_type = 'io' if self._is_wago_output(key) else 'valve'

        def _get_channel(prefix="", conf=None, o_type='valve'):
            for k, c in conf.items():
                wid_id = f'{prefix}_{k}' if prefix else k
                if k == o_type:
                    for lb, ch in c.items():
                        if f"{wid_id}_{lb}" == key:
                            return ch
                elif type(c) == dict:
                    val = _get_channel(prefix=wid_id, conf=c, o_type=o_type)
                    if val is not None:
                        return val

        channel = _get_channel(conf=self.conf, o_type=output_type)
        cur_idx = self.ui.tabWidget.currentIndex()
        if output_type == 'valve':
            slave_id = self.conf[f"station{cur_idx}"]['valve']['slave_id']
            self._valve.write_bit(slave_id=slave_id, pos=channel, val=1 if btn.text() == 'ON' else 0)
        else:
            wago = self.app.stations[f"station{cur_idx}"].wago if cur_idx > 0 else self.app.wago_peripheral
            wago.write_output(channel=channel, val=1 if btn.text() == 'ON' else 0)
        if 'alemite' in key and btn.text() == 'ON':  # Alemite Ram should be reverted off for safety...
            QTimer.singleShot(1000, partial(self._on_btn_valve_test, btn, key))

    def _on_btn_module_test(self, btn, k):
        station = k.split('_')[0]
        if station == 'final':
            station = 'final_vision'
        if 'feeders' in k:
            name = k[17:]
            host = self.conf[station]['feeders'][name]
            kk = f"{station}_{k}"
            if btn.text() == "Test":
                logger.debug(f"Testing FlexFeeder({kk}), IP: {host}")
                btn.setText("Stop")
                if self._feeders.get(kk) is None:
                    self._feeders[kk] = FlexFeeder(name=name, host=host)
                    self._feeders[kk].start_feed()
                else:
                    self._feeders[kk].resume_feed()
                timer = QTimer()
                timer.timeout.connect(partial(self._on_flex_feeder_state_update, station, k))
                timer.start(500)
                self._timers[kk] = timer
            else:
                logger.debug(f"Stopping FlexFeeder({kk}), IP: {host}")
                self._feeders[kk].pause_feed()
                btn.setText("Test")
        elif 'motor' in k:
            if self.app.motor.is_opened() or self.app.open_motors():
                dlg = MotorTestDialog(parent=self, name=station)
                dlg.exec_()
            else:
                show_message("Please check motor!", msg_type='Warning')
        else:
            for name in {'robot', 'cognex', 'wago', 'barcode'}:
                if name in k:
                    logger.debug(f"Testing {name} - {k}")
                    inst = {
                        'robot': DensoRobot,
                        'cognex': CognexVisionController,
                        'wago': WagoController,
                        'barcode': CognexBarcodeReader
                    }[name](host=self.conf[station][name])
                    if inst.connect():
                        show_message(msg=f"{name.capitalize()} is alive!", msg_type="Info")
                    else:
                        show_message(msg=f"{name.capitalize()} is offline!", msg_type="Error")
                    inst.close()

    def _on_grease_btn(self, k):
        if k == 'purge':
            if self.ui.btn_grease_purge.text() == 'Purge':
                self.ui.btn_grease_purge.setText('Stop')
            else:
                self.ui.btn_grease_purge.setText('Purge')
                self.grease_dispenser.stop_purge()
                return
        self.grease_dispenser.do_action(k)

    def _read_grease_state(self):
        if self.ui.tabWidget.currentIndex() == 1:
            self.ui.station1_grease_dispenser_state.setText(self.grease_dispenser.state)

    def _on_unload_mode_changed(self, *args):
        mode = 'boxing' if self.ui.radio_unload_boxing.isChecked() else 'binning'
        update_config_file({'station5': {'unload_mode': mode}})
        self.ui.box_binning_counter.setEnabled(mode == 'binning')
        self.ui.group_boxing.setEnabled(mode == 'boxing')
        self.changed_settings = True

    def _on_btn_reset_counter(self):
        self.ui.station5_unload_num.setText("0")
        update_config_file({'station5': {'unload_num': 0}})
        self.changed_settings = True

    def _on_en_binning_track(self, val=None):
        self.ui.btn_reset_counter.setEnabled(val)
        self.ui.station5_bin_full_count.setEnabled(val)
        update_config_file({'station5': {'en_binning_track': bool(val)}})
        self.changed_settings = True

    def closeEvent(self, event):
        for t in self._timers.values():
            t.stop()
        self._b_stop.set()
        self._tr_valve.join(.2)
        self._timer_wago.stop()
        self._timer_grease.stop()
        super(SettingsDialog, self).closeEvent(event)
