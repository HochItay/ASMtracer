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

import UI.rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        icon = QIcon()
        icon.addFile(u":/mainWindow/logo_no_bg.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.instrction_lbl = QLabel(self.centralwidget)
        self.instrction_lbl.setObjectName(u"instrction_lbl")
        self.instrction_lbl.setGeometry(QRect(60, 210, 261, 91))
        font = QFont()
        font.setPointSize(20)
        self.instrction_lbl.setFont(font)
        self.instrction_lbl.setMouseTracking(False)
        self.instrction_lbl.setStyleSheet(u"background-color: rgba(255,255,255,10)")
        self.instrction_lbl.setScaledContents(False)
        self.instrction_lbl.setAlignment(Qt.AlignCenter)
        self.instrction_lbl.setWordWrap(True)
        self.logo_lbl = QLabel(self.centralwidget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(30, 10, 331, 221))
        self.logo_lbl.setStyleSheet(u"")
        self.logo_lbl.setPixmap(QPixmap(u":/mainWindow/logo_no_bg.png"))
        self.logo_lbl.setScaledContents(True)
        self.bg_lbl = QLabel(self.centralwidget)
        self.bg_lbl.setObjectName(u"bg_lbl")
        self.bg_lbl.setGeometry(QRect(0, 0, 400, 500))
        self.bg_lbl.setPixmap(QPixmap(u":/mainWindow/MainWindowBG.png"))
        self.bg_lbl.setScaledContents(False)
        self.choose_file_btn = QPushButton(self.centralwidget)
        self.choose_file_btn.setObjectName(u"choose_file_btn")
        self.choose_file_btn.setGeometry(QRect(20, 330, 141, 31))
        self.choose_file_btn.setStyleSheet(u"QPushButton {\n"
"	 background-color: #b6f074;\n"
"    border-style: outset;\n"
"    border-radius: 8px;\n"
"    font:  18px;\n"
"    padding: 6px;\n"
"	border-width: 1px;\n"
"	border-color: #000;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	font:  bold 18px;\n"
"    border-width: 3px;\n"
"	border-color: rgb(78, 154, 6);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(29, 149, 45)\n"
"    }")
        self.run_btn = QPushButton(self.centralwidget)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setGeometry(QRect(20, 400, 354, 71))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.run_btn.setFont(font1)
        self.run_btn.setStyleSheet(u"QPushButton {\n"
"	 background-color: #b6f074;\n"
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
"	border-color: rgb(78, 154, 6);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	border-style: inset;\n"
"    background-color: rgb(29, 149, 45)\n"
"    }")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 330, 201, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.bg_lbl.raise_()
        self.instrction_lbl.raise_()
        self.logo_lbl.raise_()
        self.choose_file_btn.raise_()
        self.run_btn.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.instrction_lbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.instrction_lbl.setText(QCoreApplication.translate("MainWindow", u"choose an executable file to run", None))
        self.logo_lbl.setText("")
        self.bg_lbl.setText("")
        self.choose_file_btn.setText(QCoreApplication.translate("MainWindow", u"choose file", None))
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"start running!", None))
    # retranslateUi

