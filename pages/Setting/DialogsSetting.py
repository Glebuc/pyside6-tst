from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout

from .Dialog_config_db import Ui_Dialog as DialogConfigDB
from .Dialog_keyword import Ui_Dialog as DialogKeyWord


class DialogConfigDB(QDialog, DialogConfigDB):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Конфигурация базы данных")


class DialogKey(QDialog, DialogKeyWord):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Горячие клавиши в приложение")