# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_lift_locate.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LiftLocateDialog(object):
    def setupUi(self, LiftLocateDialog):
        if not LiftLocateDialog.objectName():
            LiftLocateDialog.setObjectName(u"LiftLocateDialog")
        LiftLocateDialog.resize(475, 310)
        self.verticalLayout = QVBoxLayout(LiftLocateDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.error = QLabel(LiftLocateDialog)
        self.error.setObjectName(u"error")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error.sizePolicy().hasHeightForWidth())
        self.error.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.error.setFont(font)
        self.error.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.error.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.error)

        self.widget_others = QWidget(LiftLocateDialog)
        self.widget_others.setObjectName(u"widget_others")
        self.widget_others.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_others)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spin_cnt = QSpinBox(self.widget_others)
        self.spin_cnt.setObjectName(u"spin_cnt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spin_cnt.sizePolicy().hasHeightForWidth())
        self.spin_cnt.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        self.spin_cnt.setFont(font1)
        self.spin_cnt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spin_cnt.setMaximum(6)

        self.horizontalLayout_2.addWidget(self.spin_cnt)


        self.verticalLayout.addWidget(self.widget_others)

        self.widget = QWidget(LiftLocateDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.box = QWidget(self.widget)
        self.box.setObjectName(u"box")
        self.box.setMinimumSize(QSize(100, 0))
        self.layout_buttons = QHBoxLayout(self.box)
        self.layout_buttons.setSpacing(20)
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.box)

        self.horizontalSpacer_2 = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(LiftLocateDialog)

        QMetaObject.connectSlotsByName(LiftLocateDialog)
    # setupUi

    def retranslateUi(self, LiftLocateDialog):
        LiftLocateDialog.setWindowTitle(QCoreApplication.translate("LiftLocateDialog", u"Lift & Locate Dialog", None))
        self.error.setText("")
    # retranslateUi

