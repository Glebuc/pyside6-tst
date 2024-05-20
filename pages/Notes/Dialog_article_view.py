from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser
from PySide6.QtGui import QFont

class ArticleDialog(QDialog):
    """Диалоговое окно для отображения статей"""
    def __init__(self, title, content):
        """
            Инициализация диалогового окна для редактирования статьи.

            :arguments:
                title (str): Заголовок статьи.
                content (str): Текст статьи.
        """
        super().__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(500, 500)
        layout = QVBoxLayout()
        self.text_browser = QTextBrowser()
        self.text_browser.setMarkdown(content)
        font = QFont()
        font.setPointSize(14)
        self.text_browser.setFont(font)
        layout.addWidget(self.text_browser)
        self.setLayout(layout)
        self.show()
