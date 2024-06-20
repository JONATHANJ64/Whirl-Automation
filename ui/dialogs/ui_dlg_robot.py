# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_robot.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.whirl_rc

class Ui_RobotDialog(object):
    def setupUi(self, RobotDialog):
        if not RobotDialog.objectName():
            RobotDialog.setObjectName(u"RobotDialog")
        RobotDialog.resize(665, 713)
        self.verticalLayout_4 = QVBoxLayout(RobotDialog)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.groupBox = QGroupBox(RobotDialog)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.speed = QSlider(self.groupBox)
        self.speed.setObjectName(u"speed")
        self.speed.setMaximum(100)
        self.speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.speed)

        self.lb_speed = QLabel(self.groupBox)
        self.lb_speed.setObjectName(u"lb_speed")

        self.horizontalLayout.addWidget(self.lb_speed)

        self.btn_set_speed = QToolButton(self.groupBox)
        self.btn_set_speed.setObjectName(u"btn_set_speed")
        self.btn_set_speed.setMinimumSize(QSize(60, 35))

        self.horizontalLayout.addWidget(self.btn_set_speed)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.widget_action = QWidget(RobotDialog)
        self.widget_action.setObjectName(u"widget_action")
        self.widget_action.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_action)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.group_hand = QGroupBox(self.widget_action)
        self.group_hand.setObjectName(u"group_hand")
        self.group_hand.setMinimumSize(QSize(0, 130))
        self.group_hand.setFont(font)
        self.verticalLayout = QVBoxLayout(self.group_hand)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.group_hand)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.state_hand = QLabel(self.group_hand)
        self.state_hand.setObjectName(u"state_hand")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.state_hand.sizePolicy().hasHeightForWidth())
        self.state_hand.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.state_hand.setFont(font1)
        self.state_hand.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.state_hand)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_hand = QToolButton(self.group_hand)
        self.btn_hand.setObjectName(u"btn_hand")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_hand.sizePolicy().hasHeightForWidth())
        self.btn_hand.setSizePolicy(sizePolicy2)
        self.btn_hand.setMinimumSize(QSize(60, 35))

        self.horizontalLayout_3.addWidget(self.btn_hand)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_9.addWidget(self.group_hand)

        self.group_picker = QGroupBox(self.widget_action)
        self.group_picker.setObjectName(u"group_picker")
        self.group_picker.setMinimumSize(QSize(0, 130))
        self.group_picker.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.group_picker)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.group_picker)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.state_picker = QLabel(self.group_picker)
        self.state_picker.setObjectName(u"state_picker")
        sizePolicy1.setHeightForWidth(self.state_picker.sizePolicy().hasHeightForWidth())
        self.state_picker.setSizePolicy(sizePolicy1)
        self.state_picker.setFont(font1)
        self.state_picker.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.state_picker)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_picker = QToolButton(self.group_picker)
        self.btn_picker.setObjectName(u"btn_picker")
        sizePolicy2.setHeightForWidth(self.btn_picker.sizePolicy().hasHeightForWidth())
        self.btn_picker.setSizePolicy(sizePolicy2)
        self.btn_picker.setMinimumSize(QSize(60, 35))

        self.horizontalLayout_5.addWidget(self.btn_picker)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_9.addWidget(self.group_picker)

        self.group_placer = QGroupBox(self.widget_action)
        self.group_placer.setObjectName(u"group_placer")
        self.group_placer.setMinimumSize(QSize(0, 130))
        self.group_placer.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.group_placer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.group_placer)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.state_placer = QLabel(self.group_placer)
        self.state_placer.setObjectName(u"state_placer")
        sizePolicy1.setHeightForWidth(self.state_placer.sizePolicy().hasHeightForWidth())
        self.state_placer.setSizePolicy(sizePolicy1)
        self.state_placer.setFont(font1)
        self.state_placer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.state_placer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.btn_placer = QToolButton(self.group_placer)
        self.btn_placer.setObjectName(u"btn_placer")
        sizePolicy2.setHeightForWidth(self.btn_placer.sizePolicy().hasHeightForWidth())
        self.btn_placer.setSizePolicy(sizePolicy2)
        self.btn_placer.setMinimumSize(QSize(60, 35))

        self.horizontalLayout_7.addWidget(self.btn_placer)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addWidget(self.group_placer)

        self.group_vacuum = QGroupBox(self.widget_action)
        self.group_vacuum.setObjectName(u"group_vacuum")
        self.group_vacuum.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.group_vacuum)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.state_vacuum = QLabel(self.group_vacuum)
        self.state_vacuum.setObjectName(u"state_vacuum")
        sizePolicy1.setHeightForWidth(self.state_vacuum.sizePolicy().hasHeightForWidth())
        self.state_vacuum.setSizePolicy(sizePolicy1)
        self.state_vacuum.setFont(font1)
        self.state_vacuum.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.state_vacuum)

        self.btn_vacuum = QToolButton(self.group_vacuum)
        self.btn_vacuum.setObjectName(u"btn_vacuum")
        sizePolicy2.setHeightForWidth(self.btn_vacuum.sizePolicy().hasHeightForWidth())
        self.btn_vacuum.setSizePolicy(sizePolicy2)
        self.btn_vacuum.setMinimumSize(QSize(80, 40))
        self.btn_vacuum.setMaximumSize(QSize(80, 16777215))

        self.verticalLayout_5.addWidget(self.btn_vacuum)


        self.horizontalLayout_9.addWidget(self.group_vacuum)


        self.verticalLayout_4.addWidget(self.widget_action)

        self.groupBox_2 = QGroupBox(RobotDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.groupBox_2.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stack_sensor_check_skip = QStackedWidget(self.groupBox_2)
        self.stack_sensor_check_skip.setObjectName(u"stack_sensor_check_skip")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_9 = QVBoxLayout(self.page_1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.chk_1_17 = QCheckBox(self.page_1)
        self.chk_1_17.setObjectName(u"chk_1_17")

        self.verticalLayout_9.addWidget(self.chk_1_17)

        self.stack_sensor_check_skip.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.chk_2_17 = QCheckBox(self.page_2)
        self.chk_2_17.setObjectName(u"chk_2_17")

        self.verticalLayout_8.addWidget(self.chk_2_17)

        self.chk_2_11 = QCheckBox(self.page_2)
        self.chk_2_11.setObjectName(u"chk_2_11")

        self.verticalLayout_8.addWidget(self.chk_2_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_2)

        self.inkjet_adjust = QSpinBox(self.page_2)
        self.inkjet_adjust.setObjectName(u"inkjet_adjust")
        self.inkjet_adjust.setMinimumSize(QSize(0, 30))
        self.inkjet_adjust.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.inkjet_adjust.setMaximum(300)

        self.horizontalLayout_12.addWidget(self.inkjet_adjust)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.stack_sensor_check_skip.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_11 = QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.chk_3_13 = QCheckBox(self.page_3)
        self.chk_3_13.setObjectName(u"chk_3_13")

        self.verticalLayout_11.addWidget(self.chk_3_13)

        self.chk_3_17 = QCheckBox(self.page_3)
        self.chk_3_17.setObjectName(u"chk_3_17")

        self.verticalLayout_11.addWidget(self.chk_3_17)

        self.stack_sensor_check_skip.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.chk_4_17 = QCheckBox(self.page_4)
        self.chk_4_17.setObjectName(u"chk_4_17")

        self.horizontalLayout_10.addWidget(self.chk_4_17)

        self.chk_4_13 = QCheckBox(self.page_4)
        self.chk_4_13.setObjectName(u"chk_4_13")

        self.horizontalLayout_10.addWidget(self.chk_4_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.chk_4_11 = QCheckBox(self.page_4)
        self.chk_4_11.setObjectName(u"chk_4_11")

        self.horizontalLayout_11.addWidget(self.chk_4_11)

        self.chk_4_12 = QCheckBox(self.page_4)
        self.chk_4_12.setObjectName(u"chk_4_12")

        self.horizontalLayout_11.addWidget(self.chk_4_12)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.stack_sensor_check_skip.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.chk_5_17 = QCheckBox(self.page_5)
        self.chk_5_17.setObjectName(u"chk_5_17")

        self.verticalLayout_10.addWidget(self.chk_5_17)

        self.stack_sensor_check_skip.addWidget(self.page_5)

        self.verticalLayout_6.addWidget(self.stack_sensor_check_skip)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(RobotDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 100))
        self.groupBox_3.setFont(font)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.chk_dcd = QCheckBox(self.groupBox_3)
        self.chk_dcd.setObjectName(u"chk_dcd")

        self.verticalLayout_12.addWidget(self.chk_dcd)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.error = QLabel(RobotDialog)
        self.error.setObjectName(u"error")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.error.sizePolicy().hasHeightForWidth())
        self.error.setSizePolicy(sizePolicy3)
        self.error.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setItalic(True)
        self.error.setFont(font2)
        self.error.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.error.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.error)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(50)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, 50, -1)
        self.btn_park = QToolButton(RobotDialog)
        self.btn_park.setObjectName(u"btn_park")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_park.sizePolicy().hasHeightForWidth())
        self.btn_park.setSizePolicy(sizePolicy4)
        self.btn_park.setMinimumSize(QSize(60, 35))
        self.btn_park.setFont(font)

        self.horizontalLayout_8.addWidget(self.btn_park)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.retranslateUi(RobotDialog)
        self.speed.valueChanged.connect(self.lb_speed.setNum)

        self.stack_sensor_check_skip.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RobotDialog)
    # setupUi

    def retranslateUi(self, RobotDialog):
        RobotDialog.setWindowTitle(QCoreApplication.translate("RobotDialog", u"Control Robot", None))
        self.groupBox.setTitle(QCoreApplication.translate("RobotDialog", u"Robot Speed", None))
        self.lb_speed.setText(QCoreApplication.translate("RobotDialog", u"20", None))
        self.btn_set_speed.setText(QCoreApplication.translate("RobotDialog", u"SET", None))
        self.group_hand.setTitle(QCoreApplication.translate("RobotDialog", u"Hand", None))
        self.label.setText(QCoreApplication.translate("RobotDialog", u"State:", None))
        self.state_hand.setText(QCoreApplication.translate("RobotDialog", u"CLOSED", None))
        self.btn_hand.setText(QCoreApplication.translate("RobotDialog", u"OPEN", None))
        self.group_picker.setTitle(QCoreApplication.translate("RobotDialog", u"Agitator Picker", None))
        self.label_3.setText(QCoreApplication.translate("RobotDialog", u"State:", None))
        self.state_picker.setText(QCoreApplication.translate("RobotDialog", u"RETRACTED", None))
        self.btn_picker.setText(QCoreApplication.translate("RobotDialog", u"EXTEND", None))
        self.group_placer.setTitle(QCoreApplication.translate("RobotDialog", u"Agitator Placer", None))
        self.label_5.setText(QCoreApplication.translate("RobotDialog", u"State:", None))
        self.state_placer.setText(QCoreApplication.translate("RobotDialog", u"RETRACTED", None))
        self.btn_placer.setText(QCoreApplication.translate("RobotDialog", u"EXTEND", None))
        self.group_vacuum.setTitle(QCoreApplication.translate("RobotDialog", u"Vacuum ", None))
        self.state_vacuum.setText(QCoreApplication.translate("RobotDialog", u"ON", None))
        self.btn_vacuum.setText(QCoreApplication.translate("RobotDialog", u"Turn OFF", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("RobotDialog", u"Sensor Check Skipping", None))
        self.chk_1_17.setText(QCoreApplication.translate("RobotDialog", u"Skip Sensor Checks", None))
        self.chk_2_17.setText(QCoreApplication.translate("RobotDialog", u"Skip Sensor Checks", None))
        self.chk_2_11.setText(QCoreApplication.translate("RobotDialog", u"Skip alignment pins check", None))
        self.label_2.setText(QCoreApplication.translate("RobotDialog", u"Ink Jet Vertical Adjust", None))
        self.chk_3_13.setText(QCoreApplication.translate("RobotDialog", u"Skip Vacuum Checks", None))
        self.chk_3_17.setText(QCoreApplication.translate("RobotDialog", u"Skip Sensor Checks", None))
        self.chk_4_17.setText(QCoreApplication.translate("RobotDialog", u"Skip Sensor Checks", None))
        self.chk_4_13.setText(QCoreApplication.translate("RobotDialog", u"Skip Vacuum Checks", None))
        self.chk_4_11.setText(QCoreApplication.translate("RobotDialog", u"Skip Handle Pins Check", None))
        self.chk_4_12.setText(QCoreApplication.translate("RobotDialog", u"Skip Hopper Pins Checks", None))
        self.chk_5_17.setText(QCoreApplication.translate("RobotDialog", u"Skip Sensor Checks", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("RobotDialog", u"Miscellaneous", None))
        self.chk_dcd.setText(QCoreApplication.translate("RobotDialog", u"Disable Collision Detection", None))
        self.error.setText("")
        self.btn_park.setText(QCoreApplication.translate("RobotDialog", u"PARK", None))
    # retranslateUi

