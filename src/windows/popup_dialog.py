import sys
from UI.ui_popupDialog import Ui_Dialog

from PySide2.QtWidgets import QApplication, QDialog, QFileDialog, QStackedWidget
from windows.trace_window import TraceWindow

class PopupDialog(QDialog):
    def __init__(self, text):
        super(PopupDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(text)
