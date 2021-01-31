from UI.ui_traceWindow import Ui_TraceWindow

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget
from PySide2.QtCore import QFile
from .instruction_widget import QInstruction

import debugger

class TraceWindow(QMainWindow):
    def __init__(self, file):
        super(TraceWindow, self).__init__()
        self.debugger = debugger.Debugger(file)
        self.ui = Ui_TraceWindow()
        self.ui.setupUi(self)
        self.ui.func_combo.addItems(self.debugger.get_function_names())
        self.ui.func_combo.currentIndexChanged.connect(lambda: self.show_function(self.ui.func_combo.currentText()))
        self.ui.pushButton.clicked.connect(self.single_step)

        self.instructions_by_func = {}
        self.init_instructions()
        self.current_instruction = None
        self.functions = self.debugger.get_function_names()

        self.debugger.place_breakpoint(self.debugger.get_function('main').start_addr)
        self.debugger.continue_execution()
        self.debugger.remove_breakpoint(self.debugger.get_function('main').start_addr)
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


    def show_function(self, func):
        self.ui.func_stack.setCurrentIndex(self.functions.index(func))

    def single_step(self):
        self.debugger.single_step()
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
