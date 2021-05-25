# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import UI.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1700, 900)
        MainWindow.setMaximumSize(QSize(1700, 900))
        MainWindow.setBaseSize(QSize(1700, 900))
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_white_bg.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.action16_bit = QAction(MainWindow)
        self.action16_bit.setObjectName(u"action16_bit")
        self.action32_bit = QAction(MainWindow)
        self.action32_bit.setObjectName(u"action32_bit")
        self.action64_bit = QAction(MainWindow)
        self.action64_bit.setObjectName(u"action64_bit")
        self.actionfull_address = QAction(MainWindow)
        self.actionfull_address.setObjectName(u"actionfull_address")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action16_bit_2 = QAction(MainWindow)
        self.action16_bit_2.setObjectName(u"action16_bit_2")
        self.actionabsolute = QAction(MainWindow)
        self.actionabsolute.setObjectName(u"actionabsolute")
        self.actionrelative_address = QAction(MainWindow)
        self.actionrelative_address.setObjectName(u"actionrelative_address")
        self.action16_bit_3 = QAction(MainWindow)
        self.action16_bit_3.setObjectName(u"action16_bit_3")
        self.action32_bit_2 = QAction(MainWindow)
        self.action32_bit_2.setObjectName(u"action32_bit_2")
        self.action64_bit_2 = QAction(MainWindow)
        self.action64_bit_2.setObjectName(u"action64_bit_2")
        self.centralwidget = QWidget(MainWindow)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 4)
        self.menu_2 = QFrame(self.centralwidget)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setMinimumSize(QSize(0, 80))
        self.menu_2.setMaximumSize(QSize(16777215, 80))
        self.menu_2.setStyleSheet(u"background-color: rgb(116, 180, 240);\n"
"")
        self.menu_2.setFrameShape(QFrame.StyledPanel)
        self.menu_2.setFrameShadow(QFrame.Raised)
        self.open_file_btn = QPushButton(self.menu_2)
        self.open_file_btn.setObjectName(u"open_file_btn")
        self.open_file_btn.setGeometry(QRect(1510, 15, 60, 50))
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
        self.exit_btn = QPushButton(self.menu_2)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(1600, 15, 60, 50))
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
        self.line_2 = QFrame(self.menu_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1570, 1, 20, 78))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.VLine)
        self.logo_lbl_2 = QLabel(self.menu_2)
        self.logo_lbl_2.setObjectName(u"logo_lbl_2")
        self.logo_lbl_2.setGeometry(QRect(0, 0, 201, 81))
        self.logo_lbl_2.setStyleSheet(u"background-color: none;")
        self.logo_lbl_2.setPixmap(QPixmap(u":/mainWindow/logo_no_bg.png"))
        self.logo_lbl_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.menu_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.logo_lbl = QLabel(self.widget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(240, 110, 861, 581))
        self.logo_lbl.setStyleSheet(u"background-color: none;")
        self.logo_lbl.setPixmap(QPixmap(u":/mainWindow/logo_no_bg.png"))
        self.logo_lbl.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ASMtracer", None))
        self.action16_bit.setText(QCoreApplication.translate("MainWindow", u"16-bit", None))
        self.action32_bit.setText(QCoreApplication.translate("MainWindow", u"32-bit", None))
        self.action64_bit.setText(QCoreApplication.translate("MainWindow", u"64-bit", None))
        self.actionfull_address.setText(QCoreApplication.translate("MainWindow", u"full address", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"address", None))
        self.action16_bit_2.setText(QCoreApplication.translate("MainWindow", u"16-bit", None))
        self.actionabsolute.setText(QCoreApplication.translate("MainWindow", u"absolute address", None))
        self.actionrelative_address.setText(QCoreApplication.translate("MainWindow", u"relative address", None))
        self.action16_bit_3.setText(QCoreApplication.translate("MainWindow", u"16-bit", None))
        self.action32_bit_2.setText(QCoreApplication.translate("MainWindow", u"32-bit", None))
        self.action64_bit_2.setText(QCoreApplication.translate("MainWindow", u"64-bit", None))
#if QT_CONFIG(tooltip)
        self.open_file_btn.setToolTip(QCoreApplication.translate("MainWindow", u"open file", None))
#endif // QT_CONFIG(tooltip)
        self.open_file_btn.setText("")
#if QT_CONFIG(tooltip)
        self.exit_btn.setToolTip(QCoreApplication.translate("MainWindow", u"exit\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.exit_btn.setText("")
        self.logo_lbl_2.setText("")
        self.logo_lbl.setText("")
    # retranslateUi

