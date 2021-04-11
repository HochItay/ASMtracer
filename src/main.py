from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QStackedWidget
from windows.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())