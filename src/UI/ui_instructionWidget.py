# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instructionWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InstructionWidget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(435, 66)
        Form.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bp_btn = QPushButton(Form)
        self.bp_btn.setObjectName(u"bp_btn")
        self.bp_btn.setMaximumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.bp_btn)

        self.description = QLabel(Form)
        self.description.setObjectName(u"description")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.description)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bp_btn.setText("")
    # retranslateUi

