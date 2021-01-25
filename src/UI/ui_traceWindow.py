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
        TraceWindow.resize(1087, 677)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_no_bg.png", QSize(), QIcon.Normal, QIcon.Off)
        TraceWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(TraceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 451, 671))
        self.code_area = QVBoxLayout(self.verticalLayoutWidget)
        self.code_area.setObjectName(u"code_area")
        self.code_area.setContentsMargins(0, 0, 0, 0)
        self.func_combo = QComboBox(self.verticalLayoutWidget)
        self.func_combo.setObjectName(u"func_combo")

        self.code_area.addWidget(self.func_combo)

        self.instruction_list = QListWidget(self.verticalLayoutWidget)
        self.instruction_list.setObjectName(u"instruction_list")
        font = QFont()
        font.setPointSize(14)
        self.instruction_list.setFont(font)
        self.instruction_list.setAutoFillBackground(False)
        self.instruction_list.setStyleSheet(u"background-color: rgb(252, 242, 162);")

        self.code_area.addWidget(self.instruction_list)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 130, 211, 81))
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        TraceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TraceWindow)

        QMetaObject.connectSlotsByName(TraceWindow)
    # setupUi

    def retranslateUi(self, TraceWindow):
        TraceWindow.setWindowTitle(QCoreApplication.translate("TraceWindow", u"ASMtracer", None))
        self.pushButton.setText(QCoreApplication.translate("TraceWindow", u"step", None))
    # retranslateUi

