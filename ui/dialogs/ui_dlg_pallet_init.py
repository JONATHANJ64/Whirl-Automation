# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_pallet_init.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PalletInitDialog(object):
    def setupUi(self, PalletInitDialog):
        if not PalletInitDialog.objectName():
            PalletInitDialog.setObjectName(u"PalletInitDialog")
        PalletInitDialog.resize(851, 581)
        self.verticalLayout_8 = QVBoxLayout(PalletInitDialog)
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(30, 30, 30, 30)
        self.label = QLabel(PalletInitDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ll_1 = QGroupBox(PalletInitDialog)
        self.ll_1.setObjectName(u"ll_1")
        self.ll_1.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(12)
        self.ll_1.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.ll_1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.pallet_1 = QLabel(self.ll_1)
        self.pallet_1.setObjectName(u"pallet_1")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.pallet_1.setFont(font2)
        self.pallet_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.pallet_1)

        self.lower_housing = QCheckBox(self.ll_1)
        self.lower_housing.setObjectName(u"lower_housing")

        self.verticalLayout.addWidget(self.lower_housing)

        self.verticalSpacer = QSpacerItem(20, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.ll_1)

        self.ll_2 = QGroupBox(PalletInitDialog)
        self.ll_2.setObjectName(u"ll_2")
        self.ll_2.setEnabled(False)
        self.ll_2.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.ll_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.pallet_2 = QLabel(self.ll_2)
        self.pallet_2.setObjectName(u"pallet_2")
        self.pallet_2.setFont(font2)
        self.pallet_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.pallet_2)

        self.grease = QCheckBox(self.ll_2)
        self.grease.setObjectName(u"grease")

        self.verticalLayout_2.addWidget(self.grease)

        self.verticalSpacer_2 = QSpacerItem(20, 74, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.ll_2)

        self.ll_3 = QGroupBox(PalletInitDialog)
        self.ll_3.setObjectName(u"ll_3")
        self.ll_3.setEnabled(False)
        self.ll_3.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.ll_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.pallet_3 = QLabel(self.ll_3)
        self.pallet_3.setObjectName(u"pallet_3")
        self.pallet_3.setFont(font2)
        self.pallet_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.pallet_3)

        self.cross_gear = QCheckBox(self.ll_3)
        self.cross_gear.setObjectName(u"cross_gear")

        self.verticalLayout_3.addWidget(self.cross_gear)

        self.pinion = QCheckBox(self.ll_3)
        self.pinion.setObjectName(u"pinion")

        self.verticalLayout_3.addWidget(self.pinion)

        self.crank_handle = QCheckBox(self.ll_3)
        self.crank_handle.setObjectName(u"crank_handle")

        self.verticalLayout_3.addWidget(self.crank_handle)

        self.ring_gear = QCheckBox(self.ll_3)
        self.ring_gear.setObjectName(u"ring_gear")

        self.verticalLayout_3.addWidget(self.ring_gear)


        self.horizontalLayout.addWidget(self.ll_3)

        self.ll_4 = QGroupBox(PalletInitDialog)
        self.ll_4.setObjectName(u"ll_4")
        self.ll_4.setEnabled(False)
        self.ll_4.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.ll_4)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.pallet_4 = QLabel(self.ll_4)
        self.pallet_4.setObjectName(u"pallet_4")
        self.pallet_4.setFont(font2)
        self.pallet_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.pallet_4)

        self.upper_housing = QCheckBox(self.ll_4)
        self.upper_housing.setObjectName(u"upper_housing")

        self.verticalLayout_4.addWidget(self.upper_housing)

        self.crank_arm = QCheckBox(self.ll_4)
        self.crank_arm.setObjectName(u"crank_arm")

        self.verticalLayout_4.addWidget(self.crank_arm)

        self.rotor = QCheckBox(self.ll_4)
        self.rotor.setObjectName(u"rotor")

        self.verticalLayout_4.addWidget(self.rotor)

        self.verticalSpacer_4 = QSpacerItem(20, 74, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.ll_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ll_5 = QGroupBox(PalletInitDialog)
        self.ll_5.setObjectName(u"ll_5")
        self.ll_5.setEnabled(False)
        self.ll_5.setFont(font1)
        self.verticalLayout_6 = QVBoxLayout(self.ll_5)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.pallet_5 = QLabel(self.ll_5)
        self.pallet_5.setObjectName(u"pallet_5")
        self.pallet_5.setFont(font2)
        self.pallet_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.pallet_5)

        self.left_handle = QCheckBox(self.ll_5)
        self.left_handle.setObjectName(u"left_handle")

        self.verticalLayout_6.addWidget(self.left_handle)

        self.dial = QCheckBox(self.ll_5)
        self.dial.setObjectName(u"dial")

        self.verticalLayout_6.addWidget(self.dial)

        self.support_arm = QCheckBox(self.ll_5)
        self.support_arm.setObjectName(u"support_arm")

        self.verticalLayout_6.addWidget(self.support_arm)

        self.trigger = QCheckBox(self.ll_5)
        self.trigger.setObjectName(u"trigger")

        self.verticalLayout_6.addWidget(self.trigger)


        self.horizontalLayout_2.addWidget(self.ll_5)

        self.ll_6 = QGroupBox(PalletInitDialog)
        self.ll_6.setObjectName(u"ll_6")
        self.ll_6.setEnabled(False)
        self.ll_6.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.ll_6)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.pallet_6 = QLabel(self.ll_6)
        self.pallet_6.setObjectName(u"pallet_6")
        self.pallet_6.setFont(font2)
        self.pallet_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.pallet_6)

        self.right_handle = QCheckBox(self.ll_6)
        self.right_handle.setObjectName(u"right_handle")

        self.verticalLayout_5.addWidget(self.right_handle)

        self.agitator = QCheckBox(self.ll_6)
        self.agitator.setObjectName(u"agitator")

        self.verticalLayout_5.addWidget(self.agitator)

        self.hopper = QCheckBox(self.ll_6)
        self.hopper.setObjectName(u"hopper")

        self.verticalLayout_5.addWidget(self.hopper)

        self.verticalSpacer_5 = QSpacerItem(20, 74, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addWidget(self.ll_6)

        self.ll_7 = QGroupBox(PalletInitDialog)
        self.ll_7.setObjectName(u"ll_7")
        self.ll_7.setEnabled(False)
        self.ll_7.setFont(font1)
        self.verticalLayout_7 = QVBoxLayout(self.ll_7)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.pallet_7 = QLabel(self.ll_7)
        self.pallet_7.setObjectName(u"pallet_7")
        self.pallet_7.setFont(font2)
        self.pallet_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.pallet_7)

        self.final_test = QCheckBox(self.ll_7)
        self.final_test.setObjectName(u"final_test")

        self.verticalLayout_7.addWidget(self.final_test)

        self.verticalSpacer_7 = QSpacerItem(20, 74, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_2.addWidget(self.ll_7)

        self.widget = QWidget(PalletInitDialog)
        self.widget.setObjectName(u"widget")
        self.btn_confirm = QPushButton(self.widget)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setGeometry(QRect(60, 180, 111, 31))
        self.btn_confirm.setFont(font1)

        self.horizontalLayout_2.addWidget(self.widget)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)


        self.retranslateUi(PalletInitDialog)

        QMetaObject.connectSlotsByName(PalletInitDialog)
    # setupUi

    def retranslateUi(self, PalletInitDialog):
        PalletInitDialog.setWindowTitle(QCoreApplication.translate("PalletInitDialog", u"Pallet Initialization", None))
        self.label.setText(QCoreApplication.translate("PalletInitDialog", u"Please make sure that the following pallets at Lift & Locates are correctly configured", None))
        self.ll_1.setTitle(QCoreApplication.translate("PalletInitDialog", u"LL1 (Robot 5)", None))
        self.pallet_1.setText("")
        self.lower_housing.setText(QCoreApplication.translate("PalletInitDialog", u"Lower Housing", None))
        self.ll_2.setTitle(QCoreApplication.translate("PalletInitDialog", u"LL2 (Grease Dispenser)", None))
        self.pallet_2.setText("")
        self.grease.setText(QCoreApplication.translate("PalletInitDialog", u"Grease", None))
        self.ll_3.setTitle(QCoreApplication.translate("PalletInitDialog", u"LL3 (Robot 1)", None))
        self.pallet_3.setText("")
        self.cross_gear.setText(QCoreApplication.translate("PalletInitDialog", u"Cross Gear", None))
        self.pinion.setText(QCoreApplication.translate("PalletInitDialog", u"Pinion", None))
        self.crank_handle.setText(QCoreApplication.translate("PalletInitDialog", u"Crank Handle", None))
        self.ring_gear.setText(QCoreApplication.translate("PalletInitDialog", u"Ring Gear", None))
        self.ll_4.setTitle(QCoreApplication.translate("PalletInitDialog", u"LL4 (Robot 2)", None))
        self.pallet_4.setText("")
        self.upper_housing.setText(QCoreApplication.translate("PalletInitDialog", u"Upper Housing", None))
        self.crank_arm.setText(QCoreApplication.translate("PalletInitDialog", u"Crank Arm", None))
        self.rotor.setText(QCoreApplication.translate("PalletInitDialog", u"Rotor", None))
        self.ll_5.setTitle(QCoreApplication.translate("PalletInitDialog", u"LL5 (Robot 3)", None))
        self.pallet_5.setText("")
        self.left_handle.setText(QCoreApplication.translate("PalletInitDialog", u"Left Handle", None))
        self.dial.setText(QCoreApplication.translate("PalletInitDialog", u"Dial", None))
        self.support_arm.setText(QCoreApplication.translate("PalletInitDialog", u"Support Arm", None))
        self.trigger.setText(QCoreApplication.translate("PalletInitDialog", u"Trigger", None))
        self.ll_6.setTitle(QCoreApplication.translate("PalletInitDialog", u"LL6 (Robot 4)", None))
        self.pallet_6.setText("")
        self.right_handle.setText(QCoreApplication.translate("PalletInitDialog", u"Right Handle", None))
        self.agitator.setText(QCoreApplication.translate("PalletInitDialog", u"Agitator", None))
        self.hopper.setText(QCoreApplication.translate("PalletInitDialog", u"Hopper", None))
        self.ll_7.setTitle(QCoreApplication.translate("PalletInitDialog", u"LL7 (Final Test)", None))
        self.pallet_7.setText("")
        self.final_test.setText(QCoreApplication.translate("PalletInitDialog", u"Final Test", None))
        self.btn_confirm.setText(QCoreApplication.translate("PalletInitDialog", u"Confirm", None))
    # retranslateUi

