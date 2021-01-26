from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# a widget for displaying an instruction
class QInstruction(QWidget):
    def __init__ (self, instruction, parent=None):
        QWidget.__init__(self, parent)
        self.instruction = instruction

        self.layout = QVBoxLayout()
        self.instruction_label = QLabel()
        self.instruction_label.setText(str(self.instruction))
        self.layout.addWidget(self.instruction_label)
        self.setLayout(self.layout)

        # setStyleSheet
        self.instruction_label.setStyleSheet('''
            color: rgb(0, 0, 0);
        ''')

    # highlight the instruction
    def highlight(self):
        self.instruction_label.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')