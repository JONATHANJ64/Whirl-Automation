# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_motor_test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.whirl_rc

class Ui_MotorTestDialog(object):
    def setupUi(self, MotorTestDialog):
        if not MotorTestDialog.objectName():
            MotorTestDialog.setObjectName(u"MotorTestDialog")
        MotorTestDialog.resize(1314, 746)
        font = QFont()
        font.setPointSize(10)
        MotorTestDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(MotorTestDialog)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_canbus_address = QLabel(MotorTestDialog)
        self.lb_canbus_address.setObjectName(u"lb_canbus_address")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.lb_canbus_address.setFont(font1)

        self.horizontalLayout.addWidget(self.lb_canbus_address)

        self.address = QLabel(MotorTestDialog)
        self.address.setObjectName(u"address")
        self.address.setFont(font1)

        self.horizontalLayout.addWidget(self.address)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.PIDBox = QGroupBox(MotorTestDialog)
        self.PIDBox.setObjectName(u"PIDBox")
        self.PIDBox.setEnabled(False)
        self.PIDBox.setMaximumSize(QSize(400, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.PIDBox.setFont(font2)
        self.verticalLayout = QVBoxLayout(self.PIDBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.groupBox_2 = QGroupBox(self.PIDBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.angle_kp = QSpinBox(self.groupBox_2)
        self.angle_kp.setObjectName(u"angle_kp")
        self.angle_kp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.angle_kp.setMinimum(1)
        self.angle_kp.setMaximum(300)

        self.horizontalLayout_5.addWidget(self.angle_kp)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.angle_ki = QSpinBox(self.groupBox_2)
        self.angle_ki.setObjectName(u"angle_ki")
        self.angle_ki.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.angle_ki.setMinimum(1)
        self.angle_ki.setMaximum(300)

        self.horizontalLayout_6.addWidget(self.angle_ki)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_22.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.PIDBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.speed_kp = QSpinBox(self.groupBox_3)
        self.speed_kp.setObjectName(u"speed_kp")
        self.speed_kp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.speed_kp.setMinimum(1)
        self.speed_kp.setMaximum(300)

        self.horizontalLayout_7.addWidget(self.speed_kp)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.speed_ki = QSpinBox(self.groupBox_3)
        self.speed_ki.setObjectName(u"speed_ki")
        self.speed_ki.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.speed_ki.setMinimum(1)
        self.speed_ki.setMaximum(300)

        self.horizontalLayout_8.addWidget(self.speed_ki)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_22.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.PIDBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.torque_kp = QSpinBox(self.groupBox_4)
        self.torque_kp.setObjectName(u"torque_kp")
        self.torque_kp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.torque_kp.setMinimum(1)
        self.torque_kp.setMaximum(300)

        self.horizontalLayout_9.addWidget(self.torque_kp)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.torque_ki = QSpinBox(self.groupBox_4)
        self.torque_ki.setObjectName(u"torque_ki")
        self.torque_ki.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.torque_ki.setMinimum(1)
        self.torque_ki.setMaximum(300)

        self.horizontalLayout_10.addWidget(self.torque_ki)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_22.addWidget(self.groupBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

        self.chkPIDROM = QCheckBox(self.PIDBox)
        self.chkPIDROM.setObjectName(u"chkPIDROM")

        self.horizontalLayout_21.addWidget(self.chkPIDROM)

        self.btnSetPID = QPushButton(self.PIDBox)
        self.btnSetPID.setObjectName(u"btnSetPID")

        self.horizontalLayout_21.addWidget(self.btnSetPID)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_4.addWidget(self.PIDBox)

        self.motorBox = QGroupBox(MotorTestDialog)
        self.motorBox.setObjectName(u"motorBox")
        self.motorBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motorBox.sizePolicy().hasHeightForWidth())
        self.motorBox.setSizePolicy(sizePolicy)
        self.motorBox.setFont(font2)
        self.horizontalLayout_3 = QHBoxLayout(self.motorBox)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupStatus = QGroupBox(self.motorBox)
        self.groupStatus.setObjectName(u"groupStatus")
        self.groupStatus.setEnabled(True)
        self.verticalLayout_10 = QVBoxLayout(self.groupStatus)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.motor_temperature = QLabel(self.groupStatus)
        self.motor_temperature.setObjectName(u"motor_temperature")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.motor_temperature.sizePolicy().hasHeightForWidth())
        self.motor_temperature.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.motor_temperature)

        self.temperature = QLineEdit(self.groupStatus)
        self.temperature.setObjectName(u"temperature")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.temperature.sizePolicy().hasHeightForWidth())
        self.temperature.setSizePolicy(sizePolicy2)
        self.temperature.setMaximumSize(QSize(70, 16777215))
        self.temperature.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.temperature.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.temperature)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.motor_temperature_2 = QLabel(self.groupStatus)
        self.motor_temperature_2.setObjectName(u"motor_temperature_2")

        self.horizontalLayout_17.addWidget(self.motor_temperature_2)

        self.voltage = QLineEdit(self.groupStatus)
        self.voltage.setObjectName(u"voltage")
        sizePolicy2.setHeightForWidth(self.voltage.sizePolicy().hasHeightForWidth())
        self.voltage.setSizePolicy(sizePolicy2)
        self.voltage.setMaximumSize(QSize(70, 16777215))
        self.voltage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.voltage.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.voltage)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.motor_temperature_3 = QLabel(self.groupStatus)
        self.motor_temperature_3.setObjectName(u"motor_temperature_3")

        self.horizontalLayout_18.addWidget(self.motor_temperature_3)

        self.torque = QLineEdit(self.groupStatus)
        self.torque.setObjectName(u"torque")
        sizePolicy2.setHeightForWidth(self.torque.sizePolicy().hasHeightForWidth())
        self.torque.setSizePolicy(sizePolicy2)
        self.torque.setMaximumSize(QSize(70, 16777215))
        self.torque.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.torque.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.torque)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.motor_temperature_4 = QLabel(self.groupStatus)
        self.motor_temperature_4.setObjectName(u"motor_temperature_4")

        self.horizontalLayout_19.addWidget(self.motor_temperature_4)

        self.speed = QLineEdit(self.groupStatus)
        self.speed.setObjectName(u"speed")
        sizePolicy2.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy2)
        self.speed.setMaximumSize(QSize(70, 16777215))
        self.speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.speed.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.speed)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_3.addWidget(self.groupStatus)

        self.groupEncoder = QGroupBox(self.motorBox)
        self.groupEncoder.setObjectName(u"groupEncoder")
        self.verticalLayout_9 = QVBoxLayout(self.groupEncoder)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.groupEncoder)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.encoder_cur_pos = QLineEdit(self.groupEncoder)
        self.encoder_cur_pos.setObjectName(u"encoder_cur_pos")
        sizePolicy2.setHeightForWidth(self.encoder_cur_pos.sizePolicy().hasHeightForWidth())
        self.encoder_cur_pos.setSizePolicy(sizePolicy2)
        self.encoder_cur_pos.setMaximumSize(QSize(80, 16777215))
        self.encoder_cur_pos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.encoder_cur_pos.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.encoder_cur_pos)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.groupEncoder)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.encoder_orig_pos = QLineEdit(self.groupEncoder)
        self.encoder_orig_pos.setObjectName(u"encoder_orig_pos")
        sizePolicy2.setHeightForWidth(self.encoder_orig_pos.sizePolicy().hasHeightForWidth())
        self.encoder_orig_pos.setSizePolicy(sizePolicy2)
        self.encoder_orig_pos.setMaximumSize(QSize(80, 16777215))
        self.encoder_orig_pos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.encoder_orig_pos.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.encoder_orig_pos)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.groupEncoder)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.encoder_offset = QLineEdit(self.groupEncoder)
        self.encoder_offset.setObjectName(u"encoder_offset")
        sizePolicy2.setHeightForWidth(self.encoder_offset.sizePolicy().hasHeightForWidth())
        self.encoder_offset.setSizePolicy(sizePolicy2)
        self.encoder_offset.setMaximumSize(QSize(80, 16777215))
        self.encoder_offset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.encoder_offset.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.encoder_offset)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_3.addWidget(self.groupEncoder)

        self.groupAngle = QGroupBox(self.motorBox)
        self.groupAngle.setObjectName(u"groupAngle")
        self.verticalLayout_8 = QVBoxLayout(self.groupAngle)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupAngle)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.single_turn_angle = QLineEdit(self.groupAngle)
        self.single_turn_angle.setObjectName(u"single_turn_angle")
        sizePolicy2.setHeightForWidth(self.single_turn_angle.sizePolicy().hasHeightForWidth())
        self.single_turn_angle.setSizePolicy(sizePolicy2)
        self.single_turn_angle.setMaximumSize(QSize(60, 16777215))
        self.single_turn_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.single_turn_angle.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.single_turn_angle)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.groupAngle)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.multi_turn_angle = QLineEdit(self.groupAngle)
        self.multi_turn_angle.setObjectName(u"multi_turn_angle")
        sizePolicy2.setHeightForWidth(self.multi_turn_angle.sizePolicy().hasHeightForWidth())
        self.multi_turn_angle.setSizePolicy(sizePolicy2)
        self.multi_turn_angle.setMaximumSize(QSize(60, 16777215))
        self.multi_turn_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.multi_turn_angle.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.multi_turn_angle)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_3.addWidget(self.groupAngle)


        self.horizontalLayout_4.addWidget(self.motorBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.OpBox = QGroupBox(MotorTestDialog)
        self.OpBox.setObjectName(u"OpBox")
        self.OpBox.setEnabled(True)
        self.OpBox.setFont(font2)
        self.horizontalLayout_2 = QHBoxLayout(self.OpBox)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupTestAngle = QGroupBox(self.OpBox)
        self.groupTestAngle.setObjectName(u"groupTestAngle")
        self.groupTestAngle.setEnabled(True)
        self.verticalLayout_11 = QVBoxLayout(self.groupTestAngle)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(30)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_15 = QLabel(self.groupTestAngle)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_23.addWidget(self.label_15)

        self.target_angle = QDoubleSpinBox(self.groupTestAngle)
        self.target_angle.setObjectName(u"target_angle")
        self.target_angle.setEnabled(True)
        self.target_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.target_angle.setMinimum(-60000.000000000000000)
        self.target_angle.setMaximum(60000.000000000000000)

        self.horizontalLayout_23.addWidget(self.target_angle)


        self.verticalLayout_11.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, -1, 10, -1)
        self.radio_single = QRadioButton(self.groupTestAngle)
        self.radio_single.setObjectName(u"radio_single")
        self.radio_single.setChecked(True)

        self.horizontalLayout_27.addWidget(self.radio_single)

        self.radio_multi = QRadioButton(self.groupTestAngle)
        self.radio_multi.setObjectName(u"radio_multi")

        self.horizontalLayout_27.addWidget(self.radio_multi)


        self.verticalLayout_11.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_19 = QLabel(self.groupTestAngle)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_29.addWidget(self.label_19)

        self.comboAngleDirection = QComboBox(self.groupTestAngle)
        self.comboAngleDirection.addItem("")
        self.comboAngleDirection.addItem("")
        self.comboAngleDirection.setObjectName(u"comboAngleDirection")

        self.horizontalLayout_29.addWidget(self.comboAngleDirection)


        self.verticalLayout_11.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_18 = QLabel(self.groupTestAngle)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_28.addWidget(self.label_18)

        self.target_angle_speed_limit = QSpinBox(self.groupTestAngle)
        self.target_angle_speed_limit.setObjectName(u"target_angle_speed_limit")
        self.target_angle_speed_limit.setMaximumSize(QSize(100, 16777215))
        self.target_angle_speed_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.target_angle_speed_limit.setMinimum(-6000)
        self.target_angle_speed_limit.setMaximum(6000)
        self.target_angle_speed_limit.setValue(360)

        self.horizontalLayout_28.addWidget(self.target_angle_speed_limit)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)

        self.btnTestAngle = QPushButton(self.groupTestAngle)
        self.btnTestAngle.setObjectName(u"btnTestAngle")
        self.btnTestAngle.setEnabled(True)

        self.verticalLayout_11.addWidget(self.btnTestAngle)


        self.horizontalLayout_2.addWidget(self.groupTestAngle)

        self.groupTestSpeed = QGroupBox(self.OpBox)
        self.groupTestSpeed.setObjectName(u"groupTestSpeed")
        self.verticalLayout_12 = QVBoxLayout(self.groupTestSpeed)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 14, -1, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(30)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_16 = QLabel(self.groupTestSpeed)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_24.addWidget(self.label_16)

        self.target_speed = QDoubleSpinBox(self.groupTestSpeed)
        self.target_speed.setObjectName(u"target_speed")
        self.target_speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.target_speed.setMinimum(-3600.000000000000000)
        self.target_speed.setMaximum(3600.000000000000000)

        self.horizontalLayout_24.addWidget(self.target_speed)


        self.verticalLayout_12.addLayout(self.horizontalLayout_24)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.btnTestSpeed = QPushButton(self.groupTestSpeed)
        self.btnTestSpeed.setObjectName(u"btnTestSpeed")

        self.verticalLayout_12.addWidget(self.btnTestSpeed)


        self.horizontalLayout_2.addWidget(self.groupTestSpeed)

        self.groupTestTorque = QGroupBox(self.OpBox)
        self.groupTestTorque.setObjectName(u"groupTestTorque")
        self.verticalLayout_13 = QVBoxLayout(self.groupTestTorque)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 14, -1, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(30)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_17 = QLabel(self.groupTestTorque)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_25.addWidget(self.label_17)

        self.target_torque = QDoubleSpinBox(self.groupTestTorque)
        self.target_torque.setObjectName(u"target_torque")
        self.target_torque.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.target_torque.setDecimals(0)
        self.target_torque.setMinimum(-32000.000000000000000)
        self.target_torque.setMaximum(32000.000000000000000)
        self.target_torque.setSingleStep(100.000000000000000)

        self.horizontalLayout_25.addWidget(self.target_torque)


        self.verticalLayout_13.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.btnTestTorque = QPushButton(self.groupTestTorque)
        self.btnTestTorque.setObjectName(u"btnTestTorque")

        self.verticalLayout_13.addWidget(self.btnTestTorque)


        self.horizontalLayout_2.addWidget(self.groupTestTorque)


        self.verticalLayout_2.addWidget(self.OpBox)

        self.btnClose = QPushButton(MotorTestDialog)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setPointSize(14)
        self.btnClose.setFont(font3)

        self.verticalLayout_2.addWidget(self.btnClose)


        self.retranslateUi(MotorTestDialog)
        self.radio_single.toggled.connect(self.comboAngleDirection.setEnabled)

        QMetaObject.connectSlotsByName(MotorTestDialog)
    # setupUi

    def retranslateUi(self, MotorTestDialog):
        MotorTestDialog.setWindowTitle(QCoreApplication.translate("MotorTestDialog", u"Motor Test", None))
        self.lb_canbus_address.setText(QCoreApplication.translate("MotorTestDialog", u"CAN bus Address:", None))
        self.address.setText(QCoreApplication.translate("MotorTestDialog", u"0", None))
        self.PIDBox.setTitle(QCoreApplication.translate("MotorTestDialog", u"PID Parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MotorTestDialog", u"Angle", None))
        self.label_4.setText(QCoreApplication.translate("MotorTestDialog", u"Kp", None))
        self.label_5.setText(QCoreApplication.translate("MotorTestDialog", u"Ki", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MotorTestDialog", u"Speed", None))
        self.label_6.setText(QCoreApplication.translate("MotorTestDialog", u"Kp", None))
        self.label_7.setText(QCoreApplication.translate("MotorTestDialog", u"Ki", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MotorTestDialog", u"Torque", None))
        self.label_8.setText(QCoreApplication.translate("MotorTestDialog", u"Kp", None))
        self.label_9.setText(QCoreApplication.translate("MotorTestDialog", u"Ki", None))
        self.chkPIDROM.setText(QCoreApplication.translate("MotorTestDialog", u"Save to ROM", None))
        self.btnSetPID.setText(QCoreApplication.translate("MotorTestDialog", u"Save", None))
        self.motorBox.setTitle(QCoreApplication.translate("MotorTestDialog", u"Motor Status", None))
        self.groupStatus.setTitle(QCoreApplication.translate("MotorTestDialog", u"General", None))
        self.motor_temperature.setText(QCoreApplication.translate("MotorTestDialog", u"Temperature(\u2103)", None))
        self.motor_temperature_2.setText(QCoreApplication.translate("MotorTestDialog", u"Voltage(V)", None))
        self.motor_temperature_3.setText(QCoreApplication.translate("MotorTestDialog", u"Torque(A)", None))
        self.motor_temperature_4.setText(QCoreApplication.translate("MotorTestDialog", u"Speed(DPS)", None))
        self.groupEncoder.setTitle(QCoreApplication.translate("MotorTestDialog", u"Encoder Data", None))
        self.label_12.setText(QCoreApplication.translate("MotorTestDialog", u"Cur Position", None))
        self.label_13.setText(QCoreApplication.translate("MotorTestDialog", u"Original Position", None))
        self.label_14.setText(QCoreApplication.translate("MotorTestDialog", u"Offset", None))
        self.groupAngle.setTitle(QCoreApplication.translate("MotorTestDialog", u"Angle", None))
        self.label_10.setText(QCoreApplication.translate("MotorTestDialog", u"Single turn angle:", None))
        self.label_11.setText(QCoreApplication.translate("MotorTestDialog", u"Multi turn angle:", None))
        self.OpBox.setTitle(QCoreApplication.translate("MotorTestDialog", u"Manual Operation", None))
        self.groupTestAngle.setTitle(QCoreApplication.translate("MotorTestDialog", u"Angle Control", None))
        self.label_15.setText(QCoreApplication.translate("MotorTestDialog", u"Target Angle(Degree)", None))
        self.radio_single.setText(QCoreApplication.translate("MotorTestDialog", u"Single-turn", None))
        self.radio_multi.setText(QCoreApplication.translate("MotorTestDialog", u"Multi-turn", None))
        self.label_19.setText(QCoreApplication.translate("MotorTestDialog", u"Direction", None))
        self.comboAngleDirection.setItemText(0, QCoreApplication.translate("MotorTestDialog", u"Clockwise", None))
        self.comboAngleDirection.setItemText(1, QCoreApplication.translate("MotorTestDialog", u"Counter Clockwise", None))

        self.label_18.setText(QCoreApplication.translate("MotorTestDialog", u"Speed Limit(DPS)", None))
        self.btnTestAngle.setText(QCoreApplication.translate("MotorTestDialog", u"Start", None))
        self.groupTestSpeed.setTitle(QCoreApplication.translate("MotorTestDialog", u"Speed Control", None))
        self.label_16.setText(QCoreApplication.translate("MotorTestDialog", u"Target Speed(DPS)", None))
        self.btnTestSpeed.setText(QCoreApplication.translate("MotorTestDialog", u"Start", None))
        self.groupTestTorque.setTitle(QCoreApplication.translate("MotorTestDialog", u"Torque Control", None))
        self.label_17.setText(QCoreApplication.translate("MotorTestDialog", u"Target Torque(mA)", None))
        self.btnTestTorque.setText(QCoreApplication.translate("MotorTestDialog", u"Start", None))
        self.btnClose.setText(QCoreApplication.translate("MotorTestDialog", u"Close", None))
    # retranslateUi

