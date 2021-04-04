from UI.ui_traceWindow import Ui_TraceWindow

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget, QLabel
from PySide2.QtCore import QFile
from .custom_widgets import QInstruction, QStackFunction
from . import models

import debugger

import sys

class TraceWindow(QMainWindow):
    def __init__(self, file):
        super(TraceWindow, self).__init__()
        self.debugger = debugger.Debugger(file)
        self.ui = Ui_TraceWindow()
        self.ui.setupUi(self)
        self.ui.func_combo.addItems(self.debugger.get_function_names())

        # connect buttons to functions
        self.ui.func_combo.currentIndexChanged.connect(lambda: self.show_function(self.ui.func_combo.currentText()))
        self.ui.step_btn.clicked.connect(self.single_step)
        self.ui.cont_btn.clicked.connect(self.continue_execution)
        self.ui.step_out_btn.clicked.connect(self.step_out)
        self.ui.step_over_btn.clicked.connect(self.step_over)

        self.instructions_by_func = {}
        self.init_instructions()
        self.current_instruction = None
        self.functions = self.debugger.get_function_names()

        self.regs_model = models.RegistersModel(self.debugger.get_registers())
        self.ui.registers_view.setModel(self.regs_model)
        self.ui.registers_view.verticalHeader().hide()

        self.debugger.place_breakpoint(self.debugger.get_function('main').start_addr)
        self.debugger.continue_execution()
        self.debugger.clear_breakpoint(self.debugger.get_function('main').start_addr)
        self.update_display()

    # initialize instructions_by_func which maps function name to list of Qinstructions
    def init_instructions(self):
        for func in self.debugger.get_function_names():
            self.instructions_by_func[func] = [QInstruction(i, self.debugger, self) for i in self.debugger.get_function(func).instructions]

            instruction_list = QListWidget()
            # create a new list widget for that function
            for i in self.instructions_by_func[func]:
                # Create QListWidgetItem
                list_widget = QListWidgetItem()
                # Set size hint
                list_widget.setSizeHint(i.sizeHint())
                instruction_list.addItem(list_widget)
                instruction_list.setItemWidget(list_widget, i)

            self.ui.func_stack.addWidget(instruction_list)

    # update the call stack
    def update_call_stack(self):
        # clear the stack
        self.ui.calling_stack.clear()

        call_satck = self.debugger.call_stack()
        for func in call_satck:
            func_in_stack = QStackFunction(func.func, func.return_addr, self)

            # Create QListWidgetItem
            list_widget = QListWidgetItem()
            # Set size hint
            list_widget.setSizeHint(func_in_stack.sizeHint())
            self.ui.calling_stack.addItem(list_widget)
            self.ui.calling_stack.setItemWidget(list_widget, func_in_stack)
    
    # show a certain function on the window
    def show_function(self, func):
        self.ui.func_stack.setCurrentIndex(self.functions.index(func))

    # show a certain instruction on the window and highlight it
    def show_instruction(self, addr):
        if self.current_instruction is not None:
            self.current_instruction.unlight()

        # search the instruction widget
        current_function = self.debugger.find_function_with_address(addr)
        if current_function.name in self.functions:
            self.ui.func_combo.setCurrentIndex(self.ui.func_combo.findText(current_function.name))
        self.current_instruction = next((i for i in self.instructions_by_func[current_function.name] if i.instruction.address == addr), None)

        # highlight current instruction, only if it exists in the original file
        if self.current_instruction is not None:
            self.current_instruction.highlight()
    
    def single_step(self):
        self.debugger.single_step()
        self.update_display()
        
    def continue_execution(self):
        self.debugger.continue_execution()
        self.update_display()

    # update the display to match current program state
    def update_display(self):
        if self.current_instruction is not None:
            self.current_instruction.unlight()

        current_address = self.debugger.get_current_instruction()

        # find what is the current instruction
        current_function = self.debugger.find_function_with_address(current_address)
        if current_function.name in self.functions:
            self.ui.func_combo.setCurrentIndex(self.ui.func_combo.findText(current_function.name))
        self.current_instruction = next((i for i in self.instructions_by_func[current_function.name] if i.instruction.address == current_address), None)

        # highlight current instruction, only if it exists in the original file
        if self.current_instruction is not None:
            self.current_instruction.highlight()

        self.regs_model.set_regs(self.debugger.get_registers())
        self.update_call_stack()

    # step out of current function
    def step_out(self):
        self.debugger.step_out()
        self.update_display()

    # step out of current function
    def step_over(self):
        self.debugger.step_over()
        self.update_display()