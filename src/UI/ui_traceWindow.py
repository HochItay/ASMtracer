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
        TraceWindow.resize(1026, 750)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_no_bg.png", QSize(), QIcon.Normal, QIcon.Off)
        TraceWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(TraceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 1011, 731))
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
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.step_btn = QPushButton(self.verticalLayoutWidget_2)
        self.step_btn.setObjectName(u"step_btn")
        self.step_btn.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(20)
        self.step_btn.setFont(font)
        self.step_btn.setToolTipDuration(1)

        self.verticalLayout_2.addWidget(self.step_btn)

        self.cont_btn = QPushButton(self.verticalLayoutWidget_2)
        self.cont_btn.setObjectName(u"cont_btn")
        self.cont_btn.setMinimumSize(QSize(0, 100))
        self.cont_btn.setFont(font)

        self.verticalLayout_2.addWidget(self.cont_btn)

        self.splitter.addWidget(self.verticalLayoutWidget_2)
        TraceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TraceWindow)

        QMetaObject.connectSlotsByName(TraceWindow)
    # setupUi

    def retranslateUi(self, TraceWindow):
        TraceWindow.setWindowTitle(QCoreApplication.translate("TraceWindow", u"ASMtracer", None))
#if QT_CONFIG(tooltip)
        self.step_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.step_btn.setText(QCoreApplication.translate("TraceWindow", u"step", None))
        self.cont_btn.setText(QCoreApplication.translate("TraceWindow", u"continue", None))
    # retranslateUi

