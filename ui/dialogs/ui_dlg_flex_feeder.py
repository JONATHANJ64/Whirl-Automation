# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_flex_feeder.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui.whirl_rc

class Ui_FlexFeederDialog(object):
    def setupUi(self, FlexFeederDialog):
        if not FlexFeederDialog.objectName():
            FlexFeederDialog.setObjectName(u"FlexFeederDialog")
        FlexFeederDialog.resize(1040, 997)
        font = QFont()
        font.setPointSize(12)
        FlexFeederDialog.setFont(font)
        self.horizontalLayout = QHBoxLayout(FlexFeederDialog)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_4 = QGroupBox(FlexFeederDialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(20)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_4)

        self.type = QLabel(self.groupBox_4)
        self.type.setObjectName(u"type")
        self.type.setMinimumSize(QSize(160, 0))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.type.setFont(font1)

        self.horizontalLayout_44.addWidget(self.type)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_5)


        self.verticalLayout_22.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_26 = QLabel(self.groupBox_7)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_33.addWidget(self.label_26)

        self.pre_check_timeout = QDoubleSpinBox(self.groupBox_7)
        self.pre_check_timeout.setObjectName(u"pre_check_timeout")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pre_check_timeout.sizePolicy().hasHeightForWidth())
        self.pre_check_timeout.setSizePolicy(sizePolicy)
        self.pre_check_timeout.setMinimumSize(QSize(86, 0))
        self.pre_check_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.pre_check_timeout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_32 = QLabel(self.groupBox_7)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_37.addWidget(self.label_32)

        self.feeding_timeout = QDoubleSpinBox(self.groupBox_7)
        self.feeding_timeout.setObjectName(u"feeding_timeout")
        sizePolicy.setHeightForWidth(self.feeding_timeout.sizePolicy().hasHeightForWidth())
        self.feeding_timeout.setSizePolicy(sizePolicy)
        self.feeding_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.feeding_timeout.setMaximum(9999.000000000000000)

        self.horizontalLayout_37.addWidget(self.feeding_timeout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_33 = QLabel(self.groupBox_7)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_38.addWidget(self.label_33)

        self.feeder_idle_timeout = QDoubleSpinBox(self.groupBox_7)
        self.feeder_idle_timeout.setObjectName(u"feeder_idle_timeout")
        sizePolicy.setHeightForWidth(self.feeder_idle_timeout.sizePolicy().hasHeightForWidth())
        self.feeder_idle_timeout.setSizePolicy(sizePolicy)
        self.feeder_idle_timeout.setMinimumSize(QSize(86, 0))
        self.feeder_idle_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.feeder_idle_timeout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_34 = QLabel(self.groupBox_7)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_39.addWidget(self.label_34)

        self.part_presence_timeout = QDoubleSpinBox(self.groupBox_7)
        self.part_presence_timeout.setObjectName(u"part_presence_timeout")
        sizePolicy.setHeightForWidth(self.part_presence_timeout.sizePolicy().hasHeightForWidth())
        self.part_presence_timeout.setSizePolicy(sizePolicy)
        self.part_presence_timeout.setMinimumSize(QSize(86, 0))
        self.part_presence_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.part_presence_timeout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_39)


        self.horizontalLayout_31.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_35 = QLabel(self.groupBox_8)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_40.addWidget(self.label_35)

        self.motors_main_speed_limit = QDoubleSpinBox(self.groupBox_8)
        self.motors_main_speed_limit.setObjectName(u"motors_main_speed_limit")
        sizePolicy.setHeightForWidth(self.motors_main_speed_limit.sizePolicy().hasHeightForWidth())
        self.motors_main_speed_limit.setSizePolicy(sizePolicy)
        self.motors_main_speed_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.motors_main_speed_limit.setDecimals(1)
        self.motors_main_speed_limit.setMaximum(3000.000000000000000)

        self.horizontalLayout_40.addWidget(self.motors_main_speed_limit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_36 = QLabel(self.groupBox_8)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_41.addWidget(self.label_36)

        self.motors_feeder_speed_limit = QDoubleSpinBox(self.groupBox_8)
        self.motors_feeder_speed_limit.setObjectName(u"motors_feeder_speed_limit")
        sizePolicy.setHeightForWidth(self.motors_feeder_speed_limit.sizePolicy().hasHeightForWidth())
        self.motors_feeder_speed_limit.setSizePolicy(sizePolicy)
        self.motors_feeder_speed_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.motors_feeder_speed_limit.setDecimals(1)
        self.motors_feeder_speed_limit.setMaximum(1000.000000000000000)

        self.horizontalLayout_41.addWidget(self.motors_feeder_speed_limit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_37 = QLabel(self.groupBox_8)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_42.addWidget(self.label_37)

        self.motors_main_speed_drop_limit = QDoubleSpinBox(self.groupBox_8)
        self.motors_main_speed_drop_limit.setObjectName(u"motors_main_speed_drop_limit")
        sizePolicy.setHeightForWidth(self.motors_main_speed_drop_limit.sizePolicy().hasHeightForWidth())
        self.motors_main_speed_drop_limit.setSizePolicy(sizePolicy)
        self.motors_main_speed_drop_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.motors_main_speed_drop_limit.setDecimals(1)
        self.motors_main_speed_drop_limit.setMaximum(1000.000000000000000)

        self.horizontalLayout_42.addWidget(self.motors_main_speed_drop_limit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_38 = QLabel(self.groupBox_8)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_43.addWidget(self.label_38)

        self.motors_feeder_speed_drop_limit = QDoubleSpinBox(self.groupBox_8)
        self.motors_feeder_speed_drop_limit.setObjectName(u"motors_feeder_speed_drop_limit")
        sizePolicy.setHeightForWidth(self.motors_feeder_speed_drop_limit.sizePolicy().hasHeightForWidth())
        self.motors_feeder_speed_drop_limit.setSizePolicy(sizePolicy)
        self.motors_feeder_speed_drop_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.motors_feeder_speed_drop_limit.setDecimals(1)
        self.motors_feeder_speed_drop_limit.setMaximum(1000.000000000000000)

        self.horizontalLayout_43.addWidget(self.motors_feeder_speed_drop_limit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_43)


        self.horizontalLayout_31.addWidget(self.groupBox_8)


        self.verticalLayout_22.addLayout(self.horizontalLayout_31)

        self.groupBox_9 = QGroupBox(self.groupBox_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(700, 200))
        self.horizontalLayout_45 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_45.setSpacing(10)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(20, 20, 20, 20)
        self.groupBox_10 = QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_40 = QLabel(self.groupBox_10)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_46.addWidget(self.label_40)

        self.ir_hopper_empty_frequency = QComboBox(self.groupBox_10)
        self.ir_hopper_empty_frequency.addItem("")
        self.ir_hopper_empty_frequency.addItem("")
        self.ir_hopper_empty_frequency.addItem("")
        self.ir_hopper_empty_frequency.addItem("")
        self.ir_hopper_empty_frequency.addItem("")
        self.ir_hopper_empty_frequency.addItem("")
        self.ir_hopper_empty_frequency.setObjectName(u"ir_hopper_empty_frequency")
        sizePolicy.setHeightForWidth(self.ir_hopper_empty_frequency.sizePolicy().hasHeightForWidth())
        self.ir_hopper_empty_frequency.setSizePolicy(sizePolicy)

        self.horizontalLayout_46.addWidget(self.ir_hopper_empty_frequency)


        self.verticalLayout_14.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_41 = QLabel(self.groupBox_10)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_47.addWidget(self.label_41)

        self.ir_hopper_empty_interval = QSpinBox(self.groupBox_10)
        self.ir_hopper_empty_interval.setObjectName(u"ir_hopper_empty_interval")
        sizePolicy.setHeightForWidth(self.ir_hopper_empty_interval.sizePolicy().hasHeightForWidth())
        self.ir_hopper_empty_interval.setSizePolicy(sizePolicy)
        self.ir_hopper_empty_interval.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ir_hopper_empty_interval.setMaximum(2000)

        self.horizontalLayout_47.addWidget(self.ir_hopper_empty_interval)


        self.verticalLayout_14.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_42 = QLabel(self.groupBox_10)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_48.addWidget(self.label_42)

        self.ir_hopper_empty_count = QSpinBox(self.groupBox_10)
        self.ir_hopper_empty_count.setObjectName(u"ir_hopper_empty_count")
        sizePolicy.setHeightForWidth(self.ir_hopper_empty_count.sizePolicy().hasHeightForWidth())
        self.ir_hopper_empty_count.setSizePolicy(sizePolicy)
        self.ir_hopper_empty_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ir_hopper_empty_count.setMaximum(20)
        self.ir_hopper_empty_count.setValue(3)

        self.horizontalLayout_48.addWidget(self.ir_hopper_empty_count)


        self.verticalLayout_14.addLayout(self.horizontalLayout_48)


        self.horizontalLayout_45.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_43 = QLabel(self.groupBox_11)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_49.addWidget(self.label_43)

        self.ir_conveyor_entrance_frequency = QComboBox(self.groupBox_11)
        self.ir_conveyor_entrance_frequency.addItem("")
        self.ir_conveyor_entrance_frequency.addItem("")
        self.ir_conveyor_entrance_frequency.addItem("")
        self.ir_conveyor_entrance_frequency.addItem("")
        self.ir_conveyor_entrance_frequency.addItem("")
        self.ir_conveyor_entrance_frequency.addItem("")
        self.ir_conveyor_entrance_frequency.setObjectName(u"ir_conveyor_entrance_frequency")
        sizePolicy.setHeightForWidth(self.ir_conveyor_entrance_frequency.sizePolicy().hasHeightForWidth())
        self.ir_conveyor_entrance_frequency.setSizePolicy(sizePolicy)

        self.horizontalLayout_49.addWidget(self.ir_conveyor_entrance_frequency)


        self.verticalLayout_15.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_44 = QLabel(self.groupBox_11)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_50.addWidget(self.label_44)

        self.ir_conveyor_entrance_interval = QSpinBox(self.groupBox_11)
        self.ir_conveyor_entrance_interval.setObjectName(u"ir_conveyor_entrance_interval")
        sizePolicy.setHeightForWidth(self.ir_conveyor_entrance_interval.sizePolicy().hasHeightForWidth())
        self.ir_conveyor_entrance_interval.setSizePolicy(sizePolicy)
        self.ir_conveyor_entrance_interval.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ir_conveyor_entrance_interval.setMaximum(2000)

        self.horizontalLayout_50.addWidget(self.ir_conveyor_entrance_interval)


        self.verticalLayout_15.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_45 = QLabel(self.groupBox_11)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_51.addWidget(self.label_45)

        self.ir_conveyor_entrance_count = QSpinBox(self.groupBox_11)
        self.ir_conveyor_entrance_count.setObjectName(u"ir_conveyor_entrance_count")
        sizePolicy.setHeightForWidth(self.ir_conveyor_entrance_count.sizePolicy().hasHeightForWidth())
        self.ir_conveyor_entrance_count.setSizePolicy(sizePolicy)
        self.ir_conveyor_entrance_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ir_conveyor_entrance_count.setMaximum(20)
        self.ir_conveyor_entrance_count.setValue(3)

        self.horizontalLayout_51.addWidget(self.ir_conveyor_entrance_count)


        self.verticalLayout_15.addLayout(self.horizontalLayout_51)


        self.horizontalLayout_45.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_46 = QLabel(self.groupBox_12)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_52.addWidget(self.label_46)

        self.ir_part_presence_frequency = QComboBox(self.groupBox_12)
        self.ir_part_presence_frequency.addItem("")
        self.ir_part_presence_frequency.addItem("")
        self.ir_part_presence_frequency.addItem("")
        self.ir_part_presence_frequency.addItem("")
        self.ir_part_presence_frequency.addItem("")
        self.ir_part_presence_frequency.addItem("")
        self.ir_part_presence_frequency.setObjectName(u"ir_part_presence_frequency")
        sizePolicy.setHeightForWidth(self.ir_part_presence_frequency.sizePolicy().hasHeightForWidth())
        self.ir_part_presence_frequency.setSizePolicy(sizePolicy)

        self.horizontalLayout_52.addWidget(self.ir_part_presence_frequency)


        self.verticalLayout_16.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_47 = QLabel(self.groupBox_12)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_53.addWidget(self.label_47)

        self.ir_part_presence_interval = QSpinBox(self.groupBox_12)
        self.ir_part_presence_interval.setObjectName(u"ir_part_presence_interval")
        sizePolicy.setHeightForWidth(self.ir_part_presence_interval.sizePolicy().hasHeightForWidth())
        self.ir_part_presence_interval.setSizePolicy(sizePolicy)
        self.ir_part_presence_interval.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ir_part_presence_interval.setMaximum(2000)

        self.horizontalLayout_53.addWidget(self.ir_part_presence_interval)


        self.verticalLayout_16.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_48 = QLabel(self.groupBox_12)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_54.addWidget(self.label_48)

        self.ir_part_presence_count = QSpinBox(self.groupBox_12)
        self.ir_part_presence_count.setObjectName(u"ir_part_presence_count")
        sizePolicy.setHeightForWidth(self.ir_part_presence_count.sizePolicy().hasHeightForWidth())
        self.ir_part_presence_count.setSizePolicy(sizePolicy)
        self.ir_part_presence_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ir_part_presence_count.setMaximum(20)
        self.ir_part_presence_count.setValue(3)

        self.horizontalLayout_54.addWidget(self.ir_part_presence_count)


        self.verticalLayout_16.addLayout(self.horizontalLayout_54)


        self.horizontalLayout_45.addWidget(self.groupBox_12)


        self.verticalLayout_22.addWidget(self.groupBox_9)

        self.group_other = QGroupBox(self.groupBox_4)
        self.group_other.setObjectName(u"group_other")
        self.group_other.setMinimumSize(QSize(0, 270))
        self.group_other.setMaximumSize(QSize(16777215, 270))
        self.verticalLayout_17 = QVBoxLayout(self.group_other)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stack_other = QStackedWidget(self.group_other)
        self.stack_other.setObjectName(u"stack_other")
        self.page_recirculating = QWidget()
        self.page_recirculating.setObjectName(u"page_recirculating")
        self.horizontalLayout_55 = QHBoxLayout(self.page_recirculating)
        self.horizontalLayout_55.setSpacing(10)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_49 = QLabel(self.page_recirculating)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_56.addWidget(self.label_49)

        self.shake_reject_counter = QSpinBox(self.page_recirculating)
        self.shake_reject_counter.setObjectName(u"shake_reject_counter")
        sizePolicy.setHeightForWidth(self.shake_reject_counter.sizePolicy().hasHeightForWidth())
        self.shake_reject_counter.setSizePolicy(sizePolicy)
        self.shake_reject_counter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.shake_reject_counter.setMaximum(20)
        self.shake_reject_counter.setValue(4)

        self.horizontalLayout_56.addWidget(self.shake_reject_counter)


        self.verticalLayout_18.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_51 = QLabel(self.page_recirculating)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_58.addWidget(self.label_51)

        self.shake_reject_timeout = QSpinBox(self.page_recirculating)
        self.shake_reject_timeout.setObjectName(u"shake_reject_timeout")
        sizePolicy.setHeightForWidth(self.shake_reject_timeout.sizePolicy().hasHeightForWidth())
        self.shake_reject_timeout.setSizePolicy(sizePolicy)
        self.shake_reject_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.shake_reject_timeout.setMaximum(10)
        self.shake_reject_timeout.setValue(3)

        self.horizontalLayout_58.addWidget(self.shake_reject_timeout)


        self.verticalLayout_18.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_52 = QLabel(self.page_recirculating)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_59.addWidget(self.label_52)

        self.shake_reject_duration = QDoubleSpinBox(self.page_recirculating)
        self.shake_reject_duration.setObjectName(u"shake_reject_duration")
        sizePolicy.setHeightForWidth(self.shake_reject_duration.sizePolicy().hasHeightForWidth())
        self.shake_reject_duration.setSizePolicy(sizePolicy)
        self.shake_reject_duration.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.shake_reject_duration.setDecimals(1)
        self.shake_reject_duration.setMaximum(20.000000000000000)

        self.horizontalLayout_59.addWidget(self.shake_reject_duration)


        self.verticalLayout_18.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_53 = QLabel(self.page_recirculating)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(260, 0))

        self.horizontalLayout_60.addWidget(self.label_53)

        self.shake_part_entered_timeout = QDoubleSpinBox(self.page_recirculating)
        self.shake_part_entered_timeout.setObjectName(u"shake_part_entered_timeout")
        sizePolicy.setHeightForWidth(self.shake_part_entered_timeout.sizePolicy().hasHeightForWidth())
        self.shake_part_entered_timeout.setSizePolicy(sizePolicy)
        self.shake_part_entered_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.shake_part_entered_timeout.setDecimals(1)
        self.shake_part_entered_timeout.setMaximum(20.000000000000000)

        self.horizontalLayout_60.addWidget(self.shake_part_entered_timeout)


        self.verticalLayout_18.addLayout(self.horizontalLayout_60)


        self.horizontalLayout_55.addLayout(self.verticalLayout_18)

        self.layout_right = QVBoxLayout()
        self.layout_right.setSpacing(20)
        self.layout_right.setObjectName(u"layout_right")
        self.layout_right.setContentsMargins(20, -1, -1, -1)
        self.group_dial = QGroupBox(self.page_recirculating)
        self.group_dial.setObjectName(u"group_dial")
        self.group_dial.setMinimumSize(QSize(0, 0))
        self.verticalLayout_19 = QVBoxLayout(self.group_dial)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_54 = QLabel(self.group_dial)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_61.addWidget(self.label_54)

        self.dial_lift_retries = QDoubleSpinBox(self.group_dial)
        self.dial_lift_retries.setObjectName(u"dial_lift_retries")
        sizePolicy.setHeightForWidth(self.dial_lift_retries.sizePolicy().hasHeightForWidth())
        self.dial_lift_retries.setSizePolicy(sizePolicy)
        self.dial_lift_retries.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dial_lift_retries.setDecimals(1)
        self.dial_lift_retries.setMaximum(1000.000000000000000)

        self.horizontalLayout_61.addWidget(self.dial_lift_retries)


        self.verticalLayout_19.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_55 = QLabel(self.group_dial)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_62.addWidget(self.label_55)

        self.recover_reverse_time = QDoubleSpinBox(self.group_dial)
        self.recover_reverse_time.setObjectName(u"recover_reverse_time")
        sizePolicy.setHeightForWidth(self.recover_reverse_time.sizePolicy().hasHeightForWidth())
        self.recover_reverse_time.setSizePolicy(sizePolicy)
        self.recover_reverse_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.recover_reverse_time.setDecimals(1)
        self.recover_reverse_time.setMaximum(1000.000000000000000)

        self.horizontalLayout_62.addWidget(self.recover_reverse_time)


        self.verticalLayout_19.addLayout(self.horizontalLayout_62)


        self.layout_right.addWidget(self.group_dial)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_56 = QLabel(self.page_recirculating)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_63.addWidget(self.label_56)

        self.motors_return_speed_drop_limit = QDoubleSpinBox(self.page_recirculating)
        self.motors_return_speed_drop_limit.setObjectName(u"motors_return_speed_drop_limit")
        sizePolicy.setHeightForWidth(self.motors_return_speed_drop_limit.sizePolicy().hasHeightForWidth())
        self.motors_return_speed_drop_limit.setSizePolicy(sizePolicy)
        self.motors_return_speed_drop_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.motors_return_speed_drop_limit.setDecimals(1)
        self.motors_return_speed_drop_limit.setMaximum(1000.000000000000000)

        self.horizontalLayout_63.addWidget(self.motors_return_speed_drop_limit)


        self.verticalLayout_20.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_57 = QLabel(self.page_recirculating)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_64.addWidget(self.label_57)

        self.motors_return_speed_limit = QDoubleSpinBox(self.page_recirculating)
        self.motors_return_speed_limit.setObjectName(u"motors_return_speed_limit")
        sizePolicy.setHeightForWidth(self.motors_return_speed_limit.sizePolicy().hasHeightForWidth())
        self.motors_return_speed_limit.setSizePolicy(sizePolicy)
        self.motors_return_speed_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.motors_return_speed_limit.setDecimals(1)
        self.motors_return_speed_limit.setMaximum(1000.000000000000000)

        self.horizontalLayout_64.addWidget(self.motors_return_speed_limit)


        self.verticalLayout_20.addLayout(self.horizontalLayout_64)


        self.layout_right.addLayout(self.verticalLayout_20)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_right.addItem(self.verticalSpacer_3)


        self.horizontalLayout_55.addLayout(self.layout_right)

        self.stack_other.addWidget(self.page_recirculating)
        self.page_reciprocating = QWidget()
        self.page_reciprocating.setObjectName(u"page_reciprocating")
        self.verticalLayout_5 = QVBoxLayout(self.page_reciprocating)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(150, -1, 150, -1)
        self.label_58 = QLabel(self.page_reciprocating)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_65.addWidget(self.label_58)

        self.hopper_off_delay = QDoubleSpinBox(self.page_reciprocating)
        self.hopper_off_delay.setObjectName(u"hopper_off_delay")
        sizePolicy.setHeightForWidth(self.hopper_off_delay.sizePolicy().hasHeightForWidth())
        self.hopper_off_delay.setSizePolicy(sizePolicy)
        self.hopper_off_delay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.hopper_off_delay.setDecimals(1)
        self.hopper_off_delay.setMaximum(20.000000000000000)

        self.horizontalLayout_65.addWidget(self.hopper_off_delay)


        self.verticalLayout_5.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(150, -1, 150, -1)
        self.label_59 = QLabel(self.page_reciprocating)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_66.addWidget(self.label_59)

        self.part_reject_timeout = QDoubleSpinBox(self.page_reciprocating)
        self.part_reject_timeout.setObjectName(u"part_reject_timeout")
        sizePolicy.setHeightForWidth(self.part_reject_timeout.sizePolicy().hasHeightForWidth())
        self.part_reject_timeout.setSizePolicy(sizePolicy)
        self.part_reject_timeout.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.part_reject_timeout.setDecimals(1)
        self.part_reject_timeout.setMaximum(20.000000000000000)

        self.horizontalLayout_66.addWidget(self.part_reject_timeout)


        self.verticalLayout_5.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(150, -1, 150, -1)
        self.label_50 = QLabel(self.page_reciprocating)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_57.addWidget(self.label_50)

        self.reverse_time = QDoubleSpinBox(self.page_reciprocating)
        self.reverse_time.setObjectName(u"reverse_time")
        sizePolicy.setHeightForWidth(self.reverse_time.sizePolicy().hasHeightForWidth())
        self.reverse_time.setSizePolicy(sizePolicy)
        self.reverse_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.reverse_time.setDecimals(1)
        self.reverse_time.setMaximum(2.000000000000000)
        self.reverse_time.setSingleStep(0.100000000000000)

        self.horizontalLayout_57.addWidget(self.reverse_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_57)

        self.stack_other.addWidget(self.page_reciprocating)

        self.verticalLayout_17.addWidget(self.stack_other)


        self.verticalLayout_22.addWidget(self.group_other)


        self.horizontalLayout.addWidget(self.groupBox_4)

        self.frame = QFrame(FlexFeederDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img = QLabel(self.frame)
        self.img.setObjectName(u"img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy1)
        self.img.setMinimumSize(QSize(250, 134))
        self.img.setMaximumSize(QSize(250, 134))
        self.img.setPixmap(QPixmap(u":/img/img/components/upper_housing.png"))

        self.verticalLayout.addWidget(self.img)

        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        self.name.setFont(font1)
        self.name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name)

        self.groupBox_13 = QGroupBox(self.frame)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy2)
        self.groupBox_13.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.group_buttons = QWidget(self.groupBox_13)
        self.group_buttons.setObjectName(u"group_buttons")
        self.group_buttons.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.group_buttons)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_start_feed = QToolButton(self.group_buttons)
        self.btn_start_feed.setObjectName(u"btn_start_feed")
        self.btn_start_feed.setMinimumSize(QSize(180, 45))
        self.btn_start_feed.setMaximumSize(QSize(180, 16777215))

        self.verticalLayout_4.addWidget(self.btn_start_feed)

        self.btn_re_acquire = QToolButton(self.group_buttons)
        self.btn_re_acquire.setObjectName(u"btn_re_acquire")
        self.btn_re_acquire.setMinimumSize(QSize(180, 45))

        self.verticalLayout_4.addWidget(self.btn_re_acquire)

        self.btn_backlight = QToolButton(self.group_buttons)
        self.btn_backlight.setObjectName(u"btn_backlight")
        self.btn_backlight.setMinimumSize(QSize(180, 45))
        self.btn_backlight.setMaximumSize(QSize(180, 16777215))
        self.btn_backlight.setFont(font)
        self.btn_backlight.setStyleSheet(u"padding-left: 10px;")
        icon = QIcon()
        icon.addFile(u":/img/img/green-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backlight.setIcon(icon)
        self.btn_backlight.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.btn_backlight)

        self.btn_dial_lift = QToolButton(self.group_buttons)
        self.btn_dial_lift.setObjectName(u"btn_dial_lift")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_dial_lift.sizePolicy().hasHeightForWidth())
        self.btn_dial_lift.setSizePolicy(sizePolicy3)
        self.btn_dial_lift.setMinimumSize(QSize(180, 45))
        self.btn_dial_lift.setMaximumSize(QSize(180, 45))

        self.verticalLayout_4.addWidget(self.btn_dial_lift)


        self.verticalLayout_3.addWidget(self.group_buttons)

        self.group_conveyor = QGroupBox(self.groupBox_13)
        self.group_conveyor.setObjectName(u"group_conveyor")
        self.verticalLayout_2 = QVBoxLayout(self.group_conveyor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.group_conveyor)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.btn_main_backward = QToolButton(self.widget_3)
        self.btn_main_backward.setObjectName(u"btn_main_backward")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_main_backward.sizePolicy().hasHeightForWidth())
        self.btn_main_backward.setSizePolicy(sizePolicy5)
        self.btn_main_backward.setMinimumSize(QSize(45, 45))

        self.horizontalLayout_6.addWidget(self.btn_main_backward)

        self.btn_main_forward = QToolButton(self.widget_3)
        self.btn_main_forward.setObjectName(u"btn_main_forward")
        sizePolicy5.setHeightForWidth(self.btn_main_forward.sizePolicy().hasHeightForWidth())
        self.btn_main_forward.setSizePolicy(sizePolicy5)
        self.btn_main_forward.setMinimumSize(QSize(45, 45))

        self.horizontalLayout_6.addWidget(self.btn_main_forward)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.group_conveyor)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(53)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.btn_feeder_forward = QToolButton(self.widget_2)
        self.btn_feeder_forward.setObjectName(u"btn_feeder_forward")
        sizePolicy5.setHeightForWidth(self.btn_feeder_forward.sizePolicy().hasHeightForWidth())
        self.btn_feeder_forward.setSizePolicy(sizePolicy5)
        self.btn_feeder_forward.setMinimumSize(QSize(45, 45))

        self.horizontalLayout_5.addWidget(self.btn_feeder_forward)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.group_return = QWidget(self.group_conveyor)
        self.group_return.setObjectName(u"group_return")
        self.horizontalLayout_4 = QHBoxLayout(self.group_return)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.group_return)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.btn_return_backward = QToolButton(self.group_return)
        self.btn_return_backward.setObjectName(u"btn_return_backward")
        sizePolicy5.setHeightForWidth(self.btn_return_backward.sizePolicy().hasHeightForWidth())
        self.btn_return_backward.setSizePolicy(sizePolicy5)
        self.btn_return_backward.setMinimumSize(QSize(45, 45))

        self.horizontalLayout_4.addWidget(self.btn_return_backward)

        self.btn_return_forward = QToolButton(self.group_return)
        self.btn_return_forward.setObjectName(u"btn_return_forward")
        sizePolicy5.setHeightForWidth(self.btn_return_forward.sizePolicy().hasHeightForWidth())
        self.btn_return_forward.setSizePolicy(sizePolicy5)
        self.btn_return_forward.setMinimumSize(QSize(45, 45))

        self.horizontalLayout_4.addWidget(self.btn_return_forward)


        self.verticalLayout_2.addWidget(self.group_return)

        self.btn_conveyor_lift = QToolButton(self.group_conveyor)
        self.btn_conveyor_lift.setObjectName(u"btn_conveyor_lift")
        sizePolicy3.setHeightForWidth(self.btn_conveyor_lift.sizePolicy().hasHeightForWidth())
        self.btn_conveyor_lift.setSizePolicy(sizePolicy3)
        self.btn_conveyor_lift.setMinimumSize(QSize(0, 45))

        self.verticalLayout_2.addWidget(self.btn_conveyor_lift)


        self.verticalLayout_3.addWidget(self.group_conveyor)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.lb_robot_paused_parked = QLabel(self.groupBox_13)
        self.lb_robot_paused_parked.setObjectName(u"lb_robot_paused_parked")
        sizePolicy4.setHeightForWidth(self.lb_robot_paused_parked.sizePolicy().hasHeightForWidth())
        self.lb_robot_paused_parked.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.lb_robot_paused_parked)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_paused = QLabel(self.groupBox_13)
        self.lb_paused.setObjectName(u"lb_paused")

        self.horizontalLayout_3.addWidget(self.lb_paused)

        self.btn_pause_resume = QToolButton(self.groupBox_13)
        self.btn_pause_resume.setObjectName(u"btn_pause_resume")
        sizePolicy1.setHeightForWidth(self.btn_pause_resume.sizePolicy().hasHeightForWidth())
        self.btn_pause_resume.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.btn_pause_resume)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_13)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lb_state = QLabel(self.groupBox_13)
        self.lb_state.setObjectName(u"lb_state")
        sizePolicy2.setHeightForWidth(self.lb_state.sizePolicy().hasHeightForWidth())
        self.lb_state.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.lb_state.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lb_state)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.lb_error = QLabel(self.groupBox_13)
        self.lb_error.setObjectName(u"lb_error")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.lb_error.setFont(font3)
        self.lb_error.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.lb_error.setAlignment(Qt.AlignCenter)
        self.lb_error.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_error)

        self.btn_clear_error = QToolButton(self.groupBox_13)
        self.btn_clear_error.setObjectName(u"btn_clear_error")
        sizePolicy3.setHeightForWidth(self.btn_clear_error.sizePolicy().hasHeightForWidth())
        self.btn_clear_error.setSizePolicy(sizePolicy3)
        self.btn_clear_error.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.btn_clear_error)


        self.verticalLayout.addWidget(self.groupBox_13)

        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(FlexFeederDialog)

        self.stack_other.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(FlexFeederDialog)
    # setupUi

    def retranslateUi(self, FlexFeederDialog):
        FlexFeederDialog.setWindowTitle(QCoreApplication.translate("FlexFeederDialog", u"FlexFeeder", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Settings", None))
        self.type.setText(QCoreApplication.translate("FlexFeederDialog", u"Type:Reciprocating", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Timeout(sec)", None))
        self.label_26.setText(QCoreApplication.translate("FlexFeederDialog", u"Pre-Check:", None))
#if QT_CONFIG(tooltip)
        self.pre_check_timeout.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How long the flex feeder will search for parts before activating the hopper conveyor", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("FlexFeederDialog", u"Feeding:", None))
#if QT_CONFIG(tooltip)
        self.feeding_timeout.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"After the hopper conveyor is active, how long the flex feeder will search for parts", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("FlexFeederDialog", u"Feeder Idle:", None))
#if QT_CONFIG(tooltip)
        self.feeder_idle_timeout.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How long the flex feeder will search for parts before activating the hopper conveyor", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("FlexFeederDialog", u"Part Presence:", None))
#if QT_CONFIG(tooltip)
        self.part_presence_timeout.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How long to scan for part at the end of the main conveyor after a part has been detected at the entrance of the main conveyor", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_8.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Motor", None))
        self.label_35.setText(QCoreApplication.translate("FlexFeederDialog", u"Main Motor Speed:", None))
#if QT_CONFIG(tooltip)
        self.motors_main_speed_limit.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Main conveyor speed", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText(QCoreApplication.translate("FlexFeederDialog", u"Hopper Motor Speed:", None))
#if QT_CONFIG(tooltip)
        self.motors_feeder_speed_limit.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Hopper conveyor speed", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("FlexFeederDialog", u"Main Motor Speed Drop Limit:", None))
#if QT_CONFIG(tooltip)
        self.motors_main_speed_drop_limit.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How much of a speed drop in a percentage of \u2018Main Motor Speed Limit\u2019 before motor is stalled", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText(QCoreApplication.translate("FlexFeederDialog", u"Hopper Motor Speed Drop Limit:", None))
#if QT_CONFIG(tooltip)
        self.motors_feeder_speed_drop_limit.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How much of a speed drop in a percentage of \u2018Hopper Motor Speed Limit\u2019 before motor is stalled", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_9.setTitle(QCoreApplication.translate("FlexFeederDialog", u"IR Settings", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Hopper Empty", None))
        self.label_40.setText(QCoreApplication.translate("FlexFeederDialog", u"Frequency(Hz):", None))
        self.ir_hopper_empty_frequency.setItemText(0, QCoreApplication.translate("FlexFeederDialog", u"35714", None))
        self.ir_hopper_empty_frequency.setItemText(1, QCoreApplication.translate("FlexFeederDialog", u"38462", None))
        self.ir_hopper_empty_frequency.setItemText(2, QCoreApplication.translate("FlexFeederDialog", u"41667", None))
        self.ir_hopper_empty_frequency.setItemText(3, QCoreApplication.translate("FlexFeederDialog", u"45455", None))
        self.ir_hopper_empty_frequency.setItemText(4, QCoreApplication.translate("FlexFeederDialog", u"50000", None))
        self.ir_hopper_empty_frequency.setItemText(5, QCoreApplication.translate("FlexFeederDialog", u"62500", None))

#if QT_CONFIG(tooltip)
        self.ir_hopper_empty_frequency.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Sensitivity of part sensor.  38000 Hz default, increase value to increase sensitivity", None))
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("FlexFeederDialog", u"Interval(ms):", None))
#if QT_CONFIG(tooltip)
        self.ir_hopper_empty_interval.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Used in conjunction with \u2018count\u2019.  Amount of time between sensor scans", None))
#endif // QT_CONFIG(tooltip)
        self.label_42.setText(QCoreApplication.translate("FlexFeederDialog", u"Count:", None))
#if QT_CONFIG(tooltip)
        self.ir_hopper_empty_count.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Number of positive detection's of sensor before a part is considered to be present at the sensor", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_11.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Conveyor Entrance", None))
        self.label_43.setText(QCoreApplication.translate("FlexFeederDialog", u"Frequency(Hz):", None))
        self.ir_conveyor_entrance_frequency.setItemText(0, QCoreApplication.translate("FlexFeederDialog", u"35714", None))
        self.ir_conveyor_entrance_frequency.setItemText(1, QCoreApplication.translate("FlexFeederDialog", u"38462", None))
        self.ir_conveyor_entrance_frequency.setItemText(2, QCoreApplication.translate("FlexFeederDialog", u"41667", None))
        self.ir_conveyor_entrance_frequency.setItemText(3, QCoreApplication.translate("FlexFeederDialog", u"45455", None))
        self.ir_conveyor_entrance_frequency.setItemText(4, QCoreApplication.translate("FlexFeederDialog", u"50000", None))
        self.ir_conveyor_entrance_frequency.setItemText(5, QCoreApplication.translate("FlexFeederDialog", u"62500", None))

#if QT_CONFIG(tooltip)
        self.ir_conveyor_entrance_frequency.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Sensitivity of part sensor.  38000 Hz default, increase value to increase sensitivity", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText(QCoreApplication.translate("FlexFeederDialog", u"Interval(ms):", None))
#if QT_CONFIG(tooltip)
        self.ir_conveyor_entrance_interval.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Used in conjunction with \u2018count\u2019.  Amount of time between sensor scans", None))
#endif // QT_CONFIG(tooltip)
        self.label_45.setText(QCoreApplication.translate("FlexFeederDialog", u"Count:", None))
#if QT_CONFIG(tooltip)
        self.ir_conveyor_entrance_count.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Number of positive detection's of sensor before a part is considered to be present at the sensor", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_12.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Part Presence", None))
        self.label_46.setText(QCoreApplication.translate("FlexFeederDialog", u"Frequency(Hz):", None))
        self.ir_part_presence_frequency.setItemText(0, QCoreApplication.translate("FlexFeederDialog", u"35714", None))
        self.ir_part_presence_frequency.setItemText(1, QCoreApplication.translate("FlexFeederDialog", u"38462", None))
        self.ir_part_presence_frequency.setItemText(2, QCoreApplication.translate("FlexFeederDialog", u"41667", None))
        self.ir_part_presence_frequency.setItemText(3, QCoreApplication.translate("FlexFeederDialog", u"45455", None))
        self.ir_part_presence_frequency.setItemText(4, QCoreApplication.translate("FlexFeederDialog", u"50000", None))
        self.ir_part_presence_frequency.setItemText(5, QCoreApplication.translate("FlexFeederDialog", u"62500", None))

#if QT_CONFIG(tooltip)
        self.ir_part_presence_frequency.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Sensitivity of part sensor.  38000 Hz default, increase value to increase sensitivity", None))
#endif // QT_CONFIG(tooltip)
        self.label_47.setText(QCoreApplication.translate("FlexFeederDialog", u"Interval(ms):", None))
#if QT_CONFIG(tooltip)
        self.ir_part_presence_interval.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Used in conjunction with \u2018count\u2019.  Amount of time between sensor scans", None))
#endif // QT_CONFIG(tooltip)
        self.label_48.setText(QCoreApplication.translate("FlexFeederDialog", u"Count:", None))
#if QT_CONFIG(tooltip)
        self.ir_part_presence_count.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Number of positive detection's of sensor before a part is considered to be present at the sensor", None))
#endif // QT_CONFIG(tooltip)
        self.group_other.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Other Settings", None))
        self.label_49.setText(QCoreApplication.translate("FlexFeederDialog", u"Shake Reject Counter:", None))
#if QT_CONFIG(tooltip)
        self.shake_reject_counter.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Number of vision part rejections in a row within \u2018shake reject timeout\u2019 value before shake motion is initiated", None))
#endif // QT_CONFIG(tooltip)
        self.label_51.setText(QCoreApplication.translate("FlexFeederDialog", u"Shake Reject Timeout(sec):", None))
#if QT_CONFIG(tooltip)
        self.shake_reject_timeout.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Used in conjunction with \u2018Shake Reject Counter\u2019", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("FlexFeederDialog", u"Shake Reject Duration(Sec)", None))
#if QT_CONFIG(tooltip)
        self.shake_reject_duration.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Amount of time to shake conveyors", None))
#endif // QT_CONFIG(tooltip)
        self.label_53.setText(QCoreApplication.translate("FlexFeederDialog", u"Shake Part Entered Timeout(Sec):", None))
#if QT_CONFIG(tooltip)
        self.shake_part_entered_timeout.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How much time to allow before shaking after a part has been detected at the main conveyor entrance", None))
#endif // QT_CONFIG(tooltip)
        self.group_dial.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Dial Settings", None))
        self.label_54.setText(QCoreApplication.translate("FlexFeederDialog", u"Dial Lift Retries:", None))
        self.label_55.setText(QCoreApplication.translate("FlexFeederDialog", u"Recover Reverse Time:", None))
        self.label_56.setText(QCoreApplication.translate("FlexFeederDialog", u"Return Motor Speed Drop Limit:", None))
#if QT_CONFIG(tooltip)
        self.motors_return_speed_drop_limit.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How much of a speed drop in a percentage of \u2018Return Motor Speed Limit\u2019 before motor is stalled", None))
#endif // QT_CONFIG(tooltip)
        self.label_57.setText(QCoreApplication.translate("FlexFeederDialog", u"Return Motor Speed Limit:", None))
#if QT_CONFIG(tooltip)
        self.motors_return_speed_limit.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"Return conveyor speed", None))
#endif // QT_CONFIG(tooltip)
        self.label_58.setText(QCoreApplication.translate("FlexFeederDialog", u"Hopper Off Delay(Sec):", None))
#if QT_CONFIG(tooltip)
        self.hopper_off_delay.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How long after detecting a part at the main conveyor entrance before deactivating the hopper conveyor", None))
#endif // QT_CONFIG(tooltip)
        self.label_59.setText(QCoreApplication.translate("FlexFeederDialog", u"Reject Timeout(Sec):", None))
#if QT_CONFIG(tooltip)
        self.part_reject_timeout.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How much time the flex feeder should run reject cycle before feeding another part", None))
#endif // QT_CONFIG(tooltip)
        self.label_50.setText(QCoreApplication.translate("FlexFeederDialog", u"Reverse Time:", None))
#if QT_CONFIG(tooltip)
        self.reverse_time.setToolTip(QCoreApplication.translate("FlexFeederDialog", u"How long to run main conveyor in reverse after part found at front of feeder", None))
#endif // QT_CONFIG(tooltip)
        self.img.setText("")
        self.name.setText(QCoreApplication.translate("FlexFeederDialog", u"Name", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Control", None))
        self.btn_start_feed.setText(QCoreApplication.translate("FlexFeederDialog", u"Start Feeding", None))
        self.btn_re_acquire.setText(QCoreApplication.translate("FlexFeederDialog", u"Re-Acquire", None))
        self.btn_backlight.setText(QCoreApplication.translate("FlexFeederDialog", u" Turn Backlight OFF", None))
        self.btn_dial_lift.setText(QCoreApplication.translate("FlexFeederDialog", u"Dial Lift UP", None))
        self.group_conveyor.setTitle(QCoreApplication.translate("FlexFeederDialog", u"Conveyor", None))
        self.label_6.setText(QCoreApplication.translate("FlexFeederDialog", u"Main:", None))
        self.btn_main_backward.setText(QCoreApplication.translate("FlexFeederDialog", u"<<", None))
        self.btn_main_forward.setText(QCoreApplication.translate("FlexFeederDialog", u">>", None))
        self.label_5.setText(QCoreApplication.translate("FlexFeederDialog", u"Feeder:", None))
        self.btn_feeder_forward.setText(QCoreApplication.translate("FlexFeederDialog", u">>", None))
        self.label_4.setText(QCoreApplication.translate("FlexFeederDialog", u"Return:", None))
        self.btn_return_backward.setText(QCoreApplication.translate("FlexFeederDialog", u"<<", None))
        self.btn_return_forward.setText(QCoreApplication.translate("FlexFeederDialog", u">>", None))
        self.btn_conveyor_lift.setText(QCoreApplication.translate("FlexFeederDialog", u"Conveyor Lift UP", None))
        self.lb_robot_paused_parked.setText(QCoreApplication.translate("FlexFeederDialog", u"<html><head/><body><p>Robot Paused &amp; Parked: <span style=\" font-weight:600;\">NO</span></p></body></html>", None))
        self.lb_paused.setText(QCoreApplication.translate("FlexFeederDialog", u"Paused:", None))
        self.btn_pause_resume.setText(QCoreApplication.translate("FlexFeederDialog", u"Pause", None))
        self.label.setText(QCoreApplication.translate("FlexFeederDialog", u"State:", None))
        self.lb_state.setText(QCoreApplication.translate("FlexFeederDialog", u"IDLE", None))
        self.lb_error.setText("")
        self.btn_clear_error.setText(QCoreApplication.translate("FlexFeederDialog", u"Clear Error", None))
        self.btn_close.setText(QCoreApplication.translate("FlexFeederDialog", u"Close", None))
    # retranslateUi

