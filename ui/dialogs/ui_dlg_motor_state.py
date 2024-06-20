# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_motor_state.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MotorStateDialog(object):
    def setupUi(self, MotorStateDialog):
        if not MotorStateDialog.objectName():
            MotorStateDialog.setObjectName(u"MotorStateDialog")
        MotorStateDialog.resize(481, 342)
        font = QFont()
        font.setPointSize(10)
        MotorStateDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(MotorStateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(MotorStateDialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_13.addWidget(self.label_12)

        self.motor_status_front_track_escapement = QLabel(MotorStateDialog)
        self.motor_status_front_track_escapement.setObjectName(u"motor_status_front_track_escapement")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motor_status_front_track_escapement.sizePolicy().hasHeightForWidth())
        self.motor_status_front_track_escapement.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.motor_status_front_track_escapement)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(MotorStateDialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_15.addWidget(self.label_14)

        self.motor_status_rear_track_escapement = QLabel(MotorStateDialog)
        self.motor_status_rear_track_escapement.setObjectName(u"motor_status_rear_track_escapement")
        sizePolicy.setHeightForWidth(self.motor_status_rear_track_escapement.sizePolicy().hasHeightForWidth())
        self.motor_status_rear_track_escapement.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.motor_status_rear_track_escapement)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(MotorStateDialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_16.addWidget(self.label_15)

        self.motor_status_front_oring_expander = QLabel(MotorStateDialog)
        self.motor_status_front_oring_expander.setObjectName(u"motor_status_front_oring_expander")
        sizePolicy.setHeightForWidth(self.motor_status_front_oring_expander.sizePolicy().hasHeightForWidth())
        self.motor_status_front_oring_expander.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.motor_status_front_oring_expander)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(MotorStateDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_11.addWidget(self.label_10)

        self.motor_status_rear_oring_expander = QLabel(MotorStateDialog)
        self.motor_status_rear_oring_expander.setObjectName(u"motor_status_rear_oring_expander")
        sizePolicy.setHeightForWidth(self.motor_status_rear_oring_expander.sizePolicy().hasHeightForWidth())
        self.motor_status_rear_oring_expander.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.motor_status_rear_oring_expander)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(MotorStateDialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_14.addWidget(self.label_13)

        self.motor_status_front_indexer = QLabel(MotorStateDialog)
        self.motor_status_front_indexer.setObjectName(u"motor_status_front_indexer")
        sizePolicy.setHeightForWidth(self.motor_status_front_indexer.sizePolicy().hasHeightForWidth())
        self.motor_status_front_indexer.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.motor_status_front_indexer)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(MotorStateDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_12.addWidget(self.label_11)

        self.motor_status_rear_indexer = QLabel(MotorStateDialog)
        self.motor_status_rear_indexer.setObjectName(u"motor_status_rear_indexer")
        sizePolicy.setHeightForWidth(self.motor_status_rear_indexer.sizePolicy().hasHeightForWidth())
        self.motor_status_rear_indexer.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.motor_status_rear_indexer)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(MotorStateDialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_17.addWidget(self.label_16)

        self.motor_status_rotary_flipper = QLabel(MotorStateDialog)
        self.motor_status_rotary_flipper.setObjectName(u"motor_status_rotary_flipper")
        sizePolicy.setHeightForWidth(self.motor_status_rotary_flipper.sizePolicy().hasHeightForWidth())
        self.motor_status_rotary_flipper.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.motor_status_rotary_flipper)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(MotorStateDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_10.addWidget(self.label_9)

        self.motor_status_piston_orientor = QLabel(MotorStateDialog)
        self.motor_status_piston_orientor.setObjectName(u"motor_status_piston_orientor")
        sizePolicy.setHeightForWidth(self.motor_status_piston_orientor.sizePolicy().hasHeightForWidth())
        self.motor_status_piston_orientor.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.motor_status_piston_orientor)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.retranslateUi(MotorStateDialog)

        QMetaObject.connectSlotsByName(MotorStateDialog)
    # setupUi

    def retranslateUi(self, MotorStateDialog):
        MotorStateDialog.setWindowTitle(QCoreApplication.translate("MotorStateDialog", u"Motor Status", None))
        self.label_12.setText(QCoreApplication.translate("MotorStateDialog", u"Front Track Escapement:", None))
        self.motor_status_front_track_escapement.setText("")
        self.label_14.setText(QCoreApplication.translate("MotorStateDialog", u"Rear Track Escapement:", None))
        self.motor_status_rear_track_escapement.setText("")
        self.label_15.setText(QCoreApplication.translate("MotorStateDialog", u"Front O-Ring Expander:", None))
        self.motor_status_front_oring_expander.setText("")
        self.label_10.setText(QCoreApplication.translate("MotorStateDialog", u"Rear O-Ring Expander:", None))
        self.motor_status_rear_oring_expander.setText("")
        self.label_13.setText(QCoreApplication.translate("MotorStateDialog", u"Front Indexer:", None))
        self.motor_status_front_indexer.setText("")
        self.label_11.setText(QCoreApplication.translate("MotorStateDialog", u"Rear Indexer:", None))
        self.motor_status_rear_indexer.setText("")
        self.label_16.setText(QCoreApplication.translate("MotorStateDialog", u"Rotary Flipper:", None))
        self.motor_status_rotary_flipper.setText("")
        self.label_9.setText(QCoreApplication.translate("MotorStateDialog", u"Piston Orientor:", None))
        self.motor_status_piston_orientor.setText("")
    # retranslateUi

