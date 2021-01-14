import sys
from UI.ui_mainwindow import Ui_MainWindow

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QStackedWidget
from trace_window import TraceWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_file_btn.clicked.connect(self.choose_file)
        self.ui.run_btn.clicked.connect(self.run_exe)

    # open file dialog to choose a file
    def choose_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'open executable file', r'\\', 'All Files (*.out *.elf)')
        self.ui.lineEdit.setText(file_name)
    
    # start the execution of the executable
    def run_exe(self):
        self.window = TraceWindow(self.ui.lineEdit.text())
        self.window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())