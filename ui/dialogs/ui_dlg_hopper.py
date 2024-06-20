# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_hopper.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HopperDialog(object):
    def setupUi(self, HopperDialog):
        if not HopperDialog.objectName():
            HopperDialog.setObjectName(u"HopperDialog")
        HopperDialog.resize(572, 197)
        self.verticalLayout = QVBoxLayout(HopperDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.msg = QLabel(HopperDialog)
        self.msg.setObjectName(u"msg")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg.sizePolicy().hasHeightForWidth())
        self.msg.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.msg.setFont(font)
        self.msg.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.msg.setWordWrap(True)

        self.verticalLayout.addWidget(self.msg)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(HopperDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.indexed = QLabel(self.widget)
        self.indexed.setObjectName(u"indexed")
        self.indexed.setMinimumSize(QSize(24, 24))
        self.indexed.setMaximumSize(QSize(24, 24))
        self.indexed.setStyleSheet(u"background-color: #aa0000;\n"
"border-radius: 12px;")

        self.horizontalLayout_2.addWidget(self.indexed)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.present = QLabel(self.widget)
        self.present.setObjectName(u"present")
        self.present.setMinimumSize(QSize(24, 24))
        self.present.setMaximumSize(QSize(24, 24))
        self.present.setStyleSheet(u"background-color: #00ff00;\n"
"border-radius: 12px;")

        self.horizontalLayout_2.addWidget(self.present)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)

        self.btn_index = QToolButton(HopperDialog)
        self.btn_index.setObjectName(u"btn_index")
        self.btn_index.setMinimumSize(QSize(80, 40))
        self.btn_index.setFont(font)

        self.horizontalLayout.addWidget(self.btn_index)

        self.btn_stop = QToolButton(HopperDialog)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(80, 40))
        self.btn_stop.setFont(font)

        self.horizontalLayout.addWidget(self.btn_stop)

        self.btn_close = QToolButton(HopperDialog)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(80, 40))
        self.btn_close.setFont(font)

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(HopperDialog)

        QMetaObject.connectSlotsByName(HopperDialog)
    # setupUi

    def retranslateUi(self, HopperDialog):
        HopperDialog.setWindowTitle(QCoreApplication.translate("HopperDialog", u"Hopper Conveyor ", None))
        self.msg.setText("")
        self.label.setText(QCoreApplication.translate("HopperDialog", u"Index:", None))
        self.indexed.setText("")
        self.label_2.setText(QCoreApplication.translate("HopperDialog", u"Part Presence:", None))
        self.present.setText("")
        self.btn_index.setText(QCoreApplication.translate("HopperDialog", u"Index", None))
        self.btn_stop.setText(QCoreApplication.translate("HopperDialog", u"Stop", None))
        self.btn_close.setText(QCoreApplication.translate("HopperDialog", u"Close", None))
    # retranslateUi

