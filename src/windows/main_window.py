import sys
from UI.ui_mainwindow import Ui_MainWindow

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QStackedWidget
from windows.trace_window import TraceWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_file_btn.clicked.connect(self.choose_file)
        self.ui.run_btn.clicked.connect(self.run_exe)
        self.ui.exit_btn.clicked.connect(lambda: self.close())

    # open file dialog to choose a file
    def choose_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'open executable file', r'\\')
        self.ui.lineEdit.setText(file_name)

    
    # start the execution of the executable
    def run_exe(self):

        # check file is really ELF by reading the magic
        with open(self.ui.lineEdit.text(), 'rb') as f:
            magic = f.read(4)
            # ELF magic is '0x7f 0x45 0x4c 0x46'
            if magic != b'\x7f\x45\x4c\x46':
                self.ui.warning_lbl.setText('file format not supported')
                return

        self.window = TraceWindow(self.ui.lineEdit.text())
        self.window.show()
        self.close()

