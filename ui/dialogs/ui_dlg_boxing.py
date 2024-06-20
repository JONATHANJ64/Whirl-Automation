# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_boxing.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BoxingDialog(object):
    def setupUi(self, BoxingDialog):
        if not BoxingDialog.objectName():
            BoxingDialog.setObjectName(u"BoxingDialog")
        BoxingDialog.resize(269, 145)
        font = QFont()
        font.setPointSize(12)
        BoxingDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(BoxingDialog)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label = QLabel(BoxingDialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.spin_cnt = QSpinBox(BoxingDialog)
        self.spin_cnt.setObjectName(u"spin_cnt")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_cnt.sizePolicy().hasHeightForWidth())
        self.spin_cnt.setSizePolicy(sizePolicy)
        self.spin_cnt.setMinimumSize(QSize(50, 0))
        font1 = QFont()
        font1.setPointSize(14)
        self.spin_cnt.setFont(font1)
        self.spin_cnt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spin_cnt.setMaximum(6)

        self.horizontalLayout.addWidget(self.spin_cnt)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_restart = QToolButton(BoxingDialog)
        self.btn_restart.setObjectName(u"btn_restart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_restart.sizePolicy().hasHeightForWidth())
        self.btn_restart.setSizePolicy(sizePolicy1)
        self.btn_restart.setMinimumSize(QSize(0, 32))
        self.btn_restart.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_restart)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(BoxingDialog)

        QMetaObject.connectSlotsByName(BoxingDialog)
    # setupUi

    def retranslateUi(self, BoxingDialog):
        BoxingDialog.setWindowTitle(QCoreApplication.translate("BoxingDialog", u"Boxing Dialog", None))
        self.label.setText(QCoreApplication.translate("BoxingDialog", u"Current Part Count:", None))
        self.btn_restart.setText(QCoreApplication.translate("BoxingDialog", u"Restart Boxing", None))
    # retranslateUi

