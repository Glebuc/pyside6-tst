from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout

from .ui_dialog_extension_search import Ui_Dialog as DialogExtensionSearch



class DialogExtensionSearch(QDialog, DialogExtensionSearch):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Расширенный поиск")