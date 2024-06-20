# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_final_assembly.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.whirl_rc

class Ui_FinalAssemblyTestDialog(object):
    def setupUi(self, FinalAssemblyTestDialog):
        if not FinalAssemblyTestDialog.objectName():
            FinalAssemblyTestDialog.setObjectName(u"FinalAssemblyTestDialog")
        FinalAssemblyTestDialog.resize(333, 230)
        font = QFont()
        font.setPointSize(12)
        FinalAssemblyTestDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(FinalAssemblyTestDialog)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 50, 50, 50)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.label_2 = QLabel(FinalAssemblyTestDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.rpm = QLabel(FinalAssemblyTestDialog)
        self.rpm.setObjectName(u"rpm")
        self.rpm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.rpm)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(FinalAssemblyTestDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sensor = QLabel(FinalAssemblyTestDialog)
        self.sensor.setObjectName(u"sensor")
        self.sensor.setMaximumSize(QSize(30, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.sensor.setFont(font1)
        self.sensor.setPixmap(QPixmap(u":/img/img/gray-circle.png"))

        self.horizontalLayout.addWidget(self.sensor)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn = QPushButton(FinalAssemblyTestDialog)
        self.btn.setObjectName(u"btn")
        self.btn.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btn)


        self.retranslateUi(FinalAssemblyTestDialog)

        QMetaObject.connectSlotsByName(FinalAssemblyTestDialog)
    # setupUi

    def retranslateUi(self, FinalAssemblyTestDialog):
        FinalAssemblyTestDialog.setWindowTitle(QCoreApplication.translate("FinalAssemblyTestDialog", u"Final Assembly Test", None))
        self.label_2.setText(QCoreApplication.translate("FinalAssemblyTestDialog", u"Current RPM:", None))
        self.rpm.setText(QCoreApplication.translate("FinalAssemblyTestDialog", u"0", None))
        self.label.setText(QCoreApplication.translate("FinalAssemblyTestDialog", u"Sensor:", None))
        self.sensor.setText("")
        self.btn.setText(QCoreApplication.translate("FinalAssemblyTestDialog", u"Start", None))
    # retranslateUi

