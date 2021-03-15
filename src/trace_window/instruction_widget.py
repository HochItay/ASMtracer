import sys
from UI.ui_instructionWidget import Ui_InstructionWidget

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QStackedWidget, QWidget

class QInstruction(QWidget):
    def __init__(self, instruction, debugger, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_InstructionWidget()
        self.ui.setupUi(self)

        self.instruction = instruction
        self.ui.description.setText(str(self.instruction))
        self.debugger = debugger

        self.bp_is_enable = False
        self.ui.bp_btn.clicked.connect(self.breakpoint_clicked)
        self.ui.bp_btn.setStyleSheet('''
            background-color: #ffffff;
        ''')


    # highlight the instruction
    def highlight(self):
        self.ui.description.setStyleSheet('''
            background-color: #b6f074;
        ''')

    # cancel the highlight the instruction
    def unlight(self):
        self.ui.description.setStyleSheet('''
        ''')

    # place breakpoint on this instruction
    def place_breakpoint(self):
        self.bp_is_enable = True
        self.debugger.place_breakpoint(self.instruction.address)
        self.ui.bp_btn.setStyleSheet('''
            background-color: #cc3300;
        ''')

    # remove breakpoint from this instruction
    def remove_breakpoint(self):
        self.bp_is_enable = False
        self.debugger.clear_breakpoint(self.instruction.address)
        self.ui.bp_btn.setStyleSheet('''
            background-color: #ffffff;
        ''')

    # change current state of brekpoint (place or remove)
    def breakpoint_clicked(self):
        if self.bp_is_enable:
            self.remove_breakpoint()
        else:
            self.place_breakpoint()

    