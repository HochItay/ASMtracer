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
        TraceWindow.resize(1400, 1000)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_no_bg.png", QSize(), QIcon.Normal, QIcon.Off)
        TraceWindow.setWindowIcon(icon)
        TraceWindow.setStyleSheet(u"background-color: rgb(220, 240, 189);")
        self.centralwidget = QWidget(TraceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 10, 1071, 731))
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.code_area = QVBoxLayout(self.verticalLayoutWidget)
        self.code_area.setObjectName(u"code_area")
        self.code_area.setContentsMargins(0, 0, 0, 0)
        self.func_combo = QComboBox(self.verticalLayoutWidget)
        self.func_combo.setObjectName(u"func_combo")

        self.code_area.addWidget(self.func_combo)

        self.func_stack = QStackedWidget(self.verticalLayoutWidget)
        self.func_stack.setObjectName(u"func_stack")
        self.func_stack.setStyleSheet(u"background-color: rgb(252, 242, 162);")

        self.code_area.addWidget(self.func_stack)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.cont_btn = QPushButton(self.widget)
        self.cont_btn.setObjectName(u"cont_btn")
        self.cont_btn.setGeometry(QRect(20, 0, 116, 100))
        self.cont_btn.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(20)
        self.cont_btn.setFont(font)
        self.step_btn = QPushButton(self.widget)
        self.step_btn.setObjectName(u"step_btn")
        self.step_btn.setGeometry(QRect(150, 0, 100, 100))
        self.step_btn.setMinimumSize(QSize(100, 100))
        self.step_btn.setFont(font)
        self.step_btn.setToolTipDuration(1)
        self.step_btn.setStyleSheet(u"border-image: url(:/traceWindow/step_in.png);")
        self.step_out_btn = QPushButton(self.widget)
        self.step_out_btn.setObjectName(u"step_out_btn")
        self.step_out_btn.setGeometry(QRect(270, 0, 100, 100))
        self.step_out_btn.setMinimumSize(QSize(100, 100))
        self.step_out_btn.setFont(font)
        self.step_out_btn.setStyleSheet(u"border-image: url(:/traceWindow/step_out.png);")
        self.step_over_btn = QPushButton(self.widget)
        self.step_over_btn.setObjectName(u"step_over_btn")
        self.step_over_btn.setGeometry(QRect(390, 0, 100, 100))
        self.step_over_btn.setMinimumSize(QSize(100, 100))
        self.step_over_btn.setMaximumSize(QSize(300, 300))
        self.step_over_btn.setSizeIncrement(QSize(1, 1))
        self.step_over_btn.setFont(font)
#if QT_CONFIG(tooltip)
        self.step_over_btn.setToolTip(u"<html><head/><body><p>step over</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.step_over_btn.setAutoFillBackground(False)
        self.step_over_btn.setStyleSheet(u"border-image: url(:/traceWindow/step_over.png);")

        self.verticalLayout.addWidget(self.widget)

        self.registers_view = QTableView(self.verticalLayoutWidget_2)
        self.registers_view.setObjectName(u"registers_view")
        self.registers_view.setMaximumSize(QSize(600, 400))
        self.registers_view.setLayoutDirection(Qt.LeftToRight)
        self.registers_view.setShowGrid(False)
        self.registers_view.setGridStyle(Qt.NoPen)

        self.verticalLayout.addWidget(self.registers_view)

        self.calling_stack = QListWidget(self.verticalLayoutWidget_2)
        self.calling_stack.setObjectName(u"calling_stack")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calling_stack.sizePolicy().hasHeightForWidth())
        self.calling_stack.setSizePolicy(sizePolicy1)
        self.calling_stack.setMinimumSize(QSize(0, 0))
        self.calling_stack.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.calling_stack)

        self.stack_frame = QListView(self.verticalLayoutWidget_2)
        self.stack_frame.setObjectName(u"stack_frame")
        sizePolicy1.setHeightForWidth(self.stack_frame.sizePolicy().hasHeightForWidth())
        self.stack_frame.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.stack_frame)

        self.splitter.addWidget(self.verticalLayoutWidget_2)
        TraceWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(TraceWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1400, 22))
        TraceWindow.setMenuBar(self.menuBar)

        self.retranslateUi(TraceWindow)

        QMetaObject.connectSlotsByName(TraceWindow)
    # setupUi

    def retranslateUi(self, TraceWindow):
        TraceWindow.setWindowTitle(QCoreApplication.translate("TraceWindow", u"ASMtracer", None))
        self.cont_btn.setText(QCoreApplication.translate("TraceWindow", u"continue", None))
#if QT_CONFIG(tooltip)
        self.step_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.step_btn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.step_btn.setText("")
        self.step_out_btn.setText("")
        self.step_over_btn.setText("")
    # retranslateUi

