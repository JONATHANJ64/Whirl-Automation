# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_robot_error_code.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RobotErrorCodeDialog(object):
    def setupUi(self, RobotErrorCodeDialog):
        if not RobotErrorCodeDialog.objectName():
            RobotErrorCodeDialog.setObjectName(u"RobotErrorCodeDialog")
        RobotErrorCodeDialog.resize(483, 168)
        font = QFont()
        font.setPointSize(12)
        RobotErrorCodeDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(RobotErrorCodeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(RobotErrorCodeDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_clear = QToolButton(RobotErrorCodeDialog)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(120, 40))

        self.horizontalLayout.addWidget(self.btn_clear)

        self.btn_cancel = QToolButton(RobotErrorCodeDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(120, 40))

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(RobotErrorCodeDialog)

        QMetaObject.connectSlotsByName(RobotErrorCodeDialog)
    # setupUi

    def retranslateUi(self, RobotErrorCodeDialog):
        RobotErrorCodeDialog.setWindowTitle(QCoreApplication.translate("RobotErrorCodeDialog", u"Robot Error", None))
        self.label.setText(QCoreApplication.translate("RobotErrorCodeDialog", u"Robot Error", None))
        self.btn_clear.setText(QCoreApplication.translate("RobotErrorCodeDialog", u"Clear Error", None))
        self.btn_cancel.setText(QCoreApplication.translate("RobotErrorCodeDialog", u"Cancel", None))
    # retranslateUi

