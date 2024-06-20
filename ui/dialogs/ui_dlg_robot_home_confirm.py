# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_robot_home_confirm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RobotHomeConfirmDialog(object):
    def setupUi(self, RobotHomeConfirmDialog):
        if not RobotHomeConfirmDialog.objectName():
            RobotHomeConfirmDialog.setObjectName(u"RobotHomeConfirmDialog")
        RobotHomeConfirmDialog.resize(511, 140)
        font = QFont()
        font.setPointSize(12)
        RobotHomeConfirmDialog.setFont(font)
        self.msg = QLabel(RobotHomeConfirmDialog)
        self.msg.setObjectName(u"msg")
        self.msg.setGeometry(QRect(10, 10, 491, 61))
        self.msg.setFont(font)
        self.msg.setWordWrap(True)
        self.btn_yes = QToolButton(RobotHomeConfirmDialog)
        self.btn_yes.setObjectName(u"btn_yes")
        self.btn_yes.setGeometry(QRect(90, 100, 131, 31))
        self.btn_pendant = QToolButton(RobotHomeConfirmDialog)
        self.btn_pendant.setObjectName(u"btn_pendant")
        self.btn_pendant.setGeometry(QRect(280, 100, 180, 31))

        self.retranslateUi(RobotHomeConfirmDialog)

        QMetaObject.connectSlotsByName(RobotHomeConfirmDialog)
    # setupUi

    def retranslateUi(self, RobotHomeConfirmDialog):
        RobotHomeConfirmDialog.setWindowTitle(QCoreApplication.translate("RobotHomeConfirmDialog", u"Confirm Robot Movement", None))
        self.msg.setText(QCoreApplication.translate("RobotHomeConfirmDialog", u"Question", None))
        self.btn_yes.setText(QCoreApplication.translate("RobotHomeConfirmDialog", u"&Yes", None))
        self.btn_pendant.setText(QCoreApplication.translate("RobotHomeConfirmDialog", u"Use &Teach Pendant", None))
    # retranslateUi

