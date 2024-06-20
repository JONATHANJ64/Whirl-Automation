# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TestDialog(object):
    def setupUi(self, TestDialog):
        if not TestDialog.objectName():
            TestDialog.setObjectName(u"TestDialog")
        TestDialog.resize(776, 524)
        self.groupBox = QGroupBox(TestDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 311, 171))
        font = QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.cognex_host = QLineEdit(self.groupBox)
        self.cognex_host.setObjectName(u"cognex_host")
        self.cognex_host.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.cognex_host)

        self.btn_cognex_connect = QPushButton(self.groupBox)
        self.btn_cognex_connect.setObjectName(u"btn_cognex_connect")

        self.horizontalLayout.addWidget(self.btn_cognex_connect)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cognex_x = QLabel(self.groupBox)
        self.cognex_x.setObjectName(u"cognex_x")

        self.verticalLayout.addWidget(self.cognex_x)

        self.cognex_y = QLabel(self.groupBox)
        self.cognex_y.setObjectName(u"cognex_y")

        self.verticalLayout.addWidget(self.cognex_y)

        self.cognex_r = QLabel(self.groupBox)
        self.cognex_r.setObjectName(u"cognex_r")

        self.verticalLayout.addWidget(self.cognex_r)

        self.groupBox_2 = QGroupBox(TestDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(490, 20, 251, 91))
        self.groupBox_2.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.robot_host = QLineEdit(self.groupBox_2)
        self.robot_host.setObjectName(u"robot_host")
        self.robot_host.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.robot_host)

        self.btn_robot_connect = QPushButton(self.groupBox_2)
        self.btn_robot_connect.setObjectName(u"btn_robot_connect")

        self.horizontalLayout_2.addWidget(self.btn_robot_connect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_transfer = QPushButton(TestDialog)
        self.btn_transfer.setObjectName(u"btn_transfer")
        self.btn_transfer.setEnabled(False)
        self.btn_transfer.setGeometry(QRect(350, 60, 91, 31))
        self.groupBox_3 = QGroupBox(TestDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(230, 300, 311, 201))
        self.groupBox_3.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.wago_host = QLineEdit(self.groupBox_3)
        self.wago_host.setObjectName(u"wago_host")
        self.wago_host.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.wago_host)

        self.btn_wago_connect = QPushButton(self.groupBox_3)
        self.btn_wago_connect.setObjectName(u"btn_wago_connect")

        self.horizontalLayout_3.addWidget(self.btn_wago_connect)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.wago_address = QSpinBox(self.groupBox_3)
        self.wago_address.setObjectName(u"wago_address")
        self.wago_address.setEnabled(False)
        self.wago_address.setMaximum(15)

        self.horizontalLayout_4.addWidget(self.wago_address)

        self.wago_status = QLabel(self.groupBox_3)
        self.wago_status.setObjectName(u"wago_status")
        self.wago_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.wago_status)

        self.btn_wago_read = QPushButton(self.groupBox_3)
        self.btn_wago_read.setObjectName(u"btn_wago_read")
        self.btn_wago_read.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.btn_wago_read)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.btn_wago = QPushButton(self.groupBox_3)
        self.btn_wago.setObjectName(u"btn_wago")
        self.btn_wago.setEnabled(False)

        self.verticalLayout_3.addWidget(self.btn_wago)

        self.btn_turn_off_others = QPushButton(self.groupBox_3)
        self.btn_turn_off_others.setObjectName(u"btn_turn_off_others")

        self.verticalLayout_3.addWidget(self.btn_turn_off_others)


        self.retranslateUi(TestDialog)

        QMetaObject.connectSlotsByName(TestDialog)
    # setupUi

    def retranslateUi(self, TestDialog):
        TestDialog.setWindowTitle(QCoreApplication.translate("TestDialog", u"Robot Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("TestDialog", u"Cognex", None))
        self.label.setText(QCoreApplication.translate("TestDialog", u"Host", None))
        self.cognex_host.setInputMask(QCoreApplication.translate("TestDialog", u"000.000.000.000", None))
        self.cognex_host.setText(QCoreApplication.translate("TestDialog", u"192.168.100.16", None))
        self.btn_cognex_connect.setText(QCoreApplication.translate("TestDialog", u"Connect", None))
        self.cognex_x.setText(QCoreApplication.translate("TestDialog", u"X:", None))
        self.cognex_y.setText(QCoreApplication.translate("TestDialog", u"Y:", None))
        self.cognex_r.setText(QCoreApplication.translate("TestDialog", u"R:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TestDialog", u"Robot", None))
        self.label_2.setText(QCoreApplication.translate("TestDialog", u"Host", None))
        self.robot_host.setInputMask(QCoreApplication.translate("TestDialog", u"000.000.000.000", None))
        self.robot_host.setText(QCoreApplication.translate("TestDialog", u"192.168.100.11", None))
        self.btn_robot_connect.setText(QCoreApplication.translate("TestDialog", u"Connect", None))
        self.btn_transfer.setText(QCoreApplication.translate("TestDialog", u"Transfer =>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TestDialog", u"Wago", None))
        self.label_3.setText(QCoreApplication.translate("TestDialog", u"Host", None))
        self.wago_host.setInputMask(QCoreApplication.translate("TestDialog", u"000.000.000.000", None))
        self.wago_host.setText(QCoreApplication.translate("TestDialog", u"192.168.100.2", None))
        self.btn_wago_connect.setText(QCoreApplication.translate("TestDialog", u"Connect", None))
        self.label_4.setText(QCoreApplication.translate("TestDialog", u"Address", None))
        self.wago_status.setText(QCoreApplication.translate("TestDialog", u"ON", None))
        self.btn_wago_read.setText(QCoreApplication.translate("TestDialog", u"Read", None))
        self.btn_wago.setText(QCoreApplication.translate("TestDialog", u"Turn ON", None))
        self.btn_turn_off_others.setText(QCoreApplication.translate("TestDialog", u"Turn OFF Others", None))
    # retranslateUi

