from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem

from .Model_notes import NoteModel
from ui_modules import Ui_MainWindow

class NoteView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print(self.ui.treeWidget)

