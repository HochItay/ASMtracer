import sys
from UI.ui_instructionWidget import Ui_instructionWidget

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QStackedWidget, QWidget, QPushButton, QLabel, QStyle, QStyleOptionButton
from PySide2.QtGui import QPainter, QPen, QBrush, QColor, QPixmap, QPaintEvent
from PySide2.QtCore import QRect, QSize

# custom button for breakpoint
class QBreakPointButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.is_enable = False

    # override paintEvent to draw red circle if needed
    def paintEvent(self, event):
        # if enabled, draw red circle
        if self.is_enable:
            painter = QPainter(self)
            painter.setPen(QPen(QBrush('#e51400'), 1))
            painter.setBrush(QBrush(QColor('#e51400')))
            painter.drawEllipse(25, 12, 10, 10)
            painter.end()

        # if mose is hovering over the button, draw brown circle
        else:
            option = QStyleOptionButton()
            option.initFrom(self)
            if option.state & QStyle.State_MouseOver:
                painter = QPainter(self)
                painter.setPen(QPen(QBrush('#6e1911'), 1))
                painter.setBrush(QBrush(QColor("#6e1911")))
                painter.drawEllipse(25, 12, 10, 10)
                painter.end()

# custom label with special hovel affects
class QHovelableLabel(QLabel):
    # get functions that describe what to do when mouse starts hovering and when mouse stops
    def __init__(self, enter_func, leave_func, parent=None):
        QLabel.__init__(self, parent)
        self.enter = enter_func
        self.leave = leave_func

    # override enterEvent
    def enterEvent(self, event):
        self.enter()

    # override leaveEvent
    def leaveEvent(self, event):
        self.leave()
        
# an instruction viewed in the list of instructions
class QInstruction(QWidget):
    def __init__(self, instruction, debugger, load_address, tooltip, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_instructionWidget()
        self.ui.setupUi(self)
        self.load_address = load_address
        self.relative_address = False

        self.instruction = instruction
        self.ui.description.setText(self.__instruction_to_str())
        self.__debugger = debugger

        self.parent = parent

        self.bp_btn = QBreakPointButton(self)
        self.bp_btn.setObjectName(u"bp_btn")
        self.bp_btn.setGeometry(QRect(0, 0, 50, 40))
        self.bp_btn.setMaximumSize(QSize(50, 40))
        self.bp_btn.setStyleSheet(u"")
        self.bp_btn.setFlat(False)


        # when hovering above the description label
        # if the instruction is jump command, mark the
        # instruction that we are about to jump to
        jmp_commands = ['jmp', 'je', 'jg', 'jl', 'jle', 'jge', 'ja', 'jb', 'jz']
        
        if self.instruction.mnemonic in jmp_commands:
            # change the description to QHovelableLabel
            self.ui.description.__class__ = QHovelableLabel

            addr = int(self.instruction.parameters, 16)
            self.ui.description.enter = lambda: self.parent.set_color_of_instruction(addr, 'blue')
            self.ui.description.leave = lambda: self.parent.set_color_of_instruction(addr, 'black')

        self.__bp_is_enable = False
        self.bp_btn.clicked.connect(self.breakpoint_clicked)

        # set tooltip to be explanation of the instruction
        if self.instruction.mnemonic in tooltip:
            self.ui.description.setToolTip(tooltip[self.instruction.mnemonic])

    def __instruction_to_str(self):
        if self.relative_address:
            try:
                par = hex(int(self.instruction.parameters, 16) - self.load_address)
            except:
                par = self.instruction.parameters

            try:
                note = hex(int(self.instruction.note, 16) - self.load_address)
            except:
                note = self.instruction.note

            if note:
                address =  hex(self.instruction.address - self.load_address) + ':'
                command = f'{self.instruction.mnemonic}\t{par} ({note})'
            else:
                address =  hex(self.instruction.address - self.load_address) + ':'
                command = f'{self.instruction.mnemonic}\t{par}'
        else:
            if self.instruction.note:
                address =  hex(self.instruction.address) + ':'
                command = f'{self.instruction.mnemonic}\t{self.instruction.parameters} ({self.instruction.note})'
            else:
                address =  hex(self.instruction.address) + ':'
                command = f'{self.instruction.mnemonic}\t{self.instruction.parameters}'

        # add spacing
        address_len = 24
        address += ' ' * (2 * (address_len - len(address)))
        return address + command

    # change the description color, get the color as a string
    def set_description_color(self, color):
        self.ui.description.setStyleSheet(f'''
            color: {color};
        ''')

    # set address mode
    def set_relative_mode(self, is_relative):
        self.relative_address = is_relative
        self.ui.description.setText(self.__instruction_to_str())

        
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

        self.bp_btn.is_enable = True
        self.bp_btn.update()

    # remove breakpoint from this instruction
    def remove_breakpoint(self):
        self.__bp_is_enable = False
        self.__debugger.clear_breakpoint(self.instruction.address)

        self.bp_btn.is_enable = False
        self.bp_btn.update()

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
"    border-width: 1px;"
"    padding: 6px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	font:  bold;\n"
"    border-width: 3px;\n"
"	background-color: #b3daff;\n"
"    }\n")
