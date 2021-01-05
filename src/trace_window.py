from UI.ui_traceWindow import Ui_TraceWindow

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from disas import Disassembler

class TraceWindow(QMainWindow):
    def __init__(self, file):
        super(TraceWindow, self).__init__()
        self.disassembler = Disassembler(file)
        self.ui = Ui_TraceWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(self.disassembler.get_functions())
        self.ui.comboBox.currentIndexChanged.connect(self.show_function)

    def show_function(self):
        code = self.disassembler.disassemble_func(self.ui.comboBox.currentText())
        self.ui.code_area.setText(code)
        