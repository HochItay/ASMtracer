from UI.ui_traceWindow import Ui_TraceWindow

from PySide2.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide2.QtCore import QFile
from instruction_widget import QInstruction

import debugger

class TraceWindow(QMainWindow):
    def __init__(self, file):
        super(TraceWindow, self).__init__()
        self.debugger = debugger.Debugger(file)
        self.ui = Ui_TraceWindow()
        self.ui.setupUi(self)
        self.ui.func_combo.addItems(self.debugger.get_function_names())
        self.ui.func_combo.currentIndexChanged.connect(self.show_function)

    def show_function(self):
        code = self.debugger.get_function(self.ui.func_combo.currentText()).instructions
        self.ui.instruction_list.clear()
        for i in code:
            instruction = QInstruction(i)
            # Create QListWidgetItem
            list_widget = QListWidgetItem()
            # Set size hint
            list_widget.setSizeHint(instruction.sizeHint())
            self.ui.instruction_list.addItem(list_widget)
            self.ui.instruction_list.setItemWidget(list_widget, instruction)

    # update the display to match current program state
    def update_display(self):
        pass        