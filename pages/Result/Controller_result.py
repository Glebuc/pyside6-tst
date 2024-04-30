from ui_modules import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)