# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_robot_error.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RobotErrorDialog(object):
    def setupUi(self, RobotErrorDialog):
        if not RobotErrorDialog.objectName():
            RobotErrorDialog.setObjectName(u"RobotErrorDialog")
        RobotErrorDialog.resize(600, 300)
        RobotErrorDialog.setMaximumSize(QSize(600, 300))
        font = QFont()
        font.setPointSize(12)
        RobotErrorDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(RobotErrorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.msg = QLabel(RobotErrorDialog)
        self.msg.setObjectName(u"msg")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg.sizePolicy().hasHeightForWidth())
        self.msg.setSizePolicy(sizePolicy)
        self.msg.setFont(font)
        self.msg.setWordWrap(True)

        self.verticalLayout.addWidget(self.msg)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_retry = QToolButton(RobotErrorDialog)
        self.btn_retry.setObjectName(u"btn_retry")
        self.btn_retry.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.btn_retry)

        self.btn_new_part = QToolButton(RobotErrorDialog)
        self.btn_new_part.setObjectName(u"btn_new_part")
        self.btn_new_part.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.btn_new_part)

        self.btn_cancel = QToolButton(RobotErrorDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(RobotErrorDialog)

        QMetaObject.connectSlotsByName(RobotErrorDialog)
    # setupUi

    def retranslateUi(self, RobotErrorDialog):
        RobotErrorDialog.setWindowTitle(QCoreApplication.translate("RobotErrorDialog", u"Robot Error", None))
        self.msg.setText(QCoreApplication.translate("RobotErrorDialog", u"Error!", None))
        self.btn_retry.setText(QCoreApplication.translate("RobotErrorDialog", u"&Retry", None))
        self.btn_new_part.setText(QCoreApplication.translate("RobotErrorDialog", u"Pick &New Part", None))
        self.btn_cancel.setText(QCoreApplication.translate("RobotErrorDialog", u"&Cancel Build/Go Home", None))
    # retranslateUi

