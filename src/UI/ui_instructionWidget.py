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

import windows.custom_widgets


class Ui_instructionWidget(object):
    def setupUi(self, instructionWidget):
        if not instructionWidget.objectName():
            instructionWidget.setObjectName(u"instructionWidget")
        instructionWidget.resize(441, 61)
        instructionWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(instructionWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(instructionWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(50, 40))
        self.bp_btn = QPushButton(self.widget)
        self.bp_btn.setObjectName(u"bp_btn")
        self.bp_btn.setGeometry(QRect(0, 0, 50, 40))
        self.bp_btn.setMaximumSize(QSize(50, 50))
        self.bp_btn.setStyleSheet(u"")
        self.bp_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.widget)

        self.description = QLabel(instructionWidget)
        self.description.setObjectName(u"description")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.description)


        self.retranslateUi(instructionWidget)

        QMetaObject.connectSlotsByName(instructionWidget)
    # setupUi

    def retranslateUi(self, instructionWidget):
        instructionWidget.setWindowTitle(QCoreApplication.translate("instructionWidget", u"Form", None))
        self.bp_btn.setText("")
        self.description.setText("")
    # retranslateUi

