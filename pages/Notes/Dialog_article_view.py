from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QTextBrowser, QWidget
from PySide6.QtGui import QFont

class ArticleDialog(QMainWindow):
    """Главное окно для отображения статей"""
    def __init__(self, title, content):
        """
            Инициализация главного окна для редактирования статьи.

            :arguments:
                title (str): Заголовок статьи.
                content (str): Текст статьи.
        """
        super().__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(500, 500)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.text_browser = QTextBrowser()
        self.text_browser.setMarkdown(content)

        font = QFont()
        font.setPointSize(14)
        self.text_browser.setFont(font)

        layout.addWidget(self.text_browser)
        self.setCentralWidget(central_widget)