from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser
from PySide6.QtGui import QFont

class EditNoteDialog(QDialog):
    def __init__(self, title, content):
        super().__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(500, 500)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.show()