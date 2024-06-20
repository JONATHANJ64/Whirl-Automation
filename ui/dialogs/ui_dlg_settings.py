# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.whirl_rc
import ui.whirl_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(1368, 1147)
        font = QFont()
        font.setPointSize(11)
        SettingsDialog.setFont(font)
        self.rootLayout = QVBoxLayout(SettingsDialog)
        self.rootLayout.setObjectName(u"rootLayout")
        self.tabWidget = QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.tabWidget.setFont(font1)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.groupBox_55 = QGroupBox(self.tab_general)
        self.groupBox_55.setObjectName(u"groupBox_55")
        self.groupBox_55.setGeometry(QRect(20, 30, 421, 291))
        self.verticalLayout_62 = QVBoxLayout(self.groupBox_55)
        self.verticalLayout_62.setSpacing(10)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_230 = QHBoxLayout()
        self.horizontalLayout_230.setSpacing(10)
        self.horizontalLayout_230.setObjectName(u"horizontalLayout_230")
        self.horizontalLayout_230.setContentsMargins(0, 0, 0, 0)
        self.label_223 = QLabel(self.groupBox_55)
        self.label_223.setObjectName(u"label_223")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_223.sizePolicy().hasHeightForWidth())
        self.label_223.setSizePolicy(sizePolicy)

        self.horizontalLayout_230.addWidget(self.label_223)

        self.peripheral_io_main_air = QSpinBox(self.groupBox_55)
        self.peripheral_io_main_air.setObjectName(u"peripheral_io_main_air")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.peripheral_io_main_air.sizePolicy().hasHeightForWidth())
        self.peripheral_io_main_air.setSizePolicy(sizePolicy1)
        self.peripheral_io_main_air.setMinimumSize(QSize(50, 0))
        self.peripheral_io_main_air.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.peripheral_io_main_air.setMinimum(1)
        self.peripheral_io_main_air.setMaximum(16)
        self.peripheral_io_main_air.setValue(6)

        self.horizontalLayout_230.addWidget(self.peripheral_io_main_air)

        self.peripheral_io_main_air_state = QLabel(self.groupBox_55)
        self.peripheral_io_main_air_state.setObjectName(u"peripheral_io_main_air_state")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.peripheral_io_main_air_state.setFont(font2)
        self.peripheral_io_main_air_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_230.addWidget(self.peripheral_io_main_air_state)

        self.peripheral_io_main_air_btn = QToolButton(self.groupBox_55)
        self.peripheral_io_main_air_btn.setObjectName(u"peripheral_io_main_air_btn")
        self.peripheral_io_main_air_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_230.addWidget(self.peripheral_io_main_air_btn)


        self.verticalLayout_62.addLayout(self.horizontalLayout_230)

        self.horizontalLayout_231 = QHBoxLayout()
        self.horizontalLayout_231.setSpacing(10)
        self.horizontalLayout_231.setObjectName(u"horizontalLayout_231")
        self.horizontalLayout_231.setContentsMargins(0, 0, 0, 0)
        self.label_224 = QLabel(self.groupBox_55)
        self.label_224.setObjectName(u"label_224")
        sizePolicy.setHeightForWidth(self.label_224.sizePolicy().hasHeightForWidth())
        self.label_224.setSizePolicy(sizePolicy)

        self.horizontalLayout_231.addWidget(self.label_224)

        self.peripheral_io_main_conveyor = QSpinBox(self.groupBox_55)
        self.peripheral_io_main_conveyor.setObjectName(u"peripheral_io_main_conveyor")
        sizePolicy1.setHeightForWidth(self.peripheral_io_main_conveyor.sizePolicy().hasHeightForWidth())
        self.peripheral_io_main_conveyor.setSizePolicy(sizePolicy1)
        self.peripheral_io_main_conveyor.setMinimumSize(QSize(50, 0))
        self.peripheral_io_main_conveyor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.peripheral_io_main_conveyor.setMinimum(1)
        self.peripheral_io_main_conveyor.setMaximum(16)
        self.peripheral_io_main_conveyor.setValue(6)

        self.horizontalLayout_231.addWidget(self.peripheral_io_main_conveyor)

        self.peripheral_io_main_conveyor_state = QLabel(self.groupBox_55)
        self.peripheral_io_main_conveyor_state.setObjectName(u"peripheral_io_main_conveyor_state")
        self.peripheral_io_main_conveyor_state.setFont(font2)
        self.peripheral_io_main_conveyor_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_231.addWidget(self.peripheral_io_main_conveyor_state)

        self.peripheral_io_main_conveyor_btn = QToolButton(self.groupBox_55)
        self.peripheral_io_main_conveyor_btn.setObjectName(u"peripheral_io_main_conveyor_btn")
        self.peripheral_io_main_conveyor_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_231.addWidget(self.peripheral_io_main_conveyor_btn)


        self.verticalLayout_62.addLayout(self.horizontalLayout_231)

        self.horizontalLayout_232 = QHBoxLayout()
        self.horizontalLayout_232.setSpacing(10)
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.horizontalLayout_232.setContentsMargins(0, 0, 0, 0)
        self.label_225 = QLabel(self.groupBox_55)
        self.label_225.setObjectName(u"label_225")
        sizePolicy.setHeightForWidth(self.label_225.sizePolicy().hasHeightForWidth())
        self.label_225.setSizePolicy(sizePolicy)

        self.horizontalLayout_232.addWidget(self.label_225)

        self.peripheral_io_aux_air = QSpinBox(self.groupBox_55)
        self.peripheral_io_aux_air.setObjectName(u"peripheral_io_aux_air")
        sizePolicy1.setHeightForWidth(self.peripheral_io_aux_air.sizePolicy().hasHeightForWidth())
        self.peripheral_io_aux_air.setSizePolicy(sizePolicy1)
        self.peripheral_io_aux_air.setMinimumSize(QSize(50, 0))
        self.peripheral_io_aux_air.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.peripheral_io_aux_air.setMinimum(1)
        self.peripheral_io_aux_air.setMaximum(16)
        self.peripheral_io_aux_air.setValue(6)

        self.horizontalLayout_232.addWidget(self.peripheral_io_aux_air)

        self.peripheral_io_aux_air_state = QLabel(self.groupBox_55)
        self.peripheral_io_aux_air_state.setObjectName(u"peripheral_io_aux_air_state")
        self.peripheral_io_aux_air_state.setFont(font2)
        self.peripheral_io_aux_air_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_232.addWidget(self.peripheral_io_aux_air_state)

        self.peripheral_io_aux_air_btn = QToolButton(self.groupBox_55)
        self.peripheral_io_aux_air_btn.setObjectName(u"peripheral_io_aux_air_btn")
        self.peripheral_io_aux_air_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_232.addWidget(self.peripheral_io_aux_air_btn)


        self.verticalLayout_62.addLayout(self.horizontalLayout_232)

        self.horizontalLayout_229 = QHBoxLayout()
        self.horizontalLayout_229.setSpacing(10)
        self.horizontalLayout_229.setObjectName(u"horizontalLayout_229")
        self.horizontalLayout_229.setContentsMargins(5, 5, 5, 5)
        self.label_222 = QLabel(self.groupBox_55)
        self.label_222.setObjectName(u"label_222")
        sizePolicy.setHeightForWidth(self.label_222.sizePolicy().hasHeightForWidth())
        self.label_222.setSizePolicy(sizePolicy)

        self.horizontalLayout_229.addWidget(self.label_222)

        self.peripheral_io_main_air_status_reverse = QSpinBox(self.groupBox_55)
        self.peripheral_io_main_air_status_reverse.setObjectName(u"peripheral_io_main_air_status_reverse")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.peripheral_io_main_air_status_reverse.sizePolicy().hasHeightForWidth())
        self.peripheral_io_main_air_status_reverse.setSizePolicy(sizePolicy2)
        self.peripheral_io_main_air_status_reverse.setMinimumSize(QSize(50, 24))
        self.peripheral_io_main_air_status_reverse.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.peripheral_io_main_air_status_reverse.setMinimum(1)
        self.peripheral_io_main_air_status_reverse.setMaximum(16)
        self.peripheral_io_main_air_status_reverse.setValue(6)

        self.horizontalLayout_229.addWidget(self.peripheral_io_main_air_status_reverse)

        self.peripheral_io_main_air_status_reverse_state = QLabel(self.groupBox_55)
        self.peripheral_io_main_air_status_reverse_state.setObjectName(u"peripheral_io_main_air_status_reverse_state")
        self.peripheral_io_main_air_status_reverse_state.setFont(font2)
        self.peripheral_io_main_air_status_reverse_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_229.addWidget(self.peripheral_io_main_air_status_reverse_state)


        self.verticalLayout_62.addLayout(self.horizontalLayout_229)

        self.horizontalLayout_233 = QHBoxLayout()
        self.horizontalLayout_233.setSpacing(10)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(5, 5, 5, 5)
        self.label_226 = QLabel(self.groupBox_55)
        self.label_226.setObjectName(u"label_226")
        sizePolicy.setHeightForWidth(self.label_226.sizePolicy().hasHeightForWidth())
        self.label_226.setSizePolicy(sizePolicy)

        self.horizontalLayout_233.addWidget(self.label_226)

        self.peripheral_io_aux_air_status_reverse = QSpinBox(self.groupBox_55)
        self.peripheral_io_aux_air_status_reverse.setObjectName(u"peripheral_io_aux_air_status_reverse")
        sizePolicy2.setHeightForWidth(self.peripheral_io_aux_air_status_reverse.sizePolicy().hasHeightForWidth())
        self.peripheral_io_aux_air_status_reverse.setSizePolicy(sizePolicy2)
        self.peripheral_io_aux_air_status_reverse.setMinimumSize(QSize(50, 24))
        self.peripheral_io_aux_air_status_reverse.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.peripheral_io_aux_air_status_reverse.setMinimum(1)
        self.peripheral_io_aux_air_status_reverse.setMaximum(16)
        self.peripheral_io_aux_air_status_reverse.setValue(6)

        self.horizontalLayout_233.addWidget(self.peripheral_io_aux_air_status_reverse)

        self.peripheral_io_aux_air_status_reverse_state = QLabel(self.groupBox_55)
        self.peripheral_io_aux_air_status_reverse_state.setObjectName(u"peripheral_io_aux_air_status_reverse_state")
        self.peripheral_io_aux_air_status_reverse_state.setFont(font2)
        self.peripheral_io_aux_air_status_reverse_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_233.addWidget(self.peripheral_io_aux_air_status_reverse_state)


        self.verticalLayout_62.addLayout(self.horizontalLayout_233)

        self.tabWidget.addTab(self.tab_general, "")
        self.tab_station1 = QWidget()
        self.tab_station1.setObjectName(u"tab_station1")
        self.verticalLayout_51 = QVBoxLayout(self.tab_station1)
        self.verticalLayout_51.setSpacing(10)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setSpacing(30)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.groupBox_4 = QGroupBox(self.tab_station1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(500, 0))
        self.groupBox_4.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(240, 0))

        self.horizontalLayout_10.addWidget(self.label_8)

        self.station1_robot = QLineEdit(self.groupBox_4)
        self.station1_robot.setObjectName(u"station1_robot")
        self.station1_robot.setMaximumSize(QSize(150, 16777215))
        self.station1_robot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.station1_robot)

        self.btn_station1_robot_test = QPushButton(self.groupBox_4)
        self.btn_station1_robot_test.setObjectName(u"btn_station1_robot_test")
        self.btn_station1_robot_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_10.addWidget(self.btn_station1_robot_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(240, 0))

        self.horizontalLayout_11.addWidget(self.label_9)

        self.station1_cognex = QLineEdit(self.groupBox_4)
        self.station1_cognex.setObjectName(u"station1_cognex")
        self.station1_cognex.setMaximumSize(QSize(150, 16777215))
        self.station1_cognex.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.station1_cognex)

        self.btn_station1_cognex_test = QPushButton(self.groupBox_4)
        self.btn_station1_cognex_test.setObjectName(u"btn_station1_cognex_test")
        self.btn_station1_cognex_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_11.addWidget(self.btn_station1_cognex_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_184 = QHBoxLayout()
        self.horizontalLayout_184.setSpacing(20)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.label_52 = QLabel(self.groupBox_4)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_184.addWidget(self.label_52)

        self.station1_barcode_2 = QLineEdit(self.groupBox_4)
        self.station1_barcode_2.setObjectName(u"station1_barcode_2")
        self.station1_barcode_2.setMaximumSize(QSize(150, 16777215))
        self.station1_barcode_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_184.addWidget(self.station1_barcode_2)

        self.btn_station1_barcode_2_test = QPushButton(self.groupBox_4)
        self.btn_station1_barcode_2_test.setObjectName(u"btn_station1_barcode_2_test")
        self.btn_station1_barcode_2_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_184.addWidget(self.btn_station1_barcode_2_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout_184)

        self.horizontalLayout_185 = QHBoxLayout()
        self.horizontalLayout_185.setSpacing(20)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.label_53 = QLabel(self.groupBox_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(240, 0))

        self.horizontalLayout_185.addWidget(self.label_53)

        self.station1_barcode_3 = QLineEdit(self.groupBox_4)
        self.station1_barcode_3.setObjectName(u"station1_barcode_3")
        self.station1_barcode_3.setMaximumSize(QSize(150, 16777215))
        self.station1_barcode_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_185.addWidget(self.station1_barcode_3)

        self.btn_station1_barcode_3_test = QPushButton(self.groupBox_4)
        self.btn_station1_barcode_3_test.setObjectName(u"btn_station1_barcode_3_test")
        self.btn_station1_barcode_3_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_185.addWidget(self.btn_station1_barcode_3_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout_185)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(240, 0))

        self.horizontalLayout_12.addWidget(self.label_10)

        self.station1_wago = QLineEdit(self.groupBox_4)
        self.station1_wago.setObjectName(u"station1_wago")
        self.station1_wago.setMaximumSize(QSize(150, 16777215))
        self.station1_wago.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.station1_wago)

        self.btn_station1_wago_test = QPushButton(self.groupBox_4)
        self.btn_station1_wago_test.setObjectName(u"btn_station1_wago_test")
        self.btn_station1_wago_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_12.addWidget(self.btn_station1_wago_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_57.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.tab_station1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(30)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.station1_feeders_cross_gear = QLineEdit(self.groupBox)
        self.station1_feeders_cross_gear.setObjectName(u"station1_feeders_cross_gear")
        self.station1_feeders_cross_gear.setMaximumSize(QSize(150, 16777215))
        self.station1_feeders_cross_gear.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.station1_feeders_cross_gear)

        self.btn_station1_feeders_cross_gear_test = QPushButton(self.groupBox)
        self.btn_station1_feeders_cross_gear_test.setObjectName(u"btn_station1_feeders_cross_gear_test")
        self.btn_station1_feeders_cross_gear_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.btn_station1_feeders_cross_gear_test)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.station1_feeders_pinion = QLineEdit(self.groupBox)
        self.station1_feeders_pinion.setObjectName(u"station1_feeders_pinion")
        self.station1_feeders_pinion.setMaximumSize(QSize(150, 16777215))
        self.station1_feeders_pinion.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.station1_feeders_pinion)

        self.btn_station1_feeders_pinion_test = QPushButton(self.groupBox)
        self.btn_station1_feeders_pinion_test.setObjectName(u"btn_station1_feeders_pinion_test")
        self.btn_station1_feeders_pinion_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.btn_station1_feeders_pinion_test)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.station1_feeders_crank_handle = QLineEdit(self.groupBox)
        self.station1_feeders_crank_handle.setObjectName(u"station1_feeders_crank_handle")
        self.station1_feeders_crank_handle.setMaximumSize(QSize(150, 16777215))
        self.station1_feeders_crank_handle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.station1_feeders_crank_handle)

        self.btn_station1_feeders_crank_handle_test = QPushButton(self.groupBox)
        self.btn_station1_feeders_crank_handle_test.setObjectName(u"btn_station1_feeders_crank_handle_test")
        self.btn_station1_feeders_crank_handle_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_15.addWidget(self.btn_station1_feeders_crank_handle_test)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(30)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.station1_feeders_ring_gear = QLineEdit(self.groupBox)
        self.station1_feeders_ring_gear.setObjectName(u"station1_feeders_ring_gear")
        self.station1_feeders_ring_gear.setMaximumSize(QSize(150, 16777215))
        self.station1_feeders_ring_gear.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.station1_feeders_ring_gear)

        self.btn_station1_feeders_ring_gear_test = QPushButton(self.groupBox)
        self.btn_station1_feeders_ring_gear_test.setObjectName(u"btn_station1_feeders_ring_gear_test")
        self.btn_station1_feeders_ring_gear_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_16.addWidget(self.btn_station1_feeders_ring_gear_test)


        self.verticalLayout.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_57.addWidget(self.groupBox)


        self.verticalLayout_51.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setSpacing(30)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.groupBox_5 = QGroupBox(self.tab_station1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(600, 0))
        self.groupBox_5.setMaximumSize(QSize(700, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy3)
        self.groupBox_7.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(40)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.label_103 = QLabel(self.groupBox_7)
        self.label_103.setObjectName(u"label_103")
        sizePolicy.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy)

        self.horizontalLayout_22.addWidget(self.label_103)

        self.station1_io_lift_locate_extended_2 = QSpinBox(self.groupBox_7)
        self.station1_io_lift_locate_extended_2.setObjectName(u"station1_io_lift_locate_extended_2")
        sizePolicy2.setHeightForWidth(self.station1_io_lift_locate_extended_2.sizePolicy().hasHeightForWidth())
        self.station1_io_lift_locate_extended_2.setSizePolicy(sizePolicy2)
        self.station1_io_lift_locate_extended_2.setMinimumSize(QSize(50, 24))
        self.station1_io_lift_locate_extended_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_lift_locate_extended_2.setMinimum(1)
        self.station1_io_lift_locate_extended_2.setMaximum(16)
        self.station1_io_lift_locate_extended_2.setValue(6)

        self.horizontalLayout_22.addWidget(self.station1_io_lift_locate_extended_2)

        self.station1_io_lift_locate_extended_2_state = QLabel(self.groupBox_7)
        self.station1_io_lift_locate_extended_2_state.setObjectName(u"station1_io_lift_locate_extended_2_state")
        self.station1_io_lift_locate_extended_2_state.setFont(font2)
        self.station1_io_lift_locate_extended_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_22.addWidget(self.station1_io_lift_locate_extended_2_state)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.label_104 = QLabel(self.groupBox_7)
        self.label_104.setObjectName(u"label_104")
        sizePolicy.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy)

        self.horizontalLayout_23.addWidget(self.label_104)

        self.station1_io_lift_locate_retracted_2 = QSpinBox(self.groupBox_7)
        self.station1_io_lift_locate_retracted_2.setObjectName(u"station1_io_lift_locate_retracted_2")
        sizePolicy1.setHeightForWidth(self.station1_io_lift_locate_retracted_2.sizePolicy().hasHeightForWidth())
        self.station1_io_lift_locate_retracted_2.setSizePolicy(sizePolicy1)
        self.station1_io_lift_locate_retracted_2.setMinimumSize(QSize(50, 0))
        self.station1_io_lift_locate_retracted_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_lift_locate_retracted_2.setMinimum(1)
        self.station1_io_lift_locate_retracted_2.setMaximum(16)
        self.station1_io_lift_locate_retracted_2.setValue(6)

        self.horizontalLayout_23.addWidget(self.station1_io_lift_locate_retracted_2)

        self.station1_io_lift_locate_retracted_2_state = QLabel(self.groupBox_7)
        self.station1_io_lift_locate_retracted_2_state.setObjectName(u"station1_io_lift_locate_retracted_2_state")
        self.station1_io_lift_locate_retracted_2_state.setFont(font2)
        self.station1_io_lift_locate_retracted_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_23.addWidget(self.station1_io_lift_locate_retracted_2_state)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_23)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(40)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(5, 5, 5, 5)
        self.label_105 = QLabel(self.groupBox_7)
        self.label_105.setObjectName(u"label_105")
        sizePolicy.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy)

        self.horizontalLayout_35.addWidget(self.label_105)

        self.station1_io_lift_locate_pre_2 = QSpinBox(self.groupBox_7)
        self.station1_io_lift_locate_pre_2.setObjectName(u"station1_io_lift_locate_pre_2")
        sizePolicy1.setHeightForWidth(self.station1_io_lift_locate_pre_2.sizePolicy().hasHeightForWidth())
        self.station1_io_lift_locate_pre_2.setSizePolicy(sizePolicy1)
        self.station1_io_lift_locate_pre_2.setMinimumSize(QSize(50, 0))
        self.station1_io_lift_locate_pre_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_lift_locate_pre_2.setMinimum(1)
        self.station1_io_lift_locate_pre_2.setMaximum(16)
        self.station1_io_lift_locate_pre_2.setValue(6)

        self.horizontalLayout_35.addWidget(self.station1_io_lift_locate_pre_2)

        self.station1_io_lift_locate_pre_2_state = QLabel(self.groupBox_7)
        self.station1_io_lift_locate_pre_2_state.setObjectName(u"station1_io_lift_locate_pre_2_state")
        self.station1_io_lift_locate_pre_2_state.setFont(font2)
        self.station1_io_lift_locate_pre_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_35.addWidget(self.station1_io_lift_locate_pre_2_state)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(5, 5, 5, 5)
        self.label_106 = QLabel(self.groupBox_7)
        self.label_106.setObjectName(u"label_106")
        sizePolicy.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy)

        self.horizontalLayout_37.addWidget(self.label_106)

        self.station1_io_lift_locate_main_2 = QSpinBox(self.groupBox_7)
        self.station1_io_lift_locate_main_2.setObjectName(u"station1_io_lift_locate_main_2")
        sizePolicy1.setHeightForWidth(self.station1_io_lift_locate_main_2.sizePolicy().hasHeightForWidth())
        self.station1_io_lift_locate_main_2.setSizePolicy(sizePolicy1)
        self.station1_io_lift_locate_main_2.setMinimumSize(QSize(50, 0))
        self.station1_io_lift_locate_main_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_lift_locate_main_2.setMinimum(1)
        self.station1_io_lift_locate_main_2.setMaximum(16)
        self.station1_io_lift_locate_main_2.setValue(6)

        self.horizontalLayout_37.addWidget(self.station1_io_lift_locate_main_2)

        self.station1_io_lift_locate_main_2_state = QLabel(self.groupBox_7)
        self.station1_io_lift_locate_main_2_state.setObjectName(u"station1_io_lift_locate_main_2_state")
        self.station1_io_lift_locate_main_2_state.setFont(font2)
        self.station1_io_lift_locate_main_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_37.addWidget(self.station1_io_lift_locate_main_2_state)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_37)


        self.verticalLayout_4.addLayout(self.horizontalLayout_34)


        self.verticalLayout_8.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy3.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy3)
        self.groupBox_8.setMinimumSize(QSize(0, 118))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(40)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setSpacing(10)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(5, 5, 5, 5)
        self.label_109 = QLabel(self.groupBox_8)
        self.label_109.setObjectName(u"label_109")
        sizePolicy.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy)

        self.horizontalLayout_42.addWidget(self.label_109)

        self.station1_io_lift_locate_extended_3 = QSpinBox(self.groupBox_8)
        self.station1_io_lift_locate_extended_3.setObjectName(u"station1_io_lift_locate_extended_3")
        sizePolicy1.setHeightForWidth(self.station1_io_lift_locate_extended_3.sizePolicy().hasHeightForWidth())
        self.station1_io_lift_locate_extended_3.setSizePolicy(sizePolicy1)
        self.station1_io_lift_locate_extended_3.setMinimumSize(QSize(50, 0))
        self.station1_io_lift_locate_extended_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_lift_locate_extended_3.setMinimum(1)
        self.station1_io_lift_locate_extended_3.setMaximum(16)
        self.station1_io_lift_locate_extended_3.setValue(6)

        self.horizontalLayout_42.addWidget(self.station1_io_lift_locate_extended_3)

        self.station1_io_lift_locate_extended_3_state = QLabel(self.groupBox_8)
        self.station1_io_lift_locate_extended_3_state.setObjectName(u"station1_io_lift_locate_extended_3_state")
        self.station1_io_lift_locate_extended_3_state.setFont(font2)
        self.station1_io_lift_locate_extended_3_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_42.addWidget(self.station1_io_lift_locate_extended_3_state)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(5, 5, 5, 5)
        self.label_110 = QLabel(self.groupBox_8)
        self.label_110.setObjectName(u"label_110")
        sizePolicy.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy)

        self.horizontalLayout_43.addWidget(self.label_110)

        self.station1_io_lift_locate_retracted_3 = QSpinBox(self.groupBox_8)
        self.station1_io_lift_locate_retracted_3.setObjectName(u"station1_io_lift_locate_retracted_3")
        sizePolicy1.setHeightForWidth(self.station1_io_lift_locate_retracted_3.sizePolicy().hasHeightForWidth())
        self.station1_io_lift_locate_retracted_3.setSizePolicy(sizePolicy1)
        self.station1_io_lift_locate_retracted_3.setMinimumSize(QSize(50, 0))
        self.station1_io_lift_locate_retracted_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_lift_locate_retracted_3.setMinimum(1)
        self.station1_io_lift_locate_retracted_3.setMaximum(16)
        self.station1_io_lift_locate_retracted_3.setValue(6)

        self.horizontalLayout_43.addWidget(self.station1_io_lift_locate_retracted_3)

        self.station1_io_lift_locate_retracted_3_state = QLabel(self.groupBox_8)
        self.station1_io_lift_locate_retracted_3_state.setObjectName(u"station1_io_lift_locate_retracted_3_state")
        self.station1_io_lift_locate_retracted_3_state.setFont(font2)
        self.station1_io_lift_locate_retracted_3_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_43.addWidget(self.station1_io_lift_locate_retracted_3_state)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_43)


        self.verticalLayout_5.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(40)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setSpacing(10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(5, 5, 5, 5)
        self.label_112 = QLabel(self.groupBox_8)
        self.label_112.setObjectName(u"label_112")
        sizePolicy.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy)

        self.horizontalLayout_46.addWidget(self.label_112)

        self.station1_io_lift_locate_main_3 = QSpinBox(self.groupBox_8)
        self.station1_io_lift_locate_main_3.setObjectName(u"station1_io_lift_locate_main_3")
        sizePolicy1.setHeightForWidth(self.station1_io_lift_locate_main_3.sizePolicy().hasHeightForWidth())
        self.station1_io_lift_locate_main_3.setSizePolicy(sizePolicy1)
        self.station1_io_lift_locate_main_3.setMinimumSize(QSize(50, 0))
        self.station1_io_lift_locate_main_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_lift_locate_main_3.setMinimum(1)
        self.station1_io_lift_locate_main_3.setMaximum(16)
        self.station1_io_lift_locate_main_3.setValue(6)

        self.horizontalLayout_46.addWidget(self.station1_io_lift_locate_main_3)

        self.station1_io_lift_locate_main_3_state = QLabel(self.groupBox_8)
        self.station1_io_lift_locate_main_3_state.setObjectName(u"station1_io_lift_locate_main_3_state")
        self.station1_io_lift_locate_main_3_state.setFont(font2)
        self.station1_io_lift_locate_main_3_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_46.addWidget(self.station1_io_lift_locate_main_3_state)


        self.horizontalLayout_44.addLayout(self.horizontalLayout_46)


        self.verticalLayout_5.addLayout(self.horizontalLayout_44)


        self.verticalLayout_8.addWidget(self.groupBox_8)

        self.groupBox_41 = QGroupBox(self.groupBox_5)
        self.groupBox_41.setObjectName(u"groupBox_41")
        sizePolicy3.setHeightForWidth(self.groupBox_41.sizePolicy().hasHeightForWidth())
        self.groupBox_41.setSizePolicy(sizePolicy3)
        self.groupBox_41.setMinimumSize(QSize(0, 74))
        self.horizontalLayout_197 = QHBoxLayout(self.groupBox_41)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_198 = QHBoxLayout()
        self.horizontalLayout_198.setSpacing(10)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalLayout_198.setContentsMargins(5, 5, 5, 5)
        self.label_115 = QLabel(self.groupBox_41)
        self.label_115.setObjectName(u"label_115")
        sizePolicy.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy)

        self.horizontalLayout_198.addWidget(self.label_115)

        self.station1_io_whirl_rotated_cw = QSpinBox(self.groupBox_41)
        self.station1_io_whirl_rotated_cw.setObjectName(u"station1_io_whirl_rotated_cw")
        sizePolicy1.setHeightForWidth(self.station1_io_whirl_rotated_cw.sizePolicy().hasHeightForWidth())
        self.station1_io_whirl_rotated_cw.setSizePolicy(sizePolicy1)
        self.station1_io_whirl_rotated_cw.setMinimumSize(QSize(50, 0))
        self.station1_io_whirl_rotated_cw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_whirl_rotated_cw.setMinimum(1)
        self.station1_io_whirl_rotated_cw.setMaximum(20)
        self.station1_io_whirl_rotated_cw.setValue(11)

        self.horizontalLayout_198.addWidget(self.station1_io_whirl_rotated_cw)

        self.station1_io_whirl_rotated_cw_state = QLabel(self.groupBox_41)
        self.station1_io_whirl_rotated_cw_state.setObjectName(u"station1_io_whirl_rotated_cw_state")
        self.station1_io_whirl_rotated_cw_state.setFont(font2)
        self.station1_io_whirl_rotated_cw_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_198.addWidget(self.station1_io_whirl_rotated_cw_state)


        self.horizontalLayout_197.addLayout(self.horizontalLayout_198)

        self.horizontalLayout_199 = QHBoxLayout()
        self.horizontalLayout_199.setSpacing(10)
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.horizontalLayout_199.setContentsMargins(5, 5, 5, 5)
        self.label_122 = QLabel(self.groupBox_41)
        self.label_122.setObjectName(u"label_122")
        sizePolicy.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy)

        self.horizontalLayout_199.addWidget(self.label_122)

        self.station1_io_whirl_rotated_ccw = QSpinBox(self.groupBox_41)
        self.station1_io_whirl_rotated_ccw.setObjectName(u"station1_io_whirl_rotated_ccw")
        sizePolicy1.setHeightForWidth(self.station1_io_whirl_rotated_ccw.sizePolicy().hasHeightForWidth())
        self.station1_io_whirl_rotated_ccw.setSizePolicy(sizePolicy1)
        self.station1_io_whirl_rotated_ccw.setMinimumSize(QSize(50, 0))
        self.station1_io_whirl_rotated_ccw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_whirl_rotated_ccw.setMinimum(1)
        self.station1_io_whirl_rotated_ccw.setMaximum(20)
        self.station1_io_whirl_rotated_ccw.setValue(6)

        self.horizontalLayout_199.addWidget(self.station1_io_whirl_rotated_ccw)

        self.station1_io_whirl_rotated_ccw_state = QLabel(self.groupBox_41)
        self.station1_io_whirl_rotated_ccw_state.setObjectName(u"station1_io_whirl_rotated_ccw_state")
        self.station1_io_whirl_rotated_ccw_state.setFont(font2)
        self.station1_io_whirl_rotated_ccw_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_199.addWidget(self.station1_io_whirl_rotated_ccw_state)


        self.horizontalLayout_197.addLayout(self.horizontalLayout_199)

        self.horizontalLayout_201 = QHBoxLayout()
        self.horizontalLayout_201.setSpacing(10)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(5, 5, 5, 5)
        self.label_130 = QLabel(self.groupBox_41)
        self.label_130.setObjectName(u"label_130")
        sizePolicy.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy)

        self.horizontalLayout_201.addWidget(self.label_130)

        self.station1_io_whirl_rotate_part_present = QSpinBox(self.groupBox_41)
        self.station1_io_whirl_rotate_part_present.setObjectName(u"station1_io_whirl_rotate_part_present")
        sizePolicy1.setHeightForWidth(self.station1_io_whirl_rotate_part_present.sizePolicy().hasHeightForWidth())
        self.station1_io_whirl_rotate_part_present.setSizePolicy(sizePolicy1)
        self.station1_io_whirl_rotate_part_present.setMinimumSize(QSize(50, 0))
        self.station1_io_whirl_rotate_part_present.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_whirl_rotate_part_present.setMinimum(1)
        self.station1_io_whirl_rotate_part_present.setMaximum(20)
        self.station1_io_whirl_rotate_part_present.setValue(6)

        self.horizontalLayout_201.addWidget(self.station1_io_whirl_rotate_part_present)

        self.station1_io_whirl_rotate_part_present_state = QLabel(self.groupBox_41)
        self.station1_io_whirl_rotate_part_present_state.setObjectName(u"station1_io_whirl_rotate_part_present_state")
        self.station1_io_whirl_rotate_part_present_state.setFont(font2)
        self.station1_io_whirl_rotate_part_present_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_201.addWidget(self.station1_io_whirl_rotate_part_present_state)


        self.horizontalLayout_197.addLayout(self.horizontalLayout_201)


        self.verticalLayout_8.addWidget(self.groupBox_41)


        self.horizontalLayout_80.addWidget(self.groupBox_5)

        self.group_valve_1 = QGroupBox(self.tab_station1)
        self.group_valve_1.setObjectName(u"group_valve_1")
        self.verticalLayout_12 = QVBoxLayout(self.group_valve_1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_12 = QGroupBox(self.group_valve_1)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 120))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setSpacing(40)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(10)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_124 = QLabel(self.groupBox_12)
        self.label_124.setObjectName(u"label_124")
        sizePolicy.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy)
        self.label_124.setMinimumSize(QSize(110, 0))
        self.label_124.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_63.addWidget(self.label_124)

        self.station1_valve_lift_locate_up_2 = QSpinBox(self.groupBox_12)
        self.station1_valve_lift_locate_up_2.setObjectName(u"station1_valve_lift_locate_up_2")
        sizePolicy1.setHeightForWidth(self.station1_valve_lift_locate_up_2.sizePolicy().hasHeightForWidth())
        self.station1_valve_lift_locate_up_2.setSizePolicy(sizePolicy1)
        self.station1_valve_lift_locate_up_2.setMinimumSize(QSize(50, 0))
        self.station1_valve_lift_locate_up_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_lift_locate_up_2.setMinimum(1)
        self.station1_valve_lift_locate_up_2.setMaximum(16)
        self.station1_valve_lift_locate_up_2.setValue(6)

        self.horizontalLayout_63.addWidget(self.station1_valve_lift_locate_up_2)

        self.station1_valve_lift_locate_up_2_state = QLabel(self.groupBox_12)
        self.station1_valve_lift_locate_up_2_state.setObjectName(u"station1_valve_lift_locate_up_2_state")
        self.station1_valve_lift_locate_up_2_state.setFont(font2)
        self.station1_valve_lift_locate_up_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_63.addWidget(self.station1_valve_lift_locate_up_2_state)

        self.station1_valve_lift_locate_up_2_btn = QToolButton(self.groupBox_12)
        self.station1_valve_lift_locate_up_2_btn.setObjectName(u"station1_valve_lift_locate_up_2_btn")
        self.station1_valve_lift_locate_up_2_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_63.addWidget(self.station1_valve_lift_locate_up_2_btn)


        self.horizontalLayout_72.addLayout(self.horizontalLayout_63)

        self.widget_2 = QWidget(self.groupBox_12)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_72.addWidget(self.widget_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setSpacing(40)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setSpacing(10)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_125 = QLabel(self.groupBox_12)
        self.label_125.setObjectName(u"label_125")
        sizePolicy.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy)

        self.horizontalLayout_65.addWidget(self.label_125)

        self.station1_valve_lift_locate_pre_2 = QSpinBox(self.groupBox_12)
        self.station1_valve_lift_locate_pre_2.setObjectName(u"station1_valve_lift_locate_pre_2")
        sizePolicy1.setHeightForWidth(self.station1_valve_lift_locate_pre_2.sizePolicy().hasHeightForWidth())
        self.station1_valve_lift_locate_pre_2.setSizePolicy(sizePolicy1)
        self.station1_valve_lift_locate_pre_2.setMinimumSize(QSize(50, 0))
        self.station1_valve_lift_locate_pre_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_lift_locate_pre_2.setMinimum(1)
        self.station1_valve_lift_locate_pre_2.setMaximum(16)
        self.station1_valve_lift_locate_pre_2.setValue(6)

        self.horizontalLayout_65.addWidget(self.station1_valve_lift_locate_pre_2)

        self.station1_valve_lift_locate_pre_2_state = QLabel(self.groupBox_12)
        self.station1_valve_lift_locate_pre_2_state.setObjectName(u"station1_valve_lift_locate_pre_2_state")
        self.station1_valve_lift_locate_pre_2_state.setMinimumSize(QSize(29, 0))
        self.station1_valve_lift_locate_pre_2_state.setFont(font2)
        self.station1_valve_lift_locate_pre_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_65.addWidget(self.station1_valve_lift_locate_pre_2_state)

        self.station1_valve_lift_locate_pre_2_btn = QToolButton(self.groupBox_12)
        self.station1_valve_lift_locate_pre_2_btn.setObjectName(u"station1_valve_lift_locate_pre_2_btn")
        self.station1_valve_lift_locate_pre_2_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_65.addWidget(self.station1_valve_lift_locate_pre_2_btn)


        self.horizontalLayout_71.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setSpacing(10)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_126 = QLabel(self.groupBox_12)
        self.label_126.setObjectName(u"label_126")
        sizePolicy.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy)

        self.horizontalLayout_66.addWidget(self.label_126)

        self.station1_valve_lift_locate_main_2 = QSpinBox(self.groupBox_12)
        self.station1_valve_lift_locate_main_2.setObjectName(u"station1_valve_lift_locate_main_2")
        sizePolicy1.setHeightForWidth(self.station1_valve_lift_locate_main_2.sizePolicy().hasHeightForWidth())
        self.station1_valve_lift_locate_main_2.setSizePolicy(sizePolicy1)
        self.station1_valve_lift_locate_main_2.setMinimumSize(QSize(50, 0))
        self.station1_valve_lift_locate_main_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_lift_locate_main_2.setMinimum(1)
        self.station1_valve_lift_locate_main_2.setMaximum(16)
        self.station1_valve_lift_locate_main_2.setValue(6)

        self.horizontalLayout_66.addWidget(self.station1_valve_lift_locate_main_2)

        self.station1_valve_lift_locate_main_2_state = QLabel(self.groupBox_12)
        self.station1_valve_lift_locate_main_2_state.setObjectName(u"station1_valve_lift_locate_main_2_state")
        self.station1_valve_lift_locate_main_2_state.setFont(font2)
        self.station1_valve_lift_locate_main_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_66.addWidget(self.station1_valve_lift_locate_main_2_state)

        self.station1_valve_lift_locate_main_2_btn = QToolButton(self.groupBox_12)
        self.station1_valve_lift_locate_main_2_btn.setObjectName(u"station1_valve_lift_locate_main_2_btn")
        self.station1_valve_lift_locate_main_2_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_66.addWidget(self.station1_valve_lift_locate_main_2_btn)


        self.horizontalLayout_71.addLayout(self.horizontalLayout_66)


        self.verticalLayout_10.addLayout(self.horizontalLayout_71)


        self.verticalLayout_12.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.group_valve_1)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(0, 50))
        self.groupBox_13.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_73 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_73.setSpacing(40)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setSpacing(10)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_127 = QLabel(self.groupBox_13)
        self.label_127.setObjectName(u"label_127")
        sizePolicy.setHeightForWidth(self.label_127.sizePolicy().hasHeightForWidth())
        self.label_127.setSizePolicy(sizePolicy)

        self.horizontalLayout_67.addWidget(self.label_127)

        self.station1_valve_lift_locate_up_3 = QSpinBox(self.groupBox_13)
        self.station1_valve_lift_locate_up_3.setObjectName(u"station1_valve_lift_locate_up_3")
        sizePolicy1.setHeightForWidth(self.station1_valve_lift_locate_up_3.sizePolicy().hasHeightForWidth())
        self.station1_valve_lift_locate_up_3.setSizePolicy(sizePolicy1)
        self.station1_valve_lift_locate_up_3.setMinimumSize(QSize(50, 0))
        self.station1_valve_lift_locate_up_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_lift_locate_up_3.setMinimum(1)
        self.station1_valve_lift_locate_up_3.setMaximum(16)
        self.station1_valve_lift_locate_up_3.setValue(6)

        self.horizontalLayout_67.addWidget(self.station1_valve_lift_locate_up_3)

        self.station1_valve_lift_locate_up_3_state = QLabel(self.groupBox_13)
        self.station1_valve_lift_locate_up_3_state.setObjectName(u"station1_valve_lift_locate_up_3_state")
        self.station1_valve_lift_locate_up_3_state.setFont(font2)
        self.station1_valve_lift_locate_up_3_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_67.addWidget(self.station1_valve_lift_locate_up_3_state)

        self.station1_valve_lift_locate_up_3_btn = QToolButton(self.groupBox_13)
        self.station1_valve_lift_locate_up_3_btn.setObjectName(u"station1_valve_lift_locate_up_3_btn")
        self.station1_valve_lift_locate_up_3_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_67.addWidget(self.station1_valve_lift_locate_up_3_btn)


        self.horizontalLayout_73.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setSpacing(10)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_131 = QLabel(self.groupBox_13)
        self.label_131.setObjectName(u"label_131")
        sizePolicy.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy)

        self.horizontalLayout_69.addWidget(self.label_131)

        self.station1_valve_lift_locate_main_3 = QSpinBox(self.groupBox_13)
        self.station1_valve_lift_locate_main_3.setObjectName(u"station1_valve_lift_locate_main_3")
        sizePolicy1.setHeightForWidth(self.station1_valve_lift_locate_main_3.sizePolicy().hasHeightForWidth())
        self.station1_valve_lift_locate_main_3.setSizePolicy(sizePolicy1)
        self.station1_valve_lift_locate_main_3.setMinimumSize(QSize(50, 0))
        self.station1_valve_lift_locate_main_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_lift_locate_main_3.setMinimum(1)
        self.station1_valve_lift_locate_main_3.setMaximum(16)
        self.station1_valve_lift_locate_main_3.setValue(6)

        self.horizontalLayout_69.addWidget(self.station1_valve_lift_locate_main_3)

        self.station1_valve_lift_locate_main_3_state = QLabel(self.groupBox_13)
        self.station1_valve_lift_locate_main_3_state.setObjectName(u"station1_valve_lift_locate_main_3_state")
        self.station1_valve_lift_locate_main_3_state.setFont(font2)
        self.station1_valve_lift_locate_main_3_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_69.addWidget(self.station1_valve_lift_locate_main_3_state)

        self.station1_valve_lift_locate_main_3_btn = QToolButton(self.groupBox_13)
        self.station1_valve_lift_locate_main_3_btn.setObjectName(u"station1_valve_lift_locate_main_3_btn")
        self.station1_valve_lift_locate_main_3_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_69.addWidget(self.station1_valve_lift_locate_main_3_btn)


        self.horizontalLayout_73.addLayout(self.horizontalLayout_69)


        self.verticalLayout_12.addWidget(self.groupBox_13)

        self.frame = QFrame(self.group_valve_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_200 = QHBoxLayout(self.frame)
        self.horizontalLayout_200.setSpacing(10)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_200.setContentsMargins(15, -1, -1, -1)
        self.label_203 = QLabel(self.frame)
        self.label_203.setObjectName(u"label_203")
        sizePolicy.setHeightForWidth(self.label_203.sizePolicy().hasHeightForWidth())
        self.label_203.setSizePolicy(sizePolicy)
        self.label_203.setMinimumSize(QSize(0, 0))
        self.label_203.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_200.addWidget(self.label_203)

        self.station1_valve_whirl_rotator = QSpinBox(self.frame)
        self.station1_valve_whirl_rotator.setObjectName(u"station1_valve_whirl_rotator")
        sizePolicy1.setHeightForWidth(self.station1_valve_whirl_rotator.sizePolicy().hasHeightForWidth())
        self.station1_valve_whirl_rotator.setSizePolicy(sizePolicy1)
        self.station1_valve_whirl_rotator.setMinimumSize(QSize(50, 0))
        self.station1_valve_whirl_rotator.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_whirl_rotator.setMinimum(1)
        self.station1_valve_whirl_rotator.setMaximum(16)
        self.station1_valve_whirl_rotator.setValue(6)

        self.horizontalLayout_200.addWidget(self.station1_valve_whirl_rotator)

        self.station1_valve_whirl_rotator_state = QLabel(self.frame)
        self.station1_valve_whirl_rotator_state.setObjectName(u"station1_valve_whirl_rotator_state")
        self.station1_valve_whirl_rotator_state.setFont(font2)
        self.station1_valve_whirl_rotator_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_200.addWidget(self.station1_valve_whirl_rotator_state)

        self.station1_valve_whirl_rotator_btn = QToolButton(self.frame)
        self.station1_valve_whirl_rotator_btn.setObjectName(u"station1_valve_whirl_rotator_btn")
        self.station1_valve_whirl_rotator_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_200.addWidget(self.station1_valve_whirl_rotator_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_200.addItem(self.horizontalSpacer_6)


        self.verticalLayout_12.addWidget(self.frame)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)


        self.horizontalLayout_80.addWidget(self.group_valve_1)


        self.verticalLayout_51.addLayout(self.horizontalLayout_80)

        self.groupBox_14 = QGroupBox(self.tab_station1)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy4)
        self.groupBox_14.setMinimumSize(QSize(0, 345))
        self.horizontalLayout_170 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_170.setSpacing(30)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.groupBox_42 = QGroupBox(self.groupBox_14)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_42)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(40)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setSpacing(10)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(5, 5, 5, 5)
        self.label_117 = QLabel(self.groupBox_42)
        self.label_117.setObjectName(u"label_117")
        sizePolicy.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy)
        self.label_117.setMinimumSize(QSize(117, 0))

        self.horizontalLayout_55.addWidget(self.label_117)

        self.station1_io_reservoir_full = QSpinBox(self.groupBox_42)
        self.station1_io_reservoir_full.setObjectName(u"station1_io_reservoir_full")
        sizePolicy1.setHeightForWidth(self.station1_io_reservoir_full.sizePolicy().hasHeightForWidth())
        self.station1_io_reservoir_full.setSizePolicy(sizePolicy1)
        self.station1_io_reservoir_full.setMinimumSize(QSize(50, 0))
        self.station1_io_reservoir_full.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_reservoir_full.setMinimum(1)
        self.station1_io_reservoir_full.setMaximum(16)
        self.station1_io_reservoir_full.setValue(6)

        self.horizontalLayout_55.addWidget(self.station1_io_reservoir_full)

        self.station1_io_reservoir_full_state = QLabel(self.groupBox_42)
        self.station1_io_reservoir_full_state.setObjectName(u"station1_io_reservoir_full_state")
        self.station1_io_reservoir_full_state.setFont(font2)
        self.station1_io_reservoir_full_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_55.addWidget(self.station1_io_reservoir_full_state)


        self.horizontalLayout_51.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(10)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(5, 5, 5, 5)
        self.label_116 = QLabel(self.groupBox_42)
        self.label_116.setObjectName(u"label_116")
        sizePolicy.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy)

        self.horizontalLayout_53.addWidget(self.label_116)

        self.station1_io_reservoir_empty = QSpinBox(self.groupBox_42)
        self.station1_io_reservoir_empty.setObjectName(u"station1_io_reservoir_empty")
        sizePolicy1.setHeightForWidth(self.station1_io_reservoir_empty.sizePolicy().hasHeightForWidth())
        self.station1_io_reservoir_empty.setSizePolicy(sizePolicy1)
        self.station1_io_reservoir_empty.setMinimumSize(QSize(50, 0))
        self.station1_io_reservoir_empty.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_reservoir_empty.setMinimum(1)
        self.station1_io_reservoir_empty.setMaximum(16)
        self.station1_io_reservoir_empty.setValue(6)

        self.horizontalLayout_53.addWidget(self.station1_io_reservoir_empty)

        self.station1_io_reservoir_empty_state = QLabel(self.groupBox_42)
        self.station1_io_reservoir_empty_state.setObjectName(u"station1_io_reservoir_empty_state")
        self.station1_io_reservoir_empty_state.setFont(font2)
        self.station1_io_reservoir_empty_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_53.addWidget(self.station1_io_reservoir_empty_state)


        self.horizontalLayout_51.addLayout(self.horizontalLayout_53)


        self.verticalLayout_14.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(40)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(5, 5, 5, 5)
        self.label_107 = QLabel(self.groupBox_42)
        self.label_107.setObjectName(u"label_107")
        sizePolicy.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy)

        self.horizontalLayout_39.addWidget(self.label_107)

        self.station1_io_grease_slide_retracted = QSpinBox(self.groupBox_42)
        self.station1_io_grease_slide_retracted.setObjectName(u"station1_io_grease_slide_retracted")
        sizePolicy1.setHeightForWidth(self.station1_io_grease_slide_retracted.sizePolicy().hasHeightForWidth())
        self.station1_io_grease_slide_retracted.setSizePolicy(sizePolicy1)
        self.station1_io_grease_slide_retracted.setMinimumSize(QSize(50, 0))
        self.station1_io_grease_slide_retracted.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_grease_slide_retracted.setMinimum(1)
        self.station1_io_grease_slide_retracted.setMaximum(16)
        self.station1_io_grease_slide_retracted.setValue(6)

        self.horizontalLayout_39.addWidget(self.station1_io_grease_slide_retracted)

        self.station1_io_grease_slide_retracted_state = QLabel(self.groupBox_42)
        self.station1_io_grease_slide_retracted_state.setObjectName(u"station1_io_grease_slide_retracted_state")
        self.station1_io_grease_slide_retracted_state.setFont(font2)
        self.station1_io_grease_slide_retracted_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_39.addWidget(self.station1_io_grease_slide_retracted_state)


        self.horizontalLayout_38.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(5, 5, 5, 5)
        self.label_108 = QLabel(self.groupBox_42)
        self.label_108.setObjectName(u"label_108")
        sizePolicy.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy)

        self.horizontalLayout_40.addWidget(self.label_108)

        self.station1_io_grease_slide_extended = QSpinBox(self.groupBox_42)
        self.station1_io_grease_slide_extended.setObjectName(u"station1_io_grease_slide_extended")
        sizePolicy1.setHeightForWidth(self.station1_io_grease_slide_extended.sizePolicy().hasHeightForWidth())
        self.station1_io_grease_slide_extended.setSizePolicy(sizePolicy1)
        self.station1_io_grease_slide_extended.setMinimumSize(QSize(50, 0))
        self.station1_io_grease_slide_extended.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_grease_slide_extended.setMinimum(1)
        self.station1_io_grease_slide_extended.setMaximum(16)
        self.station1_io_grease_slide_extended.setValue(6)

        self.horizontalLayout_40.addWidget(self.station1_io_grease_slide_extended)

        self.station1_io_grease_slide_extended_state = QLabel(self.groupBox_42)
        self.station1_io_grease_slide_extended_state.setObjectName(u"station1_io_grease_slide_extended_state")
        self.station1_io_grease_slide_extended_state.setFont(font2)
        self.station1_io_grease_slide_extended_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_40.addWidget(self.station1_io_grease_slide_extended_state)


        self.horizontalLayout_38.addLayout(self.horizontalLayout_40)


        self.verticalLayout_14.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_118 = QLabel(self.groupBox_42)
        self.label_118.setObjectName(u"label_118")
        sizePolicy.setHeightForWidth(self.label_118.sizePolicy().hasHeightForWidth())
        self.label_118.setSizePolicy(sizePolicy)

        self.horizontalLayout_52.addWidget(self.label_118)

        self.station1_io_electrovalve_to_alemite_ram = QSpinBox(self.groupBox_42)
        self.station1_io_electrovalve_to_alemite_ram.setObjectName(u"station1_io_electrovalve_to_alemite_ram")
        sizePolicy1.setHeightForWidth(self.station1_io_electrovalve_to_alemite_ram.sizePolicy().hasHeightForWidth())
        self.station1_io_electrovalve_to_alemite_ram.setSizePolicy(sizePolicy1)
        self.station1_io_electrovalve_to_alemite_ram.setMinimumSize(QSize(50, 0))
        self.station1_io_electrovalve_to_alemite_ram.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_io_electrovalve_to_alemite_ram.setMinimum(1)
        self.station1_io_electrovalve_to_alemite_ram.setMaximum(16)
        self.station1_io_electrovalve_to_alemite_ram.setValue(6)

        self.horizontalLayout_52.addWidget(self.station1_io_electrovalve_to_alemite_ram)

        self.station1_io_electrovalve_to_alemite_ram_state = QLabel(self.groupBox_42)
        self.station1_io_electrovalve_to_alemite_ram_state.setObjectName(u"station1_io_electrovalve_to_alemite_ram_state")
        self.station1_io_electrovalve_to_alemite_ram_state.setFont(font2)
        self.station1_io_electrovalve_to_alemite_ram_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_52.addWidget(self.station1_io_electrovalve_to_alemite_ram_state)

        self.station1_io_electrovalve_to_alemite_ram_btn = QToolButton(self.groupBox_42)
        self.station1_io_electrovalve_to_alemite_ram_btn.setObjectName(u"station1_io_electrovalve_to_alemite_ram_btn")
        self.station1_io_electrovalve_to_alemite_ram_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_52.addWidget(self.station1_io_electrovalve_to_alemite_ram_btn)


        self.verticalLayout_14.addLayout(self.horizontalLayout_52)


        self.verticalLayout_47.addWidget(self.groupBox_42)

        self.groupBox_22 = QGroupBox(self.groupBox_14)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.verticalLayout_45 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_45.setSpacing(5)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.btn_grease_inject = QToolButton(self.groupBox_22)
        self.btn_grease_inject.setObjectName(u"btn_grease_inject")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_grease_inject.sizePolicy().hasHeightForWidth())
        self.btn_grease_inject.setSizePolicy(sizePolicy5)

        self.horizontalLayout_162.addWidget(self.btn_grease_inject)

        self.btn_grease_clear_error = QToolButton(self.groupBox_22)
        self.btn_grease_clear_error.setObjectName(u"btn_grease_clear_error")
        sizePolicy5.setHeightForWidth(self.btn_grease_clear_error.sizePolicy().hasHeightForWidth())
        self.btn_grease_clear_error.setSizePolicy(sizePolicy5)

        self.horizontalLayout_162.addWidget(self.btn_grease_clear_error)


        self.verticalLayout_45.addLayout(self.horizontalLayout_162)

        self.horizontalLayout_171 = QHBoxLayout()
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.btn_grease_purge = QToolButton(self.groupBox_22)
        self.btn_grease_purge.setObjectName(u"btn_grease_purge")
        sizePolicy5.setHeightForWidth(self.btn_grease_purge.sizePolicy().hasHeightForWidth())
        self.btn_grease_purge.setSizePolicy(sizePolicy5)

        self.horizontalLayout_171.addWidget(self.btn_grease_purge)

        self.btn_grease_refill = QToolButton(self.groupBox_22)
        self.btn_grease_refill.setObjectName(u"btn_grease_refill")
        sizePolicy5.setHeightForWidth(self.btn_grease_refill.sizePolicy().hasHeightForWidth())
        self.btn_grease_refill.setSizePolicy(sizePolicy5)

        self.horizontalLayout_171.addWidget(self.btn_grease_refill)


        self.verticalLayout_45.addLayout(self.horizontalLayout_171)

        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.label_2 = QLabel(self.groupBox_22)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_172.addWidget(self.label_2)

        self.station1_grease_dispenser_state = QLabel(self.groupBox_22)
        self.station1_grease_dispenser_state.setObjectName(u"station1_grease_dispenser_state")
        sizePolicy.setHeightForWidth(self.station1_grease_dispenser_state.sizePolicy().hasHeightForWidth())
        self.station1_grease_dispenser_state.setSizePolicy(sizePolicy)
        self.station1_grease_dispenser_state.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_172.addWidget(self.station1_grease_dispenser_state)


        self.verticalLayout_45.addLayout(self.horizontalLayout_172)


        self.verticalLayout_47.addWidget(self.groupBox_22)


        self.horizontalLayout_170.addLayout(self.verticalLayout_47)

        self.groupBox_18 = QGroupBox(self.groupBox_14)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.label_138 = QLabel(self.groupBox_18)
        self.label_138.setObjectName(u"label_138")
        sizePolicy.setHeightForWidth(self.label_138.sizePolicy().hasHeightForWidth())
        self.label_138.setSizePolicy(sizePolicy)

        self.horizontalLayout_137.addWidget(self.label_138)

        self.station1_grease_dispenser_reservoir_back_pressure_delay = QDoubleSpinBox(self.groupBox_18)
        self.station1_grease_dispenser_reservoir_back_pressure_delay.setObjectName(u"station1_grease_dispenser_reservoir_back_pressure_delay")
        self.station1_grease_dispenser_reservoir_back_pressure_delay.setMinimumSize(QSize(0, 25))
        self.station1_grease_dispenser_reservoir_back_pressure_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_grease_dispenser_reservoir_back_pressure_delay.setDecimals(1)
        self.station1_grease_dispenser_reservoir_back_pressure_delay.setValue(1.000000000000000)

        self.horizontalLayout_137.addWidget(self.station1_grease_dispenser_reservoir_back_pressure_delay)


        self.verticalLayout_11.addLayout(self.horizontalLayout_137)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.label_179 = QLabel(self.groupBox_18)
        self.label_179.setObjectName(u"label_179")
        sizePolicy.setHeightForWidth(self.label_179.sizePolicy().hasHeightForWidth())
        self.label_179.setSizePolicy(sizePolicy)

        self.horizontalLayout_138.addWidget(self.label_179)

        self.station1_grease_dispenser_shot_chamber_filling_delay = QDoubleSpinBox(self.groupBox_18)
        self.station1_grease_dispenser_shot_chamber_filling_delay.setObjectName(u"station1_grease_dispenser_shot_chamber_filling_delay")
        self.station1_grease_dispenser_shot_chamber_filling_delay.setMinimumSize(QSize(0, 25))
        self.station1_grease_dispenser_shot_chamber_filling_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_grease_dispenser_shot_chamber_filling_delay.setDecimals(1)
        self.station1_grease_dispenser_shot_chamber_filling_delay.setValue(0.500000000000000)

        self.horizontalLayout_138.addWidget(self.station1_grease_dispenser_shot_chamber_filling_delay)


        self.verticalLayout_11.addLayout(self.horizontalLayout_138)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.label_180 = QLabel(self.groupBox_18)
        self.label_180.setObjectName(u"label_180")
        sizePolicy.setHeightForWidth(self.label_180.sizePolicy().hasHeightForWidth())
        self.label_180.setSizePolicy(sizePolicy)

        self.horizontalLayout_142.addWidget(self.label_180)

        self.station1_grease_dispenser_depressurize_delay = QDoubleSpinBox(self.groupBox_18)
        self.station1_grease_dispenser_depressurize_delay.setObjectName(u"station1_grease_dispenser_depressurize_delay")
        self.station1_grease_dispenser_depressurize_delay.setMinimumSize(QSize(0, 25))
        self.station1_grease_dispenser_depressurize_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_grease_dispenser_depressurize_delay.setDecimals(1)
        self.station1_grease_dispenser_depressurize_delay.setValue(2.000000000000000)

        self.horizontalLayout_142.addWidget(self.station1_grease_dispenser_depressurize_delay)


        self.verticalLayout_11.addLayout(self.horizontalLayout_142)

        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.label_181 = QLabel(self.groupBox_18)
        self.label_181.setObjectName(u"label_181")
        sizePolicy.setHeightForWidth(self.label_181.sizePolicy().hasHeightForWidth())
        self.label_181.setSizePolicy(sizePolicy)

        self.horizontalLayout_149.addWidget(self.label_181)

        self.station1_grease_dispenser_open_spool_valve_delay = QDoubleSpinBox(self.groupBox_18)
        self.station1_grease_dispenser_open_spool_valve_delay.setObjectName(u"station1_grease_dispenser_open_spool_valve_delay")
        self.station1_grease_dispenser_open_spool_valve_delay.setMinimumSize(QSize(0, 25))
        self.station1_grease_dispenser_open_spool_valve_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_grease_dispenser_open_spool_valve_delay.setDecimals(1)
        self.station1_grease_dispenser_open_spool_valve_delay.setValue(0.500000000000000)

        self.horizontalLayout_149.addWidget(self.station1_grease_dispenser_open_spool_valve_delay)


        self.verticalLayout_11.addLayout(self.horizontalLayout_149)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_182 = QLabel(self.groupBox_18)
        self.label_182.setObjectName(u"label_182")
        sizePolicy.setHeightForWidth(self.label_182.sizePolicy().hasHeightForWidth())
        self.label_182.setSizePolicy(sizePolicy)

        self.horizontalLayout_156.addWidget(self.label_182)

        self.station1_grease_dispenser_inject_delay = QDoubleSpinBox(self.groupBox_18)
        self.station1_grease_dispenser_inject_delay.setObjectName(u"station1_grease_dispenser_inject_delay")
        self.station1_grease_dispenser_inject_delay.setMinimumSize(QSize(0, 25))
        self.station1_grease_dispenser_inject_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_grease_dispenser_inject_delay.setDecimals(1)
        self.station1_grease_dispenser_inject_delay.setValue(1.000000000000000)

        self.horizontalLayout_156.addWidget(self.station1_grease_dispenser_inject_delay)


        self.verticalLayout_11.addLayout(self.horizontalLayout_156)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_183 = QLabel(self.groupBox_18)
        self.label_183.setObjectName(u"label_183")
        sizePolicy.setHeightForWidth(self.label_183.sizePolicy().hasHeightForWidth())
        self.label_183.setSizePolicy(sizePolicy)
        self.label_183.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_56.addWidget(self.label_183)

        self.station1_grease_dispenser_grease_reservoir_timeout = QDoubleSpinBox(self.groupBox_18)
        self.station1_grease_dispenser_grease_reservoir_timeout.setObjectName(u"station1_grease_dispenser_grease_reservoir_timeout")
        self.station1_grease_dispenser_grease_reservoir_timeout.setMinimumSize(QSize(0, 25))
        self.station1_grease_dispenser_grease_reservoir_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_grease_dispenser_grease_reservoir_timeout.setDecimals(1)
        self.station1_grease_dispenser_grease_reservoir_timeout.setValue(1.000000000000000)

        self.horizontalLayout_56.addWidget(self.station1_grease_dispenser_grease_reservoir_timeout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_169 = QHBoxLayout()
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.label_184 = QLabel(self.groupBox_18)
        self.label_184.setObjectName(u"label_184")
        sizePolicy.setHeightForWidth(self.label_184.sizePolicy().hasHeightForWidth())
        self.label_184.setSizePolicy(sizePolicy)

        self.horizontalLayout_169.addWidget(self.label_184)

        self.station1_grease_dispenser_sensor_timeout = QDoubleSpinBox(self.groupBox_18)
        self.station1_grease_dispenser_sensor_timeout.setObjectName(u"station1_grease_dispenser_sensor_timeout")
        self.station1_grease_dispenser_sensor_timeout.setMinimumSize(QSize(0, 25))
        self.station1_grease_dispenser_sensor_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_grease_dispenser_sensor_timeout.setDecimals(1)
        self.station1_grease_dispenser_sensor_timeout.setValue(1.000000000000000)

        self.horizontalLayout_169.addWidget(self.station1_grease_dispenser_sensor_timeout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_169)


        self.horizontalLayout_170.addWidget(self.groupBox_18)

        self.groupBox_9 = QGroupBox(self.groupBox_14)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setSpacing(10)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_128 = QLabel(self.groupBox_9)
        self.label_128.setObjectName(u"label_128")
        sizePolicy.setHeightForWidth(self.label_128.sizePolicy().hasHeightForWidth())
        self.label_128.setSizePolicy(sizePolicy)

        self.horizontalLayout_75.addWidget(self.label_128)

        self.station1_valve_grease_dispenser_retract_ejector_piston = QSpinBox(self.groupBox_9)
        self.station1_valve_grease_dispenser_retract_ejector_piston.setObjectName(u"station1_valve_grease_dispenser_retract_ejector_piston")
        sizePolicy1.setHeightForWidth(self.station1_valve_grease_dispenser_retract_ejector_piston.sizePolicy().hasHeightForWidth())
        self.station1_valve_grease_dispenser_retract_ejector_piston.setSizePolicy(sizePolicy1)
        self.station1_valve_grease_dispenser_retract_ejector_piston.setMinimumSize(QSize(50, 0))
        self.station1_valve_grease_dispenser_retract_ejector_piston.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_grease_dispenser_retract_ejector_piston.setMinimum(1)
        self.station1_valve_grease_dispenser_retract_ejector_piston.setMaximum(16)
        self.station1_valve_grease_dispenser_retract_ejector_piston.setValue(6)

        self.horizontalLayout_75.addWidget(self.station1_valve_grease_dispenser_retract_ejector_piston)

        self.station1_valve_grease_dispenser_retract_ejector_piston_state = QLabel(self.groupBox_9)
        self.station1_valve_grease_dispenser_retract_ejector_piston_state.setObjectName(u"station1_valve_grease_dispenser_retract_ejector_piston_state")
        self.station1_valve_grease_dispenser_retract_ejector_piston_state.setFont(font2)
        self.station1_valve_grease_dispenser_retract_ejector_piston_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_75.addWidget(self.station1_valve_grease_dispenser_retract_ejector_piston_state)

        self.station1_valve_grease_dispenser_retract_ejector_piston_btn = QToolButton(self.groupBox_9)
        self.station1_valve_grease_dispenser_retract_ejector_piston_btn.setObjectName(u"station1_valve_grease_dispenser_retract_ejector_piston_btn")
        self.station1_valve_grease_dispenser_retract_ejector_piston_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_75.addWidget(self.station1_valve_grease_dispenser_retract_ejector_piston_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setSpacing(10)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_132 = QLabel(self.groupBox_9)
        self.label_132.setObjectName(u"label_132")
        sizePolicy.setHeightForWidth(self.label_132.sizePolicy().hasHeightForWidth())
        self.label_132.setSizePolicy(sizePolicy)

        self.horizontalLayout_76.addWidget(self.label_132)

        self.station1_valve_grease_dispenser_lower_grease_block = QSpinBox(self.groupBox_9)
        self.station1_valve_grease_dispenser_lower_grease_block.setObjectName(u"station1_valve_grease_dispenser_lower_grease_block")
        sizePolicy1.setHeightForWidth(self.station1_valve_grease_dispenser_lower_grease_block.sizePolicy().hasHeightForWidth())
        self.station1_valve_grease_dispenser_lower_grease_block.setSizePolicy(sizePolicy1)
        self.station1_valve_grease_dispenser_lower_grease_block.setMinimumSize(QSize(50, 0))
        self.station1_valve_grease_dispenser_lower_grease_block.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_grease_dispenser_lower_grease_block.setMinimum(1)
        self.station1_valve_grease_dispenser_lower_grease_block.setMaximum(16)
        self.station1_valve_grease_dispenser_lower_grease_block.setValue(6)

        self.horizontalLayout_76.addWidget(self.station1_valve_grease_dispenser_lower_grease_block)

        self.station1_valve_grease_dispenser_lower_grease_block_state = QLabel(self.groupBox_9)
        self.station1_valve_grease_dispenser_lower_grease_block_state.setObjectName(u"station1_valve_grease_dispenser_lower_grease_block_state")
        self.station1_valve_grease_dispenser_lower_grease_block_state.setFont(font2)
        self.station1_valve_grease_dispenser_lower_grease_block_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_76.addWidget(self.station1_valve_grease_dispenser_lower_grease_block_state)

        self.station1_valve_grease_dispenser_lower_grease_block_btn = QToolButton(self.groupBox_9)
        self.station1_valve_grease_dispenser_lower_grease_block_btn.setObjectName(u"station1_valve_grease_dispenser_lower_grease_block_btn")
        self.station1_valve_grease_dispenser_lower_grease_block_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_76.addWidget(self.station1_valve_grease_dispenser_lower_grease_block_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setSpacing(10)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_133 = QLabel(self.groupBox_9)
        self.label_133.setObjectName(u"label_133")
        sizePolicy.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy)

        self.horizontalLayout_74.addWidget(self.label_133)

        self.station1_valve_grease_spool_valve = QSpinBox(self.groupBox_9)
        self.station1_valve_grease_spool_valve.setObjectName(u"station1_valve_grease_spool_valve")
        sizePolicy1.setHeightForWidth(self.station1_valve_grease_spool_valve.sizePolicy().hasHeightForWidth())
        self.station1_valve_grease_spool_valve.setSizePolicy(sizePolicy1)
        self.station1_valve_grease_spool_valve.setMinimumSize(QSize(50, 0))
        self.station1_valve_grease_spool_valve.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_grease_spool_valve.setMinimum(1)
        self.station1_valve_grease_spool_valve.setMaximum(16)
        self.station1_valve_grease_spool_valve.setValue(6)

        self.horizontalLayout_74.addWidget(self.station1_valve_grease_spool_valve)

        self.station1_valve_grease_spool_valve_state = QLabel(self.groupBox_9)
        self.station1_valve_grease_spool_valve_state.setObjectName(u"station1_valve_grease_spool_valve_state")
        self.station1_valve_grease_spool_valve_state.setFont(font2)
        self.station1_valve_grease_spool_valve_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_74.addWidget(self.station1_valve_grease_spool_valve_state)

        self.station1_valve_grease_spool_valve_btn = QToolButton(self.groupBox_9)
        self.station1_valve_grease_spool_valve_btn.setObjectName(u"station1_valve_grease_spool_valve_btn")
        self.station1_valve_grease_spool_valve_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_74.addWidget(self.station1_valve_grease_spool_valve_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setSpacing(10)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_134 = QLabel(self.groupBox_9)
        self.label_134.setObjectName(u"label_134")
        sizePolicy.setHeightForWidth(self.label_134.sizePolicy().hasHeightForWidth())
        self.label_134.setSizePolicy(sizePolicy)

        self.horizontalLayout_77.addWidget(self.label_134)

        self.station1_valve_grease_canister_back_pressure = QSpinBox(self.groupBox_9)
        self.station1_valve_grease_canister_back_pressure.setObjectName(u"station1_valve_grease_canister_back_pressure")
        sizePolicy1.setHeightForWidth(self.station1_valve_grease_canister_back_pressure.sizePolicy().hasHeightForWidth())
        self.station1_valve_grease_canister_back_pressure.setSizePolicy(sizePolicy1)
        self.station1_valve_grease_canister_back_pressure.setMinimumSize(QSize(50, 0))
        self.station1_valve_grease_canister_back_pressure.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_grease_canister_back_pressure.setMinimum(1)
        self.station1_valve_grease_canister_back_pressure.setMaximum(16)
        self.station1_valve_grease_canister_back_pressure.setValue(6)

        self.horizontalLayout_77.addWidget(self.station1_valve_grease_canister_back_pressure)

        self.station1_valve_grease_canister_back_pressure_state = QLabel(self.groupBox_9)
        self.station1_valve_grease_canister_back_pressure_state.setObjectName(u"station1_valve_grease_canister_back_pressure_state")
        self.station1_valve_grease_canister_back_pressure_state.setFont(font2)
        self.station1_valve_grease_canister_back_pressure_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_77.addWidget(self.station1_valve_grease_canister_back_pressure_state)

        self.station1_valve_grease_canister_back_pressure_btn = QToolButton(self.groupBox_9)
        self.station1_valve_grease_canister_back_pressure_btn.setObjectName(u"station1_valve_grease_canister_back_pressure_btn")
        self.station1_valve_grease_canister_back_pressure_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_77.addWidget(self.station1_valve_grease_canister_back_pressure_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setSpacing(10)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_135 = QLabel(self.groupBox_9)
        self.label_135.setObjectName(u"label_135")
        sizePolicy.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy)

        self.horizontalLayout_79.addWidget(self.label_135)

        self.station1_valve_grease_dispenser_advance_ejector_piston = QSpinBox(self.groupBox_9)
        self.station1_valve_grease_dispenser_advance_ejector_piston.setObjectName(u"station1_valve_grease_dispenser_advance_ejector_piston")
        sizePolicy1.setHeightForWidth(self.station1_valve_grease_dispenser_advance_ejector_piston.sizePolicy().hasHeightForWidth())
        self.station1_valve_grease_dispenser_advance_ejector_piston.setSizePolicy(sizePolicy1)
        self.station1_valve_grease_dispenser_advance_ejector_piston.setMinimumSize(QSize(50, 0))
        self.station1_valve_grease_dispenser_advance_ejector_piston.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station1_valve_grease_dispenser_advance_ejector_piston.setMinimum(1)
        self.station1_valve_grease_dispenser_advance_ejector_piston.setMaximum(16)
        self.station1_valve_grease_dispenser_advance_ejector_piston.setValue(6)

        self.horizontalLayout_79.addWidget(self.station1_valve_grease_dispenser_advance_ejector_piston)

        self.station1_valve_grease_dispenser_advance_ejector_piston_state = QLabel(self.groupBox_9)
        self.station1_valve_grease_dispenser_advance_ejector_piston_state.setObjectName(u"station1_valve_grease_dispenser_advance_ejector_piston_state")
        self.station1_valve_grease_dispenser_advance_ejector_piston_state.setFont(font2)
        self.station1_valve_grease_dispenser_advance_ejector_piston_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_79.addWidget(self.station1_valve_grease_dispenser_advance_ejector_piston_state)

        self.station1_valve_grease_dispenser_advance_ejector_piston_btn = QToolButton(self.groupBox_9)
        self.station1_valve_grease_dispenser_advance_ejector_piston_btn.setObjectName(u"station1_valve_grease_dispenser_advance_ejector_piston_btn")
        self.station1_valve_grease_dispenser_advance_ejector_piston_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_79.addWidget(self.station1_valve_grease_dispenser_advance_ejector_piston_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_79)


        self.horizontalLayout_170.addWidget(self.groupBox_9)


        self.verticalLayout_51.addWidget(self.groupBox_14)

        self.tabWidget.addTab(self.tab_station1, "")
        self.tab_station2 = QWidget()
        self.tab_station2.setObjectName(u"tab_station2")
        self.verticalLayout_20 = QVBoxLayout(self.tab_station2)
        self.verticalLayout_20.setSpacing(30)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setSpacing(30)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.groupBox_15 = QGroupBox(self.tab_station2)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(0, 0))
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_22 = QLabel(self.groupBox_15)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_24.addWidget(self.label_22)

        self.station2_robot = QLineEdit(self.groupBox_15)
        self.station2_robot.setObjectName(u"station2_robot")
        self.station2_robot.setMaximumSize(QSize(150, 16777215))
        self.station2_robot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.station2_robot)

        self.btn_station2_robot_test = QPushButton(self.groupBox_15)
        self.btn_station2_robot_test.setObjectName(u"btn_station2_robot_test")
        self.btn_station2_robot_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_24.addWidget(self.btn_station2_robot_test)


        self.verticalLayout_15.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(20)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_28 = QLabel(self.groupBox_15)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_30.addWidget(self.label_28)

        self.station2_cognex = QLineEdit(self.groupBox_15)
        self.station2_cognex.setObjectName(u"station2_cognex")
        self.station2_cognex.setMaximumSize(QSize(150, 16777215))
        self.station2_cognex.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.station2_cognex)

        self.btn_station2_cognex_test = QPushButton(self.groupBox_15)
        self.btn_station2_cognex_test.setObjectName(u"btn_station2_cognex_test")
        self.btn_station2_cognex_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_30.addWidget(self.btn_station2_cognex_test)


        self.verticalLayout_15.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_186 = QHBoxLayout()
        self.horizontalLayout_186.setSpacing(20)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.label_54 = QLabel(self.groupBox_15)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_186.addWidget(self.label_54)

        self.station2_barcode_4 = QLineEdit(self.groupBox_15)
        self.station2_barcode_4.setObjectName(u"station2_barcode_4")
        self.station2_barcode_4.setMaximumSize(QSize(150, 16777215))
        self.station2_barcode_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_186.addWidget(self.station2_barcode_4)

        self.btn_station2_barcode_4_test = QPushButton(self.groupBox_15)
        self.btn_station2_barcode_4_test.setObjectName(u"btn_station2_barcode_4_test")
        self.btn_station2_barcode_4_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_186.addWidget(self.btn_station2_barcode_4_test)


        self.verticalLayout_15.addLayout(self.horizontalLayout_186)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_23 = QLabel(self.groupBox_15)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_25.addWidget(self.label_23)

        self.station2_wago = QLineEdit(self.groupBox_15)
        self.station2_wago.setObjectName(u"station2_wago")
        self.station2_wago.setMaximumSize(QSize(150, 16777215))
        self.station2_wago.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.station2_wago)

        self.btn_station2_wago_test = QPushButton(self.groupBox_15)
        self.btn_station2_wago_test.setObjectName(u"btn_station2_wago_test")
        self.btn_station2_wago_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_25.addWidget(self.btn_station2_wago_test)


        self.verticalLayout_15.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_87.addWidget(self.groupBox_15)

        self.groupBox_3 = QGroupBox(self.tab_station2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(30)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_26.addWidget(self.label_24)

        self.station2_feeders_upper_housing = QLineEdit(self.groupBox_3)
        self.station2_feeders_upper_housing.setObjectName(u"station2_feeders_upper_housing")
        self.station2_feeders_upper_housing.setMaximumSize(QSize(150, 16777215))
        self.station2_feeders_upper_housing.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.station2_feeders_upper_housing)

        self.btn_station2_feeders_upper_housing_test = QPushButton(self.groupBox_3)
        self.btn_station2_feeders_upper_housing_test.setObjectName(u"btn_station2_feeders_upper_housing_test")
        self.btn_station2_feeders_upper_housing_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_26.addWidget(self.btn_station2_feeders_upper_housing_test)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(30)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_27.addWidget(self.label_25)

        self.station2_feeders_crank_arm = QLineEdit(self.groupBox_3)
        self.station2_feeders_crank_arm.setObjectName(u"station2_feeders_crank_arm")
        self.station2_feeders_crank_arm.setMaximumSize(QSize(150, 16777215))
        self.station2_feeders_crank_arm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.station2_feeders_crank_arm)

        self.btn_station2_feeders_crank_arm_test = QPushButton(self.groupBox_3)
        self.btn_station2_feeders_crank_arm_test.setObjectName(u"btn_station2_feeders_crank_arm_test")
        self.btn_station2_feeders_crank_arm_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_27.addWidget(self.btn_station2_feeders_crank_arm_test)


        self.verticalLayout_6.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(30)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_28.addWidget(self.label_26)

        self.station2_feeders_rotor = QLineEdit(self.groupBox_3)
        self.station2_feeders_rotor.setObjectName(u"station2_feeders_rotor")
        self.station2_feeders_rotor.setMaximumSize(QSize(150, 16777215))
        self.station2_feeders_rotor.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.station2_feeders_rotor)

        self.btn_station2_feeders_rotor_test = QPushButton(self.groupBox_3)
        self.btn_station2_feeders_rotor_test.setObjectName(u"btn_station2_feeders_rotor_test")
        self.btn_station2_feeders_rotor_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_28.addWidget(self.btn_station2_feeders_rotor_test)


        self.verticalLayout_6.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_87.addWidget(self.groupBox_3)


        self.verticalLayout_20.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setSpacing(30)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.groupBox_16 = QGroupBox(self.tab_station2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(15, 15, 15, 15)
        self.groupBox_17 = QGroupBox(self.groupBox_16)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(0, 120))
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setSpacing(40)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(10)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(5, 5, 5, 5)
        self.label_111 = QLabel(self.groupBox_17)
        self.label_111.setObjectName(u"label_111")
        sizePolicy.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy)

        self.horizontalLayout_47.addWidget(self.label_111)

        self.station2_io_lift_locate_extended_4 = QSpinBox(self.groupBox_17)
        self.station2_io_lift_locate_extended_4.setObjectName(u"station2_io_lift_locate_extended_4")
        sizePolicy1.setHeightForWidth(self.station2_io_lift_locate_extended_4.sizePolicy().hasHeightForWidth())
        self.station2_io_lift_locate_extended_4.setSizePolicy(sizePolicy1)
        self.station2_io_lift_locate_extended_4.setMinimumSize(QSize(50, 0))
        self.station2_io_lift_locate_extended_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station2_io_lift_locate_extended_4.setMinimum(1)
        self.station2_io_lift_locate_extended_4.setMaximum(16)
        self.station2_io_lift_locate_extended_4.setValue(6)

        self.horizontalLayout_47.addWidget(self.station2_io_lift_locate_extended_4)

        self.station2_io_lift_locate_extended_4_state = QLabel(self.groupBox_17)
        self.station2_io_lift_locate_extended_4_state.setObjectName(u"station2_io_lift_locate_extended_4_state")
        self.station2_io_lift_locate_extended_4_state.setFont(font2)
        self.station2_io_lift_locate_extended_4_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_47.addWidget(self.station2_io_lift_locate_extended_4_state)


        self.horizontalLayout_45.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(10)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(5, 5, 5, 5)
        self.label_113 = QLabel(self.groupBox_17)
        self.label_113.setObjectName(u"label_113")
        sizePolicy.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy)

        self.horizontalLayout_48.addWidget(self.label_113)

        self.station2_io_lift_locate_retracted_4 = QSpinBox(self.groupBox_17)
        self.station2_io_lift_locate_retracted_4.setObjectName(u"station2_io_lift_locate_retracted_4")
        sizePolicy1.setHeightForWidth(self.station2_io_lift_locate_retracted_4.sizePolicy().hasHeightForWidth())
        self.station2_io_lift_locate_retracted_4.setSizePolicy(sizePolicy1)
        self.station2_io_lift_locate_retracted_4.setMinimumSize(QSize(50, 0))
        self.station2_io_lift_locate_retracted_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station2_io_lift_locate_retracted_4.setMinimum(1)
        self.station2_io_lift_locate_retracted_4.setMaximum(16)
        self.station2_io_lift_locate_retracted_4.setValue(6)

        self.horizontalLayout_48.addWidget(self.station2_io_lift_locate_retracted_4)

        self.station2_io_lift_locate_retracted_4_state = QLabel(self.groupBox_17)
        self.station2_io_lift_locate_retracted_4_state.setObjectName(u"station2_io_lift_locate_retracted_4_state")
        self.station2_io_lift_locate_retracted_4_state.setFont(font2)
        self.station2_io_lift_locate_retracted_4_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_48.addWidget(self.station2_io_lift_locate_retracted_4_state)


        self.horizontalLayout_45.addLayout(self.horizontalLayout_48)


        self.verticalLayout_17.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(40)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setSpacing(10)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(5, 5, 5, 5)
        self.label_114 = QLabel(self.groupBox_17)
        self.label_114.setObjectName(u"label_114")
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)

        self.horizontalLayout_50.addWidget(self.label_114)

        self.station2_io_lift_locate_pre_4 = QSpinBox(self.groupBox_17)
        self.station2_io_lift_locate_pre_4.setObjectName(u"station2_io_lift_locate_pre_4")
        sizePolicy1.setHeightForWidth(self.station2_io_lift_locate_pre_4.sizePolicy().hasHeightForWidth())
        self.station2_io_lift_locate_pre_4.setSizePolicy(sizePolicy1)
        self.station2_io_lift_locate_pre_4.setMinimumSize(QSize(50, 0))
        self.station2_io_lift_locate_pre_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station2_io_lift_locate_pre_4.setMinimum(1)
        self.station2_io_lift_locate_pre_4.setMaximum(16)
        self.station2_io_lift_locate_pre_4.setValue(6)

        self.horizontalLayout_50.addWidget(self.station2_io_lift_locate_pre_4)

        self.station2_io_lift_locate_pre_4_state = QLabel(self.groupBox_17)
        self.station2_io_lift_locate_pre_4_state.setObjectName(u"station2_io_lift_locate_pre_4_state")
        self.station2_io_lift_locate_pre_4_state.setFont(font2)
        self.station2_io_lift_locate_pre_4_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_50.addWidget(self.station2_io_lift_locate_pre_4_state)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setSpacing(10)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(5, 5, 5, 5)
        self.label_136 = QLabel(self.groupBox_17)
        self.label_136.setObjectName(u"label_136")
        sizePolicy.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy)

        self.horizontalLayout_81.addWidget(self.label_136)

        self.station2_io_lift_locate_main_4 = QSpinBox(self.groupBox_17)
        self.station2_io_lift_locate_main_4.setObjectName(u"station2_io_lift_locate_main_4")
        sizePolicy1.setHeightForWidth(self.station2_io_lift_locate_main_4.sizePolicy().hasHeightForWidth())
        self.station2_io_lift_locate_main_4.setSizePolicy(sizePolicy1)
        self.station2_io_lift_locate_main_4.setMinimumSize(QSize(50, 0))
        self.station2_io_lift_locate_main_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station2_io_lift_locate_main_4.setMinimum(1)
        self.station2_io_lift_locate_main_4.setMaximum(16)
        self.station2_io_lift_locate_main_4.setValue(6)

        self.horizontalLayout_81.addWidget(self.station2_io_lift_locate_main_4)

        self.station2_io_lift_locate_main_4_state = QLabel(self.groupBox_17)
        self.station2_io_lift_locate_main_4_state.setObjectName(u"station2_io_lift_locate_main_4_state")
        self.station2_io_lift_locate_main_4_state.setFont(font2)
        self.station2_io_lift_locate_main_4_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_81.addWidget(self.station2_io_lift_locate_main_4_state)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_81)


        self.verticalLayout_17.addLayout(self.horizontalLayout_49)


        self.verticalLayout_16.addWidget(self.groupBox_17)


        self.horizontalLayout_88.addWidget(self.groupBox_16)

        self.group_valve_2 = QGroupBox(self.tab_station2)
        self.group_valve_2.setObjectName(u"group_valve_2")
        self.verticalLayout_18 = QVBoxLayout(self.group_valve_2)
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(15, 15, 15, 15)
        self.groupBox_19 = QGroupBox(self.group_valve_2)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setMinimumSize(QSize(0, 120))
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setSpacing(40)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(10)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_137 = QLabel(self.groupBox_19)
        self.label_137.setObjectName(u"label_137")
        sizePolicy.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy)
        self.label_137.setMinimumSize(QSize(134, 0))

        self.horizontalLayout_83.addWidget(self.label_137)

        self.station2_valve_lift_locate_up_4 = QSpinBox(self.groupBox_19)
        self.station2_valve_lift_locate_up_4.setObjectName(u"station2_valve_lift_locate_up_4")
        sizePolicy1.setHeightForWidth(self.station2_valve_lift_locate_up_4.sizePolicy().hasHeightForWidth())
        self.station2_valve_lift_locate_up_4.setSizePolicy(sizePolicy1)
        self.station2_valve_lift_locate_up_4.setMinimumSize(QSize(50, 0))
        self.station2_valve_lift_locate_up_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station2_valve_lift_locate_up_4.setMinimum(1)
        self.station2_valve_lift_locate_up_4.setMaximum(16)
        self.station2_valve_lift_locate_up_4.setValue(6)

        self.horizontalLayout_83.addWidget(self.station2_valve_lift_locate_up_4)

        self.station2_valve_lift_locate_up_4_state = QLabel(self.groupBox_19)
        self.station2_valve_lift_locate_up_4_state.setObjectName(u"station2_valve_lift_locate_up_4_state")
        self.station2_valve_lift_locate_up_4_state.setFont(font2)
        self.station2_valve_lift_locate_up_4_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_83.addWidget(self.station2_valve_lift_locate_up_4_state)

        self.station2_valve_lift_locate_up_4_btn = QToolButton(self.groupBox_19)
        self.station2_valve_lift_locate_up_4_btn.setObjectName(u"station2_valve_lift_locate_up_4_btn")
        self.station2_valve_lift_locate_up_4_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_83.addWidget(self.station2_valve_lift_locate_up_4_btn)


        self.horizontalLayout_82.addLayout(self.horizontalLayout_83)

        self.widget_3 = QWidget(self.groupBox_19)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_82.addWidget(self.widget_3)


        self.verticalLayout_19.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setSpacing(40)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(10)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_140 = QLabel(self.groupBox_19)
        self.label_140.setObjectName(u"label_140")
        sizePolicy.setHeightForWidth(self.label_140.sizePolicy().hasHeightForWidth())
        self.label_140.setSizePolicy(sizePolicy)
        self.label_140.setMinimumSize(QSize(134, 0))

        self.horizontalLayout_85.addWidget(self.label_140)

        self.station2_valve_lift_locate_pre_4 = QSpinBox(self.groupBox_19)
        self.station2_valve_lift_locate_pre_4.setObjectName(u"station2_valve_lift_locate_pre_4")
        sizePolicy1.setHeightForWidth(self.station2_valve_lift_locate_pre_4.sizePolicy().hasHeightForWidth())
        self.station2_valve_lift_locate_pre_4.setSizePolicy(sizePolicy1)
        self.station2_valve_lift_locate_pre_4.setMinimumSize(QSize(50, 0))
        self.station2_valve_lift_locate_pre_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station2_valve_lift_locate_pre_4.setMinimum(1)
        self.station2_valve_lift_locate_pre_4.setMaximum(16)
        self.station2_valve_lift_locate_pre_4.setValue(6)

        self.horizontalLayout_85.addWidget(self.station2_valve_lift_locate_pre_4)

        self.station2_valve_lift_locate_pre_4_state = QLabel(self.groupBox_19)
        self.station2_valve_lift_locate_pre_4_state.setObjectName(u"station2_valve_lift_locate_pre_4_state")
        self.station2_valve_lift_locate_pre_4_state.setFont(font2)
        self.station2_valve_lift_locate_pre_4_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_85.addWidget(self.station2_valve_lift_locate_pre_4_state)

        self.station2_valve_lift_locate_pre_4_btn = QToolButton(self.groupBox_19)
        self.station2_valve_lift_locate_pre_4_btn.setObjectName(u"station2_valve_lift_locate_pre_4_btn")
        self.station2_valve_lift_locate_pre_4_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_85.addWidget(self.station2_valve_lift_locate_pre_4_btn)


        self.horizontalLayout_84.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(10)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_141 = QLabel(self.groupBox_19)
        self.label_141.setObjectName(u"label_141")
        sizePolicy.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy)

        self.horizontalLayout_86.addWidget(self.label_141)

        self.station2_valve_lift_locate_main_4 = QSpinBox(self.groupBox_19)
        self.station2_valve_lift_locate_main_4.setObjectName(u"station2_valve_lift_locate_main_4")
        sizePolicy1.setHeightForWidth(self.station2_valve_lift_locate_main_4.sizePolicy().hasHeightForWidth())
        self.station2_valve_lift_locate_main_4.setSizePolicy(sizePolicy1)
        self.station2_valve_lift_locate_main_4.setMinimumSize(QSize(50, 0))
        self.station2_valve_lift_locate_main_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station2_valve_lift_locate_main_4.setMinimum(1)
        self.station2_valve_lift_locate_main_4.setMaximum(16)
        self.station2_valve_lift_locate_main_4.setValue(6)

        self.horizontalLayout_86.addWidget(self.station2_valve_lift_locate_main_4)

        self.station2_valve_lift_locate_main_4_state = QLabel(self.groupBox_19)
        self.station2_valve_lift_locate_main_4_state.setObjectName(u"station2_valve_lift_locate_main_4_state")
        self.station2_valve_lift_locate_main_4_state.setFont(font2)
        self.station2_valve_lift_locate_main_4_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_86.addWidget(self.station2_valve_lift_locate_main_4_state)

        self.station2_valve_lift_locate_main_4_btn = QToolButton(self.groupBox_19)
        self.station2_valve_lift_locate_main_4_btn.setObjectName(u"station2_valve_lift_locate_main_4_btn")
        self.station2_valve_lift_locate_main_4_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_86.addWidget(self.station2_valve_lift_locate_main_4_btn)


        self.horizontalLayout_84.addLayout(self.horizontalLayout_86)


        self.verticalLayout_19.addLayout(self.horizontalLayout_84)


        self.verticalLayout_18.addWidget(self.groupBox_19)


        self.horizontalLayout_88.addWidget(self.group_valve_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_88)

        self.verticalSpacer = QSpacerItem(20, 470, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_station2, "")
        self.tab_station3 = QWidget()
        self.tab_station3.setObjectName(u"tab_station3")
        self.verticalLayout_54 = QVBoxLayout(self.tab_station3)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setSpacing(30)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.groupBox_24 = QGroupBox(self.tab_station3)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setMinimumSize(QSize(0, 0))
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_24)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setSpacing(20)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.label_39 = QLabel(self.groupBox_24)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(260, 0))

        self.horizontalLayout_109.addWidget(self.label_39)

        self.station3_robot = QLineEdit(self.groupBox_24)
        self.station3_robot.setObjectName(u"station3_robot")
        self.station3_robot.setMaximumSize(QSize(150, 16777215))
        self.station3_robot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_109.addWidget(self.station3_robot)

        self.btn_station3_robot_test = QPushButton(self.groupBox_24)
        self.btn_station3_robot_test.setObjectName(u"btn_station3_robot_test")
        self.btn_station3_robot_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_109.addWidget(self.btn_station3_robot_test)


        self.verticalLayout_26.addLayout(self.horizontalLayout_109)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setSpacing(20)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.label_40 = QLabel(self.groupBox_24)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(260, 0))

        self.horizontalLayout_110.addWidget(self.label_40)

        self.station3_cognex = QLineEdit(self.groupBox_24)
        self.station3_cognex.setObjectName(u"station3_cognex")
        self.station3_cognex.setMaximumSize(QSize(150, 16777215))
        self.station3_cognex.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_110.addWidget(self.station3_cognex)

        self.btn_station3_cognex_test = QPushButton(self.groupBox_24)
        self.btn_station3_cognex_test.setObjectName(u"btn_station3_cognex_test")
        self.btn_station3_cognex_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_110.addWidget(self.btn_station3_cognex_test)


        self.verticalLayout_26.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setSpacing(20)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.label_55 = QLabel(self.groupBox_24)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(260, 0))

        self.horizontalLayout_187.addWidget(self.label_55)

        self.station3_barcode_5 = QLineEdit(self.groupBox_24)
        self.station3_barcode_5.setObjectName(u"station3_barcode_5")
        self.station3_barcode_5.setMaximumSize(QSize(150, 16777215))
        self.station3_barcode_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_187.addWidget(self.station3_barcode_5)

        self.btn_station3_barcode_5_test = QPushButton(self.groupBox_24)
        self.btn_station3_barcode_5_test.setObjectName(u"btn_station3_barcode_5_test")
        self.btn_station3_barcode_5_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_187.addWidget(self.btn_station3_barcode_5_test)


        self.verticalLayout_26.addLayout(self.horizontalLayout_187)

        self.horizontalLayout_188 = QHBoxLayout()
        self.horizontalLayout_188.setSpacing(20)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.label_56 = QLabel(self.groupBox_24)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_188.addWidget(self.label_56)

        self.station3_barcode_7 = QLineEdit(self.groupBox_24)
        self.station3_barcode_7.setObjectName(u"station3_barcode_7")
        self.station3_barcode_7.setMaximumSize(QSize(150, 16777215))
        self.station3_barcode_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.station3_barcode_7)

        self.btn_station3_barcode_7_test = QPushButton(self.groupBox_24)
        self.btn_station3_barcode_7_test.setObjectName(u"btn_station3_barcode_7_test")
        self.btn_station3_barcode_7_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_188.addWidget(self.btn_station3_barcode_7_test)


        self.verticalLayout_26.addLayout(self.horizontalLayout_188)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setSpacing(20)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.label_41 = QLabel(self.groupBox_24)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(260, 0))

        self.horizontalLayout_111.addWidget(self.label_41)

        self.station3_wago = QLineEdit(self.groupBox_24)
        self.station3_wago.setObjectName(u"station3_wago")
        self.station3_wago.setMaximumSize(QSize(150, 16777215))
        self.station3_wago.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.station3_wago)

        self.btn_station3_wago_test = QPushButton(self.groupBox_24)
        self.btn_station3_wago_test.setObjectName(u"btn_station3_wago_test")
        self.btn_station3_wago_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_111.addWidget(self.btn_station3_wago_test)


        self.verticalLayout_26.addLayout(self.horizontalLayout_111)


        self.horizontalLayout_108.addWidget(self.groupBox_24)

        self.groupBox_25 = QGroupBox(self.tab_station3)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_25)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setSpacing(30)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.label_42 = QLabel(self.groupBox_25)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_112.addWidget(self.label_42)

        self.station3_feeders_left_handle = QLineEdit(self.groupBox_25)
        self.station3_feeders_left_handle.setObjectName(u"station3_feeders_left_handle")
        self.station3_feeders_left_handle.setMaximumSize(QSize(150, 16777215))
        self.station3_feeders_left_handle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_112.addWidget(self.station3_feeders_left_handle)

        self.btn_station3_feeders_left_handle_test = QPushButton(self.groupBox_25)
        self.btn_station3_feeders_left_handle_test.setObjectName(u"btn_station3_feeders_left_handle_test")
        self.btn_station3_feeders_left_handle_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_112.addWidget(self.btn_station3_feeders_left_handle_test)


        self.verticalLayout_28.addLayout(self.horizontalLayout_112)

        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setSpacing(30)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.label_43 = QLabel(self.groupBox_25)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_113.addWidget(self.label_43)

        self.station3_feeders_dial = QLineEdit(self.groupBox_25)
        self.station3_feeders_dial.setObjectName(u"station3_feeders_dial")
        self.station3_feeders_dial.setMaximumSize(QSize(150, 16777215))
        self.station3_feeders_dial.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.station3_feeders_dial)

        self.btn_station3_feeders_dial_test = QPushButton(self.groupBox_25)
        self.btn_station3_feeders_dial_test.setObjectName(u"btn_station3_feeders_dial_test")
        self.btn_station3_feeders_dial_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_113.addWidget(self.btn_station3_feeders_dial_test)


        self.verticalLayout_28.addLayout(self.horizontalLayout_113)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setSpacing(30)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.label_44 = QLabel(self.groupBox_25)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_114.addWidget(self.label_44)

        self.station3_feeders_support_arm = QLineEdit(self.groupBox_25)
        self.station3_feeders_support_arm.setObjectName(u"station3_feeders_support_arm")
        self.station3_feeders_support_arm.setMaximumSize(QSize(150, 16777215))
        self.station3_feeders_support_arm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.station3_feeders_support_arm)

        self.btn_station3_feeders_support_arm_test = QPushButton(self.groupBox_25)
        self.btn_station3_feeders_support_arm_test.setObjectName(u"btn_station3_feeders_support_arm_test")
        self.btn_station3_feeders_support_arm_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_114.addWidget(self.btn_station3_feeders_support_arm_test)


        self.verticalLayout_28.addLayout(self.horizontalLayout_114)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setSpacing(30)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.label_45 = QLabel(self.groupBox_25)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_115.addWidget(self.label_45)

        self.station3_feeders_trigger = QLineEdit(self.groupBox_25)
        self.station3_feeders_trigger.setObjectName(u"station3_feeders_trigger")
        self.station3_feeders_trigger.setMaximumSize(QSize(150, 16777215))
        self.station3_feeders_trigger.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_115.addWidget(self.station3_feeders_trigger)

        self.btn_station3_feeders_trigger_test = QPushButton(self.groupBox_25)
        self.btn_station3_feeders_trigger_test.setObjectName(u"btn_station3_feeders_trigger_test")
        self.btn_station3_feeders_trigger_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_115.addWidget(self.btn_station3_feeders_trigger_test)


        self.verticalLayout_28.addLayout(self.horizontalLayout_115)


        self.horizontalLayout_108.addWidget(self.groupBox_25)


        self.verticalLayout_54.addLayout(self.horizontalLayout_108)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setSpacing(30)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.groupBox_20 = QGroupBox(self.tab_station3)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setMinimumSize(QSize(600, 0))
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.groupBox_21 = QGroupBox(self.groupBox_20)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMinimumSize(QSize(0, 120))
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setSpacing(40)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setSpacing(10)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(5, 5, 5, 5)
        self.label_142 = QLabel(self.groupBox_21)
        self.label_142.setObjectName(u"label_142")
        sizePolicy.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy)
        self.label_142.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_91.addWidget(self.label_142)

        self.station3_io_lift_locate_extended_5 = QSpinBox(self.groupBox_21)
        self.station3_io_lift_locate_extended_5.setObjectName(u"station3_io_lift_locate_extended_5")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_extended_5.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_extended_5.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_extended_5.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_extended_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_extended_5.setMinimum(1)
        self.station3_io_lift_locate_extended_5.setMaximum(16)
        self.station3_io_lift_locate_extended_5.setValue(6)

        self.horizontalLayout_91.addWidget(self.station3_io_lift_locate_extended_5)

        self.station3_io_lift_locate_extended_5_state = QLabel(self.groupBox_21)
        self.station3_io_lift_locate_extended_5_state.setObjectName(u"station3_io_lift_locate_extended_5_state")
        self.station3_io_lift_locate_extended_5_state.setFont(font2)
        self.station3_io_lift_locate_extended_5_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_91.addWidget(self.station3_io_lift_locate_extended_5_state)


        self.horizontalLayout_90.addLayout(self.horizontalLayout_91)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setSpacing(10)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(5, 5, 5, 5)
        self.label_143 = QLabel(self.groupBox_21)
        self.label_143.setObjectName(u"label_143")
        sizePolicy.setHeightForWidth(self.label_143.sizePolicy().hasHeightForWidth())
        self.label_143.setSizePolicy(sizePolicy)
        self.label_143.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_92.addWidget(self.label_143)

        self.station3_io_lift_locate_retracted_5 = QSpinBox(self.groupBox_21)
        self.station3_io_lift_locate_retracted_5.setObjectName(u"station3_io_lift_locate_retracted_5")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_retracted_5.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_retracted_5.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_retracted_5.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_retracted_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_retracted_5.setMinimum(1)
        self.station3_io_lift_locate_retracted_5.setMaximum(16)
        self.station3_io_lift_locate_retracted_5.setValue(6)

        self.horizontalLayout_92.addWidget(self.station3_io_lift_locate_retracted_5)

        self.station3_io_lift_locate_retracted_5_state = QLabel(self.groupBox_21)
        self.station3_io_lift_locate_retracted_5_state.setObjectName(u"station3_io_lift_locate_retracted_5_state")
        self.station3_io_lift_locate_retracted_5_state.setFont(font2)
        self.station3_io_lift_locate_retracted_5_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_92.addWidget(self.station3_io_lift_locate_retracted_5_state)


        self.horizontalLayout_90.addLayout(self.horizontalLayout_92)


        self.verticalLayout_22.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setSpacing(40)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setSpacing(10)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(5, 5, 5, 5)
        self.label_144 = QLabel(self.groupBox_21)
        self.label_144.setObjectName(u"label_144")
        sizePolicy.setHeightForWidth(self.label_144.sizePolicy().hasHeightForWidth())
        self.label_144.setSizePolicy(sizePolicy)
        self.label_144.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_94.addWidget(self.label_144)

        self.station3_io_lift_locate_pre_5 = QSpinBox(self.groupBox_21)
        self.station3_io_lift_locate_pre_5.setObjectName(u"station3_io_lift_locate_pre_5")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_pre_5.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_pre_5.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_pre_5.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_pre_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_pre_5.setMinimum(1)
        self.station3_io_lift_locate_pre_5.setMaximum(16)
        self.station3_io_lift_locate_pre_5.setValue(6)

        self.horizontalLayout_94.addWidget(self.station3_io_lift_locate_pre_5)

        self.station3_io_lift_locate_pre_5_state = QLabel(self.groupBox_21)
        self.station3_io_lift_locate_pre_5_state.setObjectName(u"station3_io_lift_locate_pre_5_state")
        self.station3_io_lift_locate_pre_5_state.setFont(font2)
        self.station3_io_lift_locate_pre_5_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_94.addWidget(self.station3_io_lift_locate_pre_5_state)


        self.horizontalLayout_93.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setSpacing(10)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(5, 5, 5, 5)
        self.label_145 = QLabel(self.groupBox_21)
        self.label_145.setObjectName(u"label_145")
        sizePolicy.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy)
        self.label_145.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_95.addWidget(self.label_145)

        self.station3_io_lift_locate_main_5 = QSpinBox(self.groupBox_21)
        self.station3_io_lift_locate_main_5.setObjectName(u"station3_io_lift_locate_main_5")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_main_5.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_main_5.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_main_5.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_main_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_main_5.setMinimum(1)
        self.station3_io_lift_locate_main_5.setMaximum(16)
        self.station3_io_lift_locate_main_5.setValue(6)

        self.horizontalLayout_95.addWidget(self.station3_io_lift_locate_main_5)

        self.station3_io_lift_locate_main_5_state = QLabel(self.groupBox_21)
        self.station3_io_lift_locate_main_5_state.setObjectName(u"station3_io_lift_locate_main_5_state")
        self.station3_io_lift_locate_main_5_state.setFont(font2)
        self.station3_io_lift_locate_main_5_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_95.addWidget(self.station3_io_lift_locate_main_5_state)


        self.horizontalLayout_93.addLayout(self.horizontalLayout_95)


        self.verticalLayout_22.addLayout(self.horizontalLayout_93)


        self.verticalLayout_24.addWidget(self.groupBox_21)

        self.groupBox_26 = QGroupBox(self.groupBox_20)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setMinimumSize(QSize(0, 120))
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_26)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setSpacing(40)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setSpacing(10)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(5, 5, 5, 5)
        self.label_149 = QLabel(self.groupBox_26)
        self.label_149.setObjectName(u"label_149")
        sizePolicy.setHeightForWidth(self.label_149.sizePolicy().hasHeightForWidth())
        self.label_149.setSizePolicy(sizePolicy)
        self.label_149.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_117.addWidget(self.label_149)

        self.station3_io_lift_locate_extended_7 = QSpinBox(self.groupBox_26)
        self.station3_io_lift_locate_extended_7.setObjectName(u"station3_io_lift_locate_extended_7")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_extended_7.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_extended_7.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_extended_7.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_extended_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_extended_7.setMinimum(1)
        self.station3_io_lift_locate_extended_7.setMaximum(16)
        self.station3_io_lift_locate_extended_7.setValue(6)

        self.horizontalLayout_117.addWidget(self.station3_io_lift_locate_extended_7)

        self.station3_io_lift_locate_extended_7_state = QLabel(self.groupBox_26)
        self.station3_io_lift_locate_extended_7_state.setObjectName(u"station3_io_lift_locate_extended_7_state")
        self.station3_io_lift_locate_extended_7_state.setFont(font2)
        self.station3_io_lift_locate_extended_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_117.addWidget(self.station3_io_lift_locate_extended_7_state)


        self.horizontalLayout_116.addLayout(self.horizontalLayout_117)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setSpacing(10)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(5, 5, 5, 5)
        self.label_150 = QLabel(self.groupBox_26)
        self.label_150.setObjectName(u"label_150")
        sizePolicy.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy)
        self.label_150.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_118.addWidget(self.label_150)

        self.station3_io_lift_locate_retracted_7 = QSpinBox(self.groupBox_26)
        self.station3_io_lift_locate_retracted_7.setObjectName(u"station3_io_lift_locate_retracted_7")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_retracted_7.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_retracted_7.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_retracted_7.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_retracted_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_retracted_7.setMinimum(1)
        self.station3_io_lift_locate_retracted_7.setMaximum(16)
        self.station3_io_lift_locate_retracted_7.setValue(6)

        self.horizontalLayout_118.addWidget(self.station3_io_lift_locate_retracted_7)

        self.station3_io_lift_locate_retracted_7_state = QLabel(self.groupBox_26)
        self.station3_io_lift_locate_retracted_7_state.setObjectName(u"station3_io_lift_locate_retracted_7_state")
        self.station3_io_lift_locate_retracted_7_state.setFont(font2)
        self.station3_io_lift_locate_retracted_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_118.addWidget(self.station3_io_lift_locate_retracted_7_state)


        self.horizontalLayout_116.addLayout(self.horizontalLayout_118)


        self.verticalLayout_29.addLayout(self.horizontalLayout_116)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setSpacing(40)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setSpacing(10)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(5, 5, 5, 5)
        self.label_151 = QLabel(self.groupBox_26)
        self.label_151.setObjectName(u"label_151")
        sizePolicy.setHeightForWidth(self.label_151.sizePolicy().hasHeightForWidth())
        self.label_151.setSizePolicy(sizePolicy)
        self.label_151.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_120.addWidget(self.label_151)

        self.station3_io_lift_locate_pre_7 = QSpinBox(self.groupBox_26)
        self.station3_io_lift_locate_pre_7.setObjectName(u"station3_io_lift_locate_pre_7")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_pre_7.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_pre_7.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_pre_7.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_pre_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_pre_7.setMinimum(1)
        self.station3_io_lift_locate_pre_7.setMaximum(16)
        self.station3_io_lift_locate_pre_7.setValue(6)

        self.horizontalLayout_120.addWidget(self.station3_io_lift_locate_pre_7)

        self.station3_io_lift_locate_pre_7_state = QLabel(self.groupBox_26)
        self.station3_io_lift_locate_pre_7_state.setObjectName(u"station3_io_lift_locate_pre_7_state")
        self.station3_io_lift_locate_pre_7_state.setFont(font2)
        self.station3_io_lift_locate_pre_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_120.addWidget(self.station3_io_lift_locate_pre_7_state)


        self.horizontalLayout_119.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setSpacing(10)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(5, 5, 5, 5)
        self.label_152 = QLabel(self.groupBox_26)
        self.label_152.setObjectName(u"label_152")
        sizePolicy.setHeightForWidth(self.label_152.sizePolicy().hasHeightForWidth())
        self.label_152.setSizePolicy(sizePolicy)
        self.label_152.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_121.addWidget(self.label_152)

        self.station3_io_lift_locate_main_7 = QSpinBox(self.groupBox_26)
        self.station3_io_lift_locate_main_7.setObjectName(u"station3_io_lift_locate_main_7")
        sizePolicy1.setHeightForWidth(self.station3_io_lift_locate_main_7.sizePolicy().hasHeightForWidth())
        self.station3_io_lift_locate_main_7.setSizePolicy(sizePolicy1)
        self.station3_io_lift_locate_main_7.setMinimumSize(QSize(50, 0))
        self.station3_io_lift_locate_main_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_lift_locate_main_7.setMinimum(1)
        self.station3_io_lift_locate_main_7.setMaximum(16)
        self.station3_io_lift_locate_main_7.setValue(6)

        self.horizontalLayout_121.addWidget(self.station3_io_lift_locate_main_7)

        self.station3_io_lift_locate_main_7_state = QLabel(self.groupBox_26)
        self.station3_io_lift_locate_main_7_state.setObjectName(u"station3_io_lift_locate_main_7_state")
        self.station3_io_lift_locate_main_7_state.setFont(font2)
        self.station3_io_lift_locate_main_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_121.addWidget(self.station3_io_lift_locate_main_7_state)


        self.horizontalLayout_119.addLayout(self.horizontalLayout_121)


        self.verticalLayout_29.addLayout(self.horizontalLayout_119)


        self.verticalLayout_24.addWidget(self.groupBox_26)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setSpacing(10)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(10, 5, 5, 5)
        self.label_158 = QLabel(self.groupBox_20)
        self.label_158.setObjectName(u"label_158")
        sizePolicy.setHeightForWidth(self.label_158.sizePolicy().hasHeightForWidth())
        self.label_158.setSizePolicy(sizePolicy)
        self.label_158.setMinimumSize(QSize(120, 0))
        self.label_158.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_127.addWidget(self.label_158)

        self.station3_io_rotary_test = QSpinBox(self.groupBox_20)
        self.station3_io_rotary_test.setObjectName(u"station3_io_rotary_test")
        sizePolicy1.setHeightForWidth(self.station3_io_rotary_test.sizePolicy().hasHeightForWidth())
        self.station3_io_rotary_test.setSizePolicy(sizePolicy1)
        self.station3_io_rotary_test.setMinimumSize(QSize(50, 0))
        self.station3_io_rotary_test.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_rotary_test.setMinimum(1)
        self.station3_io_rotary_test.setMaximum(16)
        self.station3_io_rotary_test.setValue(6)

        self.horizontalLayout_127.addWidget(self.station3_io_rotary_test)

        self.station3_io_rotary_test_state = QLabel(self.groupBox_20)
        self.station3_io_rotary_test_state.setObjectName(u"station3_io_rotary_test_state")
        self.station3_io_rotary_test_state.setFont(font2)
        self.station3_io_rotary_test_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_127.addWidget(self.station3_io_rotary_test_state)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_127.addItem(self.horizontalSpacer_3)


        self.verticalLayout_24.addLayout(self.horizontalLayout_127)

        self.groupBox_46 = QGroupBox(self.groupBox_20)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.groupBox_46.setMinimumSize(QSize(0, 80))
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_46)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_202 = QHBoxLayout()
        self.horizontalLayout_202.setSpacing(40)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_203 = QHBoxLayout()
        self.horizontalLayout_203.setSpacing(10)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(5, 5, 5, 5)
        self.label_204 = QLabel(self.groupBox_46)
        self.label_204.setObjectName(u"label_204")
        sizePolicy.setHeightForWidth(self.label_204.sizePolicy().hasHeightForWidth())
        self.label_204.setSizePolicy(sizePolicy)
        self.label_204.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_203.addWidget(self.label_204)

        self.station3_io_part_flip_open = QSpinBox(self.groupBox_46)
        self.station3_io_part_flip_open.setObjectName(u"station3_io_part_flip_open")
        sizePolicy1.setHeightForWidth(self.station3_io_part_flip_open.sizePolicy().hasHeightForWidth())
        self.station3_io_part_flip_open.setSizePolicy(sizePolicy1)
        self.station3_io_part_flip_open.setMinimumSize(QSize(50, 0))
        self.station3_io_part_flip_open.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_part_flip_open.setMinimum(1)
        self.station3_io_part_flip_open.setMaximum(16)
        self.station3_io_part_flip_open.setValue(6)

        self.horizontalLayout_203.addWidget(self.station3_io_part_flip_open)

        self.station3_io_part_flip_open_state = QLabel(self.groupBox_46)
        self.station3_io_part_flip_open_state.setObjectName(u"station3_io_part_flip_open_state")
        self.station3_io_part_flip_open_state.setFont(font2)
        self.station3_io_part_flip_open_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_203.addWidget(self.station3_io_part_flip_open_state)


        self.horizontalLayout_202.addLayout(self.horizontalLayout_203)

        self.horizontalLayout_204 = QHBoxLayout()
        self.horizontalLayout_204.setSpacing(10)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(5, 5, 5, 5)
        self.label_205 = QLabel(self.groupBox_46)
        self.label_205.setObjectName(u"label_205")
        sizePolicy.setHeightForWidth(self.label_205.sizePolicy().hasHeightForWidth())
        self.label_205.setSizePolicy(sizePolicy)

        self.horizontalLayout_204.addWidget(self.label_205)

        self.station3_io_part_flip_closed = QSpinBox(self.groupBox_46)
        self.station3_io_part_flip_closed.setObjectName(u"station3_io_part_flip_closed")
        sizePolicy1.setHeightForWidth(self.station3_io_part_flip_closed.sizePolicy().hasHeightForWidth())
        self.station3_io_part_flip_closed.setSizePolicy(sizePolicy1)
        self.station3_io_part_flip_closed.setMinimumSize(QSize(50, 0))
        self.station3_io_part_flip_closed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_part_flip_closed.setMinimum(1)
        self.station3_io_part_flip_closed.setMaximum(16)
        self.station3_io_part_flip_closed.setValue(6)

        self.horizontalLayout_204.addWidget(self.station3_io_part_flip_closed)

        self.station3_io_part_flip_closed_state = QLabel(self.groupBox_46)
        self.station3_io_part_flip_closed_state.setObjectName(u"station3_io_part_flip_closed_state")
        self.station3_io_part_flip_closed_state.setFont(font2)
        self.station3_io_part_flip_closed_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_204.addWidget(self.station3_io_part_flip_closed_state)


        self.horizontalLayout_202.addLayout(self.horizontalLayout_204)


        self.verticalLayout_44.addLayout(self.horizontalLayout_202)


        self.verticalLayout_24.addWidget(self.groupBox_46)

        self.groupBox_54 = QGroupBox(self.groupBox_20)
        self.groupBox_54.setObjectName(u"groupBox_54")
        self.groupBox_54.setMinimumSize(QSize(0, 80))
        self.verticalLayout_60 = QVBoxLayout(self.groupBox_54)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.horizontalLayout_223 = QHBoxLayout()
        self.horizontalLayout_223.setSpacing(40)
        self.horizontalLayout_223.setObjectName(u"horizontalLayout_223")
        self.horizontalLayout_224 = QHBoxLayout()
        self.horizontalLayout_224.setSpacing(10)
        self.horizontalLayout_224.setObjectName(u"horizontalLayout_224")
        self.horizontalLayout_224.setContentsMargins(5, 5, 5, 5)
        self.label_218 = QLabel(self.groupBox_54)
        self.label_218.setObjectName(u"label_218")
        sizePolicy.setHeightForWidth(self.label_218.sizePolicy().hasHeightForWidth())
        self.label_218.setSizePolicy(sizePolicy)
        self.label_218.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_224.addWidget(self.label_218)

        self.station3_io_laser_sensor_left_handle = QSpinBox(self.groupBox_54)
        self.station3_io_laser_sensor_left_handle.setObjectName(u"station3_io_laser_sensor_left_handle")
        sizePolicy1.setHeightForWidth(self.station3_io_laser_sensor_left_handle.sizePolicy().hasHeightForWidth())
        self.station3_io_laser_sensor_left_handle.setSizePolicy(sizePolicy1)
        self.station3_io_laser_sensor_left_handle.setMinimumSize(QSize(50, 0))
        self.station3_io_laser_sensor_left_handle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_laser_sensor_left_handle.setMinimum(1)
        self.station3_io_laser_sensor_left_handle.setMaximum(16)
        self.station3_io_laser_sensor_left_handle.setValue(6)

        self.horizontalLayout_224.addWidget(self.station3_io_laser_sensor_left_handle)

        self.station3_io_laser_sensor_left_handle_state = QLabel(self.groupBox_54)
        self.station3_io_laser_sensor_left_handle_state.setObjectName(u"station3_io_laser_sensor_left_handle_state")
        self.station3_io_laser_sensor_left_handle_state.setFont(font2)
        self.station3_io_laser_sensor_left_handle_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_224.addWidget(self.station3_io_laser_sensor_left_handle_state)


        self.horizontalLayout_223.addLayout(self.horizontalLayout_224)

        self.horizontalLayout_225 = QHBoxLayout()
        self.horizontalLayout_225.setSpacing(10)
        self.horizontalLayout_225.setObjectName(u"horizontalLayout_225")
        self.horizontalLayout_225.setContentsMargins(5, 5, 5, 5)
        self.label_219 = QLabel(self.groupBox_54)
        self.label_219.setObjectName(u"label_219")
        sizePolicy.setHeightForWidth(self.label_219.sizePolicy().hasHeightForWidth())
        self.label_219.setSizePolicy(sizePolicy)

        self.horizontalLayout_225.addWidget(self.label_219)

        self.station3_io_laser_sensor_dial = QSpinBox(self.groupBox_54)
        self.station3_io_laser_sensor_dial.setObjectName(u"station3_io_laser_sensor_dial")
        sizePolicy1.setHeightForWidth(self.station3_io_laser_sensor_dial.sizePolicy().hasHeightForWidth())
        self.station3_io_laser_sensor_dial.setSizePolicy(sizePolicy1)
        self.station3_io_laser_sensor_dial.setMinimumSize(QSize(50, 0))
        self.station3_io_laser_sensor_dial.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_io_laser_sensor_dial.setMinimum(1)
        self.station3_io_laser_sensor_dial.setMaximum(16)
        self.station3_io_laser_sensor_dial.setValue(6)

        self.horizontalLayout_225.addWidget(self.station3_io_laser_sensor_dial)

        self.station3_io_laser_sensor_dial_state = QLabel(self.groupBox_54)
        self.station3_io_laser_sensor_dial_state.setObjectName(u"station3_io_laser_sensor_dial_state")
        self.station3_io_laser_sensor_dial_state.setFont(font2)
        self.station3_io_laser_sensor_dial_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_225.addWidget(self.station3_io_laser_sensor_dial_state)


        self.horizontalLayout_223.addLayout(self.horizontalLayout_225)


        self.verticalLayout_60.addLayout(self.horizontalLayout_223)


        self.verticalLayout_24.addWidget(self.groupBox_54)


        self.horizontalLayout_89.addWidget(self.groupBox_20)

        self.group_valve_3 = QGroupBox(self.tab_station3)
        self.group_valve_3.setObjectName(u"group_valve_3")
        self.verticalLayout_21 = QVBoxLayout(self.group_valve_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_23 = QGroupBox(self.group_valve_3)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(0, 120))
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setSpacing(40)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setSpacing(10)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.label_146 = QLabel(self.groupBox_23)
        self.label_146.setObjectName(u"label_146")
        sizePolicy.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy)
        self.label_146.setMinimumSize(QSize(120, 0))
        self.label_146.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_104.addWidget(self.label_146)

        self.station3_valve_lift_locate_up_5 = QSpinBox(self.groupBox_23)
        self.station3_valve_lift_locate_up_5.setObjectName(u"station3_valve_lift_locate_up_5")
        sizePolicy1.setHeightForWidth(self.station3_valve_lift_locate_up_5.sizePolicy().hasHeightForWidth())
        self.station3_valve_lift_locate_up_5.setSizePolicy(sizePolicy1)
        self.station3_valve_lift_locate_up_5.setMinimumSize(QSize(50, 0))
        self.station3_valve_lift_locate_up_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_lift_locate_up_5.setMinimum(1)
        self.station3_valve_lift_locate_up_5.setMaximum(16)
        self.station3_valve_lift_locate_up_5.setValue(6)

        self.horizontalLayout_104.addWidget(self.station3_valve_lift_locate_up_5)

        self.station3_valve_lift_locate_up_5_state = QLabel(self.groupBox_23)
        self.station3_valve_lift_locate_up_5_state.setObjectName(u"station3_valve_lift_locate_up_5_state")
        self.station3_valve_lift_locate_up_5_state.setFont(font2)
        self.station3_valve_lift_locate_up_5_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_104.addWidget(self.station3_valve_lift_locate_up_5_state)

        self.station3_valve_lift_locate_up_5_btn = QToolButton(self.groupBox_23)
        self.station3_valve_lift_locate_up_5_btn.setObjectName(u"station3_valve_lift_locate_up_5_btn")
        self.station3_valve_lift_locate_up_5_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_104.addWidget(self.station3_valve_lift_locate_up_5_btn)


        self.horizontalLayout_96.addLayout(self.horizontalLayout_104)

        self.widget_4 = QWidget(self.groupBox_23)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_96.addWidget(self.widget_4)


        self.verticalLayout_25.addLayout(self.horizontalLayout_96)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setSpacing(40)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setSpacing(10)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_147 = QLabel(self.groupBox_23)
        self.label_147.setObjectName(u"label_147")
        sizePolicy.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy)
        self.label_147.setMinimumSize(QSize(120, 0))
        self.label_147.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_106.addWidget(self.label_147)

        self.station3_valve_lift_locate_pre_5 = QSpinBox(self.groupBox_23)
        self.station3_valve_lift_locate_pre_5.setObjectName(u"station3_valve_lift_locate_pre_5")
        sizePolicy1.setHeightForWidth(self.station3_valve_lift_locate_pre_5.sizePolicy().hasHeightForWidth())
        self.station3_valve_lift_locate_pre_5.setSizePolicy(sizePolicy1)
        self.station3_valve_lift_locate_pre_5.setMinimumSize(QSize(50, 0))
        self.station3_valve_lift_locate_pre_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_lift_locate_pre_5.setMinimum(1)
        self.station3_valve_lift_locate_pre_5.setMaximum(16)
        self.station3_valve_lift_locate_pre_5.setValue(6)

        self.horizontalLayout_106.addWidget(self.station3_valve_lift_locate_pre_5)

        self.station3_valve_lift_locate_pre_5_state = QLabel(self.groupBox_23)
        self.station3_valve_lift_locate_pre_5_state.setObjectName(u"station3_valve_lift_locate_pre_5_state")
        self.station3_valve_lift_locate_pre_5_state.setFont(font2)
        self.station3_valve_lift_locate_pre_5_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_106.addWidget(self.station3_valve_lift_locate_pre_5_state)

        self.station3_valve_lift_locate_pre_5_btn = QToolButton(self.groupBox_23)
        self.station3_valve_lift_locate_pre_5_btn.setObjectName(u"station3_valve_lift_locate_pre_5_btn")
        self.station3_valve_lift_locate_pre_5_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_106.addWidget(self.station3_valve_lift_locate_pre_5_btn)


        self.horizontalLayout_105.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setSpacing(10)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_148 = QLabel(self.groupBox_23)
        self.label_148.setObjectName(u"label_148")
        sizePolicy.setHeightForWidth(self.label_148.sizePolicy().hasHeightForWidth())
        self.label_148.setSizePolicy(sizePolicy)
        self.label_148.setMinimumSize(QSize(120, 0))
        self.label_148.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_107.addWidget(self.label_148)

        self.station3_valve_lift_locate_main_5 = QSpinBox(self.groupBox_23)
        self.station3_valve_lift_locate_main_5.setObjectName(u"station3_valve_lift_locate_main_5")
        sizePolicy1.setHeightForWidth(self.station3_valve_lift_locate_main_5.sizePolicy().hasHeightForWidth())
        self.station3_valve_lift_locate_main_5.setSizePolicy(sizePolicy1)
        self.station3_valve_lift_locate_main_5.setMinimumSize(QSize(50, 0))
        self.station3_valve_lift_locate_main_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_lift_locate_main_5.setMinimum(1)
        self.station3_valve_lift_locate_main_5.setMaximum(16)
        self.station3_valve_lift_locate_main_5.setValue(6)

        self.horizontalLayout_107.addWidget(self.station3_valve_lift_locate_main_5)

        self.station3_valve_lift_locate_main_5_state = QLabel(self.groupBox_23)
        self.station3_valve_lift_locate_main_5_state.setObjectName(u"station3_valve_lift_locate_main_5_state")
        self.station3_valve_lift_locate_main_5_state.setFont(font2)
        self.station3_valve_lift_locate_main_5_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_107.addWidget(self.station3_valve_lift_locate_main_5_state)

        self.station3_valve_lift_locate_main_5_btn = QToolButton(self.groupBox_23)
        self.station3_valve_lift_locate_main_5_btn.setObjectName(u"station3_valve_lift_locate_main_5_btn")
        self.station3_valve_lift_locate_main_5_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_107.addWidget(self.station3_valve_lift_locate_main_5_btn)


        self.horizontalLayout_105.addLayout(self.horizontalLayout_107)


        self.verticalLayout_25.addLayout(self.horizontalLayout_105)


        self.verticalLayout_21.addWidget(self.groupBox_23)

        self.groupBox_27 = QGroupBox(self.group_valve_3)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setMinimumSize(QSize(0, 120))
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_27)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setSpacing(40)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setSpacing(10)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.label_153 = QLabel(self.groupBox_27)
        self.label_153.setObjectName(u"label_153")
        sizePolicy.setHeightForWidth(self.label_153.sizePolicy().hasHeightForWidth())
        self.label_153.setSizePolicy(sizePolicy)
        self.label_153.setMinimumSize(QSize(120, 0))
        self.label_153.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_123.addWidget(self.label_153)

        self.station3_valve_lift_locate_up_7 = QSpinBox(self.groupBox_27)
        self.station3_valve_lift_locate_up_7.setObjectName(u"station3_valve_lift_locate_up_7")
        sizePolicy1.setHeightForWidth(self.station3_valve_lift_locate_up_7.sizePolicy().hasHeightForWidth())
        self.station3_valve_lift_locate_up_7.setSizePolicy(sizePolicy1)
        self.station3_valve_lift_locate_up_7.setMinimumSize(QSize(50, 0))
        self.station3_valve_lift_locate_up_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_lift_locate_up_7.setMinimum(1)
        self.station3_valve_lift_locate_up_7.setMaximum(16)
        self.station3_valve_lift_locate_up_7.setValue(6)

        self.horizontalLayout_123.addWidget(self.station3_valve_lift_locate_up_7)

        self.station3_valve_lift_locate_up_7_state = QLabel(self.groupBox_27)
        self.station3_valve_lift_locate_up_7_state.setObjectName(u"station3_valve_lift_locate_up_7_state")
        self.station3_valve_lift_locate_up_7_state.setFont(font2)
        self.station3_valve_lift_locate_up_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_123.addWidget(self.station3_valve_lift_locate_up_7_state)

        self.station3_valve_lift_locate_up_7_btn = QToolButton(self.groupBox_27)
        self.station3_valve_lift_locate_up_7_btn.setObjectName(u"station3_valve_lift_locate_up_7_btn")
        self.station3_valve_lift_locate_up_7_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_123.addWidget(self.station3_valve_lift_locate_up_7_btn)


        self.horizontalLayout_122.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setSpacing(10)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_159 = QLabel(self.groupBox_27)
        self.label_159.setObjectName(u"label_159")
        sizePolicy.setHeightForWidth(self.label_159.sizePolicy().hasHeightForWidth())
        self.label_159.setSizePolicy(sizePolicy)
        self.label_159.setMinimumSize(QSize(120, 0))
        self.label_159.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_136.addWidget(self.label_159)

        self.station3_valve_lift_locate_final_assembly_test_air_7 = QSpinBox(self.groupBox_27)
        self.station3_valve_lift_locate_final_assembly_test_air_7.setObjectName(u"station3_valve_lift_locate_final_assembly_test_air_7")
        sizePolicy1.setHeightForWidth(self.station3_valve_lift_locate_final_assembly_test_air_7.sizePolicy().hasHeightForWidth())
        self.station3_valve_lift_locate_final_assembly_test_air_7.setSizePolicy(sizePolicy1)
        self.station3_valve_lift_locate_final_assembly_test_air_7.setMinimumSize(QSize(50, 0))
        self.station3_valve_lift_locate_final_assembly_test_air_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_lift_locate_final_assembly_test_air_7.setMinimum(1)
        self.station3_valve_lift_locate_final_assembly_test_air_7.setMaximum(16)
        self.station3_valve_lift_locate_final_assembly_test_air_7.setValue(6)

        self.horizontalLayout_136.addWidget(self.station3_valve_lift_locate_final_assembly_test_air_7)

        self.station3_valve_lift_locate_final_assembly_test_air_7_state = QLabel(self.groupBox_27)
        self.station3_valve_lift_locate_final_assembly_test_air_7_state.setObjectName(u"station3_valve_lift_locate_final_assembly_test_air_7_state")
        self.station3_valve_lift_locate_final_assembly_test_air_7_state.setFont(font2)
        self.station3_valve_lift_locate_final_assembly_test_air_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_136.addWidget(self.station3_valve_lift_locate_final_assembly_test_air_7_state)

        self.station3_valve_lift_locate_final_assembly_test_air_7_btn = QToolButton(self.groupBox_27)
        self.station3_valve_lift_locate_final_assembly_test_air_7_btn.setObjectName(u"station3_valve_lift_locate_final_assembly_test_air_7_btn")
        self.station3_valve_lift_locate_final_assembly_test_air_7_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_136.addWidget(self.station3_valve_lift_locate_final_assembly_test_air_7_btn)


        self.horizontalLayout_122.addLayout(self.horizontalLayout_136)


        self.verticalLayout_30.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setSpacing(40)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setSpacing(10)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_156 = QLabel(self.groupBox_27)
        self.label_156.setObjectName(u"label_156")
        sizePolicy.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy)
        self.label_156.setMinimumSize(QSize(120, 0))
        self.label_156.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_125.addWidget(self.label_156)

        self.station3_valve_lift_locate_pre_7 = QSpinBox(self.groupBox_27)
        self.station3_valve_lift_locate_pre_7.setObjectName(u"station3_valve_lift_locate_pre_7")
        sizePolicy1.setHeightForWidth(self.station3_valve_lift_locate_pre_7.sizePolicy().hasHeightForWidth())
        self.station3_valve_lift_locate_pre_7.setSizePolicy(sizePolicy1)
        self.station3_valve_lift_locate_pre_7.setMinimumSize(QSize(50, 0))
        self.station3_valve_lift_locate_pre_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_lift_locate_pre_7.setMinimum(1)
        self.station3_valve_lift_locate_pre_7.setMaximum(16)
        self.station3_valve_lift_locate_pre_7.setValue(6)

        self.horizontalLayout_125.addWidget(self.station3_valve_lift_locate_pre_7)

        self.station3_valve_lift_locate_pre_7_state = QLabel(self.groupBox_27)
        self.station3_valve_lift_locate_pre_7_state.setObjectName(u"station3_valve_lift_locate_pre_7_state")
        self.station3_valve_lift_locate_pre_7_state.setFont(font2)
        self.station3_valve_lift_locate_pre_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_125.addWidget(self.station3_valve_lift_locate_pre_7_state)

        self.station3_valve_lift_locate_pre_7_btn = QToolButton(self.groupBox_27)
        self.station3_valve_lift_locate_pre_7_btn.setObjectName(u"station3_valve_lift_locate_pre_7_btn")
        self.station3_valve_lift_locate_pre_7_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_125.addWidget(self.station3_valve_lift_locate_pre_7_btn)


        self.horizontalLayout_124.addLayout(self.horizontalLayout_125)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setSpacing(10)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_157 = QLabel(self.groupBox_27)
        self.label_157.setObjectName(u"label_157")
        sizePolicy.setHeightForWidth(self.label_157.sizePolicy().hasHeightForWidth())
        self.label_157.setSizePolicy(sizePolicy)
        self.label_157.setMinimumSize(QSize(120, 0))
        self.label_157.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_126.addWidget(self.label_157)

        self.station3_valve_lift_locate_main_7 = QSpinBox(self.groupBox_27)
        self.station3_valve_lift_locate_main_7.setObjectName(u"station3_valve_lift_locate_main_7")
        sizePolicy1.setHeightForWidth(self.station3_valve_lift_locate_main_7.sizePolicy().hasHeightForWidth())
        self.station3_valve_lift_locate_main_7.setSizePolicy(sizePolicy1)
        self.station3_valve_lift_locate_main_7.setMinimumSize(QSize(50, 0))
        self.station3_valve_lift_locate_main_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_lift_locate_main_7.setMinimum(1)
        self.station3_valve_lift_locate_main_7.setMaximum(16)
        self.station3_valve_lift_locate_main_7.setValue(6)

        self.horizontalLayout_126.addWidget(self.station3_valve_lift_locate_main_7)

        self.station3_valve_lift_locate_main_7_state = QLabel(self.groupBox_27)
        self.station3_valve_lift_locate_main_7_state.setObjectName(u"station3_valve_lift_locate_main_7_state")
        self.station3_valve_lift_locate_main_7_state.setFont(font2)
        self.station3_valve_lift_locate_main_7_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_126.addWidget(self.station3_valve_lift_locate_main_7_state)

        self.station3_valve_lift_locate_main_7_btn = QToolButton(self.groupBox_27)
        self.station3_valve_lift_locate_main_7_btn.setObjectName(u"station3_valve_lift_locate_main_7_btn")
        self.station3_valve_lift_locate_main_7_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_126.addWidget(self.station3_valve_lift_locate_main_7_btn)


        self.horizontalLayout_124.addLayout(self.horizontalLayout_126)


        self.verticalLayout_30.addLayout(self.horizontalLayout_124)


        self.verticalLayout_21.addWidget(self.groupBox_27)

        self.groupBox_47 = QGroupBox(self.group_valve_3)
        self.groupBox_47.setObjectName(u"groupBox_47")
        self.groupBox_47.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_205 = QHBoxLayout(self.groupBox_47)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.label_206 = QLabel(self.groupBox_47)
        self.label_206.setObjectName(u"label_206")
        sizePolicy.setHeightForWidth(self.label_206.sizePolicy().hasHeightForWidth())
        self.label_206.setSizePolicy(sizePolicy)
        self.label_206.setMinimumSize(QSize(100, 0))
        self.label_206.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_205.addWidget(self.label_206)

        self.station3_valve_flip_nest_gripper_open = QSpinBox(self.groupBox_47)
        self.station3_valve_flip_nest_gripper_open.setObjectName(u"station3_valve_flip_nest_gripper_open")
        sizePolicy1.setHeightForWidth(self.station3_valve_flip_nest_gripper_open.sizePolicy().hasHeightForWidth())
        self.station3_valve_flip_nest_gripper_open.setSizePolicy(sizePolicy1)
        self.station3_valve_flip_nest_gripper_open.setMinimumSize(QSize(50, 0))
        self.station3_valve_flip_nest_gripper_open.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_valve_flip_nest_gripper_open.setMinimum(1)
        self.station3_valve_flip_nest_gripper_open.setMaximum(16)
        self.station3_valve_flip_nest_gripper_open.setValue(6)

        self.horizontalLayout_205.addWidget(self.station3_valve_flip_nest_gripper_open)

        self.station3_valve_flip_nest_gripper_open_state = QLabel(self.groupBox_47)
        self.station3_valve_flip_nest_gripper_open_state.setObjectName(u"station3_valve_flip_nest_gripper_open_state")
        self.station3_valve_flip_nest_gripper_open_state.setFont(font2)
        self.station3_valve_flip_nest_gripper_open_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_205.addWidget(self.station3_valve_flip_nest_gripper_open_state)

        self.station3_valve_flip_nest_gripper_open_btn = QToolButton(self.groupBox_47)
        self.station3_valve_flip_nest_gripper_open_btn.setObjectName(u"station3_valve_flip_nest_gripper_open_btn")
        self.station3_valve_flip_nest_gripper_open_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_205.addWidget(self.station3_valve_flip_nest_gripper_open_btn)

        self.horizontalSpacer_7 = QSpacerItem(297, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_205.addItem(self.horizontalSpacer_7)


        self.verticalLayout_21.addWidget(self.groupBox_47)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_89.addWidget(self.group_valve_3)


        self.verticalLayout_54.addLayout(self.horizontalLayout_89)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.groupBox_10 = QGroupBox(self.tab_station3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_31.setSpacing(20)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setSpacing(40)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setSpacing(10)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(5, 5, 5, 5)
        self.label_154 = QLabel(self.groupBox_10)
        self.label_154.setObjectName(u"label_154")
        sizePolicy.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy)

        self.horizontalLayout_129.addWidget(self.label_154)

        self.station3_test_duration = QSpinBox(self.groupBox_10)
        self.station3_test_duration.setObjectName(u"station3_test_duration")
        sizePolicy1.setHeightForWidth(self.station3_test_duration.sizePolicy().hasHeightForWidth())
        self.station3_test_duration.setSizePolicy(sizePolicy1)
        self.station3_test_duration.setMinimumSize(QSize(50, 0))
        self.station3_test_duration.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_test_duration.setMinimum(0)
        self.station3_test_duration.setMaximum(100)
        self.station3_test_duration.setValue(6)

        self.horizontalLayout_129.addWidget(self.station3_test_duration)


        self.horizontalLayout_133.addLayout(self.horizontalLayout_129)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setSpacing(10)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(5, 5, 5, 5)
        self.label_155 = QLabel(self.groupBox_10)
        self.label_155.setObjectName(u"label_155")
        sizePolicy.setHeightForWidth(self.label_155.sizePolicy().hasHeightForWidth())
        self.label_155.setSizePolicy(sizePolicy)

        self.horizontalLayout_130.addWidget(self.label_155)

        self.station3_test_startup_delay = QSpinBox(self.groupBox_10)
        self.station3_test_startup_delay.setObjectName(u"station3_test_startup_delay")
        sizePolicy1.setHeightForWidth(self.station3_test_startup_delay.sizePolicy().hasHeightForWidth())
        self.station3_test_startup_delay.setSizePolicy(sizePolicy1)
        self.station3_test_startup_delay.setMinimumSize(QSize(50, 0))
        self.station3_test_startup_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_test_startup_delay.setMinimum(0)
        self.station3_test_startup_delay.setMaximum(100)
        self.station3_test_startup_delay.setValue(6)

        self.horizontalLayout_130.addWidget(self.station3_test_startup_delay)


        self.horizontalLayout_133.addLayout(self.horizontalLayout_130)


        self.verticalLayout_31.addLayout(self.horizontalLayout_133)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setSpacing(40)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setSpacing(10)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(5, 5, 5, 5)
        self.label_177 = QLabel(self.groupBox_10)
        self.label_177.setObjectName(u"label_177")
        sizePolicy.setHeightForWidth(self.label_177.sizePolicy().hasHeightForWidth())
        self.label_177.setSizePolicy(sizePolicy)

        self.horizontalLayout_131.addWidget(self.label_177)

        self.station3_test_low_pass = QSpinBox(self.groupBox_10)
        self.station3_test_low_pass.setObjectName(u"station3_test_low_pass")
        sizePolicy1.setHeightForWidth(self.station3_test_low_pass.sizePolicy().hasHeightForWidth())
        self.station3_test_low_pass.setSizePolicy(sizePolicy1)
        self.station3_test_low_pass.setMinimumSize(QSize(50, 0))
        self.station3_test_low_pass.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_test_low_pass.setMinimum(1)
        self.station3_test_low_pass.setMaximum(100)
        self.station3_test_low_pass.setValue(6)

        self.horizontalLayout_131.addWidget(self.station3_test_low_pass)


        self.horizontalLayout_134.addLayout(self.horizontalLayout_131)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setSpacing(10)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(5, 5, 5, 5)
        self.label_178 = QLabel(self.groupBox_10)
        self.label_178.setObjectName(u"label_178")
        sizePolicy.setHeightForWidth(self.label_178.sizePolicy().hasHeightForWidth())
        self.label_178.setSizePolicy(sizePolicy)

        self.horizontalLayout_132.addWidget(self.label_178)

        self.station3_test_high_pass = QSpinBox(self.groupBox_10)
        self.station3_test_high_pass.setObjectName(u"station3_test_high_pass")
        sizePolicy1.setHeightForWidth(self.station3_test_high_pass.sizePolicy().hasHeightForWidth())
        self.station3_test_high_pass.setSizePolicy(sizePolicy1)
        self.station3_test_high_pass.setMinimumSize(QSize(50, 0))
        self.station3_test_high_pass.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station3_test_high_pass.setMinimum(1)
        self.station3_test_high_pass.setMaximum(100)
        self.station3_test_high_pass.setValue(10)

        self.horizontalLayout_132.addWidget(self.station3_test_high_pass)


        self.horizontalLayout_134.addLayout(self.horizontalLayout_132)


        self.verticalLayout_31.addLayout(self.horizontalLayout_134)

        self.btn_test_final_assembly = QPushButton(self.groupBox_10)
        self.btn_test_final_assembly.setObjectName(u"btn_test_final_assembly")
        self.btn_test_final_assembly.setMinimumSize(QSize(0, 40))

        self.verticalLayout_31.addWidget(self.btn_test_final_assembly)


        self.horizontalLayout_135.addWidget(self.groupBox_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_135.addItem(self.horizontalSpacer_4)


        self.verticalLayout_54.addLayout(self.horizontalLayout_135)

        self.tabWidget.addTab(self.tab_station3, "")
        self.tab_station4 = QWidget()
        self.tab_station4.setObjectName(u"tab_station4")
        self.verticalLayout_43 = QVBoxLayout(self.tab_station4)
        self.verticalLayout_43.setSpacing(10)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setSpacing(30)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.groupBox_28 = QGroupBox(self.tab_station4)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setMinimumSize(QSize(0, 0))
        self.verticalLayout_35 = QVBoxLayout(self.groupBox_28)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setSpacing(20)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.label_46 = QLabel(self.groupBox_28)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_140.addWidget(self.label_46)

        self.station4_robot = QLineEdit(self.groupBox_28)
        self.station4_robot.setObjectName(u"station4_robot")
        self.station4_robot.setMaximumSize(QSize(150, 16777215))
        self.station4_robot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_140.addWidget(self.station4_robot)

        self.btn_station4_robot_test = QPushButton(self.groupBox_28)
        self.btn_station4_robot_test.setObjectName(u"btn_station4_robot_test")
        self.btn_station4_robot_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_140.addWidget(self.btn_station4_robot_test)


        self.verticalLayout_35.addLayout(self.horizontalLayout_140)

        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setSpacing(20)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.label_47 = QLabel(self.groupBox_28)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_141.addWidget(self.label_47)

        self.station4_cognex = QLineEdit(self.groupBox_28)
        self.station4_cognex.setObjectName(u"station4_cognex")
        self.station4_cognex.setMaximumSize(QSize(150, 16777215))
        self.station4_cognex.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_141.addWidget(self.station4_cognex)

        self.btn_station4_cognex_test = QPushButton(self.groupBox_28)
        self.btn_station4_cognex_test.setObjectName(u"btn_station4_cognex_test")
        self.btn_station4_cognex_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_141.addWidget(self.btn_station4_cognex_test)


        self.verticalLayout_35.addLayout(self.horizontalLayout_141)

        self.horizontalLayout_189 = QHBoxLayout()
        self.horizontalLayout_189.setSpacing(20)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.label_57 = QLabel(self.groupBox_28)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_189.addWidget(self.label_57)

        self.station4_barcode_6 = QLineEdit(self.groupBox_28)
        self.station4_barcode_6.setObjectName(u"station4_barcode_6")
        self.station4_barcode_6.setMaximumSize(QSize(150, 16777215))
        self.station4_barcode_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.station4_barcode_6)

        self.btn_station4_barcode_6_test = QPushButton(self.groupBox_28)
        self.btn_station4_barcode_6_test.setObjectName(u"btn_station4_barcode_6_test")
        self.btn_station4_barcode_6_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_189.addWidget(self.btn_station4_barcode_6_test)


        self.verticalLayout_35.addLayout(self.horizontalLayout_189)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setSpacing(20)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.label_48 = QLabel(self.groupBox_28)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_143.addWidget(self.label_48)

        self.station4_wago = QLineEdit(self.groupBox_28)
        self.station4_wago.setObjectName(u"station4_wago")
        self.station4_wago.setMaximumSize(QSize(150, 16777215))
        self.station4_wago.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_143.addWidget(self.station4_wago)

        self.btn_station4_wago_test = QPushButton(self.groupBox_28)
        self.btn_station4_wago_test.setObjectName(u"btn_station4_wago_test")
        self.btn_station4_wago_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_143.addWidget(self.btn_station4_wago_test)


        self.verticalLayout_35.addLayout(self.horizontalLayout_143)


        self.horizontalLayout_139.addWidget(self.groupBox_28)

        self.groupBox_29 = QGroupBox(self.tab_station4)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_29)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, 30, -1, 30)
        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setSpacing(30)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_49 = QLabel(self.groupBox_29)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_144.addWidget(self.label_49)

        self.station4_feeders_right_handle = QLineEdit(self.groupBox_29)
        self.station4_feeders_right_handle.setObjectName(u"station4_feeders_right_handle")
        self.station4_feeders_right_handle.setMaximumSize(QSize(150, 16777215))
        self.station4_feeders_right_handle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_144.addWidget(self.station4_feeders_right_handle)

        self.btn_station4_feeders_right_handle_test = QPushButton(self.groupBox_29)
        self.btn_station4_feeders_right_handle_test.setObjectName(u"btn_station4_feeders_right_handle_test")
        self.btn_station4_feeders_right_handle_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_144.addWidget(self.btn_station4_feeders_right_handle_test)


        self.verticalLayout_36.addLayout(self.horizontalLayout_144)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setSpacing(30)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.label_50 = QLabel(self.groupBox_29)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_145.addWidget(self.label_50)

        self.station4_agitator = QLineEdit(self.groupBox_29)
        self.station4_agitator.setObjectName(u"station4_agitator")
        self.station4_agitator.setMaximumSize(QSize(150, 16777215))
        self.station4_agitator.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_145.addWidget(self.station4_agitator)

        self.btn_station4_agitator_test = QPushButton(self.groupBox_29)
        self.btn_station4_agitator_test.setObjectName(u"btn_station4_agitator_test")
        self.btn_station4_agitator_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_145.addWidget(self.btn_station4_agitator_test)


        self.verticalLayout_36.addLayout(self.horizontalLayout_145)


        self.horizontalLayout_139.addWidget(self.groupBox_29)


        self.verticalLayout_43.addLayout(self.horizontalLayout_139)

        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setSpacing(30)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.groupBox_30 = QGroupBox(self.tab_station4)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setMinimumSize(QSize(0, 0))
        self.verticalLayout_56 = QVBoxLayout(self.groupBox_30)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.groupBox_31 = QGroupBox(self.groupBox_30)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setMinimumSize(QSize(0, 120))
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_31)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setSpacing(40)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setSpacing(10)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(5, 5, 5, 5)
        self.label_160 = QLabel(self.groupBox_31)
        self.label_160.setObjectName(u"label_160")
        sizePolicy.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy)

        self.horizontalLayout_151.addWidget(self.label_160)

        self.station4_io_lift_locate_extended_6 = QSpinBox(self.groupBox_31)
        self.station4_io_lift_locate_extended_6.setObjectName(u"station4_io_lift_locate_extended_6")
        sizePolicy1.setHeightForWidth(self.station4_io_lift_locate_extended_6.sizePolicy().hasHeightForWidth())
        self.station4_io_lift_locate_extended_6.setSizePolicy(sizePolicy1)
        self.station4_io_lift_locate_extended_6.setMinimumSize(QSize(50, 0))
        self.station4_io_lift_locate_extended_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_lift_locate_extended_6.setMinimum(1)
        self.station4_io_lift_locate_extended_6.setMaximum(16)
        self.station4_io_lift_locate_extended_6.setValue(6)

        self.horizontalLayout_151.addWidget(self.station4_io_lift_locate_extended_6)

        self.station4_io_lift_locate_extended_6_state = QLabel(self.groupBox_31)
        self.station4_io_lift_locate_extended_6_state.setObjectName(u"station4_io_lift_locate_extended_6_state")
        self.station4_io_lift_locate_extended_6_state.setFont(font2)
        self.station4_io_lift_locate_extended_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_151.addWidget(self.station4_io_lift_locate_extended_6_state)


        self.horizontalLayout_150.addLayout(self.horizontalLayout_151)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setSpacing(10)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(5, 5, 5, 5)
        self.label_161 = QLabel(self.groupBox_31)
        self.label_161.setObjectName(u"label_161")
        sizePolicy.setHeightForWidth(self.label_161.sizePolicy().hasHeightForWidth())
        self.label_161.setSizePolicy(sizePolicy)

        self.horizontalLayout_152.addWidget(self.label_161)

        self.station4_io_lift_locate_retracted_6 = QSpinBox(self.groupBox_31)
        self.station4_io_lift_locate_retracted_6.setObjectName(u"station4_io_lift_locate_retracted_6")
        sizePolicy1.setHeightForWidth(self.station4_io_lift_locate_retracted_6.sizePolicy().hasHeightForWidth())
        self.station4_io_lift_locate_retracted_6.setSizePolicy(sizePolicy1)
        self.station4_io_lift_locate_retracted_6.setMinimumSize(QSize(50, 0))
        self.station4_io_lift_locate_retracted_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_lift_locate_retracted_6.setMinimum(1)
        self.station4_io_lift_locate_retracted_6.setMaximum(16)
        self.station4_io_lift_locate_retracted_6.setValue(6)

        self.horizontalLayout_152.addWidget(self.station4_io_lift_locate_retracted_6)

        self.station4_io_lift_locate_retracted_6_state = QLabel(self.groupBox_31)
        self.station4_io_lift_locate_retracted_6_state.setObjectName(u"station4_io_lift_locate_retracted_6_state")
        self.station4_io_lift_locate_retracted_6_state.setFont(font2)
        self.station4_io_lift_locate_retracted_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_152.addWidget(self.station4_io_lift_locate_retracted_6_state)


        self.horizontalLayout_150.addLayout(self.horizontalLayout_152)


        self.verticalLayout_38.addLayout(self.horizontalLayout_150)

        self.horizontalLayout_153 = QHBoxLayout()
        self.horizontalLayout_153.setSpacing(40)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_154 = QHBoxLayout()
        self.horizontalLayout_154.setSpacing(10)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(5, 5, 5, 5)
        self.label_162 = QLabel(self.groupBox_31)
        self.label_162.setObjectName(u"label_162")
        sizePolicy.setHeightForWidth(self.label_162.sizePolicy().hasHeightForWidth())
        self.label_162.setSizePolicy(sizePolicy)

        self.horizontalLayout_154.addWidget(self.label_162)

        self.station4_io_lift_locate_pre_6 = QSpinBox(self.groupBox_31)
        self.station4_io_lift_locate_pre_6.setObjectName(u"station4_io_lift_locate_pre_6")
        sizePolicy1.setHeightForWidth(self.station4_io_lift_locate_pre_6.sizePolicy().hasHeightForWidth())
        self.station4_io_lift_locate_pre_6.setSizePolicy(sizePolicy1)
        self.station4_io_lift_locate_pre_6.setMinimumSize(QSize(50, 0))
        self.station4_io_lift_locate_pre_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_lift_locate_pre_6.setMinimum(1)
        self.station4_io_lift_locate_pre_6.setMaximum(16)
        self.station4_io_lift_locate_pre_6.setValue(6)

        self.horizontalLayout_154.addWidget(self.station4_io_lift_locate_pre_6)

        self.station4_io_lift_locate_pre_6_state = QLabel(self.groupBox_31)
        self.station4_io_lift_locate_pre_6_state.setObjectName(u"station4_io_lift_locate_pre_6_state")
        self.station4_io_lift_locate_pre_6_state.setFont(font2)
        self.station4_io_lift_locate_pre_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_154.addWidget(self.station4_io_lift_locate_pre_6_state)


        self.horizontalLayout_153.addLayout(self.horizontalLayout_154)

        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setSpacing(10)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(5, 5, 5, 5)
        self.label_163 = QLabel(self.groupBox_31)
        self.label_163.setObjectName(u"label_163")
        sizePolicy.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy)

        self.horizontalLayout_155.addWidget(self.label_163)

        self.station4_io_lift_locate_main_6 = QSpinBox(self.groupBox_31)
        self.station4_io_lift_locate_main_6.setObjectName(u"station4_io_lift_locate_main_6")
        sizePolicy1.setHeightForWidth(self.station4_io_lift_locate_main_6.sizePolicy().hasHeightForWidth())
        self.station4_io_lift_locate_main_6.setSizePolicy(sizePolicy1)
        self.station4_io_lift_locate_main_6.setMinimumSize(QSize(50, 0))
        self.station4_io_lift_locate_main_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_lift_locate_main_6.setMinimum(1)
        self.station4_io_lift_locate_main_6.setMaximum(16)
        self.station4_io_lift_locate_main_6.setValue(6)

        self.horizontalLayout_155.addWidget(self.station4_io_lift_locate_main_6)

        self.station4_io_lift_locate_main_6_state = QLabel(self.groupBox_31)
        self.station4_io_lift_locate_main_6_state.setObjectName(u"station4_io_lift_locate_main_6_state")
        self.station4_io_lift_locate_main_6_state.setFont(font2)
        self.station4_io_lift_locate_main_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_155.addWidget(self.station4_io_lift_locate_main_6_state)


        self.horizontalLayout_153.addLayout(self.horizontalLayout_155)


        self.verticalLayout_38.addLayout(self.horizontalLayout_153)


        self.verticalLayout_56.addWidget(self.groupBox_31)

        self.groupBox_32 = QGroupBox(self.groupBox_30)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setMinimumSize(QSize(0, 75))
        self.horizontalLayout_146 = QHBoxLayout(self.groupBox_32)
        self.horizontalLayout_146.setSpacing(30)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setSpacing(10)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(5, 5, 5, 5)
        self.label_164 = QLabel(self.groupBox_32)
        self.label_164.setObjectName(u"label_164")
        sizePolicy.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy)

        self.horizontalLayout_157.addWidget(self.label_164)

        self.station4_io_upper_housing_clamp_open = QSpinBox(self.groupBox_32)
        self.station4_io_upper_housing_clamp_open.setObjectName(u"station4_io_upper_housing_clamp_open")
        sizePolicy1.setHeightForWidth(self.station4_io_upper_housing_clamp_open.sizePolicy().hasHeightForWidth())
        self.station4_io_upper_housing_clamp_open.setSizePolicy(sizePolicy1)
        self.station4_io_upper_housing_clamp_open.setMinimumSize(QSize(50, 24))
        self.station4_io_upper_housing_clamp_open.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_upper_housing_clamp_open.setMinimum(1)
        self.station4_io_upper_housing_clamp_open.setMaximum(16)
        self.station4_io_upper_housing_clamp_open.setValue(6)

        self.horizontalLayout_157.addWidget(self.station4_io_upper_housing_clamp_open)

        self.station4_io_upper_housing_clamp_open_state = QLabel(self.groupBox_32)
        self.station4_io_upper_housing_clamp_open_state.setObjectName(u"station4_io_upper_housing_clamp_open_state")
        self.station4_io_upper_housing_clamp_open_state.setFont(font2)
        self.station4_io_upper_housing_clamp_open_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_157.addWidget(self.station4_io_upper_housing_clamp_open_state)


        self.horizontalLayout_146.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setSpacing(10)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(5, 5, 5, 5)
        self.label_165 = QLabel(self.groupBox_32)
        self.label_165.setObjectName(u"label_165")
        sizePolicy.setHeightForWidth(self.label_165.sizePolicy().hasHeightForWidth())
        self.label_165.setSizePolicy(sizePolicy)

        self.horizontalLayout_158.addWidget(self.label_165)

        self.station4_io_upper_housing_clamp_closed = QSpinBox(self.groupBox_32)
        self.station4_io_upper_housing_clamp_closed.setObjectName(u"station4_io_upper_housing_clamp_closed")
        sizePolicy1.setHeightForWidth(self.station4_io_upper_housing_clamp_closed.sizePolicy().hasHeightForWidth())
        self.station4_io_upper_housing_clamp_closed.setSizePolicy(sizePolicy1)
        self.station4_io_upper_housing_clamp_closed.setMinimumSize(QSize(50, 24))
        self.station4_io_upper_housing_clamp_closed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_upper_housing_clamp_closed.setMinimum(1)
        self.station4_io_upper_housing_clamp_closed.setMaximum(16)
        self.station4_io_upper_housing_clamp_closed.setValue(6)

        self.horizontalLayout_158.addWidget(self.station4_io_upper_housing_clamp_closed)

        self.station4_io_upper_housing_clamp_closed_state = QLabel(self.groupBox_32)
        self.station4_io_upper_housing_clamp_closed_state.setObjectName(u"station4_io_upper_housing_clamp_closed_state")
        self.station4_io_upper_housing_clamp_closed_state.setFont(font2)
        self.station4_io_upper_housing_clamp_closed_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_158.addWidget(self.station4_io_upper_housing_clamp_closed_state)


        self.horizontalLayout_146.addLayout(self.horizontalLayout_158)


        self.verticalLayout_56.addWidget(self.groupBox_32)

        self.groupBox_36 = QGroupBox(self.groupBox_30)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setMinimumSize(QSize(0, 75))
        self.horizontalLayout_147 = QHBoxLayout(self.groupBox_36)
        self.horizontalLayout_147.setSpacing(30)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setSpacing(10)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(5, 5, 5, 5)
        self.label_166 = QLabel(self.groupBox_36)
        self.label_166.setObjectName(u"label_166")
        sizePolicy.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy)

        self.horizontalLayout_159.addWidget(self.label_166)

        self.station4_io_hopper_conveyor_indexing = QSpinBox(self.groupBox_36)
        self.station4_io_hopper_conveyor_indexing.setObjectName(u"station4_io_hopper_conveyor_indexing")
        sizePolicy1.setHeightForWidth(self.station4_io_hopper_conveyor_indexing.sizePolicy().hasHeightForWidth())
        self.station4_io_hopper_conveyor_indexing.setSizePolicy(sizePolicy1)
        self.station4_io_hopper_conveyor_indexing.setMinimumSize(QSize(50, 24))
        self.station4_io_hopper_conveyor_indexing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_hopper_conveyor_indexing.setMinimum(1)
        self.station4_io_hopper_conveyor_indexing.setMaximum(16)
        self.station4_io_hopper_conveyor_indexing.setValue(6)

        self.horizontalLayout_159.addWidget(self.station4_io_hopper_conveyor_indexing)

        self.station4_io_hopper_conveyor_indexing_state = QLabel(self.groupBox_36)
        self.station4_io_hopper_conveyor_indexing_state.setObjectName(u"station4_io_hopper_conveyor_indexing_state")
        self.station4_io_hopper_conveyor_indexing_state.setFont(font2)
        self.station4_io_hopper_conveyor_indexing_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_159.addWidget(self.station4_io_hopper_conveyor_indexing_state)


        self.horizontalLayout_147.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setSpacing(10)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(5, 5, 5, 5)
        self.label_167 = QLabel(self.groupBox_36)
        self.label_167.setObjectName(u"label_167")
        sizePolicy.setHeightForWidth(self.label_167.sizePolicy().hasHeightForWidth())
        self.label_167.setSizePolicy(sizePolicy)

        self.horizontalLayout_160.addWidget(self.label_167)

        self.station4_io_hopper_conveyor_part_detection = QSpinBox(self.groupBox_36)
        self.station4_io_hopper_conveyor_part_detection.setObjectName(u"station4_io_hopper_conveyor_part_detection")
        sizePolicy1.setHeightForWidth(self.station4_io_hopper_conveyor_part_detection.sizePolicy().hasHeightForWidth())
        self.station4_io_hopper_conveyor_part_detection.setSizePolicy(sizePolicy1)
        self.station4_io_hopper_conveyor_part_detection.setMinimumSize(QSize(50, 24))
        self.station4_io_hopper_conveyor_part_detection.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_hopper_conveyor_part_detection.setMinimum(1)
        self.station4_io_hopper_conveyor_part_detection.setMaximum(16)
        self.station4_io_hopper_conveyor_part_detection.setValue(6)

        self.horizontalLayout_160.addWidget(self.station4_io_hopper_conveyor_part_detection)

        self.station4_io_hopper_conveyor_part_detection_state = QLabel(self.groupBox_36)
        self.station4_io_hopper_conveyor_part_detection_state.setObjectName(u"station4_io_hopper_conveyor_part_detection_state")
        self.station4_io_hopper_conveyor_part_detection_state.setFont(font2)
        self.station4_io_hopper_conveyor_part_detection_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_160.addWidget(self.station4_io_hopper_conveyor_part_detection_state)


        self.horizontalLayout_147.addLayout(self.horizontalLayout_160)


        self.verticalLayout_56.addWidget(self.groupBox_36)

        self.groupBox_49 = QGroupBox(self.groupBox_30)
        self.groupBox_49.setObjectName(u"groupBox_49")
        self.groupBox_49.setMinimumSize(QSize(0, 120))
        self.verticalLayout_55 = QVBoxLayout(self.groupBox_49)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.horizontalLayout_207 = QHBoxLayout()
        self.horizontalLayout_207.setSpacing(30)
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.horizontalLayout_208 = QHBoxLayout()
        self.horizontalLayout_208.setSpacing(10)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(5, 5, 5, 5)
        self.label_208 = QLabel(self.groupBox_49)
        self.label_208.setObjectName(u"label_208")
        sizePolicy.setHeightForWidth(self.label_208.sizePolicy().hasHeightForWidth())
        self.label_208.setSizePolicy(sizePolicy)

        self.horizontalLayout_208.addWidget(self.label_208)

        self.station4_io_right_handle_rotator_slide_open = QSpinBox(self.groupBox_49)
        self.station4_io_right_handle_rotator_slide_open.setObjectName(u"station4_io_right_handle_rotator_slide_open")
        sizePolicy1.setHeightForWidth(self.station4_io_right_handle_rotator_slide_open.sizePolicy().hasHeightForWidth())
        self.station4_io_right_handle_rotator_slide_open.setSizePolicy(sizePolicy1)
        self.station4_io_right_handle_rotator_slide_open.setMinimumSize(QSize(50, 25))
        self.station4_io_right_handle_rotator_slide_open.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_right_handle_rotator_slide_open.setMinimum(1)
        self.station4_io_right_handle_rotator_slide_open.setMaximum(16)
        self.station4_io_right_handle_rotator_slide_open.setValue(6)

        self.horizontalLayout_208.addWidget(self.station4_io_right_handle_rotator_slide_open)

        self.station4_io_right_handle_rotator_slide_open_state = QLabel(self.groupBox_49)
        self.station4_io_right_handle_rotator_slide_open_state.setObjectName(u"station4_io_right_handle_rotator_slide_open_state")
        self.station4_io_right_handle_rotator_slide_open_state.setFont(font2)
        self.station4_io_right_handle_rotator_slide_open_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_208.addWidget(self.station4_io_right_handle_rotator_slide_open_state)


        self.horizontalLayout_207.addLayout(self.horizontalLayout_208)

        self.horizontalLayout_209 = QHBoxLayout()
        self.horizontalLayout_209.setSpacing(10)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(5, 5, 5, 5)
        self.label_209 = QLabel(self.groupBox_49)
        self.label_209.setObjectName(u"label_209")
        sizePolicy.setHeightForWidth(self.label_209.sizePolicy().hasHeightForWidth())
        self.label_209.setSizePolicy(sizePolicy)

        self.horizontalLayout_209.addWidget(self.label_209)

        self.station4_io_right_handle_rotator_slide_closed = QSpinBox(self.groupBox_49)
        self.station4_io_right_handle_rotator_slide_closed.setObjectName(u"station4_io_right_handle_rotator_slide_closed")
        sizePolicy1.setHeightForWidth(self.station4_io_right_handle_rotator_slide_closed.sizePolicy().hasHeightForWidth())
        self.station4_io_right_handle_rotator_slide_closed.setSizePolicy(sizePolicy1)
        self.station4_io_right_handle_rotator_slide_closed.setMinimumSize(QSize(50, 25))
        self.station4_io_right_handle_rotator_slide_closed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_right_handle_rotator_slide_closed.setMinimum(1)
        self.station4_io_right_handle_rotator_slide_closed.setMaximum(16)
        self.station4_io_right_handle_rotator_slide_closed.setValue(6)

        self.horizontalLayout_209.addWidget(self.station4_io_right_handle_rotator_slide_closed)

        self.station4_io_right_handle_rotator_slide_closed_state = QLabel(self.groupBox_49)
        self.station4_io_right_handle_rotator_slide_closed_state.setObjectName(u"station4_io_right_handle_rotator_slide_closed_state")
        self.station4_io_right_handle_rotator_slide_closed_state.setFont(font2)
        self.station4_io_right_handle_rotator_slide_closed_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_209.addWidget(self.station4_io_right_handle_rotator_slide_closed_state)


        self.horizontalLayout_207.addLayout(self.horizontalLayout_209)


        self.verticalLayout_55.addLayout(self.horizontalLayout_207)

        self.horizontalLayout_212 = QHBoxLayout()
        self.horizontalLayout_212.setSpacing(30)
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.horizontalLayout_210 = QHBoxLayout()
        self.horizontalLayout_210.setSpacing(10)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(5, 5, 5, 5)
        self.label_210 = QLabel(self.groupBox_49)
        self.label_210.setObjectName(u"label_210")
        sizePolicy.setHeightForWidth(self.label_210.sizePolicy().hasHeightForWidth())
        self.label_210.setSizePolicy(sizePolicy)

        self.horizontalLayout_210.addWidget(self.label_210)

        self.station4_io_right_handle_rotator_place = QSpinBox(self.groupBox_49)
        self.station4_io_right_handle_rotator_place.setObjectName(u"station4_io_right_handle_rotator_place")
        sizePolicy1.setHeightForWidth(self.station4_io_right_handle_rotator_place.sizePolicy().hasHeightForWidth())
        self.station4_io_right_handle_rotator_place.setSizePolicy(sizePolicy1)
        self.station4_io_right_handle_rotator_place.setMinimumSize(QSize(50, 25))
        self.station4_io_right_handle_rotator_place.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_right_handle_rotator_place.setMinimum(1)
        self.station4_io_right_handle_rotator_place.setMaximum(16)
        self.station4_io_right_handle_rotator_place.setValue(6)

        self.horizontalLayout_210.addWidget(self.station4_io_right_handle_rotator_place)

        self.station4_io_right_handle_rotator_place_state = QLabel(self.groupBox_49)
        self.station4_io_right_handle_rotator_place_state.setObjectName(u"station4_io_right_handle_rotator_place_state")
        self.station4_io_right_handle_rotator_place_state.setFont(font2)
        self.station4_io_right_handle_rotator_place_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_210.addWidget(self.station4_io_right_handle_rotator_place_state)


        self.horizontalLayout_212.addLayout(self.horizontalLayout_210)

        self.horizontalLayout_211 = QHBoxLayout()
        self.horizontalLayout_211.setSpacing(10)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(5, 5, 5, 5)
        self.label_211 = QLabel(self.groupBox_49)
        self.label_211.setObjectName(u"label_211")
        sizePolicy.setHeightForWidth(self.label_211.sizePolicy().hasHeightForWidth())
        self.label_211.setSizePolicy(sizePolicy)

        self.horizontalLayout_211.addWidget(self.label_211)

        self.station4_io_right_handle_rotator_pick = QSpinBox(self.groupBox_49)
        self.station4_io_right_handle_rotator_pick.setObjectName(u"station4_io_right_handle_rotator_pick")
        sizePolicy1.setHeightForWidth(self.station4_io_right_handle_rotator_pick.sizePolicy().hasHeightForWidth())
        self.station4_io_right_handle_rotator_pick.setSizePolicy(sizePolicy1)
        self.station4_io_right_handle_rotator_pick.setMinimumSize(QSize(50, 25))
        self.station4_io_right_handle_rotator_pick.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_right_handle_rotator_pick.setMinimum(1)
        self.station4_io_right_handle_rotator_pick.setMaximum(16)
        self.station4_io_right_handle_rotator_pick.setValue(6)

        self.horizontalLayout_211.addWidget(self.station4_io_right_handle_rotator_pick)

        self.station4_io_right_handle_rotator_pick_state = QLabel(self.groupBox_49)
        self.station4_io_right_handle_rotator_pick_state.setObjectName(u"station4_io_right_handle_rotator_pick_state")
        self.station4_io_right_handle_rotator_pick_state.setFont(font2)
        self.station4_io_right_handle_rotator_pick_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_211.addWidget(self.station4_io_right_handle_rotator_pick_state)


        self.horizontalLayout_212.addLayout(self.horizontalLayout_211)


        self.verticalLayout_55.addLayout(self.horizontalLayout_212)


        self.verticalLayout_56.addWidget(self.groupBox_49)

        self.groupBox_48 = QGroupBox(self.groupBox_30)
        self.groupBox_48.setObjectName(u"groupBox_48")
        self.verticalLayout_37 = QVBoxLayout(self.groupBox_48)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_206 = QHBoxLayout()
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.label_207 = QLabel(self.groupBox_48)
        self.label_207.setObjectName(u"label_207")
        sizePolicy.setHeightForWidth(self.label_207.sizePolicy().hasHeightForWidth())
        self.label_207.setSizePolicy(sizePolicy)

        self.horizontalLayout_206.addWidget(self.label_207)

        self.station4_io_robot4_air1_toggle = QSpinBox(self.groupBox_48)
        self.station4_io_robot4_air1_toggle.setObjectName(u"station4_io_robot4_air1_toggle")
        sizePolicy1.setHeightForWidth(self.station4_io_robot4_air1_toggle.sizePolicy().hasHeightForWidth())
        self.station4_io_robot4_air1_toggle.setSizePolicy(sizePolicy1)
        self.station4_io_robot4_air1_toggle.setMinimumSize(QSize(50, 0))
        self.station4_io_robot4_air1_toggle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_io_robot4_air1_toggle.setMinimum(1)
        self.station4_io_robot4_air1_toggle.setMaximum(16)
        self.station4_io_robot4_air1_toggle.setValue(6)

        self.horizontalLayout_206.addWidget(self.station4_io_robot4_air1_toggle)

        self.station4_io_robot4_air1_toggle_state = QLabel(self.groupBox_48)
        self.station4_io_robot4_air1_toggle_state.setObjectName(u"station4_io_robot4_air1_toggle_state")
        self.station4_io_robot4_air1_toggle_state.setFont(font2)
        self.station4_io_robot4_air1_toggle_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_206.addWidget(self.station4_io_robot4_air1_toggle_state)

        self.station4_io_robot4_air1_toggle_btn = QToolButton(self.groupBox_48)
        self.station4_io_robot4_air1_toggle_btn.setObjectName(u"station4_io_robot4_air1_toggle_btn")
        self.station4_io_robot4_air1_toggle_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_206.addWidget(self.station4_io_robot4_air1_toggle_btn)


        self.verticalLayout_37.addLayout(self.horizontalLayout_206)


        self.verticalLayout_56.addWidget(self.groupBox_48)


        self.horizontalLayout_148.addWidget(self.groupBox_30)

        self.group_valve_4 = QGroupBox(self.tab_station4)
        self.group_valve_4.setObjectName(u"group_valve_4")
        self.group_valve_4.setMinimumSize(QSize(0, 0))
        self.verticalLayout_40 = QVBoxLayout(self.group_valve_4)
        self.verticalLayout_40.setSpacing(20)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.groupBox_34 = QGroupBox(self.group_valve_4)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setMinimumSize(QSize(0, 120))
        self.verticalLayout_41 = QVBoxLayout(self.groupBox_34)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setSpacing(40)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setSpacing(10)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.label_169 = QLabel(self.groupBox_34)
        self.label_169.setObjectName(u"label_169")
        sizePolicy.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy)
        self.label_169.setMinimumSize(QSize(134, 0))

        self.horizontalLayout_164.addWidget(self.label_169)

        self.station4_valve_lift_locate_up_6 = QSpinBox(self.groupBox_34)
        self.station4_valve_lift_locate_up_6.setObjectName(u"station4_valve_lift_locate_up_6")
        sizePolicy1.setHeightForWidth(self.station4_valve_lift_locate_up_6.sizePolicy().hasHeightForWidth())
        self.station4_valve_lift_locate_up_6.setSizePolicy(sizePolicy1)
        self.station4_valve_lift_locate_up_6.setMinimumSize(QSize(50, 0))
        self.station4_valve_lift_locate_up_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_valve_lift_locate_up_6.setMinimum(1)
        self.station4_valve_lift_locate_up_6.setMaximum(16)
        self.station4_valve_lift_locate_up_6.setValue(6)

        self.horizontalLayout_164.addWidget(self.station4_valve_lift_locate_up_6)

        self.station4_valve_lift_locate_up_6_state = QLabel(self.groupBox_34)
        self.station4_valve_lift_locate_up_6_state.setObjectName(u"station4_valve_lift_locate_up_6_state")
        self.station4_valve_lift_locate_up_6_state.setFont(font2)
        self.station4_valve_lift_locate_up_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_164.addWidget(self.station4_valve_lift_locate_up_6_state)

        self.station4_valve_lift_locate_up_6_btn = QToolButton(self.groupBox_34)
        self.station4_valve_lift_locate_up_6_btn.setObjectName(u"station4_valve_lift_locate_up_6_btn")
        self.station4_valve_lift_locate_up_6_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_164.addWidget(self.station4_valve_lift_locate_up_6_btn)


        self.horizontalLayout_163.addLayout(self.horizontalLayout_164)

        self.widget_5 = QWidget(self.groupBox_34)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_163.addWidget(self.widget_5)


        self.verticalLayout_41.addLayout(self.horizontalLayout_163)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setSpacing(40)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setSpacing(10)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.label_170 = QLabel(self.groupBox_34)
        self.label_170.setObjectName(u"label_170")
        sizePolicy.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy)
        self.label_170.setMinimumSize(QSize(134, 0))

        self.horizontalLayout_166.addWidget(self.label_170)

        self.station4_valve_lift_locate_pre_6 = QSpinBox(self.groupBox_34)
        self.station4_valve_lift_locate_pre_6.setObjectName(u"station4_valve_lift_locate_pre_6")
        sizePolicy1.setHeightForWidth(self.station4_valve_lift_locate_pre_6.sizePolicy().hasHeightForWidth())
        self.station4_valve_lift_locate_pre_6.setSizePolicy(sizePolicy1)
        self.station4_valve_lift_locate_pre_6.setMinimumSize(QSize(50, 0))
        self.station4_valve_lift_locate_pre_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_valve_lift_locate_pre_6.setMinimum(1)
        self.station4_valve_lift_locate_pre_6.setMaximum(16)
        self.station4_valve_lift_locate_pre_6.setValue(6)

        self.horizontalLayout_166.addWidget(self.station4_valve_lift_locate_pre_6)

        self.station4_valve_lift_locate_pre_6_state = QLabel(self.groupBox_34)
        self.station4_valve_lift_locate_pre_6_state.setObjectName(u"station4_valve_lift_locate_pre_6_state")
        self.station4_valve_lift_locate_pre_6_state.setFont(font2)
        self.station4_valve_lift_locate_pre_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_166.addWidget(self.station4_valve_lift_locate_pre_6_state)

        self.station4_valve_lift_locate_pre_6_btn = QToolButton(self.groupBox_34)
        self.station4_valve_lift_locate_pre_6_btn.setObjectName(u"station4_valve_lift_locate_pre_6_btn")
        self.station4_valve_lift_locate_pre_6_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_166.addWidget(self.station4_valve_lift_locate_pre_6_btn)


        self.horizontalLayout_165.addLayout(self.horizontalLayout_166)

        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setSpacing(10)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.groupBox_34)
        self.label_171.setObjectName(u"label_171")
        sizePolicy.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy)

        self.horizontalLayout_167.addWidget(self.label_171)

        self.station4_valve_lift_locate_main_6 = QSpinBox(self.groupBox_34)
        self.station4_valve_lift_locate_main_6.setObjectName(u"station4_valve_lift_locate_main_6")
        sizePolicy1.setHeightForWidth(self.station4_valve_lift_locate_main_6.sizePolicy().hasHeightForWidth())
        self.station4_valve_lift_locate_main_6.setSizePolicy(sizePolicy1)
        self.station4_valve_lift_locate_main_6.setMinimumSize(QSize(50, 0))
        self.station4_valve_lift_locate_main_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_valve_lift_locate_main_6.setMinimum(1)
        self.station4_valve_lift_locate_main_6.setMaximum(16)
        self.station4_valve_lift_locate_main_6.setValue(6)

        self.horizontalLayout_167.addWidget(self.station4_valve_lift_locate_main_6)

        self.station4_valve_lift_locate_main_6_state = QLabel(self.groupBox_34)
        self.station4_valve_lift_locate_main_6_state.setObjectName(u"station4_valve_lift_locate_main_6_state")
        self.station4_valve_lift_locate_main_6_state.setFont(font2)
        self.station4_valve_lift_locate_main_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_167.addWidget(self.station4_valve_lift_locate_main_6_state)

        self.station4_valve_lift_locate_main_6_btn = QToolButton(self.groupBox_34)
        self.station4_valve_lift_locate_main_6_btn.setObjectName(u"station4_valve_lift_locate_main_6_btn")
        self.station4_valve_lift_locate_main_6_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_167.addWidget(self.station4_valve_lift_locate_main_6_btn)


        self.horizontalLayout_165.addLayout(self.horizontalLayout_167)


        self.verticalLayout_41.addLayout(self.horizontalLayout_165)


        self.verticalLayout_40.addWidget(self.groupBox_34)

        self.horizontalLayout_168 = QHBoxLayout()
        self.horizontalLayout_168.setSpacing(10)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(10, 0, 10, 0)
        self.label_172 = QLabel(self.group_valve_4)
        self.label_172.setObjectName(u"label_172")
        sizePolicy.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy)
        self.label_172.setMinimumSize(QSize(134, 0))

        self.horizontalLayout_168.addWidget(self.label_172)

        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6 = QSpinBox(self.group_valve_4)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.setObjectName(u"station4_valve_lift_locate_upper_housing_pallet_clamp_6")
        sizePolicy1.setHeightForWidth(self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.sizePolicy().hasHeightForWidth())
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.setSizePolicy(sizePolicy1)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.setMinimumSize(QSize(50, 0))
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.setMinimum(1)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.setMaximum(16)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6.setValue(6)

        self.horizontalLayout_168.addWidget(self.station4_valve_lift_locate_upper_housing_pallet_clamp_6)

        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_state = QLabel(self.group_valve_4)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_state.setObjectName(u"station4_valve_lift_locate_upper_housing_pallet_clamp_6_state")
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_state.setFont(font2)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_168.addWidget(self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_state)

        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_btn = QToolButton(self.group_valve_4)
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_btn.setObjectName(u"station4_valve_lift_locate_upper_housing_pallet_clamp_6_btn")
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_168.addWidget(self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_btn)


        self.verticalLayout_40.addLayout(self.horizontalLayout_168)

        self.groupBox_50 = QGroupBox(self.group_valve_4)
        self.groupBox_50.setObjectName(u"groupBox_50")
        self.horizontalLayout_215 = QHBoxLayout(self.groupBox_50)
        self.horizontalLayout_215.setSpacing(30)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_213 = QHBoxLayout()
        self.horizontalLayout_213.setSpacing(10)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.horizontalLayout_213.setContentsMargins(0, 0, 0, 0)
        self.label_212 = QLabel(self.groupBox_50)
        self.label_212.setObjectName(u"label_212")
        sizePolicy.setHeightForWidth(self.label_212.sizePolicy().hasHeightForWidth())
        self.label_212.setSizePolicy(sizePolicy)
        self.label_212.setMinimumSize(QSize(134, 0))

        self.horizontalLayout_213.addWidget(self.label_212)

        self.station4_valve_right_handle_rotator_slide_close = QSpinBox(self.groupBox_50)
        self.station4_valve_right_handle_rotator_slide_close.setObjectName(u"station4_valve_right_handle_rotator_slide_close")
        sizePolicy1.setHeightForWidth(self.station4_valve_right_handle_rotator_slide_close.sizePolicy().hasHeightForWidth())
        self.station4_valve_right_handle_rotator_slide_close.setSizePolicy(sizePolicy1)
        self.station4_valve_right_handle_rotator_slide_close.setMinimumSize(QSize(50, 0))
        self.station4_valve_right_handle_rotator_slide_close.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_valve_right_handle_rotator_slide_close.setMinimum(1)
        self.station4_valve_right_handle_rotator_slide_close.setMaximum(16)
        self.station4_valve_right_handle_rotator_slide_close.setValue(6)

        self.horizontalLayout_213.addWidget(self.station4_valve_right_handle_rotator_slide_close)

        self.station4_valve_right_handle_rotator_slide_close_state = QLabel(self.groupBox_50)
        self.station4_valve_right_handle_rotator_slide_close_state.setObjectName(u"station4_valve_right_handle_rotator_slide_close_state")
        self.station4_valve_right_handle_rotator_slide_close_state.setFont(font2)
        self.station4_valve_right_handle_rotator_slide_close_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_213.addWidget(self.station4_valve_right_handle_rotator_slide_close_state)

        self.station4_valve_right_handle_rotator_slide_close_btn = QToolButton(self.groupBox_50)
        self.station4_valve_right_handle_rotator_slide_close_btn.setObjectName(u"station4_valve_right_handle_rotator_slide_close_btn")
        self.station4_valve_right_handle_rotator_slide_close_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_213.addWidget(self.station4_valve_right_handle_rotator_slide_close_btn)


        self.horizontalLayout_215.addLayout(self.horizontalLayout_213)

        self.horizontalLayout_214 = QHBoxLayout()
        self.horizontalLayout_214.setSpacing(10)
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.horizontalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.label_213 = QLabel(self.groupBox_50)
        self.label_213.setObjectName(u"label_213")
        sizePolicy.setHeightForWidth(self.label_213.sizePolicy().hasHeightForWidth())
        self.label_213.setSizePolicy(sizePolicy)
        self.label_213.setMinimumSize(QSize(134, 0))

        self.horizontalLayout_214.addWidget(self.label_213)

        self.station4_valve_right_handle_rotator_pick_orient = QSpinBox(self.groupBox_50)
        self.station4_valve_right_handle_rotator_pick_orient.setObjectName(u"station4_valve_right_handle_rotator_pick_orient")
        sizePolicy1.setHeightForWidth(self.station4_valve_right_handle_rotator_pick_orient.sizePolicy().hasHeightForWidth())
        self.station4_valve_right_handle_rotator_pick_orient.setSizePolicy(sizePolicy1)
        self.station4_valve_right_handle_rotator_pick_orient.setMinimumSize(QSize(50, 0))
        self.station4_valve_right_handle_rotator_pick_orient.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_valve_right_handle_rotator_pick_orient.setMinimum(1)
        self.station4_valve_right_handle_rotator_pick_orient.setMaximum(16)
        self.station4_valve_right_handle_rotator_pick_orient.setValue(6)

        self.horizontalLayout_214.addWidget(self.station4_valve_right_handle_rotator_pick_orient)

        self.station4_valve_right_handle_rotator_pick_orient_state = QLabel(self.groupBox_50)
        self.station4_valve_right_handle_rotator_pick_orient_state.setObjectName(u"station4_valve_right_handle_rotator_pick_orient_state")
        self.station4_valve_right_handle_rotator_pick_orient_state.setFont(font2)
        self.station4_valve_right_handle_rotator_pick_orient_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_214.addWidget(self.station4_valve_right_handle_rotator_pick_orient_state)

        self.station4_valve_right_handle_rotator_pick_orient_btn = QToolButton(self.groupBox_50)
        self.station4_valve_right_handle_rotator_pick_orient_btn.setObjectName(u"station4_valve_right_handle_rotator_pick_orient_btn")
        self.station4_valve_right_handle_rotator_pick_orient_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_214.addWidget(self.station4_valve_right_handle_rotator_pick_orient_btn)


        self.horizontalLayout_215.addLayout(self.horizontalLayout_214)


        self.verticalLayout_40.addWidget(self.groupBox_50)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_3)


        self.horizontalLayout_148.addWidget(self.group_valve_4)


        self.verticalLayout_43.addLayout(self.horizontalLayout_148)

        self.groupBox_40 = QGroupBox(self.tab_station4)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.verticalLayout_46 = QVBoxLayout(self.groupBox_40)
        self.verticalLayout_46.setSpacing(20)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setSpacing(30)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setSpacing(10)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(5, 5, 5, 5)
        self.label_173 = QLabel(self.groupBox_40)
        self.label_173.setObjectName(u"label_173")
        sizePolicy.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy)

        self.horizontalLayout_98.addWidget(self.label_173)

        self.station4_hopper_conveyor_index_speed = QSpinBox(self.groupBox_40)
        self.station4_hopper_conveyor_index_speed.setObjectName(u"station4_hopper_conveyor_index_speed")
        sizePolicy1.setHeightForWidth(self.station4_hopper_conveyor_index_speed.sizePolicy().hasHeightForWidth())
        self.station4_hopper_conveyor_index_speed.setSizePolicy(sizePolicy1)
        self.station4_hopper_conveyor_index_speed.setMinimumSize(QSize(100, 0))
        self.station4_hopper_conveyor_index_speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_hopper_conveyor_index_speed.setMinimum(0)
        self.station4_hopper_conveyor_index_speed.setMaximum(2000)
        self.station4_hopper_conveyor_index_speed.setValue(200)

        self.horizontalLayout_98.addWidget(self.station4_hopper_conveyor_index_speed)


        self.horizontalLayout_102.addLayout(self.horizontalLayout_98)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setSpacing(10)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(5, 5, 5, 5)
        self.label_174 = QLabel(self.groupBox_40)
        self.label_174.setObjectName(u"label_174")
        sizePolicy.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy)

        self.horizontalLayout_99.addWidget(self.label_174)

        self.station4_hopper_conveyor_homing_speed = QSpinBox(self.groupBox_40)
        self.station4_hopper_conveyor_homing_speed.setObjectName(u"station4_hopper_conveyor_homing_speed")
        sizePolicy1.setHeightForWidth(self.station4_hopper_conveyor_homing_speed.sizePolicy().hasHeightForWidth())
        self.station4_hopper_conveyor_homing_speed.setSizePolicy(sizePolicy1)
        self.station4_hopper_conveyor_homing_speed.setMinimumSize(QSize(100, 0))
        self.station4_hopper_conveyor_homing_speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_hopper_conveyor_homing_speed.setMinimum(0)
        self.station4_hopper_conveyor_homing_speed.setMaximum(2000)
        self.station4_hopper_conveyor_homing_speed.setValue(50)

        self.horizontalLayout_99.addWidget(self.station4_hopper_conveyor_homing_speed)


        self.horizontalLayout_102.addLayout(self.horizontalLayout_99)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setSpacing(10)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(5, 5, 5, 5)
        self.label_175 = QLabel(self.groupBox_40)
        self.label_175.setObjectName(u"label_175")
        sizePolicy.setHeightForWidth(self.label_175.sizePolicy().hasHeightForWidth())
        self.label_175.setSizePolicy(sizePolicy)

        self.horizontalLayout_100.addWidget(self.label_175)

        self.station4_hopper_conveyor_index_length = QSpinBox(self.groupBox_40)
        self.station4_hopper_conveyor_index_length.setObjectName(u"station4_hopper_conveyor_index_length")
        sizePolicy1.setHeightForWidth(self.station4_hopper_conveyor_index_length.sizePolicy().hasHeightForWidth())
        self.station4_hopper_conveyor_index_length.setSizePolicy(sizePolicy1)
        self.station4_hopper_conveyor_index_length.setMinimumSize(QSize(100, 0))
        self.station4_hopper_conveyor_index_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_hopper_conveyor_index_length.setMinimum(0)
        self.station4_hopper_conveyor_index_length.setMaximum(2000)
        self.station4_hopper_conveyor_index_length.setValue(1220)

        self.horizontalLayout_100.addWidget(self.station4_hopper_conveyor_index_length)


        self.horizontalLayout_102.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setSpacing(10)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(5, 5, 5, 5)
        self.label_176 = QLabel(self.groupBox_40)
        self.label_176.setObjectName(u"label_176")
        sizePolicy.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy)

        self.horizontalLayout_101.addWidget(self.label_176)

        self.station4_hopper_conveyor_home_offset = QSpinBox(self.groupBox_40)
        self.station4_hopper_conveyor_home_offset.setObjectName(u"station4_hopper_conveyor_home_offset")
        sizePolicy1.setHeightForWidth(self.station4_hopper_conveyor_home_offset.sizePolicy().hasHeightForWidth())
        self.station4_hopper_conveyor_home_offset.setSizePolicy(sizePolicy1)
        self.station4_hopper_conveyor_home_offset.setMinimumSize(QSize(100, 0))
        self.station4_hopper_conveyor_home_offset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station4_hopper_conveyor_home_offset.setMinimum(0)
        self.station4_hopper_conveyor_home_offset.setMaximum(2000)
        self.station4_hopper_conveyor_home_offset.setValue(0)

        self.horizontalLayout_101.addWidget(self.station4_hopper_conveyor_home_offset)


        self.horizontalLayout_102.addLayout(self.horizontalLayout_101)


        self.verticalLayout_46.addLayout(self.horizontalLayout_102)

        self.groupBox_61 = QGroupBox(self.groupBox_40)
        self.groupBox_61.setObjectName(u"groupBox_61")
        self.verticalLayout_39 = QVBoxLayout(self.groupBox_61)
        self.verticalLayout_39.setSpacing(15)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_173 = QHBoxLayout()
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.label_185 = QLabel(self.groupBox_61)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_173.addWidget(self.label_185)

        self.station5_motor_address_2 = QSpinBox(self.groupBox_61)
        self.station5_motor_address_2.setObjectName(u"station5_motor_address_2")
        sizePolicy1.setHeightForWidth(self.station5_motor_address_2.sizePolicy().hasHeightForWidth())
        self.station5_motor_address_2.setSizePolicy(sizePolicy1)
        self.station5_motor_address_2.setMinimumSize(QSize(50, 0))
        self.station5_motor_address_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_motor_address_2.setMinimum(0)
        self.station5_motor_address_2.setMaximum(7)
        self.station5_motor_address_2.setValue(7)

        self.horizontalLayout_173.addWidget(self.station5_motor_address_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_5)

        self.label_129 = QLabel(self.groupBox_61)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_173.addWidget(self.label_129)

        self.station5_motor_speed_limit_2 = QSpinBox(self.groupBox_61)
        self.station5_motor_speed_limit_2.setObjectName(u"station5_motor_speed_limit_2")
        self.station5_motor_speed_limit_2.setMaximumSize(QSize(80, 16777215))
        self.station5_motor_speed_limit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_motor_speed_limit_2.setMinimum(1)
        self.station5_motor_speed_limit_2.setMaximum(1080)
        self.station5_motor_speed_limit_2.setValue(150)

        self.horizontalLayout_173.addWidget(self.station5_motor_speed_limit_2)

        self.horizontalSpacer_90 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_173.addItem(self.horizontalSpacer_90)

        self.btn_station4_motor_test = QPushButton(self.groupBox_61)
        self.btn_station4_motor_test.setObjectName(u"btn_station4_motor_test")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_station4_motor_test.sizePolicy().hasHeightForWidth())
        self.btn_station4_motor_test.setSizePolicy(sizePolicy6)
        self.btn_station4_motor_test.setMinimumSize(QSize(0, 36))

        self.horizontalLayout_173.addWidget(self.btn_station4_motor_test)


        self.verticalLayout_39.addLayout(self.horizontalLayout_173)


        self.verticalLayout_46.addWidget(self.groupBox_61)


        self.verticalLayout_43.addWidget(self.groupBox_40)

        self.tabWidget.addTab(self.tab_station4, "")
        self.tab_station5 = QWidget()
        self.tab_station5.setObjectName(u"tab_station5")
        self.verticalLayout_66 = QVBoxLayout(self.tab_station5)
        self.verticalLayout_66.setSpacing(30)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setSpacing(50)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.groupBox_35 = QGroupBox(self.tab_station5)
        self.groupBox_35.setObjectName(u"groupBox_35")
        sizePolicy4.setHeightForWidth(self.groupBox_35.sizePolicy().hasHeightForWidth())
        self.groupBox_35.setSizePolicy(sizePolicy4)
        self.groupBox_35.setMinimumSize(QSize(0, 0))
        self.groupBox_35.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_35)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(20)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_30 = QLabel(self.groupBox_35)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_32.addWidget(self.label_30)

        self.station5_robot = QLineEdit(self.groupBox_35)
        self.station5_robot.setObjectName(u"station5_robot")
        self.station5_robot.setMaximumSize(QSize(150, 16777215))
        self.station5_robot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.station5_robot)

        self.btn_station5_robot_test = QPushButton(self.groupBox_35)
        self.btn_station5_robot_test.setObjectName(u"btn_station5_robot_test")
        self.btn_station5_robot_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_32.addWidget(self.btn_station5_robot_test)


        self.verticalLayout_13.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(20)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_29 = QLabel(self.groupBox_35)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_31.addWidget(self.label_29)

        self.station5_cognex = QLineEdit(self.groupBox_35)
        self.station5_cognex.setObjectName(u"station5_cognex")
        self.station5_cognex.setMaximumSize(QSize(150, 16777215))
        self.station5_cognex.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.station5_cognex)

        self.btn_station5_cognex_test = QPushButton(self.groupBox_35)
        self.btn_station5_cognex_test.setObjectName(u"btn_station5_cognex_test")
        self.btn_station5_cognex_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_31.addWidget(self.btn_station5_cognex_test)


        self.verticalLayout_13.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(20)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_34 = QLabel(self.groupBox_35)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_36.addWidget(self.label_34)

        self.station5_barcode_1 = QLineEdit(self.groupBox_35)
        self.station5_barcode_1.setObjectName(u"station5_barcode_1")
        self.station5_barcode_1.setMaximumSize(QSize(150, 16777215))
        self.station5_barcode_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.station5_barcode_1)

        self.btn_station5_barcode_1_test = QPushButton(self.groupBox_35)
        self.btn_station5_barcode_1_test.setObjectName(u"btn_station5_barcode_1_test")
        self.btn_station5_barcode_1_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_36.addWidget(self.btn_station5_barcode_1_test)


        self.verticalLayout_13.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setSpacing(20)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.label_51 = QLabel(self.groupBox_35)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_183.addWidget(self.label_51)

        self.station5_barcode_labeler = QLineEdit(self.groupBox_35)
        self.station5_barcode_labeler.setObjectName(u"station5_barcode_labeler")
        self.station5_barcode_labeler.setMaximumSize(QSize(150, 16777215))
        self.station5_barcode_labeler.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_183.addWidget(self.station5_barcode_labeler)

        self.btn_station5_barcode_labeler_test_2 = QPushButton(self.groupBox_35)
        self.btn_station5_barcode_labeler_test_2.setObjectName(u"btn_station5_barcode_labeler_test_2")
        self.btn_station5_barcode_labeler_test_2.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_183.addWidget(self.btn_station5_barcode_labeler_test_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_183)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(20)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_27 = QLabel(self.groupBox_35)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_29.addWidget(self.label_27)

        self.station5_wago = QLineEdit(self.groupBox_35)
        self.station5_wago.setObjectName(u"station5_wago")
        self.station5_wago.setMaximumSize(QSize(150, 16777215))
        self.station5_wago.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.station5_wago)

        self.btn_station5_wago_test = QPushButton(self.groupBox_35)
        self.btn_station5_wago_test.setObjectName(u"btn_station5_wago_test")
        self.btn_station5_wago_test.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_29.addWidget(self.btn_station5_wago_test)


        self.verticalLayout_13.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_97.addWidget(self.groupBox_35)

        self.groupBox_37 = QGroupBox(self.tab_station5)
        self.groupBox_37.setObjectName(u"groupBox_37")
        sizePolicy.setHeightForWidth(self.groupBox_37.sizePolicy().hasHeightForWidth())
        self.groupBox_37.setSizePolicy(sizePolicy)
        self.groupBox_37.setMaximumSize(QSize(4500, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_37)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_31 = QLabel(self.groupBox_37)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_33.addWidget(self.label_31)

        self.station5_feeders_lower_housing = QLineEdit(self.groupBox_37)
        self.station5_feeders_lower_housing.setObjectName(u"station5_feeders_lower_housing")
        self.station5_feeders_lower_housing.setMaximumSize(QSize(150, 16777215))
        self.station5_feeders_lower_housing.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.station5_feeders_lower_housing)

        self.btn_station5_feeders_lower_housing_test = QPushButton(self.groupBox_37)
        self.btn_station5_feeders_lower_housing_test.setObjectName(u"btn_station5_feeders_lower_housing_test")
        self.btn_station5_feeders_lower_housing_test.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_33.addWidget(self.btn_station5_feeders_lower_housing_test)


        self.verticalLayout_23.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_10)


        self.horizontalLayout_97.addWidget(self.groupBox_37)


        self.verticalLayout_66.addLayout(self.horizontalLayout_97)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setSpacing(50)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(30)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.groupBox_33 = QGroupBox(self.tab_station5)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setMinimumSize(QSize(633, 0))
        self.verticalLayout_57 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_57.setSpacing(10)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.groupBox_6 = QGroupBox(self.groupBox_33)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 120))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(40)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_99 = QLabel(self.groupBox_6)
        self.label_99.setObjectName(u"label_99")
        sizePolicy.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_99)

        self.station5_io_lift_locate_extended_1 = QSpinBox(self.groupBox_6)
        self.station5_io_lift_locate_extended_1.setObjectName(u"station5_io_lift_locate_extended_1")
        sizePolicy1.setHeightForWidth(self.station5_io_lift_locate_extended_1.sizePolicy().hasHeightForWidth())
        self.station5_io_lift_locate_extended_1.setSizePolicy(sizePolicy1)
        self.station5_io_lift_locate_extended_1.setMinimumSize(QSize(50, 0))
        self.station5_io_lift_locate_extended_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_lift_locate_extended_1.setMinimum(1)
        self.station5_io_lift_locate_extended_1.setMaximum(16)
        self.station5_io_lift_locate_extended_1.setValue(6)

        self.horizontalLayout_8.addWidget(self.station5_io_lift_locate_extended_1)

        self.station5_io_lift_locate_extended_1_state = QLabel(self.groupBox_6)
        self.station5_io_lift_locate_extended_1_state.setObjectName(u"station5_io_lift_locate_extended_1_state")
        self.station5_io_lift_locate_extended_1_state.setFont(font2)
        self.station5_io_lift_locate_extended_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_8.addWidget(self.station5_io_lift_locate_extended_1_state)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_100 = QLabel(self.groupBox_6)
        self.label_100.setObjectName(u"label_100")
        sizePolicy.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_100)

        self.station5_io_lift_locate_retracted_1 = QSpinBox(self.groupBox_6)
        self.station5_io_lift_locate_retracted_1.setObjectName(u"station5_io_lift_locate_retracted_1")
        sizePolicy1.setHeightForWidth(self.station5_io_lift_locate_retracted_1.sizePolicy().hasHeightForWidth())
        self.station5_io_lift_locate_retracted_1.setSizePolicy(sizePolicy1)
        self.station5_io_lift_locate_retracted_1.setMinimumSize(QSize(50, 0))
        self.station5_io_lift_locate_retracted_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_lift_locate_retracted_1.setMinimum(1)
        self.station5_io_lift_locate_retracted_1.setMaximum(16)
        self.station5_io_lift_locate_retracted_1.setValue(6)

        self.horizontalLayout_9.addWidget(self.station5_io_lift_locate_retracted_1)

        self.station5_io_lift_locate_retracted_1_state = QLabel(self.groupBox_6)
        self.station5_io_lift_locate_retracted_1_state.setObjectName(u"station5_io_lift_locate_retracted_1_state")
        self.station5_io_lift_locate_retracted_1_state.setFont(font2)
        self.station5_io_lift_locate_retracted_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_9.addWidget(self.station5_io_lift_locate_retracted_1_state)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(40)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.label_101 = QLabel(self.groupBox_6)
        self.label_101.setObjectName(u"label_101")
        sizePolicy.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_101)

        self.station5_io_lift_locate_pre_1 = QSpinBox(self.groupBox_6)
        self.station5_io_lift_locate_pre_1.setObjectName(u"station5_io_lift_locate_pre_1")
        sizePolicy1.setHeightForWidth(self.station5_io_lift_locate_pre_1.sizePolicy().hasHeightForWidth())
        self.station5_io_lift_locate_pre_1.setSizePolicy(sizePolicy1)
        self.station5_io_lift_locate_pre_1.setMinimumSize(QSize(50, 0))
        self.station5_io_lift_locate_pre_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_lift_locate_pre_1.setMinimum(1)
        self.station5_io_lift_locate_pre_1.setMaximum(16)
        self.station5_io_lift_locate_pre_1.setValue(6)

        self.horizontalLayout_17.addWidget(self.station5_io_lift_locate_pre_1)

        self.station5_io_lift_locate_pre_1_state = QLabel(self.groupBox_6)
        self.station5_io_lift_locate_pre_1_state.setObjectName(u"station5_io_lift_locate_pre_1_state")
        self.station5_io_lift_locate_pre_1_state.setFont(font2)
        self.station5_io_lift_locate_pre_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_17.addWidget(self.station5_io_lift_locate_pre_1_state)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.label_102 = QLabel(self.groupBox_6)
        self.label_102.setObjectName(u"label_102")
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.label_102)

        self.station5_io_lift_locate_main_1 = QSpinBox(self.groupBox_6)
        self.station5_io_lift_locate_main_1.setObjectName(u"station5_io_lift_locate_main_1")
        sizePolicy1.setHeightForWidth(self.station5_io_lift_locate_main_1.sizePolicy().hasHeightForWidth())
        self.station5_io_lift_locate_main_1.setSizePolicy(sizePolicy1)
        self.station5_io_lift_locate_main_1.setMinimumSize(QSize(50, 0))
        self.station5_io_lift_locate_main_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_lift_locate_main_1.setMinimum(1)
        self.station5_io_lift_locate_main_1.setMaximum(16)
        self.station5_io_lift_locate_main_1.setValue(6)

        self.horizontalLayout_18.addWidget(self.station5_io_lift_locate_main_1)

        self.station5_io_lift_locate_main_1_state = QLabel(self.groupBox_6)
        self.station5_io_lift_locate_main_1_state.setObjectName(u"station5_io_lift_locate_main_1_state")
        self.station5_io_lift_locate_main_1_state.setFont(font2)
        self.station5_io_lift_locate_main_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_18.addWidget(self.station5_io_lift_locate_main_1_state)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_18)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)


        self.verticalLayout_57.addWidget(self.groupBox_6)

        self.groupBox_51 = QGroupBox(self.groupBox_33)
        self.groupBox_51.setObjectName(u"groupBox_51")
        sizePolicy3.setHeightForWidth(self.groupBox_51.sizePolicy().hasHeightForWidth())
        self.groupBox_51.setSizePolicy(sizePolicy3)
        self.groupBox_51.setMinimumSize(QSize(0, 118))
        self.verticalLayout_42 = QVBoxLayout(self.groupBox_51)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_216 = QHBoxLayout()
        self.horizontalLayout_216.setSpacing(20)
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.horizontalLayout_217 = QHBoxLayout()
        self.horizontalLayout_217.setSpacing(10)
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.horizontalLayout_217.setContentsMargins(5, 5, 5, 5)
        self.label_214 = QLabel(self.groupBox_51)
        self.label_214.setObjectName(u"label_214")
        sizePolicy.setHeightForWidth(self.label_214.sizePolicy().hasHeightForWidth())
        self.label_214.setSizePolicy(sizePolicy)
        self.label_214.setMinimumSize(QSize(150, 0))
        self.label_214.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_217.addWidget(self.label_214)

        self.station5_io_whirl_rotator_cw = QSpinBox(self.groupBox_51)
        self.station5_io_whirl_rotator_cw.setObjectName(u"station5_io_whirl_rotator_cw")
        sizePolicy1.setHeightForWidth(self.station5_io_whirl_rotator_cw.sizePolicy().hasHeightForWidth())
        self.station5_io_whirl_rotator_cw.setSizePolicy(sizePolicy1)
        self.station5_io_whirl_rotator_cw.setMinimumSize(QSize(50, 0))
        self.station5_io_whirl_rotator_cw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_whirl_rotator_cw.setMinimum(1)
        self.station5_io_whirl_rotator_cw.setMaximum(32)
        self.station5_io_whirl_rotator_cw.setValue(6)

        self.horizontalLayout_217.addWidget(self.station5_io_whirl_rotator_cw)

        self.station5_io_whirl_rotator_cw_state = QLabel(self.groupBox_51)
        self.station5_io_whirl_rotator_cw_state.setObjectName(u"station5_io_whirl_rotator_cw_state")
        self.station5_io_whirl_rotator_cw_state.setFont(font2)
        self.station5_io_whirl_rotator_cw_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_217.addWidget(self.station5_io_whirl_rotator_cw_state)


        self.horizontalLayout_216.addLayout(self.horizontalLayout_217)

        self.horizontalLayout_218 = QHBoxLayout()
        self.horizontalLayout_218.setSpacing(10)
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.horizontalLayout_218.setContentsMargins(5, 5, 5, 5)
        self.label_215 = QLabel(self.groupBox_51)
        self.label_215.setObjectName(u"label_215")
        sizePolicy.setHeightForWidth(self.label_215.sizePolicy().hasHeightForWidth())
        self.label_215.setSizePolicy(sizePolicy)

        self.horizontalLayout_218.addWidget(self.label_215)

        self.station5_io_whirl_rotator_ccw = QSpinBox(self.groupBox_51)
        self.station5_io_whirl_rotator_ccw.setObjectName(u"station5_io_whirl_rotator_ccw")
        sizePolicy1.setHeightForWidth(self.station5_io_whirl_rotator_ccw.sizePolicy().hasHeightForWidth())
        self.station5_io_whirl_rotator_ccw.setSizePolicy(sizePolicy1)
        self.station5_io_whirl_rotator_ccw.setMinimumSize(QSize(50, 0))
        self.station5_io_whirl_rotator_ccw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_whirl_rotator_ccw.setMinimum(1)
        self.station5_io_whirl_rotator_ccw.setMaximum(32)
        self.station5_io_whirl_rotator_ccw.setValue(6)

        self.horizontalLayout_218.addWidget(self.station5_io_whirl_rotator_ccw)

        self.station5_io_whirl_rotator_ccw_state = QLabel(self.groupBox_51)
        self.station5_io_whirl_rotator_ccw_state.setObjectName(u"station5_io_whirl_rotator_ccw_state")
        self.station5_io_whirl_rotator_ccw_state.setFont(font2)
        self.station5_io_whirl_rotator_ccw_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_218.addWidget(self.station5_io_whirl_rotator_ccw_state)


        self.horizontalLayout_216.addLayout(self.horizontalLayout_218)


        self.verticalLayout_42.addLayout(self.horizontalLayout_216)

        self.horizontalLayout_219 = QHBoxLayout()
        self.horizontalLayout_219.setSpacing(40)
        self.horizontalLayout_219.setObjectName(u"horizontalLayout_219")
        self.horizontalLayout_220 = QHBoxLayout()
        self.horizontalLayout_220.setSpacing(10)
        self.horizontalLayout_220.setObjectName(u"horizontalLayout_220")
        self.horizontalLayout_220.setContentsMargins(5, 5, 5, 5)
        self.label_216 = QLabel(self.groupBox_51)
        self.label_216.setObjectName(u"label_216")
        sizePolicy.setHeightForWidth(self.label_216.sizePolicy().hasHeightForWidth())
        self.label_216.setSizePolicy(sizePolicy)
        self.label_216.setMinimumSize(QSize(150, 0))
        self.label_216.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_220.addWidget(self.label_216)

        self.station5_io_whirl_rotator_part_presence = QSpinBox(self.groupBox_51)
        self.station5_io_whirl_rotator_part_presence.setObjectName(u"station5_io_whirl_rotator_part_presence")
        sizePolicy1.setHeightForWidth(self.station5_io_whirl_rotator_part_presence.sizePolicy().hasHeightForWidth())
        self.station5_io_whirl_rotator_part_presence.setSizePolicy(sizePolicy1)
        self.station5_io_whirl_rotator_part_presence.setMinimumSize(QSize(50, 0))
        self.station5_io_whirl_rotator_part_presence.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_whirl_rotator_part_presence.setMinimum(1)
        self.station5_io_whirl_rotator_part_presence.setMaximum(32)
        self.station5_io_whirl_rotator_part_presence.setValue(1)

        self.horizontalLayout_220.addWidget(self.station5_io_whirl_rotator_part_presence)

        self.station5_io_whirl_rotator_part_presence_state = QLabel(self.groupBox_51)
        self.station5_io_whirl_rotator_part_presence_state.setObjectName(u"station5_io_whirl_rotator_part_presence_state")
        self.station5_io_whirl_rotator_part_presence_state.setFont(font2)
        self.station5_io_whirl_rotator_part_presence_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_220.addWidget(self.station5_io_whirl_rotator_part_presence_state)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_220.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_219.addLayout(self.horizontalLayout_220)


        self.verticalLayout_42.addLayout(self.horizontalLayout_219)


        self.verticalLayout_57.addWidget(self.groupBox_51)

        self.group_boxing = QGroupBox(self.groupBox_33)
        self.group_boxing.setObjectName(u"group_boxing")
        sizePolicy3.setHeightForWidth(self.group_boxing.sizePolicy().hasHeightForWidth())
        self.group_boxing.setSizePolicy(sizePolicy3)
        self.group_boxing.setMinimumSize(QSize(0, 0))
        self.verticalLayout_48 = QVBoxLayout(self.group_boxing)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_242 = QHBoxLayout()
        self.horizontalLayout_242.setSpacing(20)
        self.horizontalLayout_242.setObjectName(u"horizontalLayout_242")
        self.horizontalLayout_243 = QHBoxLayout()
        self.horizontalLayout_243.setSpacing(10)
        self.horizontalLayout_243.setObjectName(u"horizontalLayout_243")
        self.horizontalLayout_243.setContentsMargins(5, 5, 5, 5)
        self.label_231 = QLabel(self.group_boxing)
        self.label_231.setObjectName(u"label_231")
        sizePolicy.setHeightForWidth(self.label_231.sizePolicy().hasHeightForWidth())
        self.label_231.setSizePolicy(sizePolicy)
        self.label_231.setMinimumSize(QSize(150, 0))
        self.label_231.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_243.addWidget(self.label_231)

        self.station5_io_box_clamp_engaged = QSpinBox(self.group_boxing)
        self.station5_io_box_clamp_engaged.setObjectName(u"station5_io_box_clamp_engaged")
        sizePolicy1.setHeightForWidth(self.station5_io_box_clamp_engaged.sizePolicy().hasHeightForWidth())
        self.station5_io_box_clamp_engaged.setSizePolicy(sizePolicy1)
        self.station5_io_box_clamp_engaged.setMinimumSize(QSize(50, 0))
        self.station5_io_box_clamp_engaged.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_box_clamp_engaged.setMinimum(1)
        self.station5_io_box_clamp_engaged.setMaximum(32)
        self.station5_io_box_clamp_engaged.setValue(6)

        self.horizontalLayout_243.addWidget(self.station5_io_box_clamp_engaged)

        self.station5_io_box_clamp_engaged_state = QLabel(self.group_boxing)
        self.station5_io_box_clamp_engaged_state.setObjectName(u"station5_io_box_clamp_engaged_state")
        self.station5_io_box_clamp_engaged_state.setFont(font2)
        self.station5_io_box_clamp_engaged_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))
        self.station5_io_box_clamp_engaged_state.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_243.addWidget(self.station5_io_box_clamp_engaged_state)


        self.horizontalLayout_242.addLayout(self.horizontalLayout_243)

        self.horizontalLayout_244 = QHBoxLayout()
        self.horizontalLayout_244.setSpacing(10)
        self.horizontalLayout_244.setObjectName(u"horizontalLayout_244")
        self.horizontalLayout_244.setContentsMargins(5, 5, 5, 5)
        self.label_232 = QLabel(self.group_boxing)
        self.label_232.setObjectName(u"label_232")
        sizePolicy.setHeightForWidth(self.label_232.sizePolicy().hasHeightForWidth())
        self.label_232.setSizePolicy(sizePolicy)

        self.horizontalLayout_244.addWidget(self.label_232)

        self.station5_io_box_clamp_retracted = QSpinBox(self.group_boxing)
        self.station5_io_box_clamp_retracted.setObjectName(u"station5_io_box_clamp_retracted")
        sizePolicy1.setHeightForWidth(self.station5_io_box_clamp_retracted.sizePolicy().hasHeightForWidth())
        self.station5_io_box_clamp_retracted.setSizePolicy(sizePolicy1)
        self.station5_io_box_clamp_retracted.setMinimumSize(QSize(50, 0))
        self.station5_io_box_clamp_retracted.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_box_clamp_retracted.setMinimum(1)
        self.station5_io_box_clamp_retracted.setMaximum(32)
        self.station5_io_box_clamp_retracted.setValue(6)

        self.horizontalLayout_244.addWidget(self.station5_io_box_clamp_retracted)

        self.station5_io_box_clamp_retracted_state = QLabel(self.group_boxing)
        self.station5_io_box_clamp_retracted_state.setObjectName(u"station5_io_box_clamp_retracted_state")
        self.station5_io_box_clamp_retracted_state.setFont(font2)
        self.station5_io_box_clamp_retracted_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_244.addWidget(self.station5_io_box_clamp_retracted_state)


        self.horizontalLayout_242.addLayout(self.horizontalLayout_244)


        self.verticalLayout_48.addLayout(self.horizontalLayout_242)

        self.horizontalLayout_236 = QHBoxLayout()
        self.horizontalLayout_236.setSpacing(20)
        self.horizontalLayout_236.setObjectName(u"horizontalLayout_236")
        self.horizontalLayout_238 = QHBoxLayout()
        self.horizontalLayout_238.setSpacing(10)
        self.horizontalLayout_238.setObjectName(u"horizontalLayout_238")
        self.horizontalLayout_238.setContentsMargins(5, 5, 5, 5)
        self.label_228 = QLabel(self.group_boxing)
        self.label_228.setObjectName(u"label_228")
        sizePolicy.setHeightForWidth(self.label_228.sizePolicy().hasHeightForWidth())
        self.label_228.setSizePolicy(sizePolicy)
        self.label_228.setMinimumSize(QSize(150, 0))
        self.label_228.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_238.addWidget(self.label_228)

        self.station5_io_boxing_sensor_1 = QSpinBox(self.group_boxing)
        self.station5_io_boxing_sensor_1.setObjectName(u"station5_io_boxing_sensor_1")
        sizePolicy1.setHeightForWidth(self.station5_io_boxing_sensor_1.sizePolicy().hasHeightForWidth())
        self.station5_io_boxing_sensor_1.setSizePolicy(sizePolicy1)
        self.station5_io_boxing_sensor_1.setMinimumSize(QSize(50, 0))
        self.station5_io_boxing_sensor_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_boxing_sensor_1.setMinimum(1)
        self.station5_io_boxing_sensor_1.setMaximum(32)
        self.station5_io_boxing_sensor_1.setValue(6)

        self.horizontalLayout_238.addWidget(self.station5_io_boxing_sensor_1)

        self.station5_io_boxing_sensor_1_state = QLabel(self.group_boxing)
        self.station5_io_boxing_sensor_1_state.setObjectName(u"station5_io_boxing_sensor_1_state")
        self.station5_io_boxing_sensor_1_state.setFont(font2)
        self.station5_io_boxing_sensor_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))
        self.station5_io_boxing_sensor_1_state.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_238.addWidget(self.station5_io_boxing_sensor_1_state)


        self.horizontalLayout_236.addLayout(self.horizontalLayout_238)

        self.horizontalLayout_239 = QHBoxLayout()
        self.horizontalLayout_239.setSpacing(10)
        self.horizontalLayout_239.setObjectName(u"horizontalLayout_239")
        self.horizontalLayout_239.setContentsMargins(5, 5, 5, 5)
        self.label_229 = QLabel(self.group_boxing)
        self.label_229.setObjectName(u"label_229")
        sizePolicy.setHeightForWidth(self.label_229.sizePolicy().hasHeightForWidth())
        self.label_229.setSizePolicy(sizePolicy)

        self.horizontalLayout_239.addWidget(self.label_229)

        self.station5_io_boxing_sensor_2 = QSpinBox(self.group_boxing)
        self.station5_io_boxing_sensor_2.setObjectName(u"station5_io_boxing_sensor_2")
        sizePolicy1.setHeightForWidth(self.station5_io_boxing_sensor_2.sizePolicy().hasHeightForWidth())
        self.station5_io_boxing_sensor_2.setSizePolicy(sizePolicy1)
        self.station5_io_boxing_sensor_2.setMinimumSize(QSize(50, 0))
        self.station5_io_boxing_sensor_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_boxing_sensor_2.setMinimum(1)
        self.station5_io_boxing_sensor_2.setMaximum(32)
        self.station5_io_boxing_sensor_2.setValue(6)

        self.horizontalLayout_239.addWidget(self.station5_io_boxing_sensor_2)

        self.station5_io_boxing_sensor_2_state = QLabel(self.group_boxing)
        self.station5_io_boxing_sensor_2_state.setObjectName(u"station5_io_boxing_sensor_2_state")
        self.station5_io_boxing_sensor_2_state.setFont(font2)
        self.station5_io_boxing_sensor_2_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_239.addWidget(self.station5_io_boxing_sensor_2_state)


        self.horizontalLayout_236.addLayout(self.horizontalLayout_239)


        self.verticalLayout_48.addLayout(self.horizontalLayout_236)

        self.horizontalLayout_245 = QHBoxLayout()
        self.horizontalLayout_245.setSpacing(20)
        self.horizontalLayout_245.setObjectName(u"horizontalLayout_245")
        self.horizontalLayout_241 = QHBoxLayout()
        self.horizontalLayout_241.setSpacing(10)
        self.horizontalLayout_241.setObjectName(u"horizontalLayout_241")
        self.horizontalLayout_241.setContentsMargins(5, 5, 5, 5)
        self.label_230 = QLabel(self.group_boxing)
        self.label_230.setObjectName(u"label_230")
        sizePolicy.setHeightForWidth(self.label_230.sizePolicy().hasHeightForWidth())
        self.label_230.setSizePolicy(sizePolicy)
        self.label_230.setMinimumSize(QSize(150, 0))
        self.label_230.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_241.addWidget(self.label_230)

        self.station5_io_boxing_sensor_3 = QSpinBox(self.group_boxing)
        self.station5_io_boxing_sensor_3.setObjectName(u"station5_io_boxing_sensor_3")
        sizePolicy1.setHeightForWidth(self.station5_io_boxing_sensor_3.sizePolicy().hasHeightForWidth())
        self.station5_io_boxing_sensor_3.setSizePolicy(sizePolicy1)
        self.station5_io_boxing_sensor_3.setMinimumSize(QSize(50, 0))
        self.station5_io_boxing_sensor_3.setLayoutDirection(Qt.LeftToRight)
        self.station5_io_boxing_sensor_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_boxing_sensor_3.setMinimum(1)
        self.station5_io_boxing_sensor_3.setMaximum(32)
        self.station5_io_boxing_sensor_3.setValue(1)

        self.horizontalLayout_241.addWidget(self.station5_io_boxing_sensor_3)

        self.station5_io_boxing_sensor_3_state = QLabel(self.group_boxing)
        self.station5_io_boxing_sensor_3_state.setObjectName(u"station5_io_boxing_sensor_3_state")
        self.station5_io_boxing_sensor_3_state.setFont(font2)
        self.station5_io_boxing_sensor_3_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))
        self.station5_io_boxing_sensor_3_state.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_241.addWidget(self.station5_io_boxing_sensor_3_state)


        self.horizontalLayout_245.addLayout(self.horizontalLayout_241)

        self.horizontalLayout_240 = QHBoxLayout()
        self.horizontalLayout_240.setSpacing(10)
        self.horizontalLayout_240.setObjectName(u"horizontalLayout_240")
        self.horizontalLayout_240.setContentsMargins(5, 5, 5, 5)
        self.label_233 = QLabel(self.group_boxing)
        self.label_233.setObjectName(u"label_233")
        sizePolicy.setHeightForWidth(self.label_233.sizePolicy().hasHeightForWidth())
        self.label_233.setSizePolicy(sizePolicy)
        self.label_233.setMinimumSize(QSize(150, 0))
        self.label_233.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_240.addWidget(self.label_233)

        self.station5_io_box_cylinder_retracted = QSpinBox(self.group_boxing)
        self.station5_io_box_cylinder_retracted.setObjectName(u"station5_io_box_cylinder_retracted")
        sizePolicy1.setHeightForWidth(self.station5_io_box_cylinder_retracted.sizePolicy().hasHeightForWidth())
        self.station5_io_box_cylinder_retracted.setSizePolicy(sizePolicy1)
        self.station5_io_box_cylinder_retracted.setMinimumSize(QSize(50, 0))
        self.station5_io_box_cylinder_retracted.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_box_cylinder_retracted.setMinimum(1)
        self.station5_io_box_cylinder_retracted.setMaximum(32)
        self.station5_io_box_cylinder_retracted.setValue(6)

        self.horizontalLayout_240.addWidget(self.station5_io_box_cylinder_retracted)

        self.station5_io_box_cylinder_retracted_state = QLabel(self.group_boxing)
        self.station5_io_box_cylinder_retracted_state.setObjectName(u"station5_io_box_cylinder_retracted_state")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.station5_io_box_cylinder_retracted_state.sizePolicy().hasHeightForWidth())
        self.station5_io_box_cylinder_retracted_state.setSizePolicy(sizePolicy7)
        self.station5_io_box_cylinder_retracted_state.setFont(font2)
        self.station5_io_box_cylinder_retracted_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_240.addWidget(self.station5_io_box_cylinder_retracted_state)


        self.horizontalLayout_245.addLayout(self.horizontalLayout_240)


        self.verticalLayout_48.addLayout(self.horizontalLayout_245)

        self.horizontalLayout_251 = QHBoxLayout()
        self.horizontalLayout_251.setSpacing(20)
        self.horizontalLayout_251.setObjectName(u"horizontalLayout_251")
        self.horizontalLayout_251.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_249 = QHBoxLayout()
        self.horizontalLayout_249.setSpacing(10)
        self.horizontalLayout_249.setObjectName(u"horizontalLayout_249")
        self.horizontalLayout_249.setContentsMargins(5, 5, 5, 5)
        self.label_235 = QLabel(self.group_boxing)
        self.label_235.setObjectName(u"label_235")
        sizePolicy.setHeightForWidth(self.label_235.sizePolicy().hasHeightForWidth())
        self.label_235.setSizePolicy(sizePolicy)
        self.label_235.setMinimumSize(QSize(0, 0))
        self.label_235.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_249.addWidget(self.label_235)

        self.station5_io_reject_conveyor_sensor = QSpinBox(self.group_boxing)
        self.station5_io_reject_conveyor_sensor.setObjectName(u"station5_io_reject_conveyor_sensor")
        sizePolicy1.setHeightForWidth(self.station5_io_reject_conveyor_sensor.sizePolicy().hasHeightForWidth())
        self.station5_io_reject_conveyor_sensor.setSizePolicy(sizePolicy1)
        self.station5_io_reject_conveyor_sensor.setMinimumSize(QSize(50, 0))
        self.station5_io_reject_conveyor_sensor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_reject_conveyor_sensor.setMinimum(1)
        self.station5_io_reject_conveyor_sensor.setValue(7)

        self.horizontalLayout_249.addWidget(self.station5_io_reject_conveyor_sensor)

        self.station5_io_reject_conveyor_sensor_state = QLabel(self.group_boxing)
        self.station5_io_reject_conveyor_sensor_state.setObjectName(u"station5_io_reject_conveyor_sensor_state")
        self.station5_io_reject_conveyor_sensor_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_249.addWidget(self.station5_io_reject_conveyor_sensor_state)


        self.horizontalLayout_251.addLayout(self.horizontalLayout_249)

        self.horizontalLayout_250 = QHBoxLayout()
        self.horizontalLayout_250.setSpacing(10)
        self.horizontalLayout_250.setObjectName(u"horizontalLayout_250")
        self.horizontalLayout_250.setContentsMargins(5, 5, 5, 5)
        self.label_236 = QLabel(self.group_boxing)
        self.label_236.setObjectName(u"label_236")
        sizePolicy.setHeightForWidth(self.label_236.sizePolicy().hasHeightForWidth())
        self.label_236.setSizePolicy(sizePolicy)
        self.label_236.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_250.addWidget(self.label_236)

        self.station5_io_product_exit_conveyor = QSpinBox(self.group_boxing)
        self.station5_io_product_exit_conveyor.setObjectName(u"station5_io_product_exit_conveyor")
        self.station5_io_product_exit_conveyor.setMinimumSize(QSize(50, 0))
        self.station5_io_product_exit_conveyor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_product_exit_conveyor.setMinimum(1)
        self.station5_io_product_exit_conveyor.setValue(7)

        self.horizontalLayout_250.addWidget(self.station5_io_product_exit_conveyor)

        self.station5_io_product_exit_conveyor_state = QLabel(self.group_boxing)
        self.station5_io_product_exit_conveyor_state.setObjectName(u"station5_io_product_exit_conveyor_state")
        self.station5_io_product_exit_conveyor_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_250.addWidget(self.station5_io_product_exit_conveyor_state)


        self.horizontalLayout_251.addLayout(self.horizontalLayout_250)


        self.verticalLayout_48.addLayout(self.horizontalLayout_251)

        self.horizontalLayout_246 = QHBoxLayout()
        self.horizontalLayout_246.setSpacing(10)
        self.horizontalLayout_246.setObjectName(u"horizontalLayout_246")
        self.horizontalLayout_246.setContentsMargins(5, 5, 5, 5)
        self.label_234 = QLabel(self.group_boxing)
        self.label_234.setObjectName(u"label_234")
        sizePolicy5.setHeightForWidth(self.label_234.sizePolicy().hasHeightForWidth())
        self.label_234.setSizePolicy(sizePolicy5)
        self.label_234.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_246.addWidget(self.label_234)

        self.station5_io_box_cylinder_actuate = QSpinBox(self.group_boxing)
        self.station5_io_box_cylinder_actuate.setObjectName(u"station5_io_box_cylinder_actuate")
        sizePolicy1.setHeightForWidth(self.station5_io_box_cylinder_actuate.sizePolicy().hasHeightForWidth())
        self.station5_io_box_cylinder_actuate.setSizePolicy(sizePolicy1)
        self.station5_io_box_cylinder_actuate.setMinimumSize(QSize(50, 0))
        self.station5_io_box_cylinder_actuate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_io_box_cylinder_actuate.setMinimum(1)
        self.station5_io_box_cylinder_actuate.setMaximum(16)
        self.station5_io_box_cylinder_actuate.setValue(6)

        self.horizontalLayout_246.addWidget(self.station5_io_box_cylinder_actuate)

        self.station5_io_box_cylinder_actuate_state = QLabel(self.group_boxing)
        self.station5_io_box_cylinder_actuate_state.setObjectName(u"station5_io_box_cylinder_actuate_state")
        self.station5_io_box_cylinder_actuate_state.setFont(font2)
        self.station5_io_box_cylinder_actuate_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_246.addWidget(self.station5_io_box_cylinder_actuate_state)

        self.station5_io_box_cylinder_actuate_btn = QToolButton(self.group_boxing)
        self.station5_io_box_cylinder_actuate_btn.setObjectName(u"station5_io_box_cylinder_actuate_btn")
        self.station5_io_box_cylinder_actuate_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_246.addWidget(self.station5_io_box_cylinder_actuate_btn)


        self.verticalLayout_48.addLayout(self.horizontalLayout_246)


        self.verticalLayout_57.addWidget(self.group_boxing)


        self.verticalLayout_59.addWidget(self.groupBox_33)

        self.groupBox_58 = QGroupBox(self.tab_station5)
        self.groupBox_58.setObjectName(u"groupBox_58")
        self.horizontalLayout_68 = QHBoxLayout(self.groupBox_58)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.groupBox_53 = QGroupBox(self.groupBox_58)
        self.groupBox_53.setObjectName(u"groupBox_53")
        self.verticalLayout_58 = QVBoxLayout(self.groupBox_53)
        self.verticalLayout_58.setSpacing(10)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(30, 15, 30, 15)
        self.radio_unload_binning = QRadioButton(self.groupBox_53)
        self.radio_unload_binning.setObjectName(u"radio_unload_binning")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.radio_unload_binning.setFont(font3)

        self.verticalLayout_58.addWidget(self.radio_unload_binning)

        self.radio_unload_boxing = QRadioButton(self.groupBox_53)
        self.radio_unload_boxing.setObjectName(u"radio_unload_boxing")
        self.radio_unload_boxing.setFont(font3)

        self.verticalLayout_58.addWidget(self.radio_unload_boxing)


        self.horizontalLayout_68.addWidget(self.groupBox_53)

        self.box_binning_counter = QGroupBox(self.groupBox_58)
        self.box_binning_counter.setObjectName(u"box_binning_counter")
        self.verticalLayout_61 = QVBoxLayout(self.box_binning_counter)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.station5_en_binning_track = QCheckBox(self.box_binning_counter)
        self.station5_en_binning_track.setObjectName(u"station5_en_binning_track")

        self.verticalLayout_61.addWidget(self.station5_en_binning_track)

        self.horizontalLayout_227 = QHBoxLayout()
        self.horizontalLayout_227.setSpacing(15)
        self.horizontalLayout_227.setObjectName(u"horizontalLayout_227")
        self.label_5 = QLabel(self.box_binning_counter)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_227.addWidget(self.label_5)

        self.station5_bin_full_count = QSpinBox(self.box_binning_counter)
        self.station5_bin_full_count.setObjectName(u"station5_bin_full_count")
        self.station5_bin_full_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_227.addWidget(self.station5_bin_full_count)


        self.verticalLayout_61.addLayout(self.horizontalLayout_227)

        self.horizontalLayout_228 = QHBoxLayout()
        self.horizontalLayout_228.setObjectName(u"horizontalLayout_228")
        self.label_6 = QLabel(self.box_binning_counter)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_228.addWidget(self.label_6)

        self.station5_unload_num = QLabel(self.box_binning_counter)
        self.station5_unload_num.setObjectName(u"station5_unload_num")
        self.station5_unload_num.setFont(font3)
        self.station5_unload_num.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_228.addWidget(self.station5_unload_num)


        self.verticalLayout_61.addLayout(self.horizontalLayout_228)

        self.btn_reset_counter = QToolButton(self.box_binning_counter)
        self.btn_reset_counter.setObjectName(u"btn_reset_counter")
        sizePolicy5.setHeightForWidth(self.btn_reset_counter.sizePolicy().hasHeightForWidth())
        self.btn_reset_counter.setSizePolicy(sizePolicy5)

        self.verticalLayout_61.addWidget(self.btn_reset_counter)


        self.horizontalLayout_68.addWidget(self.box_binning_counter)


        self.verticalLayout_59.addWidget(self.groupBox_58)


        self.horizontalLayout_70.addLayout(self.verticalLayout_59)

        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setSpacing(30)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.group_valve_5 = QGroupBox(self.tab_station5)
        self.group_valve_5.setObjectName(u"group_valve_5")
        self.group_valve_5.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.group_valve_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_11 = QGroupBox(self.group_valve_5)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 120))
        self.verticalLayout_49 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_49.setSpacing(10)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setSpacing(10)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_119 = QLabel(self.groupBox_11)
        self.label_119.setObjectName(u"label_119")
        sizePolicy.setHeightForWidth(self.label_119.sizePolicy().hasHeightForWidth())
        self.label_119.setSizePolicy(sizePolicy)

        self.horizontalLayout_58.addWidget(self.label_119)

        self.station5_valve_lift_locate_up_1 = QSpinBox(self.groupBox_11)
        self.station5_valve_lift_locate_up_1.setObjectName(u"station5_valve_lift_locate_up_1")
        sizePolicy1.setHeightForWidth(self.station5_valve_lift_locate_up_1.sizePolicy().hasHeightForWidth())
        self.station5_valve_lift_locate_up_1.setSizePolicy(sizePolicy1)
        self.station5_valve_lift_locate_up_1.setMinimumSize(QSize(50, 0))
        self.station5_valve_lift_locate_up_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_valve_lift_locate_up_1.setMinimum(1)
        self.station5_valve_lift_locate_up_1.setMaximum(16)
        self.station5_valve_lift_locate_up_1.setValue(6)

        self.horizontalLayout_58.addWidget(self.station5_valve_lift_locate_up_1)

        self.station5_valve_lift_locate_up_1_state = QLabel(self.groupBox_11)
        self.station5_valve_lift_locate_up_1_state.setObjectName(u"station5_valve_lift_locate_up_1_state")
        self.station5_valve_lift_locate_up_1_state.setFont(font2)
        self.station5_valve_lift_locate_up_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_58.addWidget(self.station5_valve_lift_locate_up_1_state)

        self.station5_valve_lift_locate_up_1_btn = QToolButton(self.groupBox_11)
        self.station5_valve_lift_locate_up_1_btn.setObjectName(u"station5_valve_lift_locate_up_1_btn")
        self.station5_valve_lift_locate_up_1_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_58.addWidget(self.station5_valve_lift_locate_up_1_btn)


        self.verticalLayout_49.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setSpacing(10)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_120 = QLabel(self.groupBox_11)
        self.label_120.setObjectName(u"label_120")
        sizePolicy.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy)
        self.label_120.setMinimumSize(QSize(115, 0))

        self.horizontalLayout_61.addWidget(self.label_120)

        self.station5_valve_lift_locate_pre_1 = QSpinBox(self.groupBox_11)
        self.station5_valve_lift_locate_pre_1.setObjectName(u"station5_valve_lift_locate_pre_1")
        sizePolicy1.setHeightForWidth(self.station5_valve_lift_locate_pre_1.sizePolicy().hasHeightForWidth())
        self.station5_valve_lift_locate_pre_1.setSizePolicy(sizePolicy1)
        self.station5_valve_lift_locate_pre_1.setMinimumSize(QSize(50, 0))
        self.station5_valve_lift_locate_pre_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_valve_lift_locate_pre_1.setMinimum(1)
        self.station5_valve_lift_locate_pre_1.setMaximum(16)
        self.station5_valve_lift_locate_pre_1.setValue(6)

        self.horizontalLayout_61.addWidget(self.station5_valve_lift_locate_pre_1)

        self.station5_valve_lift_locate_pre_1_state = QLabel(self.groupBox_11)
        self.station5_valve_lift_locate_pre_1_state.setObjectName(u"station5_valve_lift_locate_pre_1_state")
        self.station5_valve_lift_locate_pre_1_state.setFont(font2)
        self.station5_valve_lift_locate_pre_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_61.addWidget(self.station5_valve_lift_locate_pre_1_state)

        self.station5_valve_lift_locate_pre_1_btn = QToolButton(self.groupBox_11)
        self.station5_valve_lift_locate_pre_1_btn.setObjectName(u"station5_valve_lift_locate_pre_1_btn")
        self.station5_valve_lift_locate_pre_1_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_61.addWidget(self.station5_valve_lift_locate_pre_1_btn)


        self.verticalLayout_49.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setSpacing(10)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_121 = QLabel(self.groupBox_11)
        self.label_121.setObjectName(u"label_121")
        sizePolicy.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy)

        self.horizontalLayout_62.addWidget(self.label_121)

        self.station5_valve_lift_locate_main_1 = QSpinBox(self.groupBox_11)
        self.station5_valve_lift_locate_main_1.setObjectName(u"station5_valve_lift_locate_main_1")
        sizePolicy1.setHeightForWidth(self.station5_valve_lift_locate_main_1.sizePolicy().hasHeightForWidth())
        self.station5_valve_lift_locate_main_1.setSizePolicy(sizePolicy1)
        self.station5_valve_lift_locate_main_1.setMinimumSize(QSize(50, 0))
        self.station5_valve_lift_locate_main_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_valve_lift_locate_main_1.setMinimum(1)
        self.station5_valve_lift_locate_main_1.setMaximum(16)
        self.station5_valve_lift_locate_main_1.setValue(6)

        self.horizontalLayout_62.addWidget(self.station5_valve_lift_locate_main_1)

        self.station5_valve_lift_locate_main_1_state = QLabel(self.groupBox_11)
        self.station5_valve_lift_locate_main_1_state.setObjectName(u"station5_valve_lift_locate_main_1_state")
        self.station5_valve_lift_locate_main_1_state.setFont(font2)
        self.station5_valve_lift_locate_main_1_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_62.addWidget(self.station5_valve_lift_locate_main_1_state)

        self.station5_valve_lift_locate_main_1_btn = QToolButton(self.groupBox_11)
        self.station5_valve_lift_locate_main_1_btn.setObjectName(u"station5_valve_lift_locate_main_1_btn")
        self.station5_valve_lift_locate_main_1_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_62.addWidget(self.station5_valve_lift_locate_main_1_btn)


        self.verticalLayout_49.addLayout(self.horizontalLayout_62)


        self.horizontalLayout.addWidget(self.groupBox_11)

        self.groupBox_52 = QGroupBox(self.group_valve_5)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_52)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_221 = QHBoxLayout()
        self.horizontalLayout_221.setSpacing(10)
        self.horizontalLayout_221.setObjectName(u"horizontalLayout_221")
        self.horizontalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.label_217 = QLabel(self.groupBox_52)
        self.label_217.setObjectName(u"label_217")
        sizePolicy.setHeightForWidth(self.label_217.sizePolicy().hasHeightForWidth())
        self.label_217.setSizePolicy(sizePolicy)
        self.label_217.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_221.addWidget(self.label_217)

        self.station5_valve_whirl_rotator = QSpinBox(self.groupBox_52)
        self.station5_valve_whirl_rotator.setObjectName(u"station5_valve_whirl_rotator")
        sizePolicy1.setHeightForWidth(self.station5_valve_whirl_rotator.sizePolicy().hasHeightForWidth())
        self.station5_valve_whirl_rotator.setSizePolicy(sizePolicy1)
        self.station5_valve_whirl_rotator.setMinimumSize(QSize(50, 0))
        self.station5_valve_whirl_rotator.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_valve_whirl_rotator.setMinimum(1)
        self.station5_valve_whirl_rotator.setMaximum(16)
        self.station5_valve_whirl_rotator.setValue(6)

        self.horizontalLayout_221.addWidget(self.station5_valve_whirl_rotator)

        self.station5_valve_whirl_rotator_state = QLabel(self.groupBox_52)
        self.station5_valve_whirl_rotator_state.setObjectName(u"station5_valve_whirl_rotator_state")
        self.station5_valve_whirl_rotator_state.setFont(font2)
        self.station5_valve_whirl_rotator_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_221.addWidget(self.station5_valve_whirl_rotator_state)

        self.station5_valve_whirl_rotator_btn = QToolButton(self.groupBox_52)
        self.station5_valve_whirl_rotator_btn.setObjectName(u"station5_valve_whirl_rotator_btn")
        self.station5_valve_whirl_rotator_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_221.addWidget(self.station5_valve_whirl_rotator_btn)


        self.verticalLayout_9.addLayout(self.horizontalLayout_221)

        self.horizontalLayout_222 = QHBoxLayout()
        self.horizontalLayout_222.setSpacing(10)
        self.horizontalLayout_222.setObjectName(u"horizontalLayout_222")
        self.horizontalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.label_221 = QLabel(self.groupBox_52)
        self.label_221.setObjectName(u"label_221")
        sizePolicy.setHeightForWidth(self.label_221.sizePolicy().hasHeightForWidth())
        self.label_221.setSizePolicy(sizePolicy)

        self.horizontalLayout_222.addWidget(self.label_221)

        self.station5_valve_label_air = QSpinBox(self.groupBox_52)
        self.station5_valve_label_air.setObjectName(u"station5_valve_label_air")
        sizePolicy1.setHeightForWidth(self.station5_valve_label_air.sizePolicy().hasHeightForWidth())
        self.station5_valve_label_air.setSizePolicy(sizePolicy1)
        self.station5_valve_label_air.setMinimumSize(QSize(50, 0))
        self.station5_valve_label_air.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_valve_label_air.setMinimum(1)
        self.station5_valve_label_air.setMaximum(16)
        self.station5_valve_label_air.setValue(6)

        self.horizontalLayout_222.addWidget(self.station5_valve_label_air)

        self.station5_valve_label_air_state = QLabel(self.groupBox_52)
        self.station5_valve_label_air_state.setObjectName(u"station5_valve_label_air_state")
        self.station5_valve_label_air_state.setFont(font2)
        self.station5_valve_label_air_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_222.addWidget(self.station5_valve_label_air_state)

        self.station5_valve_label_air_btn = QToolButton(self.groupBox_52)
        self.station5_valve_label_air_btn.setObjectName(u"station5_valve_label_air_btn")
        self.station5_valve_label_air_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_222.addWidget(self.station5_valve_label_air_btn)


        self.verticalLayout_9.addLayout(self.horizontalLayout_222)

        self.horizontalLayout_237 = QHBoxLayout()
        self.horizontalLayout_237.setSpacing(10)
        self.horizontalLayout_237.setObjectName(u"horizontalLayout_237")
        self.horizontalLayout_237.setContentsMargins(0, 0, 0, 0)
        self.label_227 = QLabel(self.groupBox_52)
        self.label_227.setObjectName(u"label_227")
        sizePolicy.setHeightForWidth(self.label_227.sizePolicy().hasHeightForWidth())
        self.label_227.setSizePolicy(sizePolicy)
        self.label_227.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_237.addWidget(self.label_227)

        self.station5_valve_box_clamp_engage = QSpinBox(self.groupBox_52)
        self.station5_valve_box_clamp_engage.setObjectName(u"station5_valve_box_clamp_engage")
        sizePolicy1.setHeightForWidth(self.station5_valve_box_clamp_engage.sizePolicy().hasHeightForWidth())
        self.station5_valve_box_clamp_engage.setSizePolicy(sizePolicy1)
        self.station5_valve_box_clamp_engage.setMinimumSize(QSize(50, 0))
        self.station5_valve_box_clamp_engage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_valve_box_clamp_engage.setMinimum(1)
        self.station5_valve_box_clamp_engage.setMaximum(16)
        self.station5_valve_box_clamp_engage.setValue(6)

        self.horizontalLayout_237.addWidget(self.station5_valve_box_clamp_engage)

        self.station5_valve_box_clamp_engage_state = QLabel(self.groupBox_52)
        self.station5_valve_box_clamp_engage_state.setObjectName(u"station5_valve_box_clamp_engage_state")
        self.station5_valve_box_clamp_engage_state.setFont(font2)
        self.station5_valve_box_clamp_engage_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_237.addWidget(self.station5_valve_box_clamp_engage_state)

        self.station5_valve_box_clamp_engage_btn = QToolButton(self.groupBox_52)
        self.station5_valve_box_clamp_engage_btn.setObjectName(u"station5_valve_box_clamp_engage_btn")
        self.station5_valve_box_clamp_engage_btn.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_237.addWidget(self.station5_valve_box_clamp_engage_btn)


        self.verticalLayout_9.addLayout(self.horizontalLayout_237)


        self.horizontalLayout.addWidget(self.groupBox_52)


        self.verticalLayout_65.addWidget(self.group_valve_5)

        self.groupBox_2 = QGroupBox(self.tab_station5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_33 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(10, 10, 10, 10)
        self.groupBox_39 = QGroupBox(self.groupBox_2)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setMinimumSize(QSize(0, 250))
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_39)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.station5_labeler_enabled = QCheckBox(self.groupBox_39)
        self.station5_labeler_enabled.setObjectName(u"station5_labeler_enabled")
        self.station5_labeler_enabled.setFont(font3)

        self.verticalLayout_32.addWidget(self.station5_labeler_enabled)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setSpacing(50)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_32 = QLabel(self.groupBox_39)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_2.addWidget(self.label_32)

        self.station5_labeler_home_offset = QDoubleSpinBox(self.groupBox_39)
        self.station5_labeler_home_offset.setObjectName(u"station5_labeler_home_offset")
        self.station5_labeler_home_offset.setMaximumSize(QSize(100, 16777215))
        self.station5_labeler_home_offset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_labeler_home_offset.setMaximum(359.990000000000009)

        self.horizontalLayout_2.addWidget(self.station5_labeler_home_offset)


        self.horizontalLayout_59.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_33 = QLabel(self.groupBox_39)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_3.addWidget(self.label_33)

        self.station5_labeler_rot_per_revolution = QDoubleSpinBox(self.groupBox_39)
        self.station5_labeler_rot_per_revolution.setObjectName(u"station5_labeler_rot_per_revolution")
        self.station5_labeler_rot_per_revolution.setMaximumSize(QSize(100, 16777215))
        self.station5_labeler_rot_per_revolution.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_labeler_rot_per_revolution.setMaximum(359.990000000000009)

        self.horizontalLayout_3.addWidget(self.station5_labeler_rot_per_revolution)


        self.horizontalLayout_59.addLayout(self.horizontalLayout_3)


        self.verticalLayout_32.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setSpacing(50)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_35 = QLabel(self.groupBox_39)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_4.addWidget(self.label_35)

        self.station5_labeler_label_pitch = QDoubleSpinBox(self.groupBox_39)
        self.station5_labeler_label_pitch.setObjectName(u"station5_labeler_label_pitch")
        self.station5_labeler_label_pitch.setMaximumSize(QSize(100, 16777215))
        self.station5_labeler_label_pitch.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_labeler_label_pitch.setMaximum(359.990000000000009)

        self.horizontalLayout_4.addWidget(self.station5_labeler_label_pitch)


        self.horizontalLayout_54.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_36 = QLabel(self.groupBox_39)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_5.addWidget(self.label_36)

        self.station5_labeler_label_length = QDoubleSpinBox(self.groupBox_39)
        self.station5_labeler_label_length.setObjectName(u"station5_labeler_label_length")
        self.station5_labeler_label_length.setMaximumSize(QSize(100, 16777215))
        self.station5_labeler_label_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_labeler_label_length.setMaximum(359.990000000000009)

        self.horizontalLayout_5.addWidget(self.station5_labeler_label_length)


        self.horizontalLayout_54.addLayout(self.horizontalLayout_5)


        self.verticalLayout_32.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setSpacing(50)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_37 = QLabel(self.groupBox_39)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_6.addWidget(self.label_37)

        self.station5_labeler_sensor_timeout = QDoubleSpinBox(self.groupBox_39)
        self.station5_labeler_sensor_timeout.setObjectName(u"station5_labeler_sensor_timeout")
        self.station5_labeler_sensor_timeout.setMaximumSize(QSize(100, 16777215))
        self.station5_labeler_sensor_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_labeler_sensor_timeout.setMaximum(359.990000000000009)

        self.horizontalLayout_6.addWidget(self.station5_labeler_sensor_timeout)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_38 = QLabel(self.groupBox_39)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_7.addWidget(self.label_38)

        self.station5_labeler_sensor_offset = QDoubleSpinBox(self.groupBox_39)
        self.station5_labeler_sensor_offset.setObjectName(u"station5_labeler_sensor_offset")
        self.station5_labeler_sensor_offset.setMaximumSize(QSize(100, 16777215))
        self.station5_labeler_sensor_offset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_labeler_sensor_offset.setMaximum(359.990000000000009)

        self.horizontalLayout_7.addWidget(self.station5_labeler_sensor_offset)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_7)


        self.verticalLayout_32.addLayout(self.horizontalLayout_64)


        self.verticalLayout_33.addWidget(self.groupBox_39)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setSpacing(50)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.groupBox_38 = QGroupBox(self.groupBox_2)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_38)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setSpacing(10)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(5, 5, 5, 5)
        self.label_168 = QLabel(self.groupBox_38)
        self.label_168.setObjectName(u"label_168")
        sizePolicy.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy)

        self.horizontalLayout_161.addWidget(self.label_168)

        self.station5_labeler_io_label_applicator = QSpinBox(self.groupBox_38)
        self.station5_labeler_io_label_applicator.setObjectName(u"station5_labeler_io_label_applicator")
        sizePolicy1.setHeightForWidth(self.station5_labeler_io_label_applicator.sizePolicy().hasHeightForWidth())
        self.station5_labeler_io_label_applicator.setSizePolicy(sizePolicy1)
        self.station5_labeler_io_label_applicator.setMinimumSize(QSize(50, 0))
        self.station5_labeler_io_label_applicator.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_labeler_io_label_applicator.setMinimum(1)
        self.station5_labeler_io_label_applicator.setMaximum(16)
        self.station5_labeler_io_label_applicator.setValue(6)

        self.horizontalLayout_161.addWidget(self.station5_labeler_io_label_applicator)

        self.station5_labeler_io_label_applicator_state = QLabel(self.groupBox_38)
        self.station5_labeler_io_label_applicator_state.setObjectName(u"station5_labeler_io_label_applicator_state")
        self.station5_labeler_io_label_applicator_state.setFont(font2)
        self.station5_labeler_io_label_applicator_state.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout_161.addWidget(self.station5_labeler_io_label_applicator_state)


        self.verticalLayout_27.addLayout(self.horizontalLayout_161)


        self.horizontalLayout_78.addWidget(self.groupBox_38)

        self.groupBox_60 = QGroupBox(self.groupBox_2)
        self.groupBox_60.setObjectName(u"groupBox_60")
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_60)
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_139 = QLabel(self.groupBox_60)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_60.addWidget(self.label_139)

        self.station5_motor_address = QSpinBox(self.groupBox_60)
        self.station5_motor_address.setObjectName(u"station5_motor_address")
        sizePolicy1.setHeightForWidth(self.station5_motor_address.sizePolicy().hasHeightForWidth())
        self.station5_motor_address.setSizePolicy(sizePolicy1)
        self.station5_motor_address.setMinimumSize(QSize(50, 0))
        self.station5_motor_address.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_motor_address.setMinimum(0)
        self.station5_motor_address.setMaximum(7)
        self.station5_motor_address.setValue(7)

        self.horizontalLayout_60.addWidget(self.station5_motor_address)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_89)

        self.btn_station5_motor_test = QPushButton(self.groupBox_60)
        self.btn_station5_motor_test.setObjectName(u"btn_station5_motor_test")
        sizePolicy6.setHeightForWidth(self.btn_station5_motor_test.sizePolicy().hasHeightForWidth())
        self.btn_station5_motor_test.setSizePolicy(sizePolicy6)

        self.horizontalLayout_60.addWidget(self.btn_station5_motor_test)


        self.verticalLayout_34.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setSpacing(10)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(10, 10, 10, 10)
        self.label_123 = QLabel(self.groupBox_60)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_103.addWidget(self.label_123)

        self.station5_motor_speed_limit = QSpinBox(self.groupBox_60)
        self.station5_motor_speed_limit.setObjectName(u"station5_motor_speed_limit")
        self.station5_motor_speed_limit.setMaximumSize(QSize(80, 16777215))
        self.station5_motor_speed_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.station5_motor_speed_limit.setMinimum(1)
        self.station5_motor_speed_limit.setMaximum(1080)
        self.station5_motor_speed_limit.setValue(150)

        self.horizontalLayout_103.addWidget(self.station5_motor_speed_limit)

        self.horizontalSpacer_118 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_118)


        self.verticalLayout_34.addLayout(self.horizontalLayout_103)


        self.horizontalLayout_78.addWidget(self.groupBox_60)


        self.verticalLayout_33.addLayout(self.horizontalLayout_78)


        self.verticalLayout_65.addWidget(self.groupBox_2)


        self.horizontalLayout_70.addLayout(self.verticalLayout_65)


        self.verticalLayout_66.addLayout(self.horizontalLayout_70)

        self.tabWidget.addTab(self.tab_station5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_43 = QGroupBox(self.tab)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.groupBox_43.setGeometry(QRect(30, 100, 391, 241))
        self.verticalLayout_50 = QVBoxLayout(self.groupBox_43)
        self.verticalLayout_50.setSpacing(10)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_226 = QHBoxLayout()
        self.horizontalLayout_226.setObjectName(u"horizontalLayout_226")
        self.label_220 = QLabel(self.groupBox_43)
        self.label_220.setObjectName(u"label_220")
        sizePolicy.setHeightForWidth(self.label_220.sizePolicy().hasHeightForWidth())
        self.label_220.setSizePolicy(sizePolicy)

        self.horizontalLayout_226.addWidget(self.label_220)

        self.pallet_count = QSpinBox(self.groupBox_43)
        self.pallet_count.setObjectName(u"pallet_count")
        self.pallet_count.setMinimumSize(QSize(0, 25))
        self.pallet_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pallet_count.setMinimum(1)
        self.pallet_count.setMaximum(20)

        self.horizontalLayout_226.addWidget(self.pallet_count)


        self.verticalLayout_50.addLayout(self.horizontalLayout_226)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.label_186 = QLabel(self.groupBox_43)
        self.label_186.setObjectName(u"label_186")
        sizePolicy.setHeightForWidth(self.label_186.sizePolicy().hasHeightForWidth())
        self.label_186.setSizePolicy(sizePolicy)

        self.horizontalLayout_128.addWidget(self.label_186)

        self.pallet_startup_timeout = QDoubleSpinBox(self.groupBox_43)
        self.pallet_startup_timeout.setObjectName(u"pallet_startup_timeout")
        self.pallet_startup_timeout.setMinimumSize(QSize(0, 25))
        self.pallet_startup_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pallet_startup_timeout.setDecimals(1)
        self.pallet_startup_timeout.setValue(0.500000000000000)

        self.horizontalLayout_128.addWidget(self.pallet_startup_timeout)


        self.verticalLayout_50.addLayout(self.horizontalLayout_128)

        self.horizontalLayout_174 = QHBoxLayout()
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.label_187 = QLabel(self.groupBox_43)
        self.label_187.setObjectName(u"label_187")
        sizePolicy.setHeightForWidth(self.label_187.sizePolicy().hasHeightForWidth())
        self.label_187.setSizePolicy(sizePolicy)

        self.horizontalLayout_174.addWidget(self.label_187)

        self.pallet_gate_actuation_time = QDoubleSpinBox(self.groupBox_43)
        self.pallet_gate_actuation_time.setObjectName(u"pallet_gate_actuation_time")
        self.pallet_gate_actuation_time.setMinimumSize(QSize(0, 25))
        self.pallet_gate_actuation_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pallet_gate_actuation_time.setDecimals(1)
        self.pallet_gate_actuation_time.setValue(0.500000000000000)

        self.horizontalLayout_174.addWidget(self.pallet_gate_actuation_time)


        self.verticalLayout_50.addLayout(self.horizontalLayout_174)

        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.label_188 = QLabel(self.groupBox_43)
        self.label_188.setObjectName(u"label_188")
        sizePolicy.setHeightForWidth(self.label_188.sizePolicy().hasHeightForWidth())
        self.label_188.setSizePolicy(sizePolicy)

        self.horizontalLayout_175.addWidget(self.label_188)

        self.pallet_main_gate_on_delay = QDoubleSpinBox(self.groupBox_43)
        self.pallet_main_gate_on_delay.setObjectName(u"pallet_main_gate_on_delay")
        self.pallet_main_gate_on_delay.setMinimumSize(QSize(0, 25))
        self.pallet_main_gate_on_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pallet_main_gate_on_delay.setDecimals(1)
        self.pallet_main_gate_on_delay.setValue(0.500000000000000)

        self.horizontalLayout_175.addWidget(self.pallet_main_gate_on_delay)


        self.verticalLayout_50.addLayout(self.horizontalLayout_175)

        self.groupBox_44 = QGroupBox(self.tab)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.groupBox_44.setGeometry(QRect(430, 40, 421, 361))
        self.verticalLayout_52 = QVBoxLayout(self.groupBox_44)
        self.verticalLayout_52.setSpacing(10)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(15, 15, 15, 15)
        self.label_3 = QLabel(self.groupBox_44)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_52.addWidget(self.label_3)

        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(20, -1, -1, -1)
        self.label_189 = QLabel(self.groupBox_44)
        self.label_189.setObjectName(u"label_189")
        sizePolicy.setHeightForWidth(self.label_189.sizePolicy().hasHeightForWidth())
        self.label_189.setSizePolicy(sizePolicy)

        self.horizontalLayout_176.addWidget(self.label_189)

        self.pallet_spacing_1 = QSpinBox(self.groupBox_44)
        self.pallet_spacing_1.setObjectName(u"pallet_spacing_1")
        sizePolicy6.setHeightForWidth(self.pallet_spacing_1.sizePolicy().hasHeightForWidth())
        self.pallet_spacing_1.setSizePolicy(sizePolicy6)
        self.pallet_spacing_1.setMinimumSize(QSize(0, 30))
        self.pallet_spacing_1.setValue(1)

        self.horizontalLayout_176.addWidget(self.pallet_spacing_1)


        self.verticalLayout_52.addLayout(self.horizontalLayout_176)

        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(20, -1, -1, -1)
        self.label_190 = QLabel(self.groupBox_44)
        self.label_190.setObjectName(u"label_190")
        sizePolicy.setHeightForWidth(self.label_190.sizePolicy().hasHeightForWidth())
        self.label_190.setSizePolicy(sizePolicy)

        self.horizontalLayout_177.addWidget(self.label_190)

        self.pallet_spacing_2 = QSpinBox(self.groupBox_44)
        self.pallet_spacing_2.setObjectName(u"pallet_spacing_2")
        sizePolicy6.setHeightForWidth(self.pallet_spacing_2.sizePolicy().hasHeightForWidth())
        self.pallet_spacing_2.setSizePolicy(sizePolicy6)
        self.pallet_spacing_2.setMinimumSize(QSize(0, 30))
        self.pallet_spacing_2.setValue(0)

        self.horizontalLayout_177.addWidget(self.pallet_spacing_2)


        self.verticalLayout_52.addLayout(self.horizontalLayout_177)

        self.horizontalLayout_178 = QHBoxLayout()
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(20, -1, -1, -1)
        self.label_191 = QLabel(self.groupBox_44)
        self.label_191.setObjectName(u"label_191")
        sizePolicy.setHeightForWidth(self.label_191.sizePolicy().hasHeightForWidth())
        self.label_191.setSizePolicy(sizePolicy)

        self.horizontalLayout_178.addWidget(self.label_191)

        self.pallet_spacing_3 = QSpinBox(self.groupBox_44)
        self.pallet_spacing_3.setObjectName(u"pallet_spacing_3")
        sizePolicy6.setHeightForWidth(self.pallet_spacing_3.sizePolicy().hasHeightForWidth())
        self.pallet_spacing_3.setSizePolicy(sizePolicy6)
        self.pallet_spacing_3.setMinimumSize(QSize(0, 30))
        self.pallet_spacing_3.setValue(1)

        self.horizontalLayout_178.addWidget(self.pallet_spacing_3)


        self.verticalLayout_52.addLayout(self.horizontalLayout_178)

        self.horizontalLayout_179 = QHBoxLayout()
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(20, -1, -1, -1)
        self.label_192 = QLabel(self.groupBox_44)
        self.label_192.setObjectName(u"label_192")
        sizePolicy.setHeightForWidth(self.label_192.sizePolicy().hasHeightForWidth())
        self.label_192.setSizePolicy(sizePolicy)

        self.horizontalLayout_179.addWidget(self.label_192)

        self.pallet_spacing_4 = QSpinBox(self.groupBox_44)
        self.pallet_spacing_4.setObjectName(u"pallet_spacing_4")
        sizePolicy6.setHeightForWidth(self.pallet_spacing_4.sizePolicy().hasHeightForWidth())
        self.pallet_spacing_4.setSizePolicy(sizePolicy6)
        self.pallet_spacing_4.setMinimumSize(QSize(0, 30))
        self.pallet_spacing_4.setValue(2)

        self.horizontalLayout_179.addWidget(self.pallet_spacing_4)


        self.verticalLayout_52.addLayout(self.horizontalLayout_179)

        self.horizontalLayout_180 = QHBoxLayout()
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(20, -1, -1, -1)
        self.label_193 = QLabel(self.groupBox_44)
        self.label_193.setObjectName(u"label_193")
        sizePolicy.setHeightForWidth(self.label_193.sizePolicy().hasHeightForWidth())
        self.label_193.setSizePolicy(sizePolicy)

        self.horizontalLayout_180.addWidget(self.label_193)

        self.pallet_spacing_5 = QSpinBox(self.groupBox_44)
        self.pallet_spacing_5.setObjectName(u"pallet_spacing_5")
        sizePolicy6.setHeightForWidth(self.pallet_spacing_5.sizePolicy().hasHeightForWidth())
        self.pallet_spacing_5.setSizePolicy(sizePolicy6)
        self.pallet_spacing_5.setMinimumSize(QSize(0, 30))
        self.pallet_spacing_5.setValue(4)

        self.horizontalLayout_180.addWidget(self.pallet_spacing_5)


        self.verticalLayout_52.addLayout(self.horizontalLayout_180)

        self.horizontalLayout_181 = QHBoxLayout()
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(20, -1, -1, -1)
        self.label_194 = QLabel(self.groupBox_44)
        self.label_194.setObjectName(u"label_194")
        sizePolicy.setHeightForWidth(self.label_194.sizePolicy().hasHeightForWidth())
        self.label_194.setSizePolicy(sizePolicy)

        self.horizontalLayout_181.addWidget(self.label_194)

        self.pallet_spacing_6 = QSpinBox(self.groupBox_44)
        self.pallet_spacing_6.setObjectName(u"pallet_spacing_6")
        sizePolicy6.setHeightForWidth(self.pallet_spacing_6.sizePolicy().hasHeightForWidth())
        self.pallet_spacing_6.setSizePolicy(sizePolicy6)
        self.pallet_spacing_6.setMinimumSize(QSize(0, 30))
        self.pallet_spacing_6.setValue(3)

        self.horizontalLayout_181.addWidget(self.pallet_spacing_6)


        self.verticalLayout_52.addLayout(self.horizontalLayout_181)

        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(20, -1, -1, -1)
        self.label_195 = QLabel(self.groupBox_44)
        self.label_195.setObjectName(u"label_195")
        sizePolicy.setHeightForWidth(self.label_195.sizePolicy().hasHeightForWidth())
        self.label_195.setSizePolicy(sizePolicy)

        self.horizontalLayout_182.addWidget(self.label_195)

        self.pallet_spacing_7 = QSpinBox(self.groupBox_44)
        self.pallet_spacing_7.setObjectName(u"pallet_spacing_7")
        sizePolicy6.setHeightForWidth(self.pallet_spacing_7.sizePolicy().hasHeightForWidth())
        self.pallet_spacing_7.setSizePolicy(sizePolicy6)
        self.pallet_spacing_7.setMinimumSize(QSize(0, 30))
        self.pallet_spacing_7.setValue(6)

        self.horizontalLayout_182.addWidget(self.pallet_spacing_7)


        self.verticalLayout_52.addLayout(self.horizontalLayout_182)

        self.groupBox_45 = QGroupBox(self.tab)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.groupBox_45.setGeometry(QRect(880, 40, 371, 361))
        self.verticalLayout_53 = QVBoxLayout(self.groupBox_45)
        self.verticalLayout_53.setSpacing(10)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(15, 15, 15, 15)
        self.label_4 = QLabel(self.groupBox_45)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_53.addWidget(self.label_4)

        self.horizontalLayout_190 = QHBoxLayout()
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(20, -1, -1, -1)
        self.label_196 = QLabel(self.groupBox_45)
        self.label_196.setObjectName(u"label_196")
        sizePolicy.setHeightForWidth(self.label_196.sizePolicy().hasHeightForWidth())
        self.label_196.setSizePolicy(sizePolicy)

        self.horizontalLayout_190.addWidget(self.label_196)

        self.pallet_release_delay_1 = QSpinBox(self.groupBox_45)
        self.pallet_release_delay_1.setObjectName(u"pallet_release_delay_1")
        sizePolicy6.setHeightForWidth(self.pallet_release_delay_1.sizePolicy().hasHeightForWidth())
        self.pallet_release_delay_1.setSizePolicy(sizePolicy6)
        self.pallet_release_delay_1.setMinimumSize(QSize(0, 30))
        self.pallet_release_delay_1.setValue(1)

        self.horizontalLayout_190.addWidget(self.pallet_release_delay_1)


        self.verticalLayout_53.addLayout(self.horizontalLayout_190)

        self.horizontalLayout_191 = QHBoxLayout()
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.horizontalLayout_191.setContentsMargins(20, -1, -1, -1)
        self.label_197 = QLabel(self.groupBox_45)
        self.label_197.setObjectName(u"label_197")
        sizePolicy.setHeightForWidth(self.label_197.sizePolicy().hasHeightForWidth())
        self.label_197.setSizePolicy(sizePolicy)

        self.horizontalLayout_191.addWidget(self.label_197)

        self.pallet_release_delay_2 = QSpinBox(self.groupBox_45)
        self.pallet_release_delay_2.setObjectName(u"pallet_release_delay_2")
        sizePolicy6.setHeightForWidth(self.pallet_release_delay_2.sizePolicy().hasHeightForWidth())
        self.pallet_release_delay_2.setSizePolicy(sizePolicy6)
        self.pallet_release_delay_2.setMinimumSize(QSize(0, 30))
        self.pallet_release_delay_2.setValue(1)

        self.horizontalLayout_191.addWidget(self.pallet_release_delay_2)


        self.verticalLayout_53.addLayout(self.horizontalLayout_191)

        self.horizontalLayout_192 = QHBoxLayout()
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(20, -1, -1, -1)
        self.label_198 = QLabel(self.groupBox_45)
        self.label_198.setObjectName(u"label_198")
        sizePolicy.setHeightForWidth(self.label_198.sizePolicy().hasHeightForWidth())
        self.label_198.setSizePolicy(sizePolicy)

        self.horizontalLayout_192.addWidget(self.label_198)

        self.pallet_release_delay_3 = QSpinBox(self.groupBox_45)
        self.pallet_release_delay_3.setObjectName(u"pallet_release_delay_3")
        sizePolicy6.setHeightForWidth(self.pallet_release_delay_3.sizePolicy().hasHeightForWidth())
        self.pallet_release_delay_3.setSizePolicy(sizePolicy6)
        self.pallet_release_delay_3.setMinimumSize(QSize(0, 30))
        self.pallet_release_delay_3.setValue(1)

        self.horizontalLayout_192.addWidget(self.pallet_release_delay_3)


        self.verticalLayout_53.addLayout(self.horizontalLayout_192)

        self.horizontalLayout_193 = QHBoxLayout()
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(20, -1, -1, -1)
        self.label_199 = QLabel(self.groupBox_45)
        self.label_199.setObjectName(u"label_199")
        sizePolicy.setHeightForWidth(self.label_199.sizePolicy().hasHeightForWidth())
        self.label_199.setSizePolicy(sizePolicy)

        self.horizontalLayout_193.addWidget(self.label_199)

        self.pallet_release_delay_4 = QSpinBox(self.groupBox_45)
        self.pallet_release_delay_4.setObjectName(u"pallet_release_delay_4")
        sizePolicy6.setHeightForWidth(self.pallet_release_delay_4.sizePolicy().hasHeightForWidth())
        self.pallet_release_delay_4.setSizePolicy(sizePolicy6)
        self.pallet_release_delay_4.setMinimumSize(QSize(0, 30))
        self.pallet_release_delay_4.setValue(1)

        self.horizontalLayout_193.addWidget(self.pallet_release_delay_4)


        self.verticalLayout_53.addLayout(self.horizontalLayout_193)

        self.horizontalLayout_194 = QHBoxLayout()
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(20, -1, -1, -1)
        self.label_200 = QLabel(self.groupBox_45)
        self.label_200.setObjectName(u"label_200")
        sizePolicy.setHeightForWidth(self.label_200.sizePolicy().hasHeightForWidth())
        self.label_200.setSizePolicy(sizePolicy)

        self.horizontalLayout_194.addWidget(self.label_200)

        self.pallet_release_delay_5 = QSpinBox(self.groupBox_45)
        self.pallet_release_delay_5.setObjectName(u"pallet_release_delay_5")
        sizePolicy6.setHeightForWidth(self.pallet_release_delay_5.sizePolicy().hasHeightForWidth())
        self.pallet_release_delay_5.setSizePolicy(sizePolicy6)
        self.pallet_release_delay_5.setMinimumSize(QSize(0, 30))
        self.pallet_release_delay_5.setValue(1)

        self.horizontalLayout_194.addWidget(self.pallet_release_delay_5)


        self.verticalLayout_53.addLayout(self.horizontalLayout_194)

        self.horizontalLayout_195 = QHBoxLayout()
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(20, -1, -1, -1)
        self.label_201 = QLabel(self.groupBox_45)
        self.label_201.setObjectName(u"label_201")
        sizePolicy.setHeightForWidth(self.label_201.sizePolicy().hasHeightForWidth())
        self.label_201.setSizePolicy(sizePolicy)

        self.horizontalLayout_195.addWidget(self.label_201)

        self.pallet_release_delay_6 = QSpinBox(self.groupBox_45)
        self.pallet_release_delay_6.setObjectName(u"pallet_release_delay_6")
        sizePolicy6.setHeightForWidth(self.pallet_release_delay_6.sizePolicy().hasHeightForWidth())
        self.pallet_release_delay_6.setSizePolicy(sizePolicy6)
        self.pallet_release_delay_6.setMinimumSize(QSize(0, 30))
        self.pallet_release_delay_6.setValue(1)

        self.horizontalLayout_195.addWidget(self.pallet_release_delay_6)


        self.verticalLayout_53.addLayout(self.horizontalLayout_195)

        self.horizontalLayout_196 = QHBoxLayout()
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(20, -1, -1, -1)
        self.label_202 = QLabel(self.groupBox_45)
        self.label_202.setObjectName(u"label_202")
        sizePolicy.setHeightForWidth(self.label_202.sizePolicy().hasHeightForWidth())
        self.label_202.setSizePolicy(sizePolicy)

        self.horizontalLayout_196.addWidget(self.label_202)

        self.pallet_release_delay_7 = QSpinBox(self.groupBox_45)
        self.pallet_release_delay_7.setObjectName(u"pallet_release_delay_7")
        sizePolicy6.setHeightForWidth(self.pallet_release_delay_7.sizePolicy().hasHeightForWidth())
        self.pallet_release_delay_7.setSizePolicy(sizePolicy6)
        self.pallet_release_delay_7.setMinimumSize(QSize(0, 30))
        self.pallet_release_delay_7.setValue(1)

        self.horizontalLayout_196.addWidget(self.pallet_release_delay_7)


        self.verticalLayout_53.addLayout(self.horizontalLayout_196)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 554, 32))
        self.horizontalLayout_234 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_234.setSpacing(20)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.horizontalLayout_234.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(240, 0))

        self.horizontalLayout_234.addWidget(self.label_15)

        self.final_vision_cognex = QLineEdit(self.layoutWidget)
        self.final_vision_cognex.setObjectName(u"final_vision_cognex")
        self.final_vision_cognex.setMaximumSize(QSize(150, 16777215))
        self.final_vision_cognex.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_234.addWidget(self.final_vision_cognex)

        self.btn_final_vision_cognex_test = QPushButton(self.layoutWidget)
        self.btn_final_vision_cognex_test.setObjectName(u"btn_final_vision_cognex_test")
        self.btn_final_vision_cognex_test.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_234.addWidget(self.btn_final_vision_cognex_test)

        self.layoutWidget1234 = QWidget(self.tab_2)
        self.layoutWidget1234.setObjectName(u"layoutWidget1234")
        self.layoutWidget1234.setGeometry(QRect(30, 180, 841, 318))
        self.horizontalLayout_235 = QHBoxLayout(self.layoutWidget1234)
        self.horizontalLayout_235.setSpacing(30)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalLayout_235.setContentsMargins(0, 0, 0, 0)
        self.groupBox_56 = QGroupBox(self.layoutWidget1234)
        self.groupBox_56.setObjectName(u"groupBox_56")
        self.verticalLayout_63 = QVBoxLayout(self.groupBox_56)
        self.verticalLayout_63.setSpacing(10)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(30, 30, 30, 30)
        self.final_vision_trigger_open = QCheckBox(self.groupBox_56)
        self.final_vision_trigger_open.setObjectName(u"final_vision_trigger_open")
        self.final_vision_trigger_open.setMinimumSize(QSize(0, 30))

        self.verticalLayout_63.addWidget(self.final_vision_trigger_open)

        self.final_vision_dial_open = QCheckBox(self.groupBox_56)
        self.final_vision_dial_open.setObjectName(u"final_vision_dial_open")
        self.final_vision_dial_open.setMinimumSize(QSize(0, 30))

        self.verticalLayout_63.addWidget(self.final_vision_dial_open)

        self.final_vision_support_arm_open = QCheckBox(self.groupBox_56)
        self.final_vision_support_arm_open.setObjectName(u"final_vision_support_arm_open")
        self.final_vision_support_arm_open.setMinimumSize(QSize(0, 30))

        self.verticalLayout_63.addWidget(self.final_vision_support_arm_open)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_2)


        self.horizontalLayout_235.addWidget(self.groupBox_56)

        self.groupBox_57 = QGroupBox(self.layoutWidget1234)
        self.groupBox_57.setObjectName(u"groupBox_57")
        self.verticalLayout_64 = QVBoxLayout(self.groupBox_57)
        self.verticalLayout_64.setSpacing(15)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(20, 20, 20, 20)
        self.final_vision_pinion_final = QCheckBox(self.groupBox_57)
        self.final_vision_pinion_final.setObjectName(u"final_vision_pinion_final")
        self.final_vision_pinion_final.setMinimumSize(QSize(0, 30))

        self.verticalLayout_64.addWidget(self.final_vision_pinion_final)

        self.final_vision_dial_final = QCheckBox(self.groupBox_57)
        self.final_vision_dial_final.setObjectName(u"final_vision_dial_final")
        self.final_vision_dial_final.setMinimumSize(QSize(0, 30))

        self.verticalLayout_64.addWidget(self.final_vision_dial_final)

        self.final_vision_handle_gaps_final = QCheckBox(self.groupBox_57)
        self.final_vision_handle_gaps_final.setObjectName(u"final_vision_handle_gaps_final")
        self.final_vision_handle_gaps_final.setMinimumSize(QSize(0, 30))

        self.verticalLayout_64.addWidget(self.final_vision_handle_gaps_final)

        self.final_vision_support_arm_final = QCheckBox(self.groupBox_57)
        self.final_vision_support_arm_final.setObjectName(u"final_vision_support_arm_final")
        self.final_vision_support_arm_final.setMinimumSize(QSize(0, 30))

        self.verticalLayout_64.addWidget(self.final_vision_support_arm_final)

        self.final_vision_hopper_final = QCheckBox(self.groupBox_57)
        self.final_vision_hopper_final.setObjectName(u"final_vision_hopper_final")
        self.final_vision_hopper_final.setMinimumSize(QSize(0, 30))

        self.verticalLayout_64.addWidget(self.final_vision_hopper_final)

        self.final_vision_trigger_final = QCheckBox(self.groupBox_57)
        self.final_vision_trigger_final.setObjectName(u"final_vision_trigger_final")
        self.final_vision_trigger_final.setMinimumSize(QSize(0, 30))

        self.verticalLayout_64.addWidget(self.final_vision_trigger_final)


        self.horizontalLayout_235.addWidget(self.groupBox_57)

        self.tabWidget.addTab(self.tab_2, "")

        self.rootLayout.addWidget(self.tabWidget)

#if QT_CONFIG(shortcut)
        self.label_8.setBuddy(self.station1_robot)
        self.label_9.setBuddy(self.station1_robot)
        self.label_52.setBuddy(self.station1_robot)
        self.label_53.setBuddy(self.station1_robot)
        self.label_10.setBuddy(self.station1_robot)
        self.label_11.setBuddy(self.station1_robot)
        self.label_12.setBuddy(self.station1_robot)
        self.label_13.setBuddy(self.station1_robot)
        self.label_14.setBuddy(self.station1_robot)
        self.label_22.setBuddy(self.station1_robot)
        self.label_28.setBuddy(self.station1_robot)
        self.label_54.setBuddy(self.station1_robot)
        self.label_23.setBuddy(self.station1_robot)
        self.label_24.setBuddy(self.station1_robot)
        self.label_25.setBuddy(self.station1_robot)
        self.label_26.setBuddy(self.station1_robot)
        self.label_39.setBuddy(self.station1_robot)
        self.label_40.setBuddy(self.station1_robot)
        self.label_55.setBuddy(self.station1_robot)
        self.label_56.setBuddy(self.station1_robot)
        self.label_41.setBuddy(self.station1_robot)
        self.label_42.setBuddy(self.station1_robot)
        self.label_43.setBuddy(self.station1_robot)
        self.label_44.setBuddy(self.station1_robot)
        self.label_45.setBuddy(self.station1_robot)
        self.label_46.setBuddy(self.station1_robot)
        self.label_47.setBuddy(self.station1_robot)
        self.label_57.setBuddy(self.station1_robot)
        self.label_48.setBuddy(self.station1_robot)
        self.label_49.setBuddy(self.station1_robot)
        self.label_50.setBuddy(self.station1_robot)
        self.label_30.setBuddy(self.station1_robot)
        self.label_29.setBuddy(self.station1_robot)
        self.label_34.setBuddy(self.station1_robot)
        self.label_51.setBuddy(self.station1_robot)
        self.label_27.setBuddy(self.station1_robot)
        self.label_31.setBuddy(self.station1_robot)
        self.label_32.setBuddy(self.station1_robot)
        self.label_33.setBuddy(self.station1_robot)
        self.label_35.setBuddy(self.station1_robot)
        self.label_36.setBuddy(self.station1_robot)
        self.label_37.setBuddy(self.station1_robot)
        self.label_38.setBuddy(self.station1_robot)
        self.label_15.setBuddy(self.station1_robot)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SettingsDialog)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.groupBox_55.setTitle(QCoreApplication.translate("SettingsDialog", u"Miscellaneous", None))
        self.label_223.setText(QCoreApplication.translate("SettingsDialog", u"Main Air:", None))
        self.peripheral_io_main_air_state.setText("")
        self.peripheral_io_main_air_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_224.setText(QCoreApplication.translate("SettingsDialog", u"Main Conveyor:", None))
        self.peripheral_io_main_conveyor_state.setText("")
        self.peripheral_io_main_conveyor_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_225.setText(QCoreApplication.translate("SettingsDialog", u"Auxiliary Air:", None))
        self.peripheral_io_aux_air_state.setText("")
        self.peripheral_io_aux_air_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_222.setText(QCoreApplication.translate("SettingsDialog", u"Main Air Status:", None))
        self.peripheral_io_main_air_status_reverse_state.setText("")
        self.label_226.setText(QCoreApplication.translate("SettingsDialog", u"Auxiliary Air Status:", None))
        self.peripheral_io_aux_air_status_reverse_state.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("SettingsDialog", u"General", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SettingsDialog", u"Modules", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"Denso Robot:", None))
        self.station1_robot.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_robot.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_robot_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"Cognex:", None))
        self.station1_cognex.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_cognex.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_cognex_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_52.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Lift && Locate 2 - Grease):", None))
        self.station1_barcode_2.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_barcode_2.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_barcode_2_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_53.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Lift && Locate 3):", None))
        self.station1_barcode_3.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_barcode_3.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_barcode_3_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Wago IO:", None))
        self.station1_wago.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_wago.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_wago_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"FlexFeeders", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDialog", u"Cross Gear:", None))
        self.station1_feeders_cross_gear.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_feeders_cross_gear.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_feeders_cross_gear_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_12.setText(QCoreApplication.translate("SettingsDialog", u"Pinion:", None))
        self.station1_feeders_pinion.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_feeders_pinion.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_feeders_pinion_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_13.setText(QCoreApplication.translate("SettingsDialog", u"Crank Handle", None))
        self.station1_feeders_crank_handle.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_feeders_crank_handle.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_feeders_crank_handle_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_14.setText(QCoreApplication.translate("SettingsDialog", u"Ring Gear", None))
        self.station1_feeders_ring_gear.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station1_feeders_ring_gear.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station1_feeders_ring_gear_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SettingsDialog", u"Wago Input", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 2", None))
        self.label_103.setText(QCoreApplication.translate("SettingsDialog", u"Extended:", None))
        self.station1_io_lift_locate_extended_2_state.setText("")
        self.label_104.setText(QCoreApplication.translate("SettingsDialog", u"Retracted:", None))
        self.station1_io_lift_locate_retracted_2_state.setText("")
        self.label_105.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate:", None))
        self.station1_io_lift_locate_pre_2_state.setText("")
        self.label_106.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate:", None))
        self.station1_io_lift_locate_main_2_state.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 3", None))
        self.label_109.setText(QCoreApplication.translate("SettingsDialog", u"Extended:", None))
        self.station1_io_lift_locate_extended_3_state.setText("")
        self.label_110.setText(QCoreApplication.translate("SettingsDialog", u"Retracted:", None))
        self.station1_io_lift_locate_retracted_3_state.setText("")
        self.label_112.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate:", None))
        self.station1_io_lift_locate_main_3_state.setText("")
        self.groupBox_41.setTitle(QCoreApplication.translate("SettingsDialog", u"Whirl Rotator", None))
        self.label_115.setText(QCoreApplication.translate("SettingsDialog", u"CW:", None))
        self.station1_io_whirl_rotated_cw_state.setText("")
        self.label_122.setText(QCoreApplication.translate("SettingsDialog", u"CCW:", None))
        self.station1_io_whirl_rotated_ccw_state.setText("")
        self.label_130.setText(QCoreApplication.translate("SettingsDialog", u"Present:", None))
        self.station1_io_whirl_rotate_part_present_state.setText("")
        self.group_valve_1.setTitle(QCoreApplication.translate("SettingsDialog", u"Valve(DeviceNet)", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 2", None))
        self.label_124.setText(QCoreApplication.translate("SettingsDialog", u"Lift Up:", None))
        self.station1_valve_lift_locate_up_2_state.setText("")
        self.station1_valve_lift_locate_up_2_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_125.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate Open:", None))
        self.station1_valve_lift_locate_pre_2_state.setText("")
        self.station1_valve_lift_locate_pre_2_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_126.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate Open:", None))
        self.station1_valve_lift_locate_main_2_state.setText("")
        self.station1_valve_lift_locate_main_2_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 3", None))
        self.label_127.setText(QCoreApplication.translate("SettingsDialog", u"Lift Up:", None))
        self.station1_valve_lift_locate_up_3_state.setText("")
        self.station1_valve_lift_locate_up_3_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_131.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate Open:", None))
        self.station1_valve_lift_locate_main_3_state.setText("")
        self.station1_valve_lift_locate_main_3_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_203.setText(QCoreApplication.translate("SettingsDialog", u"Whirl Rotator:", None))
        self.station1_valve_whirl_rotator_state.setText("")
        self.station1_valve_whirl_rotator_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("SettingsDialog", u"Grease Dispenser", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("SettingsDialog", u"Wago Input/Output", None))
        self.label_117.setText(QCoreApplication.translate("SettingsDialog", u"Reservoir Full:", None))
        self.station1_io_reservoir_full_state.setText("")
        self.label_116.setText(QCoreApplication.translate("SettingsDialog", u"Reservoir Empty:", None))
        self.station1_io_reservoir_empty_state.setText("")
        self.label_107.setText(QCoreApplication.translate("SettingsDialog", u"Slide Retracted:", None))
        self.station1_io_grease_slide_retracted_state.setText("")
        self.label_108.setText(QCoreApplication.translate("SettingsDialog", u"Slide Extended:", None))
        self.station1_io_grease_slide_extended_state.setText("")
        self.label_118.setText(QCoreApplication.translate("SettingsDialog", u"Electrovalve to Grease Pump:", None))
        self.station1_io_electrovalve_to_alemite_ram_state.setText("")
        self.station1_io_electrovalve_to_alemite_ram_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("SettingsDialog", u"Manual Operations", None))
        self.btn_grease_inject.setText(QCoreApplication.translate("SettingsDialog", u"Inject", None))
        self.btn_grease_clear_error.setText(QCoreApplication.translate("SettingsDialog", u"Clear Greaser Error State", None))
        self.btn_grease_purge.setText(QCoreApplication.translate("SettingsDialog", u"Purge", None))
        self.btn_grease_refill.setText(QCoreApplication.translate("SettingsDialog", u"Re-fill Grease Reservoir", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"State:", None))
        self.station1_grease_dispenser_state.setText(QCoreApplication.translate("SettingsDialog", u"Idle", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("SettingsDialog", u"Parameters", None))
        self.label_138.setText(QCoreApplication.translate("SettingsDialog", u"Reservoir Back Pressure Delay:", None))
        self.label_179.setText(QCoreApplication.translate("SettingsDialog", u"Shot Chamber Filling Delay:", None))
        self.label_180.setText(QCoreApplication.translate("SettingsDialog", u"Depressurize Delay:", None))
        self.label_181.setText(QCoreApplication.translate("SettingsDialog", u"Open Spool Valve Delay:", None))
        self.label_182.setText(QCoreApplication.translate("SettingsDialog", u"Inject Delay:", None))
        self.label_183.setText(QCoreApplication.translate("SettingsDialog", u"Grease Reservoir Timeout:", None))
        self.label_184.setText(QCoreApplication.translate("SettingsDialog", u"Sensor Timeout:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("SettingsDialog", u"Valve(DeviceNet)", None))
        self.label_128.setText(QCoreApplication.translate("SettingsDialog", u"Retract Ejector Pistons:", None))
        self.station1_valve_grease_dispenser_retract_ejector_piston_state.setText("")
        self.station1_valve_grease_dispenser_retract_ejector_piston_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_132.setText(QCoreApplication.translate("SettingsDialog", u"Lower Grease Block:", None))
        self.station1_valve_grease_dispenser_lower_grease_block_state.setText("")
        self.station1_valve_grease_dispenser_lower_grease_block_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_133.setText(QCoreApplication.translate("SettingsDialog", u"Spool Valves - Open:", None))
        self.station1_valve_grease_spool_valve_state.setText("")
        self.station1_valve_grease_spool_valve_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_134.setText(QCoreApplication.translate("SettingsDialog", u"Canister Back Pressure:", None))
        self.station1_valve_grease_canister_back_pressure_state.setText("")
        self.station1_valve_grease_canister_back_pressure_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_135.setText(QCoreApplication.translate("SettingsDialog", u"Advance Ejector Pistons:", None))
        self.station1_valve_grease_dispenser_advance_ejector_piston_state.setText("")
        self.station1_valve_grease_dispenser_advance_ejector_piston_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_station1), QCoreApplication.translate("SettingsDialog", u"Station 1", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("SettingsDialog", u"Modules", None))
        self.label_22.setText(QCoreApplication.translate("SettingsDialog", u"Denso Robot:", None))
        self.station2_robot.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station2_robot.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station2_robot_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_28.setText(QCoreApplication.translate("SettingsDialog", u"Cognex:", None))
        self.station2_cognex.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station2_cognex.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station2_cognex_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_54.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Lift && Locate 4):", None))
        self.station2_barcode_4.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station2_barcode_4.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station2_barcode_4_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_23.setText(QCoreApplication.translate("SettingsDialog", u"Wago IO:", None))
        self.station2_wago.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station2_wago.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station2_wago_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SettingsDialog", u"FlexFeeders", None))
        self.label_24.setText(QCoreApplication.translate("SettingsDialog", u"Upper Housing:", None))
        self.station2_feeders_upper_housing.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station2_feeders_upper_housing.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station2_feeders_upper_housing_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_25.setText(QCoreApplication.translate("SettingsDialog", u"Crank Arm:", None))
        self.station2_feeders_crank_arm.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station2_feeders_crank_arm.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station2_feeders_crank_arm_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_26.setText(QCoreApplication.translate("SettingsDialog", u"Rotor:", None))
        self.station2_feeders_rotor.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station2_feeders_rotor.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station2_feeders_rotor_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("SettingsDialog", u"Wago Input", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 4", None))
        self.label_111.setText(QCoreApplication.translate("SettingsDialog", u"Extended:", None))
        self.station2_io_lift_locate_extended_4_state.setText("")
        self.label_113.setText(QCoreApplication.translate("SettingsDialog", u"Retracted:", None))
        self.station2_io_lift_locate_retracted_4_state.setText("")
        self.label_114.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate:", None))
        self.station2_io_lift_locate_pre_4_state.setText("")
        self.label_136.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate:", None))
        self.station2_io_lift_locate_main_4_state.setText("")
        self.group_valve_2.setTitle(QCoreApplication.translate("SettingsDialog", u"Valve(DeviceNet)", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 4", None))
        self.label_137.setText(QCoreApplication.translate("SettingsDialog", u"Lift Up:", None))
        self.station2_valve_lift_locate_up_4_state.setText("")
        self.station2_valve_lift_locate_up_4_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_140.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate Open:", None))
        self.station2_valve_lift_locate_pre_4_state.setText("")
        self.station2_valve_lift_locate_pre_4_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_141.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate Open:", None))
        self.station2_valve_lift_locate_main_4_state.setText("")
        self.station2_valve_lift_locate_main_4_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_station2), QCoreApplication.translate("SettingsDialog", u"Station 2", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("SettingsDialog", u"Modules", None))
        self.label_39.setText(QCoreApplication.translate("SettingsDialog", u"Denso Robot:", None))
        self.station3_robot.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_robot.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_robot_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_40.setText(QCoreApplication.translate("SettingsDialog", u"Cognex:", None))
        self.station3_cognex.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_cognex.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_cognex_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_55.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Lift && Locate 5):", None))
        self.station3_barcode_5.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_barcode_5.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_barcode_5_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_56.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Lift && Locate 7 - Final Test):", None))
        self.station3_barcode_7.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_barcode_7.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_barcode_7_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_41.setText(QCoreApplication.translate("SettingsDialog", u"Wago IO:", None))
        self.station3_wago.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_wago.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_wago_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("SettingsDialog", u"FlexFeeders", None))
        self.label_42.setText(QCoreApplication.translate("SettingsDialog", u"Left Handle:", None))
        self.station3_feeders_left_handle.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_feeders_left_handle.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_feeders_left_handle_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_43.setText(QCoreApplication.translate("SettingsDialog", u"Dial:", None))
        self.station3_feeders_dial.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_feeders_dial.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_feeders_dial_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_44.setText(QCoreApplication.translate("SettingsDialog", u"Support Arm:", None))
        self.station3_feeders_support_arm.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_feeders_support_arm.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_feeders_support_arm_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_45.setText(QCoreApplication.translate("SettingsDialog", u"Trigger:", None))
        self.station3_feeders_trigger.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station3_feeders_trigger.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station3_feeders_trigger_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("SettingsDialog", u"Wago Input", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 5", None))
        self.label_142.setText(QCoreApplication.translate("SettingsDialog", u"Extended:", None))
        self.station3_io_lift_locate_extended_5_state.setText("")
        self.label_143.setText(QCoreApplication.translate("SettingsDialog", u"Retracted:", None))
        self.station3_io_lift_locate_retracted_5_state.setText("")
        self.label_144.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate:", None))
        self.station3_io_lift_locate_pre_5_state.setText("")
        self.label_145.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate:", None))
        self.station3_io_lift_locate_main_5_state.setText("")
        self.groupBox_26.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 7", None))
        self.label_149.setText(QCoreApplication.translate("SettingsDialog", u"Extended:", None))
        self.station3_io_lift_locate_extended_7_state.setText("")
        self.label_150.setText(QCoreApplication.translate("SettingsDialog", u"Retracted:", None))
        self.station3_io_lift_locate_retracted_7_state.setText("")
        self.label_151.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate:", None))
        self.station3_io_lift_locate_pre_7_state.setText("")
        self.label_152.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate:", None))
        self.station3_io_lift_locate_main_7_state.setText("")
        self.label_158.setText(QCoreApplication.translate("SettingsDialog", u"Rotary Test:", None))
        self.station3_io_rotary_test_state.setText("")
        self.groupBox_46.setTitle(QCoreApplication.translate("SettingsDialog", u"Part Flip Nest", None))
        self.label_204.setText(QCoreApplication.translate("SettingsDialog", u"Slide Open:", None))
        self.station3_io_part_flip_open_state.setText("")
        self.label_205.setText(QCoreApplication.translate("SettingsDialog", u"Slide Closed:", None))
        self.station3_io_part_flip_closed_state.setText("")
        self.groupBox_54.setTitle(QCoreApplication.translate("SettingsDialog", u"Laser Sensor", None))
        self.label_218.setText(QCoreApplication.translate("SettingsDialog", u"Left Handle:", None))
        self.station3_io_laser_sensor_left_handle_state.setText("")
        self.label_219.setText(QCoreApplication.translate("SettingsDialog", u"Dial:", None))
        self.station3_io_laser_sensor_dial_state.setText("")
        self.group_valve_3.setTitle(QCoreApplication.translate("SettingsDialog", u"Valve(DeviceNet)", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 5", None))
        self.label_146.setText(QCoreApplication.translate("SettingsDialog", u"Lift Up:", None))
        self.station3_valve_lift_locate_up_5_state.setText("")
        self.station3_valve_lift_locate_up_5_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_147.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate Open:", None))
        self.station3_valve_lift_locate_pre_5_state.setText("")
        self.station3_valve_lift_locate_pre_5_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_148.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate Open:", None))
        self.station3_valve_lift_locate_main_5_state.setText("")
        self.station3_valve_lift_locate_main_5_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 7", None))
        self.label_153.setText(QCoreApplication.translate("SettingsDialog", u"Lift Up:", None))
        self.station3_valve_lift_locate_up_7_state.setText("")
        self.station3_valve_lift_locate_up_7_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_159.setText(QCoreApplication.translate("SettingsDialog", u"Final Test Air:", None))
        self.station3_valve_lift_locate_final_assembly_test_air_7_state.setText("")
        self.station3_valve_lift_locate_final_assembly_test_air_7_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_156.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate Open:", None))
        self.station3_valve_lift_locate_pre_7_state.setText("")
        self.station3_valve_lift_locate_pre_7_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_157.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate Open:", None))
        self.station3_valve_lift_locate_main_7_state.setText("")
        self.station3_valve_lift_locate_main_7_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_47.setTitle(QCoreApplication.translate("SettingsDialog", u"Part Flip Nest", None))
        self.label_206.setText(QCoreApplication.translate("SettingsDialog", u"Gripper Open:", None))
        self.station3_valve_flip_nest_gripper_open_state.setText("")
        self.station3_valve_flip_nest_gripper_open_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("SettingsDialog", u"Final Test", None))
        self.label_154.setText(QCoreApplication.translate("SettingsDialog", u"Duration(sec):", None))
        self.label_155.setText(QCoreApplication.translate("SettingsDialog", u"Startup Delay(sec):", None))
        self.label_177.setText(QCoreApplication.translate("SettingsDialog", u"Low Pass(RPM):", None))
        self.label_178.setText(QCoreApplication.translate("SettingsDialog", u"High Pass(RPM):", None))
        self.btn_test_final_assembly.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_station3), QCoreApplication.translate("SettingsDialog", u"Station 3", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("SettingsDialog", u"Modules", None))
        self.label_46.setText(QCoreApplication.translate("SettingsDialog", u"Denso Robot:", None))
        self.station4_robot.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station4_robot.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station4_robot_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_47.setText(QCoreApplication.translate("SettingsDialog", u"Cognex:", None))
        self.station4_cognex.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station4_cognex.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station4_cognex_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_57.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Lift && Locate 6):", None))
        self.station4_barcode_6.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station4_barcode_6.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station4_barcode_6_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_48.setText(QCoreApplication.translate("SettingsDialog", u"Wago IO:", None))
        self.station4_wago.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station4_wago.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station4_wago_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("SettingsDialog", u"FlexFeeders", None))
        self.label_49.setText(QCoreApplication.translate("SettingsDialog", u"Right Handle:", None))
        self.station4_feeders_right_handle.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station4_feeders_right_handle.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station4_feeders_right_handle_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_50.setText(QCoreApplication.translate("SettingsDialog", u"Agitator:", None))
        self.station4_agitator.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station4_agitator.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station4_agitator_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("SettingsDialog", u"Wago Input/Output", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 6", None))
        self.label_160.setText(QCoreApplication.translate("SettingsDialog", u"Extended:", None))
        self.station4_io_lift_locate_extended_6_state.setText("")
        self.label_161.setText(QCoreApplication.translate("SettingsDialog", u"Retracted:", None))
        self.station4_io_lift_locate_retracted_6_state.setText("")
        self.label_162.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate:", None))
        self.station4_io_lift_locate_pre_6_state.setText("")
        self.label_163.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate:", None))
        self.station4_io_lift_locate_main_6_state.setText("")
        self.groupBox_32.setTitle(QCoreApplication.translate("SettingsDialog", u"Upper Housing", None))
        self.label_164.setText(QCoreApplication.translate("SettingsDialog", u"Clamp Open:", None))
        self.station4_io_upper_housing_clamp_open_state.setText("")
        self.label_165.setText(QCoreApplication.translate("SettingsDialog", u"Clamp Closed:", None))
        self.station4_io_upper_housing_clamp_closed_state.setText("")
        self.groupBox_36.setTitle(QCoreApplication.translate("SettingsDialog", u"Hopper Conveyor", None))
        self.label_166.setText(QCoreApplication.translate("SettingsDialog", u"Indexing Sensor:", None))
        self.station4_io_hopper_conveyor_indexing_state.setText("")
        self.label_167.setText(QCoreApplication.translate("SettingsDialog", u"Part Detection:", None))
        self.station4_io_hopper_conveyor_part_detection_state.setText("")
        self.groupBox_49.setTitle(QCoreApplication.translate("SettingsDialog", u"Right Handle Rotator", None))
        self.label_208.setText(QCoreApplication.translate("SettingsDialog", u"Slide Open:", None))
        self.station4_io_right_handle_rotator_slide_open_state.setText("")
        self.label_209.setText(QCoreApplication.translate("SettingsDialog", u"Slide Closed:", None))
        self.station4_io_right_handle_rotator_slide_closed_state.setText("")
        self.label_210.setText(QCoreApplication.translate("SettingsDialog", u"Rotator Place:", None))
        self.station4_io_right_handle_rotator_place_state.setText("")
        self.label_211.setText(QCoreApplication.translate("SettingsDialog", u"Rotator Pick:", None))
        self.station4_io_right_handle_rotator_pick_state.setText("")
        self.groupBox_48.setTitle(QCoreApplication.translate("SettingsDialog", u"Output", None))
        self.label_207.setText(QCoreApplication.translate("SettingsDialog", u"Robot4 Air1 Toggle:", None))
        self.station4_io_robot4_air1_toggle_state.setText("")
        self.station4_io_robot4_air1_toggle_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.group_valve_4.setTitle(QCoreApplication.translate("SettingsDialog", u"Valve(DeviceNet)", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 6", None))
        self.label_169.setText(QCoreApplication.translate("SettingsDialog", u"Lift Up:", None))
        self.station4_valve_lift_locate_up_6_state.setText("")
        self.station4_valve_lift_locate_up_6_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_170.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate Open:", None))
        self.station4_valve_lift_locate_pre_6_state.setText("")
        self.station4_valve_lift_locate_pre_6_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_171.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate Open:", None))
        self.station4_valve_lift_locate_main_6_state.setText("")
        self.station4_valve_lift_locate_main_6_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_172.setText(QCoreApplication.translate("SettingsDialog", u"Upper Housing Pallet Clamp:", None))
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_state.setText("")
        self.station4_valve_lift_locate_upper_housing_pallet_clamp_6_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_50.setTitle(QCoreApplication.translate("SettingsDialog", u"Right Handle Rotator", None))
        self.label_212.setText(QCoreApplication.translate("SettingsDialog", u"Slide Close:", None))
        self.station4_valve_right_handle_rotator_slide_close_state.setText("")
        self.station4_valve_right_handle_rotator_slide_close_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_213.setText(QCoreApplication.translate("SettingsDialog", u"Pick Orientation:", None))
        self.station4_valve_right_handle_rotator_pick_orient_state.setText("")
        self.station4_valve_right_handle_rotator_pick_orient_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("SettingsDialog", u"Hopper Conveyor", None))
        self.label_173.setText(QCoreApplication.translate("SettingsDialog", u"Index Speed(\u00b0):", None))
        self.label_174.setText(QCoreApplication.translate("SettingsDialog", u"Homing Speed(\u00b0):", None))
        self.label_175.setText(QCoreApplication.translate("SettingsDialog", u"Index Length(\u00b0):", None))
        self.label_176.setText(QCoreApplication.translate("SettingsDialog", u"Home Offset(\u00b0):", None))
        self.groupBox_61.setTitle(QCoreApplication.translate("SettingsDialog", u"Motor", None))
        self.label_185.setText(QCoreApplication.translate("SettingsDialog", u"CAN bus Address", None))
        self.label_129.setText(QCoreApplication.translate("SettingsDialog", u"Speed Limit(DPS):", None))
        self.btn_station4_motor_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_station4), QCoreApplication.translate("SettingsDialog", u"Station 4", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("SettingsDialog", u"Modules", None))
        self.label_30.setText(QCoreApplication.translate("SettingsDialog", u"Denso Robot:", None))
        self.station5_robot.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station5_robot.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station5_robot_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_29.setText(QCoreApplication.translate("SettingsDialog", u"Cognex Vision:", None))
        self.station5_cognex.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station5_cognex.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station5_cognex_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_34.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Lift && Locate 1):", None))
        self.station5_barcode_1.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station5_barcode_1.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station5_barcode_1_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_51.setText(QCoreApplication.translate("SettingsDialog", u"Barcode(Labeler):", None))
        self.station5_barcode_labeler.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station5_barcode_labeler.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station5_barcode_labeler_test_2.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.label_27.setText(QCoreApplication.translate("SettingsDialog", u"Wago IO:", None))
        self.station5_wago.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station5_wago.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station5_wago_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("SettingsDialog", u"Flex Feeders", None))
        self.label_31.setText(QCoreApplication.translate("SettingsDialog", u"Lower Housing:", None))
        self.station5_feeders_lower_housing.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.station5_feeders_lower_housing.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_station5_feeders_lower_housing_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("SettingsDialog", u"Wago Input/Output", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 1", None))
        self.label_99.setText(QCoreApplication.translate("SettingsDialog", u"Extended:", None))
        self.station5_io_lift_locate_extended_1_state.setText("")
        self.label_100.setText(QCoreApplication.translate("SettingsDialog", u"Retracted:", None))
        self.station5_io_lift_locate_retracted_1_state.setText("")
        self.label_101.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate:", None))
        self.station5_io_lift_locate_pre_1_state.setText("")
        self.label_102.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate:", None))
        self.station5_io_lift_locate_main_1_state.setText("")
        self.groupBox_51.setTitle(QCoreApplication.translate("SettingsDialog", u"Whirl Rotator", None))
        self.label_214.setText(QCoreApplication.translate("SettingsDialog", u"Rotated Clockwise:", None))
        self.station5_io_whirl_rotator_cw_state.setText("")
        self.label_215.setText(QCoreApplication.translate("SettingsDialog", u"Rotated Counter Clockwise:", None))
        self.station5_io_whirl_rotator_ccw_state.setText("")
        self.label_216.setText(QCoreApplication.translate("SettingsDialog", u"Part Present:", None))
        self.station5_io_whirl_rotator_part_presence_state.setText("")
        self.group_boxing.setTitle(QCoreApplication.translate("SettingsDialog", u"Boxing", None))
        self.label_231.setText(QCoreApplication.translate("SettingsDialog", u"Clamp Engaged:", None))
        self.station5_io_box_clamp_engaged_state.setText("")
        self.label_232.setText(QCoreApplication.translate("SettingsDialog", u"Clamp Retracted:", None))
        self.station5_io_box_clamp_retracted_state.setText("")
        self.label_228.setText(QCoreApplication.translate("SettingsDialog", u"Sensor 1:", None))
        self.station5_io_boxing_sensor_1_state.setText("")
        self.label_229.setText(QCoreApplication.translate("SettingsDialog", u"Sensor 2:", None))
        self.station5_io_boxing_sensor_2_state.setText("")
        self.label_230.setText(QCoreApplication.translate("SettingsDialog", u"Sensor 3:", None))
        self.station5_io_boxing_sensor_3_state.setText("")
        self.label_233.setText(QCoreApplication.translate("SettingsDialog", u"Cylinder Retracted:", None))
        self.station5_io_box_cylinder_retracted_state.setText("")
        self.label_235.setText(QCoreApplication.translate("SettingsDialog", u"Reject Conveyor: ", None))
        self.station5_io_reject_conveyor_sensor_state.setText("")
        self.label_236.setText(QCoreApplication.translate("SettingsDialog", u"Exit Conveyor:", None))
        self.station5_io_product_exit_conveyor_state.setText("")
        self.label_234.setText(QCoreApplication.translate("SettingsDialog", u"Cylinder Actuate:", None))
        self.station5_io_box_cylinder_actuate_state.setText("")
        self.station5_io_box_cylinder_actuate_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_58.setTitle(QCoreApplication.translate("SettingsDialog", u"Unloading", None))
        self.groupBox_53.setTitle(QCoreApplication.translate("SettingsDialog", u"Mode", None))
        self.radio_unload_binning.setText(QCoreApplication.translate("SettingsDialog", u"Binning", None))
        self.radio_unload_boxing.setText(QCoreApplication.translate("SettingsDialog", u"Boxing", None))
        self.box_binning_counter.setTitle(QCoreApplication.translate("SettingsDialog", u"Product Counter(Binning)", None))
        self.station5_en_binning_track.setText(QCoreApplication.translate("SettingsDialog", u"qty. tracking", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Limit:", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Current:", None))
        self.station5_unload_num.setText(QCoreApplication.translate("SettingsDialog", u"10", None))
        self.btn_reset_counter.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
        self.group_valve_5.setTitle(QCoreApplication.translate("SettingsDialog", u"Valve(DeviceNet)", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("SettingsDialog", u"Lift && Locate 1", None))
        self.label_119.setText(QCoreApplication.translate("SettingsDialog", u"Lift Up:", None))
        self.station5_valve_lift_locate_up_1_state.setText("")
        self.station5_valve_lift_locate_up_1_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_120.setText(QCoreApplication.translate("SettingsDialog", u"Pre-Gate Open:", None))
        self.station5_valve_lift_locate_pre_1_state.setText("")
        self.station5_valve_lift_locate_pre_1_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_121.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate Open:", None))
        self.station5_valve_lift_locate_main_1_state.setText("")
        self.station5_valve_lift_locate_main_1_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_52.setTitle(QCoreApplication.translate("SettingsDialog", u"Others", None))
        self.label_217.setText(QCoreApplication.translate("SettingsDialog", u"Whirl Rotator:", None))
        self.station5_valve_whirl_rotator_state.setText("")
        self.station5_valve_whirl_rotator_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_221.setText(QCoreApplication.translate("SettingsDialog", u"Labeler Air:", None))
        self.station5_valve_label_air_state.setText("")
        self.station5_valve_label_air_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.label_227.setText(QCoreApplication.translate("SettingsDialog", u"Box Clamp Engage:", None))
        self.station5_valve_box_clamp_engage_state.setText("")
        self.station5_valve_box_clamp_engage_btn.setText(QCoreApplication.translate("SettingsDialog", u"ON", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsDialog", u"Labeler", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("SettingsDialog", u"General", None))
        self.station5_labeler_enabled.setText(QCoreApplication.translate("SettingsDialog", u"Enabled", None))
        self.label_32.setText(QCoreApplication.translate("SettingsDialog", u"Home Offset(\u00b0):", None))
        self.label_33.setText(QCoreApplication.translate("SettingsDialog", u"Rotation per Revolution(mm):", None))
        self.label_35.setText(QCoreApplication.translate("SettingsDialog", u"Label Pitch(mm):", None))
        self.label_36.setText(QCoreApplication.translate("SettingsDialog", u"Label Length(mm):", None))
        self.label_37.setText(QCoreApplication.translate("SettingsDialog", u"Sensor Timeout(sec):", None))
        self.label_38.setText(QCoreApplication.translate("SettingsDialog", u"Sensor Offset(\u00b0):", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("SettingsDialog", u"Wago Input", None))
        self.label_168.setText(QCoreApplication.translate("SettingsDialog", u"Label Applicator:", None))
        self.station5_labeler_io_label_applicator_state.setText("")
        self.groupBox_60.setTitle(QCoreApplication.translate("SettingsDialog", u"Motor", None))
        self.label_139.setText(QCoreApplication.translate("SettingsDialog", u"CAN bus Address", None))
        self.btn_station5_motor_test.setText(QCoreApplication.translate("SettingsDialog", u"Test", None))
        self.label_123.setText(QCoreApplication.translate("SettingsDialog", u"Speed Limit(DPS):", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_station5), QCoreApplication.translate("SettingsDialog", u"Station 1 (continued)", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("SettingsDialog", u"General", None))
        self.label_220.setText(QCoreApplication.translate("SettingsDialog", u"Pallet Count:", None))
        self.label_186.setText(QCoreApplication.translate("SettingsDialog", u"Startup Timeout:", None))
        self.label_187.setText(QCoreApplication.translate("SettingsDialog", u"Gate Actuation Time:", None))
        self.label_188.setText(QCoreApplication.translate("SettingsDialog", u"Main Gate ON Delay:", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("SettingsDialog", u"Spacing", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Pallet spaces available ahead of main gate:", None))
        self.label_189.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 1:", None))
        self.label_190.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 2:", None))
        self.label_191.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 3:", None))
        self.label_192.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 4:", None))
        self.label_193.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 5:", None))
        self.label_194.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 6:", None))
        self.label_195.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 7:", None))
        self.groupBox_45.setTitle(QCoreApplication.translate("SettingsDialog", u"Release Delay", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Delay before releasing the pallet via main gate ", None))
        self.label_196.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 1:", None))
        self.label_197.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 2:", None))
        self.label_198.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 3:", None))
        self.label_199.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 4:", None))
        self.label_200.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 5:", None))
        self.label_201.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 6:", None))
        self.label_202.setText(QCoreApplication.translate("SettingsDialog", u"Lift & Locate 7:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SettingsDialog", u"  Pallet  ", None))
        self.label_15.setText(QCoreApplication.translate("SettingsDialog", u"Cognex:", None))
        self.final_vision_cognex.setInputMask(QCoreApplication.translate("SettingsDialog", u"000.000.000.000", None))
        self.final_vision_cognex.setText(QCoreApplication.translate("SettingsDialog", u"192.168.1.244", None))
        self.btn_final_vision_cognex_test.setText(QCoreApplication.translate("SettingsDialog", u"Test Connection", None))
        self.groupBox_56.setTitle(QCoreApplication.translate("SettingsDialog", u"Left Handle Preliminary Inspection", None))
        self.final_vision_trigger_open.setText(QCoreApplication.translate("SettingsDialog", u"Trigger Open Pass", None))
        self.final_vision_dial_open.setText(QCoreApplication.translate("SettingsDialog", u"Dial Open Pass", None))
        self.final_vision_support_arm_open.setText(QCoreApplication.translate("SettingsDialog", u"Arm Support Open Pass", None))
        self.groupBox_57.setTitle(QCoreApplication.translate("SettingsDialog", u"Final Assembly Inspection", None))
        self.final_vision_pinion_final.setText(QCoreApplication.translate("SettingsDialog", u"Pinion Final Pass", None))
        self.final_vision_dial_final.setText(QCoreApplication.translate("SettingsDialog", u"Dial Final Pass", None))
        self.final_vision_handle_gaps_final.setText(QCoreApplication.translate("SettingsDialog", u"Handle Gaps Final Pass", None))
        self.final_vision_support_arm_final.setText(QCoreApplication.translate("SettingsDialog", u"Arm Support Final Pass", None))
        self.final_vision_hopper_final.setText(QCoreApplication.translate("SettingsDialog", u"Hopper Final Pass", None))
        self.final_vision_trigger_final.setText(QCoreApplication.translate("SettingsDialog", u"Trigger Final Pass", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SettingsDialog", u"Final Vision", None))
    # retranslateUi

