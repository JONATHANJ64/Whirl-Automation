# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_pallet_edit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PalletEditDialog(object):
    def setupUi(self, PalletEditDialog):
        if not PalletEditDialog.objectName():
            PalletEditDialog.setObjectName(u"PalletEditDialog")
        PalletEditDialog.resize(851, 297)
        font = QFont()
        font.setPointSize(12)
        PalletEditDialog.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(PalletEditDialog)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.station_5 = QGroupBox(PalletEditDialog)
        self.station_5.setObjectName(u"station_5")
        self.verticalLayout_5 = QVBoxLayout(self.station_5)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.lower_housing = QCheckBox(self.station_5)
        self.lower_housing.setObjectName(u"lower_housing")

        self.verticalLayout_5.addWidget(self.lower_housing)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.station_5)

        self.station_1 = QGroupBox(PalletEditDialog)
        self.station_1.setObjectName(u"station_1")
        self.verticalLayout = QVBoxLayout(self.station_1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.cross_gear = QCheckBox(self.station_1)
        self.cross_gear.setObjectName(u"cross_gear")

        self.verticalLayout.addWidget(self.cross_gear)

        self.pinion = QCheckBox(self.station_1)
        self.pinion.setObjectName(u"pinion")

        self.verticalLayout.addWidget(self.pinion)

        self.crank_handle = QCheckBox(self.station_1)
        self.crank_handle.setObjectName(u"crank_handle")

        self.verticalLayout.addWidget(self.crank_handle)

        self.ring_gear = QCheckBox(self.station_1)
        self.ring_gear.setObjectName(u"ring_gear")

        self.verticalLayout.addWidget(self.ring_gear)

        self.grease = QCheckBox(self.station_1)
        self.grease.setObjectName(u"grease")

        self.verticalLayout.addWidget(self.grease)


        self.horizontalLayout_2.addWidget(self.station_1)

        self.station_2 = QGroupBox(PalletEditDialog)
        self.station_2.setObjectName(u"station_2")
        self.verticalLayout_2 = QVBoxLayout(self.station_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.upper_housing = QCheckBox(self.station_2)
        self.upper_housing.setObjectName(u"upper_housing")

        self.verticalLayout_2.addWidget(self.upper_housing)

        self.crank_arm = QCheckBox(self.station_2)
        self.crank_arm.setObjectName(u"crank_arm")

        self.verticalLayout_2.addWidget(self.crank_arm)

        self.rotor = QCheckBox(self.station_2)
        self.rotor.setObjectName(u"rotor")

        self.verticalLayout_2.addWidget(self.rotor)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.station_2)

        self.station_3 = QGroupBox(PalletEditDialog)
        self.station_3.setObjectName(u"station_3")
        self.verticalLayout_3 = QVBoxLayout(self.station_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.left_handle = QCheckBox(self.station_3)
        self.left_handle.setObjectName(u"left_handle")

        self.verticalLayout_3.addWidget(self.left_handle)

        self.dial = QCheckBox(self.station_3)
        self.dial.setObjectName(u"dial")

        self.verticalLayout_3.addWidget(self.dial)

        self.support_arm = QCheckBox(self.station_3)
        self.support_arm.setObjectName(u"support_arm")

        self.verticalLayout_3.addWidget(self.support_arm)

        self.trigger = QCheckBox(self.station_3)
        self.trigger.setObjectName(u"trigger")

        self.verticalLayout_3.addWidget(self.trigger)


        self.horizontalLayout_2.addWidget(self.station_3)

        self.station_4 = QGroupBox(PalletEditDialog)
        self.station_4.setObjectName(u"station_4")
        self.verticalLayout_4 = QVBoxLayout(self.station_4)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.right_handle = QCheckBox(self.station_4)
        self.right_handle.setObjectName(u"right_handle")

        self.verticalLayout_4.addWidget(self.right_handle)

        self.hopper = QCheckBox(self.station_4)
        self.hopper.setObjectName(u"hopper")

        self.verticalLayout_4.addWidget(self.hopper)

        self.agitator = QCheckBox(self.station_4)
        self.agitator.setObjectName(u"agitator")

        self.verticalLayout_4.addWidget(self.agitator)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.station_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_apply = QToolButton(PalletEditDialog)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setEnabled(False)
        self.btn_apply.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.btn_apply)

        self.btn_close = QToolButton(PalletEditDialog)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.retranslateUi(PalletEditDialog)

        QMetaObject.connectSlotsByName(PalletEditDialog)
    # setupUi

    def retranslateUi(self, PalletEditDialog):
        PalletEditDialog.setWindowTitle(QCoreApplication.translate("PalletEditDialog", u"Edit Pallet 123", None))
        self.station_5.setTitle(QCoreApplication.translate("PalletEditDialog", u"Station 5", None))
        self.lower_housing.setText(QCoreApplication.translate("PalletEditDialog", u"Lower Housing", None))
        self.station_1.setTitle(QCoreApplication.translate("PalletEditDialog", u"Station 1", None))
        self.cross_gear.setText(QCoreApplication.translate("PalletEditDialog", u"Cross Gear", None))
        self.pinion.setText(QCoreApplication.translate("PalletEditDialog", u"Pinion", None))
        self.crank_handle.setText(QCoreApplication.translate("PalletEditDialog", u"Crank Handle", None))
        self.ring_gear.setText(QCoreApplication.translate("PalletEditDialog", u"Ring Gear", None))
        self.grease.setText(QCoreApplication.translate("PalletEditDialog", u"Grease", None))
        self.station_2.setTitle(QCoreApplication.translate("PalletEditDialog", u"Station 2", None))
        self.upper_housing.setText(QCoreApplication.translate("PalletEditDialog", u"Upper Housing", None))
        self.crank_arm.setText(QCoreApplication.translate("PalletEditDialog", u"Crank Arm", None))
        self.rotor.setText(QCoreApplication.translate("PalletEditDialog", u"Rotor", None))
        self.station_3.setTitle(QCoreApplication.translate("PalletEditDialog", u"Station 3", None))
        self.left_handle.setText(QCoreApplication.translate("PalletEditDialog", u"Left Handle", None))
        self.dial.setText(QCoreApplication.translate("PalletEditDialog", u"Dial", None))
        self.support_arm.setText(QCoreApplication.translate("PalletEditDialog", u"Support Arm", None))
        self.trigger.setText(QCoreApplication.translate("PalletEditDialog", u"Trigger", None))
        self.station_4.setTitle(QCoreApplication.translate("PalletEditDialog", u"Station 4", None))
        self.right_handle.setText(QCoreApplication.translate("PalletEditDialog", u"Right Handle", None))
        self.hopper.setText(QCoreApplication.translate("PalletEditDialog", u"Hopper", None))
        self.agitator.setText(QCoreApplication.translate("PalletEditDialog", u"Agitator", None))
        self.btn_apply.setText(QCoreApplication.translate("PalletEditDialog", u"Apply Change", None))
        self.btn_close.setText(QCoreApplication.translate("PalletEditDialog", u"Close", None))
    # retranslateUi

