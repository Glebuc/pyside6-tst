from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem

from .Model_notes import NoteModel
from ui_modules import Ui_MainWindow

class NoteView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.note_model = NoteModel('sections')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.populate_tree_widget()

    def populate_tree_widget(self):
        section_names = self.note_model.get_section_names()
        self.ui.treeWidget.clear()
        for name in section_names:
            item = QTreeWidgetItem([name])
            self.ui.treeWidget.addTopLevelItem(item)