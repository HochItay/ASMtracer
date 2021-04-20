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
        TraceWindow.resize(1600, 900)
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        TraceWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_no_bg.png", QSize(), QIcon.Normal, QIcon.Off)
        TraceWindow.setWindowIcon(icon)
        TraceWindow.setStyleSheet(u"\n"
"background-color: rgb(220, 240, 189);\n"
"font:  \"Ubuntu Mono\";")
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
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 1600, 900))
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(True)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.code_area = QVBoxLayout()
        self.code_area.setObjectName(u"code_area")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.func_combo = QComboBox(self.layoutWidget)
        self.func_combo.setObjectName(u"func_combo")

        self.horizontalLayout_3.addWidget(self.func_combo)


        self.code_area.addLayout(self.horizontalLayout_3)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setFamily(u"Ubuntu Mono")
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_8.setFont(font2)

        self.code_area.addWidget(self.label_8)

        self.func_stack = QStackedWidget(self.layoutWidget)
        self.func_stack.setObjectName(u"func_stack")
        font3 = QFont()
        font3.setFamily(u"Ubuntu Mono")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.func_stack.setFont(font3)
        self.func_stack.setStyleSheet(u"background-color: rgb(255, 255, 255);")


        self.code_area.addWidget(self.func_stack)


        self.horizontalLayout_2.addLayout(self.code_area)

        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(140, 0))
        self.cont_btn = QPushButton(self.widget)
        self.cont_btn.setObjectName(u"cont_btn")
        self.cont_btn.setGeometry(QRect(10, 400, 120, 100))
        self.cont_btn.setMinimumSize(QSize(0, 100))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.cont_btn.setFont(font4)
        self.cont_btn.setStyleSheet(u"QPushButton {\n"
"border-image: url(:/traceWindow/continue.png);\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #b5e48c, stop: 1 #76c893);\n"
"border-radius: 15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #76c893, stop: 1 #b5e48c);\n"
"    }")
        self.cont_btn.setFlat(False)
        self.step_btn = QPushButton(self.widget)
        self.step_btn.setObjectName(u"step_btn")
        self.step_btn.setGeometry(QRect(10, 20, 120, 100))
        self.step_btn.setMinimumSize(QSize(100, 100))
        self.step_btn.setFont(font4)
        self.step_btn.setToolTipDuration(1)
        self.step_btn.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"border-image: url(:/traceWindow/step_in.png);\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #b5e48c, stop: 1 #76c893);\n"
"border-radius: 15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #76c893, stop: 1 #b5e48c);\n"
"    }")
        self.step_out_btn = QPushButton(self.widget)
        self.step_out_btn.setObjectName(u"step_out_btn")
        self.step_out_btn.setGeometry(QRect(10, 270, 120, 100))
        self.step_out_btn.setMinimumSize(QSize(100, 100))
        self.step_out_btn.setFont(font4)
        self.step_out_btn.setStyleSheet(u"QPushButton {\n"
"border-image: url(:/traceWindow/step_out.png);\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #b5e48c, stop: 1 #76c893);\n"
"border-radius: 15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #76c893, stop: 1 #b5e48c);\n"
"    }")
        self.step_over_btn = QPushButton(self.widget)
        self.step_over_btn.setObjectName(u"step_over_btn")
        self.step_over_btn.setGeometry(QRect(10, 140, 120, 100))
        self.step_over_btn.setMinimumSize(QSize(100, 100))
        self.step_over_btn.setMaximumSize(QSize(300, 300))
        self.step_over_btn.setSizeIncrement(QSize(1, 1))
        self.step_over_btn.setFont(font4)
#if QT_CONFIG(tooltip)
        self.step_over_btn.setToolTip(u"<html><head/><body><p>step over</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.step_over_btn.setAutoFillBackground(False)
        self.step_over_btn.setStyleSheet(u"QPushButton {\n"
"border-image: url(:/traceWindow/step_over.png);\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #b5e48c, stop: 1 #76c893);\n"
"border-radius: 15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #76c893, stop: 1 #b5e48c);\n"
"    }")
        self.back_instruction = QPushButton(self.widget)
        self.back_instruction.setObjectName(u"back_instruction")
        self.back_instruction.setGeometry(QRect(10, 530, 120, 100))
        self.back_instruction.setMinimumSize(QSize(0, 100))
        self.back_instruction.setFont(font4)
        self.back_instruction.setStyleSheet(u"QPushButton {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #b5e48c, stop: 1 #76c893);\n"
"border-radius: 15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #76c893, stop: 1 #b5e48c);\n"
"    }")
        self.back_instruction.setFlat(False)
        self.restart_btn = QPushButton(self.widget)
        self.restart_btn.setObjectName(u"restart_btn")
        self.restart_btn.setGeometry(QRect(10, 660, 120, 100))
        self.restart_btn.setMinimumSize(QSize(0, 100))
        self.restart_btn.setFont(font4)
        self.restart_btn.setStyleSheet(u"QPushButton {\n"
"border-image: url(:/traceWindow/restart.png);\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #b5e48c, stop: 1 #76c893);\n"
"border-radius: 15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #76c893, stop: 1 #b5e48c);\n"
"    }")
        self.restart_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.widget)

        self.splitter.addWidget(self.layoutWidget)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(750, 0))
        self.stack_frame = QListView(self.widget_2)
        self.stack_frame.setObjectName(u"stack_frame")
        self.stack_frame.setGeometry(QRect(30, 430, 221, 241))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stack_frame.sizePolicy().hasHeightForWidth())
        self.stack_frame.setSizePolicy(sizePolicy1)
        self.stack_frame.setFont(font3)
        self.stack_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.calling_stack = QListWidget(self.widget_2)
        self.calling_stack.setObjectName(u"calling_stack")
        self.calling_stack.setGeometry(QRect(470, 70, 251, 311))
        sizePolicy1.setHeightForWidth(self.calling_stack.sizePolicy().hasHeightForWidth())
        self.calling_stack.setSizePolicy(sizePolicy1)
        self.calling_stack.setMinimumSize(QSize(0, 0))
        self.calling_stack.setMaximumSize(QSize(300, 16777215))
        self.calling_stack.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.calling_stack.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.calling_stack.setSelectionMode(QAbstractItemView.NoSelection)
        self.calling_stack.setProperty("isWrapping", False)
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 690, 591, 161))
        self.frame.setStyleSheet(u"border-width: 10px")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 51, 41))
        self.label.setFont(font2)
        self.num_bytes_line_edit = QLineEdit(self.frame)
        self.num_bytes_line_edit.setObjectName(u"num_bytes_line_edit")
        self.num_bytes_line_edit.setGeometry(QRect(80, 20, 111, 25))
        self.num_bytes_line_edit.setFont(font3)
        self.num_bytes_line_edit.setStyleSheet(u"background-color: #ffffff")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 10, 211, 41))
        self.label_2.setFont(font2)
        self.address_line_edit = QLineEdit(self.frame)
        self.address_line_edit.setObjectName(u"address_line_edit")
        self.address_line_edit.setGeometry(QRect(420, 20, 161, 25))
        self.address_line_edit.setFont(font3)
        self.address_line_edit.setStyleSheet(u"background-color: #ffffff")
        self.data_area = QTextEdit(self.frame)
        self.data_area.setObjectName(u"data_area")
        self.data_area.setGeometry(QRect(160, 60, 421, 91))
        self.data_area.setFont(font3)
        self.data_area.setStyleSheet(u"background-color: #ffffff")
        self.data_area.setReadOnly(True)
        self.get_data_btn = QPushButton(self.frame)
        self.get_data_btn.setObjectName(u"get_data_btn")
        self.get_data_btn.setGeometry(QRect(20, 90, 121, 41))
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 40, 431, 341))
        self.parameters_tab = QWidget()
        self.parameters_tab.setObjectName(u"parameters_tab")
        self.regs1_view = QListView(self.parameters_tab)
        self.regs1_view.setObjectName(u"regs1_view")
        self.regs1_view.setGeometry(QRect(0, 0, 431, 311))
        self.regs1_view.setMaximumSize(QSize(800, 400))
        self.regs1_view.setFont(font3)
        self.regs1_view.setLayoutDirection(Qt.LeftToRight)
        self.regs1_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.parameters_tab, "")
        self.caller_saved_tab = QWidget()
        self.caller_saved_tab.setObjectName(u"caller_saved_tab")
        self.regs2_view = QListView(self.caller_saved_tab)
        self.regs2_view.setObjectName(u"regs2_view")
        self.regs2_view.setGeometry(QRect(0, 0, 431, 311))
        self.regs2_view.setMaximumSize(QSize(800, 400))
        self.regs2_view.setFont(font3)
        self.regs2_view.setLayoutDirection(Qt.LeftToRight)
        self.regs2_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.caller_saved_tab, "")
        self.callee_saved_tab = QWidget()
        self.callee_saved_tab.setObjectName(u"callee_saved_tab")
        self.regs3_view = QListView(self.callee_saved_tab)
        self.regs3_view.setObjectName(u"regs3_view")
        self.regs3_view.setGeometry(QRect(0, 0, 431, 311))
        self.regs3_view.setMaximumSize(QSize(800, 400))
        self.regs3_view.setFont(font3)
        self.regs3_view.setLayoutDirection(Qt.LeftToRight)
        self.regs3_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.callee_saved_tab, "")
        self.special_tab = QWidget()
        self.special_tab.setObjectName(u"special_tab")
        self.regs4_view = QListView(self.special_tab)
        self.regs4_view.setObjectName(u"regs4_view")
        self.regs4_view.setGeometry(QRect(0, 0, 431, 311))
        self.regs4_view.setMaximumSize(QSize(800, 400))
        self.regs4_view.setFont(font3)
        self.regs4_view.setLayoutDirection(Qt.LeftToRight)
        self.regs4_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.special_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.regs5_view = QListView(self.tab)
        self.regs5_view.setObjectName(u"regs5_view")
        self.regs5_view.setGeometry(QRect(0, 0, 431, 311))
        self.regs5_view.setMaximumSize(QSize(800, 400))
        self.regs5_view.setFont(font3)
        self.regs5_view.setLayoutDirection(Qt.LeftToRight)
        self.regs5_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.tab, "")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 10, 361, 31))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 20, 231, 31))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.inOutArea = QPlainTextEdit(self.widget_2)
        self.inOutArea.setObjectName(u"inOutArea")
        self.inOutArea.setGeometry(QRect(290, 430, 391, 241))
        self.inOutArea.setFont(font3)
        self.inOutArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 390, 211, 31))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 400, 241, 31))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.exit_btn = QPushButton(self.widget_2)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(640, 800, 91, 51))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.exit_btn.setFont(font5)
        self.exit_btn.setStyleSheet(u"QPushButton {\n"
"	 background-color: #ff8080;\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"    font:  30px;\n"
"    padding: 6px;\n"
"	border-width: 1px;\n"
"	border-color: #000;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	font:  bold 30px;\n"
"    border-width: 3px;\n"
"	border-color: #ff3333;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	border-style: inset;\n"
"    background-color: #ff3333;\n"
"    }")
        self.splitter.addWidget(self.widget_2)
        TraceWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(TraceWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1600, 22))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(220, 240, 189, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(246, 246, 245, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(119, 119, 118, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(159, 159, 157, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush8 = QBrush(QColor(238, 238, 236, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.menuBar.setPalette(palette)
        self.menuview = QMenu(self.menuBar)
        self.menuview.setObjectName(u"menuview")
        self.menuaddress = QMenu(self.menuview)
        self.menuaddress.setObjectName(u"menuaddress")
        self.menulocal_variable_size = QMenu(self.menuview)
        self.menulocal_variable_size.setObjectName(u"menulocal_variable_size")
        TraceWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuview.menuAction())
        self.menuview.addSeparator()
        self.menuview.addAction(self.menuaddress.menuAction())
        self.menuview.addAction(self.menulocal_variable_size.menuAction())
        self.menuaddress.addSeparator()
        self.menuaddress.addAction(self.actionabsolute)
        self.menuaddress.addAction(self.actionrelative_address)
        self.menulocal_variable_size.addAction(self.action16_bit_3)
        self.menulocal_variable_size.addAction(self.action32_bit_2)
        self.menulocal_variable_size.addAction(self.action64_bit_2)

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
        self.label_7.setText(QCoreApplication.translate("TraceWindow", u"function:", None))
        self.label_8.setText(QCoreApplication.translate("TraceWindow", u"        address      command", None))
        self.cont_btn.setText("")
#if QT_CONFIG(tooltip)
        self.step_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.step_btn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.step_btn.setText("")
        self.step_out_btn.setText("")
        self.step_over_btn.setText("")
        self.back_instruction.setText(QCoreApplication.translate("TraceWindow", u"current", None))
        self.restart_btn.setText("")
        self.label.setText(QCoreApplication.translate("TraceWindow", u"read", None))
        self.label_2.setText(QCoreApplication.translate("TraceWindow", u"bytes from address", None))
        self.get_data_btn.setText(QCoreApplication.translate("TraceWindow", u"get data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameters_tab), QCoreApplication.translate("TraceWindow", u"parametes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.caller_saved_tab), QCoreApplication.translate("TraceWindow", u"caller saved", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.callee_saved_tab), QCoreApplication.translate("TraceWindow", u"calle saved", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.special_tab), QCoreApplication.translate("TraceWindow", u"special", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TraceWindow", u"flags", None))
        self.label_3.setText(QCoreApplication.translate("TraceWindow", u"registers", None))
        self.label_4.setText(QCoreApplication.translate("TraceWindow", u"call stack", None))
        self.label_5.setText(QCoreApplication.translate("TraceWindow", u"stack content", None))
        self.label_6.setText(QCoreApplication.translate("TraceWindow", u"input/output area", None))
        self.exit_btn.setText(QCoreApplication.translate("TraceWindow", u"exit", None))
        self.menuview.setTitle(QCoreApplication.translate("TraceWindow", u"view", None))
        self.menuaddress.setTitle(QCoreApplication.translate("TraceWindow", u"address", None))
        self.menulocal_variable_size.setTitle(QCoreApplication.translate("TraceWindow", u"local variable size", None))
    # retranslateUi

