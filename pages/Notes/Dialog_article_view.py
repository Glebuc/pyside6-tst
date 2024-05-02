from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser
from PySide6.QtGui import QFont

class ArticleDialog(QDialog):
    def __init__(self, title, content):
        super().__init__()
        self.setWindowTitle(title)

        # Устанавливаем минимальный размер окна
        self.setMinimumSize(500, 500)

        layout = QVBoxLayout()
        self.text_browser = QTextBrowser()
        self.text_browser.setText(content)

        # Устанавливаем размер отображаемого текста
        font = QFont()
        font.setPointSize(14)
        self.text_browser.setFont(font)

        layout.addWidget(self.text_browser)

        self.setLayout(layout)

        self.show()
