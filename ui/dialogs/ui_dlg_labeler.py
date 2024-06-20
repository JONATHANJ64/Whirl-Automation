# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_labeler.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LabelerDialog(object):
    def setupUi(self, LabelerDialog):
        if not LabelerDialog.objectName():
            LabelerDialog.setObjectName(u"LabelerDialog")
        LabelerDialog.resize(435, 203)
        self.verticalLayout_2 = QVBoxLayout(LabelerDialog)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(LabelerDialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.state = QLabel(LabelerDialog)
        self.state.setObjectName(u"state")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.state.setFont(font1)
        self.state.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.state)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(LabelerDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_sensor = QLabel(LabelerDialog)
        self.label_sensor.setObjectName(u"label_sensor")
        self.label_sensor.setMinimumSize(QSize(25, 25))
        self.label_sensor.setMaximumSize(QSize(25, 25))
        self.label_sensor.setStyleSheet(u"background-color: #aa0000;\n"
"border-radius: 12px;")

        self.horizontalLayout_2.addWidget(self.label_sensor)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.error = QLabel(LabelerDialog)
        self.error.setObjectName(u"error")
        font2 = QFont()
        font2.setPointSize(10)
        self.error.setFont(font2)
        self.error.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.error.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.error)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_feed = QToolButton(LabelerDialog)
        self.btn_feed.setObjectName(u"btn_feed")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_feed.sizePolicy().hasHeightForWidth())
        self.btn_feed.setSizePolicy(sizePolicy)
        self.btn_feed.setFont(font)

        self.horizontalLayout.addWidget(self.btn_feed)

        self.btn_unlock = QToolButton(LabelerDialog)
        self.btn_unlock.setObjectName(u"btn_unlock")
        sizePolicy.setHeightForWidth(self.btn_unlock.sizePolicy().hasHeightForWidth())
        self.btn_unlock.setSizePolicy(sizePolicy)
        self.btn_unlock.setFont(font)

        self.horizontalLayout.addWidget(self.btn_unlock)

        self.btn_clear = QToolButton(LabelerDialog)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setFont(font)

        self.horizontalLayout.addWidget(self.btn_clear)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(LabelerDialog)

        QMetaObject.connectSlotsByName(LabelerDialog)
    # setupUi

    def retranslateUi(self, LabelerDialog):
        LabelerDialog.setWindowTitle(QCoreApplication.translate("LabelerDialog", u"Labeler", None))
        self.label_3.setText(QCoreApplication.translate("LabelerDialog", u"Current State:", None))
        self.state.setText(QCoreApplication.translate("LabelerDialog", u"idle", None))
        self.label_2.setText(QCoreApplication.translate("LabelerDialog", u"Label Sensor:", None))
        self.label_sensor.setText("")
        self.error.setText("")
        self.btn_feed.setText(QCoreApplication.translate("LabelerDialog", u"Feed Label", None))
        self.btn_unlock.setText(QCoreApplication.translate("LabelerDialog", u"Unlock Motor", None))
        self.btn_clear.setText(QCoreApplication.translate("LabelerDialog", u"Clear Error State", None))
    # retranslateUi

