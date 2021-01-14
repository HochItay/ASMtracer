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


class Ui_TraceWindow(object):
    def setupUi(self, TraceWindow):
        if not TraceWindow.objectName():
            TraceWindow.setObjectName(u"TraceWindow")
        TraceWindow.resize(1087, 677)
        self.centralwidget = QWidget(TraceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 451, 671))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.func_combo = QComboBox(self.verticalLayoutWidget)
        self.func_combo.setObjectName(u"func_combo")

        self.verticalLayout.addWidget(self.func_combo)

        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(540, 20, 449, 638))
        font = QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(u"background-color: rgb(252, 242, 162);")
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setItemAlignment(Qt.AlignLeading)
        TraceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TraceWindow)

        QMetaObject.connectSlotsByName(TraceWindow)
    # setupUi

    def retranslateUi(self, TraceWindow):
        TraceWindow.setWindowTitle(QCoreApplication.translate("TraceWindow", u"MainWindow", None))
    # retranslateUi

