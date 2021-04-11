import sys
from UI.ui_instructionWidget import Ui_InstructionWidget

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QStackedWidget, QWidget, QPushButton, QLabel

# an instruction viewed in the list of instructions
class QInstruction(QWidget):
    def __init__(self, instruction, debugger, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_InstructionWidget()
        self.ui.setupUi(self)

        self.instruction = instruction
        self.ui.description.setText(str(self.instruction))
        self.__debugger = debugger

        self.__bp_is_enable = False
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
        self.__bp_is_enable = True
        self.__debugger.place_breakpoint(self.instruction.address)
        self.ui.bp_btn.setStyleSheet('''
            background-color: #cc3300;
        ''')

    # remove breakpoint from this instruction
    def remove_breakpoint(self):
        self.__bp_is_enable = False
        self.__debugger.clear_breakpoint(self.instruction.address)
        self.ui.bp_btn.setStyleSheet('''
            background-color: #ffffff;
        ''')

    # change current state of brekpoint (place or remove)
    def breakpoint_clicked(self):
        if self.__bp_is_enable:
            self.remove_breakpoint()
        else:
            self.place_breakpoint()

# a function viewed in the calling stack
class QStackFunction(QPushButton):
    def __init__(self, function, return_addr, window, parent=None):
        QPushButton.__init__(self, parent)
        self.__function_name = function.name
        self.__return_addr = return_addr
        self.__window = window

        self.setText(self.__function_name)
        self.setFlat(True)
        self.clicked.connect(lambda: self.__window.show_instruction(self.__return_addr))
        self.setStyleSheet(u"QPushButton {\n"
"	 background-color: #cce6ff;\n"
"    border-style: outset;\n"
"    padding: 6px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	font:  bold;\n"
"    border-width: 3px;\n"
"	background-color: #b3daff;\n"
"    }\n")
