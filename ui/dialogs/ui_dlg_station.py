# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_station.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StationDialog(object):
    def setupUi(self, StationDialog):
        if not StationDialog.objectName():
            StationDialog.setObjectName(u"StationDialog")
        StationDialog.resize(976, 653)
        self.verticalLayout_6 = QVBoxLayout(StationDialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(StationDialog)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.state_station1 = QLabel(self.groupBox)
        self.state_station1.setObjectName(u"state_station1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.state_station1.sizePolicy().hasHeightForWidth())
        self.state_station1.setSizePolicy(sizePolicy1)
        self.state_station1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.state_station1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.error_station1 = QLabel(self.groupBox)
        self.error_station1.setObjectName(u"error_station1")
        sizePolicy1.setHeightForWidth(self.error_station1.sizePolicy().hasHeightForWidth())
        self.error_station1.setSizePolicy(sizePolicy1)
        self.error_station1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.error_station1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(StationDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.state_station2 = QLabel(self.groupBox_3)
        self.state_station2.setObjectName(u"state_station2")
        sizePolicy1.setHeightForWidth(self.state_station2.sizePolicy().hasHeightForWidth())
        self.state_station2.setSizePolicy(sizePolicy1)
        self.state_station2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.state_station2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.error_station2 = QLabel(self.groupBox_3)
        self.error_station2.setObjectName(u"error_station2")
        sizePolicy1.setHeightForWidth(self.error_station2.sizePolicy().hasHeightForWidth())
        self.error_station2.setSizePolicy(sizePolicy1)
        self.error_station2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.error_station2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(StationDialog)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.label_13)

        self.state_station3 = QLabel(self.groupBox_7)
        self.state_station3.setObjectName(u"state_station3")
        sizePolicy1.setHeightForWidth(self.state_station3.sizePolicy().hasHeightForWidth())
        self.state_station3.setSizePolicy(sizePolicy1)
        self.state_station3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.state_station3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.label_14)

        self.error_station3 = QLabel(self.groupBox_7)
        self.error_station3.setObjectName(u"error_station3")
        sizePolicy1.setHeightForWidth(self.error_station3.sizePolicy().hasHeightForWidth())
        self.error_station3.setSizePolicy(sizePolicy1)
        self.error_station3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.error_station3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)


        self.verticalLayout_6.addWidget(self.groupBox_7)

        self.groupBox_9 = QGroupBox(StationDialog)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.label_17 = QLabel(self.groupBox_9)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)

        self.horizontalLayout_25.addWidget(self.label_17)

        self.state_station4 = QLabel(self.groupBox_9)
        self.state_station4.setObjectName(u"state_station4")
        sizePolicy1.setHeightForWidth(self.state_station4.sizePolicy().hasHeightForWidth())
        self.state_station4.setSizePolicy(sizePolicy1)
        self.state_station4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.state_station4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.label_18 = QLabel(self.groupBox_9)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)

        self.horizontalLayout_26.addWidget(self.label_18)

        self.error_station4 = QLabel(self.groupBox_9)
        self.error_station4.setObjectName(u"error_station4")
        sizePolicy1.setHeightForWidth(self.error_station4.sizePolicy().hasHeightForWidth())
        self.error_station4.setSizePolicy(sizePolicy1)
        self.error_station4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.error_station4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_26)


        self.verticalLayout_6.addWidget(self.groupBox_9)

        self.groupBox_5 = QGroupBox(StationDialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.state_station5 = QLabel(self.groupBox_5)
        self.state_station5.setObjectName(u"state_station5")
        sizePolicy1.setHeightForWidth(self.state_station5.sizePolicy().hasHeightForWidth())
        self.state_station5.setSizePolicy(sizePolicy1)
        self.state_station5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.state_station5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.label_6)

        self.error_station5 = QLabel(self.groupBox_5)
        self.error_station5.setObjectName(u"error_station5")
        sizePolicy1.setHeightForWidth(self.error_station5.sizePolicy().hasHeightForWidth())
        self.error_station5.setSizePolicy(sizePolicy1)
        self.error_station5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.error_station5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.widget = QWidget(StationDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_31 = QHBoxLayout(self.widget)
        self.horizontalLayout_31.setSpacing(30)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.groupBox_11 = QGroupBox(self.widget)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font)
        self.horizontalLayout_34 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_34.setSpacing(20)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.label_21 = QLabel(self.groupBox_11)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)

        self.horizontalLayout_32.addWidget(self.label_21)

        self.state_grease = QLabel(self.groupBox_11)
        self.state_grease.setObjectName(u"state_grease")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.state_grease.sizePolicy().hasHeightForWidth())
        self.state_grease.setSizePolicy(sizePolicy2)
        self.state_grease.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.state_grease)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(5, 5, 5, 5)
        self.label_22 = QLabel(self.groupBox_11)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)

        self.horizontalLayout_33.addWidget(self.label_22)

        self.error_grease = QLabel(self.groupBox_11)
        self.error_grease.setObjectName(u"error_grease")
        sizePolicy1.setHeightForWidth(self.error_grease.sizePolicy().hasHeightForWidth())
        self.error_grease.setSizePolicy(sizePolicy1)
        self.error_grease.setMinimumSize(QSize(100, 0))
        self.error_grease.setMaximumSize(QSize(150, 16777215))
        self.error_grease.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.error_grease)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_31.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.widget)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font)
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_35.setSpacing(20)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(5, 5, 5, 5)
        self.label_23 = QLabel(self.groupBox_12)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)

        self.horizontalLayout_36.addWidget(self.label_23)

        self.state_final_test = QLabel(self.groupBox_12)
        self.state_final_test.setObjectName(u"state_final_test")
        sizePolicy2.setHeightForWidth(self.state_final_test.sizePolicy().hasHeightForWidth())
        self.state_final_test.setSizePolicy(sizePolicy2)
        self.state_final_test.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.state_final_test)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(5, 5, 5, 5)
        self.label_24 = QLabel(self.groupBox_12)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)

        self.horizontalLayout_37.addWidget(self.label_24)

        self.error_final_test = QLabel(self.groupBox_12)
        self.error_final_test.setObjectName(u"error_final_test")
        sizePolicy1.setHeightForWidth(self.error_final_test.sizePolicy().hasHeightForWidth())
        self.error_final_test.setSizePolicy(sizePolicy1)
        self.error_final_test.setMinimumSize(QSize(100, 0))
        self.error_final_test.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.error_final_test)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_37)


        self.horizontalLayout_31.addWidget(self.groupBox_12)


        self.verticalLayout_6.addWidget(self.widget)


        self.retranslateUi(StationDialog)

        QMetaObject.connectSlotsByName(StationDialog)
    # setupUi

    def retranslateUi(self, StationDialog):
        StationDialog.setWindowTitle(QCoreApplication.translate("StationDialog", u"Station Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("StationDialog", u"Station 1", None))
        self.label.setText(QCoreApplication.translate("StationDialog", u"State:", None))
        self.state_station1.setText("")
        self.label_2.setText(QCoreApplication.translate("StationDialog", u"Robot Error:", None))
        self.error_station1.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("StationDialog", u"Station 2", None))
        self.label_3.setText(QCoreApplication.translate("StationDialog", u"State:", None))
        self.state_station2.setText("")
        self.label_4.setText(QCoreApplication.translate("StationDialog", u"Robot Error:", None))
        self.error_station2.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("StationDialog", u"Station 3", None))
        self.label_13.setText(QCoreApplication.translate("StationDialog", u"State:", None))
        self.state_station3.setText("")
        self.label_14.setText(QCoreApplication.translate("StationDialog", u"Robot Error:", None))
        self.error_station3.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("StationDialog", u"Station 4", None))
        self.label_17.setText(QCoreApplication.translate("StationDialog", u"State:", None))
        self.state_station4.setText("")
        self.label_18.setText(QCoreApplication.translate("StationDialog", u"Robot Error:", None))
        self.error_station4.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("StationDialog", u"Station 5", None))
        self.label_5.setText(QCoreApplication.translate("StationDialog", u"State:", None))
        self.state_station5.setText("")
        self.label_6.setText(QCoreApplication.translate("StationDialog", u"Robot Error:", None))
        self.error_station5.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("StationDialog", u"Grease Dispenser", None))
        self.label_21.setText(QCoreApplication.translate("StationDialog", u"State:", None))
        self.state_grease.setText("")
        self.label_22.setText(QCoreApplication.translate("StationDialog", u"Error:", None))
        self.error_grease.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("StationDialog", u"Final Test", None))
        self.label_23.setText(QCoreApplication.translate("StationDialog", u"State:", None))
        self.state_final_test.setText("")
        self.label_24.setText(QCoreApplication.translate("StationDialog", u"Error:", None))
        self.error_final_test.setText("")
    # retranslateUi

