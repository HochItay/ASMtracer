# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'traceWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import UI.resources_rc

class Ui_TraceWindow(object):
    def setupUi(self, TraceWindow):
        if not TraceWindow.objectName():
            TraceWindow.setObjectName(u"TraceWindow")
        TraceWindow.setWindowModality(Qt.NonModal)
        TraceWindow.resize(1850, 1000)
        TraceWindow.setMaximumSize(QSize(2000, 1200))
        TraceWindow.setBaseSize(QSize(1700, 900))
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        TraceWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_white_bg.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        TraceWindow.setWindowIcon(icon)
        TraceWindow.setStyleSheet(u"QToolTip { color: #000000; background-color: #ffffff; border: 1px; }")
        self.action16_bit = QAction(TraceWindow)
        self.action16_bit.setObjectName(u"action16_bit")
        self.action32_bit = QAction(TraceWindow)
        self.action32_bit.setObjectName(u"action32_bit")
        self.action64_bit = QAction(TraceWindow)
        self.action64_bit.setObjectName(u"action64_bit")
        self.actionfull_address = QAction(TraceWindow)
        self.actionfull_address.setObjectName(u"actionfull_address")
        self.action_3 = QAction(TraceWindow)
        self.action_3.setObjectName(u"action_3")
        self.action16_bit_2 = QAction(TraceWindow)
        self.action16_bit_2.setObjectName(u"action16_bit_2")
        self.actionabsolute = QAction(TraceWindow)
        self.actionabsolute.setObjectName(u"actionabsolute")
        self.actionrelative_address = QAction(TraceWindow)
        self.actionrelative_address.setObjectName(u"actionrelative_address")
        self.action16_bit_3 = QAction(TraceWindow)
        self.action16_bit_3.setObjectName(u"action16_bit_3")
        self.action32_bit_2 = QAction(TraceWindow)
        self.action32_bit_2.setObjectName(u"action32_bit_2")
        self.action64_bit_2 = QAction(TraceWindow)
        self.action64_bit_2.setObjectName(u"action64_bit_2")
        self.centralwidget = QWidget(TraceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"border-image: url(:/mainWindow/background3.png) 0 0 0 0 stretch stretch;\n"
"\n"
"background-color: rgb(220, 240, 189);\n"
"font:  \"Ubuntu Mono\";\n"
"\n"
"}\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(0, 80))
        self.menu.setMaximumSize(QSize(16777215, 80))
        self.menu.setStyleSheet(u"QFrame#menu{background-color: #34A0A4;}")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.open_file_btn = QPushButton(self.menu)
        self.open_file_btn.setObjectName(u"open_file_btn")
        self.open_file_btn.setGeometry(QRect(1560, 15, 60, 50))
        self.open_file_btn.setStyleSheet(u"QPushButton {\n"
"image: url(:/traceWindow/open_file.png) 0 0 0 0 stretch stretch;\n"
"background-color:rgb(225, 245, 195);\n"
"\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")
        self.restart_btn = QPushButton(self.menu)
        self.restart_btn.setObjectName(u"restart_btn")
        self.restart_btn.setGeometry(QRect(1640, 15, 60, 50))
        self.restart_btn.setStyleSheet(u"QPushButton {\n"
"image: url(:/traceWindow/restart.png) 0 0 0 0 stretch stretch;\n"
"background-color:rgb(225, 245, 195);\n"
"\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")
        self.exit_btn = QPushButton(self.menu)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(1750, 15, 60, 50))
        self.exit_btn.setStyleSheet(u"QPushButton {\n"
"image: url(:/traceWindow/exit.png) 0 0 0 0 stretch stretch;\n"
"background-color:rgb(225, 245, 195);\n"
"\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")
        self.line_2 = QFrame(self.menu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1720, 1, 20, 78))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.VLine)
        self.logo_lbl = QLabel(self.menu)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(0, 0, 201, 81))
        self.logo_lbl.setStyleSheet(u"background-color: none;")
        self.logo_lbl.setPixmap(QPixmap(u":/mainWindow/logo_no_bg.png"))
        self.logo_lbl.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.menu)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(0, 50))
        self.label_11.setMaximumSize(QSize(700, 200))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color:#34A0A4;")

        self.verticalLayout_2.addWidget(self.label_11)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMaximumSize(QSize(820, 16777215))
        self.frame_7.setStyleSheet(u"QFrame#frame_7{\n"
"background-color:rgb(225, 245, 195);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Panel)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(1)
        self.frame_7.setMidLineWidth(2)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, -1, 6, -1)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 70))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color: #34A0A4;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.Panel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setLineWidth(2)
        self.frame_10.setMidLineWidth(4)
        self.gridLayout_2 = QGridLayout(self.frame_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.step_btn = QPushButton(self.frame_10)
        self.step_btn.setObjectName(u"step_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.step_btn.sizePolicy().hasHeightForWidth())
        self.step_btn.setSizePolicy(sizePolicy2)
        self.step_btn.setMinimumSize(QSize(60, 50))
        self.step_btn.setMaximumSize(QSize(70, 16777215))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.step_btn.setFont(font2)
        self.step_btn.setFocusPolicy(Qt.NoFocus)
        self.step_btn.setToolTipDuration(1)
        self.step_btn.setStyleSheet(u"QPushButton {\n"
"image: url(:/traceWindow/step_in.png) 0 0 0 0 stretch stretch;\n"
"background-color:rgb(245, 255, 225);\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")

        self.horizontalLayout.addWidget(self.step_btn)

        self.step_over_btn = QPushButton(self.frame_10)
        self.step_over_btn.setObjectName(u"step_over_btn")
        self.step_over_btn.setMinimumSize(QSize(60, 50))
        self.step_over_btn.setMaximumSize(QSize(60, 16777215))
        self.step_over_btn.setFont(font2)
        self.step_over_btn.setFocusPolicy(Qt.NoFocus)
        self.step_over_btn.setStyleSheet(u"QPushButton {\n"
"image: url(:/traceWindow/step_over.png) 0 0 0 0 stretch stretch;\n"
"background-color:rgb(245, 255, 225);\n"
"\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")

        self.horizontalLayout.addWidget(self.step_over_btn)

        self.step_out_btn = QPushButton(self.frame_10)
        self.step_out_btn.setObjectName(u"step_out_btn")
        sizePolicy2.setHeightForWidth(self.step_out_btn.sizePolicy().hasHeightForWidth())
        self.step_out_btn.setSizePolicy(sizePolicy2)
        self.step_out_btn.setMinimumSize(QSize(60, 50))
        self.step_out_btn.setMaximumSize(QSize(60, 16777215))
        self.step_out_btn.setFont(font2)
        self.step_out_btn.setFocusPolicy(Qt.NoFocus)
        self.step_out_btn.setStyleSheet(u"QPushButton {\n"
"image: url(:/traceWindow/step_out.png) 0 0 0 0 stretch stretch;\n"
"background-color:rgb(245, 255, 225);\n"
"\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")

        self.horizontalLayout.addWidget(self.step_out_btn)

        self.cont_btn = QPushButton(self.frame_10)
        self.cont_btn.setObjectName(u"cont_btn")
        sizePolicy2.setHeightForWidth(self.cont_btn.sizePolicy().hasHeightForWidth())
        self.cont_btn.setSizePolicy(sizePolicy2)
        self.cont_btn.setMinimumSize(QSize(60, 50))
        self.cont_btn.setMaximumSize(QSize(60, 16777215))
        self.cont_btn.setFont(font2)
        self.cont_btn.setFocusPolicy(Qt.NoFocus)
        self.cont_btn.setStyleSheet(u"QPushButton {\n"
"image: url(:/traceWindow/continue.png) 0 0 0 0 stretch stretch;\n"
"background-color:rgb(245, 255, 225);\n"
"\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")
        self.cont_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.cont_btn)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 3)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_10, 4, 0, 1, 1)

        self.func_stack = QStackedWidget(self.frame_7)
        self.func_stack.setObjectName(u"func_stack")
        font3 = QFont()
        font3.setFamily(u"Ubuntu Mono")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.func_stack.setFont(font3)
        self.func_stack.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.func_stack, 7, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.relative_address_btn = QCheckBox(self.frame_7)
        self.relative_address_btn.setObjectName(u"relative_address_btn")
        self.relative_address_btn.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setPointSize(18)
        self.relative_address_btn.setFont(font4)
        self.relative_address_btn.setAutoFillBackground(False)
        self.relative_address_btn.setStyleSheet(u"\n"
"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.relative_address_btn.setChecked(False)
        self.relative_address_btn.setAutoRepeat(False)

        self.horizontalLayout_3.addWidget(self.relative_address_btn)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(220, 0))
        self.frame_3.setStyleSheet(u"background-color:rgb(225, 245, 195);")
        self.frame_3.setFrameShape(QFrame.Panel)
        self.font_size_spin = QSpinBox(self.frame_3)
        self.font_size_spin.setObjectName(u"font_size_spin")
        self.font_size_spin.setGeometry(QRect(130, 10, 81, 41))
        font5 = QFont()
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.font_size_spin.setFont(font5)
        self.font_size_spin.setStyleSheet(u"background-color:rgb(225, 245, 195);")
        self.font_size_spin.setMinimum(8)
        self.font_size_spin.setMaximum(16)
        self.font_size_spin.setValue(11)
        self.font_size_spin.setDisplayIntegerBase(10)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 31))
        self.label.setFont(font5)

        self.horizontalLayout_3.addWidget(self.frame_3)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(150, 16777215))
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.func_combo = QComboBox(self.frame_7)
        self.func_combo.setObjectName(u"func_combo")
        self.func_combo.setMinimumSize(QSize(200, 0))
        self.func_combo.setFocusPolicy(Qt.NoFocus)
        self.func_combo.setStyleSheet(u"\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QComboBox::item { \n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"\n"
"QComboBox::item:selected { \n"
"    color: white;\n"
"    background-color: blue;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.func_combo)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        font6 = QFont()
        font6.setFamily(u"Ubuntu Mono")
        font6.setPointSize(19)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(980, 0))
        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 630, 621, 231))
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"background-color:rgb(225, 245, 195);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(2)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 51, 41))
        font7 = QFont()
        font7.setFamily(u"Ubuntu Mono")
        font7.setPointSize(18)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.label_4.setFont(font7)
        self.num_bytes_line_edit = QLineEdit(self.frame_2)
        self.num_bytes_line_edit.setObjectName(u"num_bytes_line_edit")
        self.num_bytes_line_edit.setGeometry(QRect(70, 15, 100, 31))
        self.num_bytes_line_edit.setFont(font7)
        self.num_bytes_line_edit.setFocusPolicy(Qt.StrongFocus)
        self.num_bytes_line_edit.setStyleSheet(u"background-color: #ffffff")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 10, 221, 41))
        self.label_5.setFont(font7)
        self.address_line_edit = QLineEdit(self.frame_2)
        self.address_line_edit.setObjectName(u"address_line_edit")
        self.address_line_edit.setGeometry(QRect(410, 15, 191, 31))
        self.address_line_edit.setFont(font7)
        self.address_line_edit.setFocusPolicy(Qt.StrongFocus)
        self.address_line_edit.setStyleSheet(u"background-color: #ffffff")
        self.address_line_edit.setFrame(True)
        self.data_area = QTextEdit(self.frame_2)
        self.data_area.setObjectName(u"data_area")
        self.data_area.setGeometry(QRect(170, 70, 431, 151))
        font8 = QFont()
        font8.setFamily(u"Ubuntu Mono")
        font8.setPointSize(16)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.data_area.setFont(font8)
        self.data_area.setFocusPolicy(Qt.NoFocus)
        self.data_area.setStyleSheet(u"background-color: #ffffff")
        self.data_area.setReadOnly(True)
        self.get_data_btn = QPushButton(self.frame_2)
        self.get_data_btn.setObjectName(u"get_data_btn")
        self.get_data_btn.setGeometry(QRect(10, 110, 141, 61))
        self.get_data_btn.setFont(font4)
        self.get_data_btn.setFocusPolicy(Qt.NoFocus)
        self.get_data_btn.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(245, 255, 225);\n"
"\n"
"border-radius:3px;\n"
"border: 1px solid black;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(180, 215, 225);\n"
"    }\n"
"")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 20, 141, 31))
        font9 = QFont()
        font9.setFamily(u"Ubuntu Mono")
        font9.setPointSize(22)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.label_6.setFont(font9)
        self.label_6.setStyleSheet(u"color:#34A0A4;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(690, 590, 161, 31))
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color:#34A0A4;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(680, 20, 211, 31))
        font10 = QFont()
        font10.setFamily(u"Ubuntu Mono")
        font10.setPointSize(20)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setWeight(75)
        self.label_10.setFont(font10)
        self.label_10.setStyleSheet(u"color:#34A0A4;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 590, 301, 31))
        self.label_12.setFont(font9)
        self.label_12.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color:#34A0A4;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(660, 630, 321, 241))
        self.frame_4.setStyleSheet(u"QFrame#frame_4{\n"
"background-color:rgb(225, 245, 195);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setMidLineWidth(2)
        self.calling_stack = QListWidget(self.frame_4)
        self.calling_stack.setObjectName(u"calling_stack")
        self.calling_stack.setGeometry(QRect(20, 20, 291, 191))
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.calling_stack.sizePolicy().hasHeightForWidth())
        self.calling_stack.setSizePolicy(sizePolicy3)
        self.calling_stack.setMinimumSize(QSize(0, 0))
        self.calling_stack.setMaximumSize(QSize(300, 16777215))
        font11 = QFont()
        font11.setPointSize(16)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.calling_stack.setFont(font11)
        self.calling_stack.setFocusPolicy(Qt.NoFocus)
        self.calling_stack.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.calling_stack.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.calling_stack.setSelectionMode(QAbstractItemView.NoSelection)
        self.calling_stack.setProperty("isWrapping", False)
        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 60, 611, 341))
        self.frame_5.setStyleSheet(u"QFrame#frame_5{\n"
"background-color:rgb(225, 245, 195);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(2)
        self.tabWidget = QTabWidget(self.frame_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 591, 300))
        font12 = QFont()
        font12.setPointSize(17)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        self.tabWidget.setFont(font12)
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.parameters_tab = QWidget()
        self.parameters_tab.setObjectName(u"parameters_tab")
        self.regs1_view = QListView(self.parameters_tab)
        self.regs1_view.setObjectName(u"regs1_view")
        self.regs1_view.setGeometry(QRect(0, 0, 591, 271))
        self.regs1_view.setMaximumSize(QSize(800, 400))
        self.regs1_view.setFont(font7)
        self.regs1_view.setLayoutDirection(Qt.LeftToRight)
        self.regs1_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.regs1_view.setGridSize(QSize(0, 40))
        self.tabWidget.addTab(self.parameters_tab, "")
        self.caller_saved_tab = QWidget()
        self.caller_saved_tab.setObjectName(u"caller_saved_tab")
        self.regs2_view = QListView(self.caller_saved_tab)
        self.regs2_view.setObjectName(u"regs2_view")
        self.regs2_view.setGeometry(QRect(0, 0, 591, 271))
        self.regs2_view.setMaximumSize(QSize(800, 400))
        self.regs2_view.setFont(font7)
        self.regs2_view.setLayoutDirection(Qt.LeftToRight)
        self.regs2_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.regs2_view.setGridSize(QSize(0, 40))
        self.tabWidget.addTab(self.caller_saved_tab, "")
        self.callee_saved_tab = QWidget()
        self.callee_saved_tab.setObjectName(u"callee_saved_tab")
        self.regs3_view = QListView(self.callee_saved_tab)
        self.regs3_view.setObjectName(u"regs3_view")
        self.regs3_view.setGeometry(QRect(0, 0, 591, 311))
        self.regs3_view.setMaximumSize(QSize(800, 400))
        self.regs3_view.setFont(font7)
        self.regs3_view.setLayoutDirection(Qt.LeftToRight)
        self.regs3_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.regs3_view.setGridSize(QSize(0, 40))
        self.tabWidget.addTab(self.callee_saved_tab, "")
        self.special_tab = QWidget()
        self.special_tab.setObjectName(u"special_tab")
        self.regs4_view = QListView(self.special_tab)
        self.regs4_view.setObjectName(u"regs4_view")
        self.regs4_view.setGeometry(QRect(0, 0, 591, 311))
        self.regs4_view.setMaximumSize(QSize(800, 400))
        self.regs4_view.setFont(font7)
        self.regs4_view.setLayoutDirection(Qt.LeftToRight)
        self.regs4_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.regs4_view.setGridSize(QSize(0, 40))
        self.tabWidget.addTab(self.special_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.regs5_view = QListView(self.tab)
        self.regs5_view.setObjectName(u"regs5_view")
        self.regs5_view.setGeometry(QRect(0, 0, 591, 311))
        self.regs5_view.setMaximumSize(QSize(800, 400))
        self.regs5_view.setFont(font7)
        self.regs5_view.setLayoutDirection(Qt.LeftToRight)
        self.regs5_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.regs5_view.setGridSize(QSize(0, 40))
        self.tabWidget.addTab(self.tab, "")
        self.frame_6 = QFrame(self.widget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(660, 60, 321, 491))
        self.frame_6.setStyleSheet(u"QFrame#frame_6{\n"
"background-color:rgb(225, 245, 195);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(1)
        self.frame_6.setMidLineWidth(2)
        self.verticalLayoutWidget = QWidget(self.frame_6)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 301, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setBaseSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"\n"
"background-color:rgb(225, 245, 195);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(4)
        self.radio_16bit = QRadioButton(self.frame)
        self.radio_16bit.setObjectName(u"radio_16bit")
        self.radio_16bit.setGeometry(QRect(10, 10, 70, 20))
        font13 = QFont()
        font13.setPointSize(13)
        font13.setBold(False)
        font13.setItalic(False)
        font13.setWeight(50)
        self.radio_16bit.setFont(font13)
        self.radio_16bit.setStyleSheet(u"border: none;")
        self.radio_64bit = QRadioButton(self.frame)
        self.radio_64bit.setObjectName(u"radio_64bit")
        self.radio_64bit.setGeometry(QRect(190, 10, 70, 20))
        font14 = QFont()
        font14.setPointSize(13)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        font14.setKerning(True)
        self.radio_64bit.setFont(font14)
        self.radio_64bit.setStyleSheet(u"border: none;")
        self.radio_64bit.setChecked(True)
        self.radio_32bit = QRadioButton(self.frame)
        self.radio_32bit.setObjectName(u"radio_32bit")
        self.radio_32bit.setGeometry(QRect(100, 10, 70, 20))
        self.radio_32bit.setFont(font13)
        self.radio_32bit.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.frame)

        self.frame_combo = QComboBox(self.verticalLayoutWidget)
        self.frame_combo.setObjectName(u"frame_combo")
        self.frame_combo.setStyleSheet(u"\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QComboBox::item { \n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"\n"
"QComboBox::item:selected { \n"
"    color: white;\n"
"    background-color: blue;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.frame_combo)

        self.stack_frame = QListView(self.verticalLayoutWidget)
        self.stack_frame.setObjectName(u"stack_frame")
        sizePolicy3.setHeightForWidth(self.stack_frame.sizePolicy().hasHeightForWidth())
        self.stack_frame.setSizePolicy(sizePolicy3)
        self.stack_frame.setFont(font7)
        self.stack_frame.setFocusPolicy(Qt.NoFocus)
        self.stack_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stack_frame.setGridSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.stack_frame)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 15, 201, 20))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0%)")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(15, 17, 20, 20))
        self.label_16.setPixmap(QPixmap(u":/traceWindow/info.png"))
        self.label_16.setScaledContents(True)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 20, 20))
        self.label_3.setPixmap(QPixmap(u":/traceWindow/info.png"))
        self.label_3.setScaledContents(True)
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(670, 600, 20, 20))
        self.label_13.setPixmap(QPixmap(u":/traceWindow/info.png"))
        self.label_13.setScaledContents(True)
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 600, 20, 20))
        self.label_14.setPixmap(QPixmap(u":/traceWindow/info.png"))
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(670, 30, 20, 20))
        self.label_15.setPixmap(QPixmap(u":/traceWindow/info.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 2, 2)

        TraceWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(TraceWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1850, 22))
        TraceWindow.setMenuBar(self.menuBar)

        self.retranslateUi(TraceWindow)

        self.func_stack.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TraceWindow)
    # setupUi

    def retranslateUi(self, TraceWindow):
        TraceWindow.setWindowTitle(QCoreApplication.translate("TraceWindow", u"ASMtracer", None))
        self.action16_bit.setText(QCoreApplication.translate("TraceWindow", u"16-bit", None))
        self.action32_bit.setText(QCoreApplication.translate("TraceWindow", u"32-bit", None))
        self.action64_bit.setText(QCoreApplication.translate("TraceWindow", u"64-bit", None))
        self.actionfull_address.setText(QCoreApplication.translate("TraceWindow", u"full address", None))
        self.action_3.setText(QCoreApplication.translate("TraceWindow", u"address", None))
        self.action16_bit_2.setText(QCoreApplication.translate("TraceWindow", u"16-bit", None))
        self.actionabsolute.setText(QCoreApplication.translate("TraceWindow", u"absolute address", None))
        self.actionrelative_address.setText(QCoreApplication.translate("TraceWindow", u"relative address", None))
        self.action16_bit_3.setText(QCoreApplication.translate("TraceWindow", u"16-bit", None))
        self.action32_bit_2.setText(QCoreApplication.translate("TraceWindow", u"32-bit", None))
        self.action64_bit_2.setText(QCoreApplication.translate("TraceWindow", u"64-bit", None))
#if QT_CONFIG(tooltip)
        self.open_file_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"open file", None))
#endif // QT_CONFIG(tooltip)
        self.open_file_btn.setText("")
#if QT_CONFIG(tooltip)
        self.restart_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"restart", None))
#endif // QT_CONFIG(tooltip)
        self.restart_btn.setText("")
#if QT_CONFIG(tooltip)
        self.exit_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"exit\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.exit_btn.setText("")
        self.logo_lbl.setText("")
        self.label_11.setText(QCoreApplication.translate("TraceWindow", u"assembly code", None))
#if QT_CONFIG(tooltip)
        self.step_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"step into", u"aaa"))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.step_btn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.step_btn.setText("")
#if QT_CONFIG(tooltip)
        self.step_over_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"step over", None))
#endif // QT_CONFIG(tooltip)
        self.step_over_btn.setText("")
#if QT_CONFIG(tooltip)
        self.step_out_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"step out", None))
#endif // QT_CONFIG(tooltip)
        self.step_out_btn.setText("")
#if QT_CONFIG(tooltip)
        self.cont_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"<html><head/><body><p>continue execution</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cont_btn.setText("")
#if QT_CONFIG(tooltip)
        self.relative_address_btn.setToolTip(QCoreApplication.translate("TraceWindow", u"toggle relative address mode", None))
#endif // QT_CONFIG(tooltip)
        self.relative_address_btn.setText(QCoreApplication.translate("TraceWindow", u"relative\n"
"address", None))
        self.label.setText(QCoreApplication.translate("TraceWindow", u"font size:", None))
        self.label_7.setText(QCoreApplication.translate("TraceWindow", u"function:", None))
        self.label_8.setText(QCoreApplication.translate("TraceWindow", u"     address        command", None))
        self.label_4.setText(QCoreApplication.translate("TraceWindow", u"read", None))
        self.num_bytes_line_edit.setPlaceholderText(QCoreApplication.translate("TraceWindow", u"number", None))
        self.label_5.setText(QCoreApplication.translate("TraceWindow", u"bytes from address", None))
        self.address_line_edit.setPlaceholderText(QCoreApplication.translate("TraceWindow", u"address", None))
        self.get_data_btn.setText(QCoreApplication.translate("TraceWindow", u"get data", None))
        self.label_6.setText(QCoreApplication.translate("TraceWindow", u"registers", None))
        self.label_9.setText(QCoreApplication.translate("TraceWindow", u"call stack", None))
        self.label_10.setText(QCoreApplication.translate("TraceWindow", u"stack content", None))
        self.label_12.setText(QCoreApplication.translate("TraceWindow", u"read data from memory", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameters_tab), QCoreApplication.translate("TraceWindow", u"parametes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.caller_saved_tab), QCoreApplication.translate("TraceWindow", u"caller saved", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.callee_saved_tab), QCoreApplication.translate("TraceWindow", u"calle saved", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.special_tab), QCoreApplication.translate("TraceWindow", u"special", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TraceWindow", u"flags", None))
        self.radio_16bit.setText(QCoreApplication.translate("TraceWindow", u"16-bit", None))
        self.radio_64bit.setText(QCoreApplication.translate("TraceWindow", u"64-bit", None))
        self.radio_32bit.setText(QCoreApplication.translate("TraceWindow", u"32-bit", None))
        self.label_2.setText(QCoreApplication.translate("TraceWindow", u"stack variable size", None))
        self.label_16.setText("")
        self.label_3.setText("")
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("TraceWindow", u"placeHolder", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
    # retranslateUi

