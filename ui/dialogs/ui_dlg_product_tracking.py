# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_product_tracking.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProductTrackingDialog(object):
    def setupUi(self, ProductTrackingDialog):
        if not ProductTrackingDialog.objectName():
            ProductTrackingDialog.setObjectName(u"ProductTrackingDialog")
        ProductTrackingDialog.resize(389, 432)
        font = QFont()
        font.setPointSize(12)
        ProductTrackingDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(ProductTrackingDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.lb_total = QLabel(ProductTrackingDialog)
        self.lb_total.setObjectName(u"lb_total")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_total.sizePolicy().hasHeightForWidth())
        self.lb_total.setSizePolicy(sizePolicy)
        self.lb_total.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_total)

        self.total = QLabel(ProductTrackingDialog)
        self.total.setObjectName(u"total")
        self.total.setMinimumSize(QSize(50, 0))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.total.setFont(font1)

        self.horizontalLayout.addWidget(self.total)

        self.btn_reset_total = QPushButton(ProductTrackingDialog)
        self.btn_reset_total.setObjectName(u"btn_reset_total")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_reset_total.sizePolicy().hasHeightForWidth())
        self.btn_reset_total.setSizePolicy(sizePolicy1)
        self.btn_reset_total.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_reset_total)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.lb_total_current = QLabel(ProductTrackingDialog)
        self.lb_total_current.setObjectName(u"lb_total_current")
        sizePolicy.setHeightForWidth(self.lb_total_current.sizePolicy().hasHeightForWidth())
        self.lb_total_current.setSizePolicy(sizePolicy)
        self.lb_total_current.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lb_total_current)

        self.total_current = QLabel(ProductTrackingDialog)
        self.total_current.setObjectName(u"total_current")
        self.total_current.setMinimumSize(QSize(50, 0))
        self.total_current.setFont(font1)

        self.horizontalLayout_2.addWidget(self.total_current)

        self.btn_reset_total_current = QPushButton(ProductTrackingDialog)
        self.btn_reset_total_current.setObjectName(u"btn_reset_total_current")
        sizePolicy1.setHeightForWidth(self.btn_reset_total_current.sizePolicy().hasHeightForWidth())
        self.btn_reset_total_current.setSizePolicy(sizePolicy1)
        self.btn_reset_total_current.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btn_reset_total_current)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.lb_rejected = QLabel(ProductTrackingDialog)
        self.lb_rejected.setObjectName(u"lb_rejected")
        sizePolicy.setHeightForWidth(self.lb_rejected.sizePolicy().hasHeightForWidth())
        self.lb_rejected.setSizePolicy(sizePolicy)
        self.lb_rejected.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_rejected)

        self.rejected = QLabel(ProductTrackingDialog)
        self.rejected.setObjectName(u"rejected")
        self.rejected.setMinimumSize(QSize(50, 0))
        self.rejected.setFont(font1)

        self.horizontalLayout_3.addWidget(self.rejected)

        self.btn_reset_rejected = QPushButton(ProductTrackingDialog)
        self.btn_reset_rejected.setObjectName(u"btn_reset_rejected")
        sizePolicy1.setHeightForWidth(self.btn_reset_rejected.sizePolicy().hasHeightForWidth())
        self.btn_reset_rejected.setSizePolicy(sizePolicy1)
        self.btn_reset_rejected.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btn_reset_rejected)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.lb_rejected_current = QLabel(ProductTrackingDialog)
        self.lb_rejected_current.setObjectName(u"lb_rejected_current")
        sizePolicy.setHeightForWidth(self.lb_rejected_current.sizePolicy().hasHeightForWidth())
        self.lb_rejected_current.setSizePolicy(sizePolicy)
        self.lb_rejected_current.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_rejected_current)

        self.rejected_current = QLabel(ProductTrackingDialog)
        self.rejected_current.setObjectName(u"rejected_current")
        self.rejected_current.setMinimumSize(QSize(50, 0))
        self.rejected_current.setFont(font1)

        self.horizontalLayout_4.addWidget(self.rejected_current)

        self.btn_reset_rejected_current = QPushButton(ProductTrackingDialog)
        self.btn_reset_rejected_current.setObjectName(u"btn_reset_rejected_current")
        sizePolicy1.setHeightForWidth(self.btn_reset_rejected_current.sizePolicy().hasHeightForWidth())
        self.btn_reset_rejected_current.setSizePolicy(sizePolicy1)
        self.btn_reset_rejected_current.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.btn_reset_rejected_current)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 5, 10, 5)
        self.lb_avg_built_hourly = QLabel(ProductTrackingDialog)
        self.lb_avg_built_hourly.setObjectName(u"lb_avg_built_hourly")
        sizePolicy.setHeightForWidth(self.lb_avg_built_hourly.sizePolicy().hasHeightForWidth())
        self.lb_avg_built_hourly.setSizePolicy(sizePolicy)
        self.lb_avg_built_hourly.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_avg_built_hourly)

        self.avg_built_hourly = QLabel(ProductTrackingDialog)
        self.avg_built_hourly.setObjectName(u"avg_built_hourly")
        self.avg_built_hourly.setMinimumSize(QSize(50, 0))
        self.avg_built_hourly.setFont(font1)

        self.horizontalLayout_5.addWidget(self.avg_built_hourly)

        self.btn_reset_avg_built_hourly = QPushButton(ProductTrackingDialog)
        self.btn_reset_avg_built_hourly.setObjectName(u"btn_reset_avg_built_hourly")
        sizePolicy1.setHeightForWidth(self.btn_reset_avg_built_hourly.sizePolicy().hasHeightForWidth())
        self.btn_reset_avg_built_hourly.setSizePolicy(sizePolicy1)
        self.btn_reset_avg_built_hourly.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.btn_reset_avg_built_hourly)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 5, 10, 5)
        self.lb_avg_rejected_hourly = QLabel(ProductTrackingDialog)
        self.lb_avg_rejected_hourly.setObjectName(u"lb_avg_rejected_hourly")
        sizePolicy.setHeightForWidth(self.lb_avg_rejected_hourly.sizePolicy().hasHeightForWidth())
        self.lb_avg_rejected_hourly.setSizePolicy(sizePolicy)
        self.lb_avg_rejected_hourly.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_avg_rejected_hourly)

        self.avg_rejected_hourly = QLabel(ProductTrackingDialog)
        self.avg_rejected_hourly.setObjectName(u"avg_rejected_hourly")
        self.avg_rejected_hourly.setMinimumSize(QSize(50, 0))
        self.avg_rejected_hourly.setFont(font1)

        self.horizontalLayout_6.addWidget(self.avg_rejected_hourly)

        self.btn_reset_avg_rejected_hourly = QPushButton(ProductTrackingDialog)
        self.btn_reset_avg_rejected_hourly.setObjectName(u"btn_reset_avg_rejected_hourly")
        sizePolicy1.setHeightForWidth(self.btn_reset_avg_rejected_hourly.sizePolicy().hasHeightForWidth())
        self.btn_reset_avg_rejected_hourly.setSizePolicy(sizePolicy1)
        self.btn_reset_avg_rejected_hourly.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.btn_reset_avg_rejected_hourly)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.widget = QWidget(ProductTrackingDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(185, 0))
        self.label.setMaximumSize(QSize(185, 16777215))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.parts_count = QLabel(self.widget)
        self.parts_count.setObjectName(u"parts_count")
        sizePolicy.setHeightForWidth(self.parts_count.sizePolicy().hasHeightForWidth())
        self.parts_count.setSizePolicy(sizePolicy)
        self.parts_count.setFont(font1)

        self.horizontalLayout_8.addWidget(self.parts_count)


        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_reset_all = QPushButton(ProductTrackingDialog)
        self.btn_reset_all.setObjectName(u"btn_reset_all")
        self.btn_reset_all.setMinimumSize(QSize(100, 35))

        self.horizontalLayout_7.addWidget(self.btn_reset_all)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.retranslateUi(ProductTrackingDialog)

        QMetaObject.connectSlotsByName(ProductTrackingDialog)
    # setupUi

    def retranslateUi(self, ProductTrackingDialog):
        ProductTrackingDialog.setWindowTitle(QCoreApplication.translate("ProductTrackingDialog", u"Product Tracking", None))
        self.lb_total.setText(QCoreApplication.translate("ProductTrackingDialog", u"Parts Produced(All Time):", None))
        self.total.setText(QCoreApplication.translate("ProductTrackingDialog", u"0", None))
        self.btn_reset_total.setText(QCoreApplication.translate("ProductTrackingDialog", u"Reset", None))
        self.lb_total_current.setText(QCoreApplication.translate("ProductTrackingDialog", u"Parts Produced(Current):", None))
        self.total_current.setText(QCoreApplication.translate("ProductTrackingDialog", u"0", None))
        self.btn_reset_total_current.setText(QCoreApplication.translate("ProductTrackingDialog", u"Reset", None))
        self.lb_rejected.setText(QCoreApplication.translate("ProductTrackingDialog", u"Parts Rejected(All Time):", None))
        self.rejected.setText(QCoreApplication.translate("ProductTrackingDialog", u"0", None))
        self.btn_reset_rejected.setText(QCoreApplication.translate("ProductTrackingDialog", u"Reset", None))
        self.lb_rejected_current.setText(QCoreApplication.translate("ProductTrackingDialog", u"Parts Rejected(Current):", None))
        self.rejected_current.setText(QCoreApplication.translate("ProductTrackingDialog", u"0", None))
        self.btn_reset_rejected_current.setText(QCoreApplication.translate("ProductTrackingDialog", u"Reset", None))
        self.lb_avg_built_hourly.setText(QCoreApplication.translate("ProductTrackingDialog", u"Avg. Produced Hourly:", None))
        self.avg_built_hourly.setText(QCoreApplication.translate("ProductTrackingDialog", u"0", None))
        self.btn_reset_avg_built_hourly.setText(QCoreApplication.translate("ProductTrackingDialog", u"Reset", None))
        self.lb_avg_rejected_hourly.setText(QCoreApplication.translate("ProductTrackingDialog", u"Avg. Rejected Hourly:", None))
        self.avg_rejected_hourly.setText(QCoreApplication.translate("ProductTrackingDialog", u"0", None))
        self.btn_reset_avg_rejected_hourly.setText(QCoreApplication.translate("ProductTrackingDialog", u"Reset", None))
        self.label.setText(QCoreApplication.translate("ProductTrackingDialog", u"Current Parts in Box:", None))
        self.parts_count.setText(QCoreApplication.translate("ProductTrackingDialog", u"0", None))
        self.btn_reset_all.setText(QCoreApplication.translate("ProductTrackingDialog", u"Reset All", None))
    # retranslateUi

