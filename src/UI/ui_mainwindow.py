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
        MainWindow.resize(496, 620)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_no_bg.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.instrction_lbl = QLabel(self.centralwidget)
        self.instrction_lbl.setObjectName(u"instrction_lbl")
        self.instrction_lbl.setGeometry(QRect(40, 250, 401, 91))
        font1 = QFont()
        font1.setPointSize(22)
        self.instrction_lbl.setFont(font1)
        self.instrction_lbl.setMouseTracking(False)
        self.instrction_lbl.setStyleSheet(u"background-color: rgba(255,255,255,10)")
        self.instrction_lbl.setScaledContents(False)
        self.instrction_lbl.setAlignment(Qt.AlignCenter)
        self.instrction_lbl.setWordWrap(True)
        self.logo_lbl = QLabel(self.centralwidget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(50, 10, 381, 241))
        self.logo_lbl.setStyleSheet(u"")
        self.logo_lbl.setPixmap(QPixmap(u":/mainWindow/logo_no_bg.png"))
        self.logo_lbl.setScaledContents(True)
        self.bg_lbl = QLabel(self.centralwidget)
        self.bg_lbl.setObjectName(u"bg_lbl")
        self.bg_lbl.setGeometry(QRect(0, 0, 496, 620))
        self.bg_lbl.setPixmap(QPixmap(u":/mainWindow/MainWindowBG.png"))
        self.bg_lbl.setScaledContents(False)
        self.choose_file_btn = QPushButton(self.centralwidget)
        self.choose_file_btn.setObjectName(u"choose_file_btn")
        self.choose_file_btn.setGeometry(QRect(40, 410, 161, 41))
        self.choose_file_btn.setStyleSheet(u"QPushButton {\n"
"	 background-color: #B5E48C;\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    font:  20px;\n"
"    padding: 6px;\n"
"	border-width: 1px;\n"
"	border-color: #000;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	font:  bold;\n"
"    border-width: 3px;\n"
"	border-color: rgb(78, 154, 6);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(29, 149, 45)\n"
"    }")
        self.run_btn = QPushButton(self.centralwidget)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setGeometry(QRect(40, 470, 411, 81))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.run_btn.setFont(font2)
        self.run_btn.setStyleSheet(u"QPushButton {\n"
"	 background-color: #B5E48C;\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"    font:  35px;\n"
"    padding: 6px;\n"
"	border-width: 1px;\n"
"	border-color: #000;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	font:  bold;\n"
"    border-width: 3px;\n"
"	border-color: rgb(78, 154, 6);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	border-style: inset;\n"
"    background-color: rgb(29, 149, 45)\n"
"    }")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 410, 221, 41))
        self.warning_lbl = QLabel(self.centralwidget)
        self.warning_lbl.setObjectName(u"warning_lbl")
        self.warning_lbl.setGeometry(QRect(70, 350, 331, 41))
        self.warning_lbl.setFont(font)
        self.warning_lbl.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.warning_lbl.setAlignment(Qt.AlignCenter)
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(390, 560, 91, 51))
        self.exit_btn.setFont(font2)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.bg_lbl.raise_()
        self.instrction_lbl.raise_()
        self.logo_lbl.raise_()
        self.choose_file_btn.raise_()
        self.run_btn.raise_()
        self.lineEdit.raise_()
        self.warning_lbl.raise_()
        self.exit_btn.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.instrction_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.instrction_lbl.setText(QCoreApplication.translate("MainWindow", u"choose an ELF file to run", None))
        self.logo_lbl.setText("")
        self.bg_lbl.setText("")
        self.choose_file_btn.setText(QCoreApplication.translate("MainWindow", u"browse", None))
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"start running!", None))
        self.warning_lbl.setText("")
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"exit", None))
    # retranslateUi

