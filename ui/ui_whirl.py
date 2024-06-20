# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whirl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets.board import BoardWidget

import ui.whirl_rc

class Ui_Whirl(object):
    def setupUi(self, Whirl):
        if not Whirl.objectName():
            Whirl.setObjectName(u"Whirl")
        Whirl.resize(1458, 927)
        Whirl.setMaximumSize(QSize(16777215, 1080))
        font = QFont()
        font.setPointSize(12)
        Whirl.setFont(font)
        self.actionTest = QAction(Whirl)
        self.actionTest.setObjectName(u"actionTest")
        icon = QIcon()
        icon.addFile(u":/img/img/test.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTest.setIcon(icon)
        self.actionAbout = QAction(Whirl)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSettings = QAction(Whirl)
        self.actionSettings.setObjectName(u"actionSettings")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/Settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionStation = QAction(Whirl)
        self.actionStation.setObjectName(u"actionStation")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/station.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStation.setIcon(icon2)
        self.actionDoor = QAction(Whirl)
        self.actionDoor.setObjectName(u"actionDoor")
        icon3 = QIcon()
        icon3.addFile(u":/img/img/door_closed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDoor.setIcon(icon3)
        self.actionProductTracking = QAction(Whirl)
        self.actionProductTracking.setObjectName(u"actionProductTracking")
        icon4 = QIcon()
        icon4.addFile(u":/img/img/barchart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionProductTracking.setIcon(icon4)
        self.centralwidget = QWidget(Whirl)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.board = BoardWidget(self.centralwidget)
        self.board.setObjectName(u"board")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.board.sizePolicy().hasHeightForWidth())
        self.board.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.board)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.door_circuit = QLabel(self.widget)
        self.door_circuit.setObjectName(u"door_circuit")
        self.door_circuit.setMinimumSize(QSize(25, 25))
        self.door_circuit.setMaximumSize(QSize(25, 25))
        self.door_circuit.setStyleSheet(u"background-color: #aa0000;\n"
"border-radius: 12px;")

        self.horizontalLayout_2.addWidget(self.door_circuit)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.lb_product_type = QLabel(self.centralwidget)
        self.lb_product_type.setObjectName(u"lb_product_type")

        self.horizontalLayout.addWidget(self.lb_product_type)

        self.btn_clear_pallet_state = QPushButton(self.centralwidget)
        self.btn_clear_pallet_state.setObjectName(u"btn_clear_pallet_state")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_clear_pallet_state.sizePolicy().hasHeightForWidth())
        self.btn_clear_pallet_state.setSizePolicy(sizePolicy1)
        self.btn_clear_pallet_state.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.btn_clear_pallet_state)

        self.mode = QComboBox(self.centralwidget)
        icon5 = QIcon()
        icon5.addFile(u":/img/img/continuous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mode.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/img/img/cycle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mode.addItem(icon6, "")
        self.mode.setObjectName(u"mode")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mode.sizePolicy().hasHeightForWidth())
        self.mode.setSizePolicy(sizePolicy2)
        self.mode.setMinimumSize(QSize(130, 0))

        self.horizontalLayout.addWidget(self.mode)

        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        sizePolicy1.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btn_stop)

        self.btn_flush = QPushButton(self.centralwidget)
        self.btn_flush.setObjectName(u"btn_flush")
        sizePolicy1.setHeightForWidth(self.btn_flush.sizePolicy().hasHeightForWidth())
        self.btn_flush.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btn_flush)

        self.btn_build = QPushButton(self.centralwidget)
        self.btn_build.setObjectName(u"btn_build")
        sizePolicy1.setHeightForWidth(self.btn_build.sizePolicy().hasHeightForWidth())
        self.btn_build.setSizePolicy(sizePolicy1)
        self.btn_build.setMinimumSize(QSize(80, 35))

        self.horizontalLayout.addWidget(self.btn_build)


        self.verticalLayout.addLayout(self.horizontalLayout)

        Whirl.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Whirl)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1458, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menuActions = QMenu(self.menubar)
        self.menuActions.setObjectName(u"menuActions")
        Whirl.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Whirl)
        self.statusbar.setObjectName(u"statusbar")
        Whirl.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(Whirl)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setIconSize(QSize(36, 36))
        Whirl.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Help.addAction(self.actionAbout)
        self.menuActions.addAction(self.actionStation)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionSettings)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionTest)
        self.menuActions.addAction(self.actionProductTracking)
        self.toolBar.addAction(self.actionStation)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTest)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDoor)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionProductTracking)

        self.retranslateUi(Whirl)

        QMetaObject.connectSlotsByName(Whirl)
    # setupUi

    def retranslateUi(self, Whirl):
        Whirl.setWindowTitle(QCoreApplication.translate("Whirl", u"Whirl", None))
        self.actionTest.setText(QCoreApplication.translate("Whirl", u"Test Peripherals", None))
#if QT_CONFIG(tooltip)
        self.actionTest.setToolTip(QCoreApplication.translate("Whirl", u"Test Robot & Cognex & FlexFeeder", None))
#endif // QT_CONFIG(tooltip)
        self.actionAbout.setText(QCoreApplication.translate("Whirl", u"&About", None))
        self.actionSettings.setText(QCoreApplication.translate("Whirl", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.actionSettings.setToolTip(QCoreApplication.translate("Whirl", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.actionStation.setText(QCoreApplication.translate("Whirl", u"Station", None))
#if QT_CONFIG(tooltip)
        self.actionStation.setToolTip(QCoreApplication.translate("Whirl", u"Test & monitor station", None))
#endif // QT_CONFIG(tooltip)
        self.actionDoor.setText(QCoreApplication.translate("Whirl", u"actionDoor", None))
#if QT_CONFIG(tooltip)
        self.actionDoor.setToolTip(QCoreApplication.translate("Whirl", u"Open/Close Door", None))
#endif // QT_CONFIG(tooltip)
        self.actionProductTracking.setText(QCoreApplication.translate("Whirl", u"Product Tracking", None))
#if QT_CONFIG(shortcut)
        self.actionProductTracking.setShortcut(QCoreApplication.translate("Whirl", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("Whirl", u"Door Circuit:", None))
        self.door_circuit.setText("")
        self.lb_product_type.setText(QCoreApplication.translate("Whirl", u"Product Type: Not Selected", None))
        self.btn_clear_pallet_state.setText(QCoreApplication.translate("Whirl", u" Clear Pallet State ", None))
        self.mode.setItemText(0, QCoreApplication.translate("Whirl", u"Continuous", None))
        self.mode.setItemText(1, QCoreApplication.translate("Whirl", u"Cycle", None))

        self.btn_stop.setText(QCoreApplication.translate("Whirl", u"Stop", None))
        self.btn_flush.setText(QCoreApplication.translate("Whirl", u"Flush", None))
        self.btn_build.setText(QCoreApplication.translate("Whirl", u"Start", None))
        self.menu_File.setTitle(QCoreApplication.translate("Whirl", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("Whirl", u"&Help", None))
        self.menuActions.setTitle(QCoreApplication.translate("Whirl", u"&Dialogs", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Whirl", u"toolBar", None))
    # retranslateUi

