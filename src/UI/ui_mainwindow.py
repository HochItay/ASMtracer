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
        MainWindow.resize(1480, 900)
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
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(0, 80))
        self.menu.setMaximumSize(QSize(16777215, 80))
        self.menu.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"background-color: rgb(181, 228, 140);")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.open_file_btn = QPushButton(self.menu)
        self.open_file_btn.setObjectName(u"open_file_btn")
        self.open_file_btn.setGeometry(QRect(20, 15, 60, 50))
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
        self.restart_btn.setGeometry(QRect(100, 15, 60, 50))
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
        self.restart_btn.setFlat(True)
        self.line = QFrame(self.menu)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(180, 1, 20, 78))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.VLine)
        self.exit_btn = QPushButton(self.menu)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(1400, 15, 60, 50))
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
        self.font_size_spin = QSpinBox(self.menu)
        self.font_size_spin.setObjectName(u"font_size_spin")
        self.font_size_spin.setGeometry(QRect(230, 30, 51, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.font_size_spin.setFont(font1)
        self.font_size_spin.setStyleSheet(u"background-color:rgb(225, 245, 195);")
        self.font_size_spin.setReadOnly(True)
        self.font_size_spin.setMinimum(8)
        self.font_size_spin.setMaximum(25)
        self.font_size_spin.setValue(11)
        self.font_size_spin.setDisplayIntegerBase(10)
        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 81, 17))
        self.label.setFont(font1)
        self.label_2 = QLabel(self.menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 2, 161, 15))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0%)")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.menu)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(320, 10, 300, 60))
        self.frame.setStyleSheet(u"border: 1px solid grey;\n"
"border-radius: 10px;\n"
"\n"
"background-color:rgb(225, 245, 195);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(4)
        self.radio_16bit = QRadioButton(self.frame)
        self.radio_16bit.setObjectName(u"radio_16bit")
        self.radio_16bit.setGeometry(QRect(10, 20, 70, 20))
        self.radio_16bit.setFont(font2)
        self.radio_16bit.setStyleSheet(u"border: none;")
        self.radio_16bit.setCheckable(False)
        self.radio_16bit.setChecked(False)
        self.radio_64bit = QRadioButton(self.frame)
        self.radio_64bit.setObjectName(u"radio_64bit")
        self.radio_64bit.setGeometry(QRect(200, 20, 70, 20))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setKerning(True)
        self.radio_64bit.setFont(font3)
        self.radio_64bit.setStyleSheet(u"border: none;")
        self.radio_64bit.setCheckable(False)
        self.radio_64bit.setChecked(False)
        self.radio_32bit = QRadioButton(self.frame)
        self.radio_32bit.setObjectName(u"radio_32bit")
        self.radio_32bit.setGeometry(QRect(105, 20, 70, 20))
        self.radio_32bit.setFont(font2)
        self.radio_32bit.setStyleSheet(u"border: none;")
        self.radio_32bit.setCheckable(False)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 0, 161, 21))
        self.label_3.setStyleSheet(u"background-color:rgb(225, 245, 195);\n"
"border: none;\n"
"border-radius: 0px;")
        self.relative_address_btn = QPushButton(self.menu)
        self.relative_address_btn.setObjectName(u"relative_address_btn")
        self.relative_address_btn.setGeometry(QRect(640, 15, 71, 51))
        self.relative_address_btn.setStyleSheet(u"QPushButton {\n"
"\n"
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
        self.relative_address_btn.setFlat(True)
        self.open_file_btn.raise_()
        self.restart_btn.raise_()
        self.line.raise_()
        self.exit_btn.raise_()
        self.font_size_spin.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.relative_address_btn.raise_()

        self.verticalLayout_2.addWidget(self.menu)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.logo_lbl = QLabel(self.widget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(350, 110, 721, 501))
        self.logo_lbl.setStyleSheet(u"background-color: none;")
        self.logo_lbl.setPixmap(QPixmap(u":/mainWindow/logo_no_bg.png"))
        self.logo_lbl.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout_2.setStretch(0, 2)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.restart_btn.setDefault(False)


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
        self.restart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"restart", None))
#endif // QT_CONFIG(tooltip)
        self.restart_btn.setText("")
#if QT_CONFIG(tooltip)
        self.exit_btn.setToolTip(QCoreApplication.translate("MainWindow", u"exit\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.exit_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"font size", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"stack variable size", None))
        self.radio_16bit.setText(QCoreApplication.translate("MainWindow", u"16-bit", None))
        self.radio_64bit.setText(QCoreApplication.translate("MainWindow", u"64-bit", None))
        self.radio_32bit.setText(QCoreApplication.translate("MainWindow", u"32-bit", None))
        self.label_3.setText("")
#if QT_CONFIG(tooltip)
        self.relative_address_btn.setToolTip(QCoreApplication.translate("MainWindow", u"toggle relative address mode", None))
#endif // QT_CONFIG(tooltip)
        self.relative_address_btn.setText(QCoreApplication.translate("MainWindow", u"relative\n"
"address", None))
        self.logo_lbl.setText("")
    # retranslateUi

