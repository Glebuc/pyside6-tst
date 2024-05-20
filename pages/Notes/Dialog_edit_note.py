from PySide6.QtWidgets import (QApplication,
                               QDialog,
                               QVBoxLayout,
                               QLabel,
                               QLineEdit,
                               QTextEdit,
                               QPushButton,
                               QMessageBox,
                               QTabWidget)
from PySide6.QtGui import QFont

import sys

from .Model_notes import NoteModel

class EditNoteDialog(QDialog):
    """
        Диалоговое окно для редактирования статьи.
    """
    def __init__(self, title="", text=""):
        """
            Инициализация диалогового окна для редактирования статьи.

            :arguments:
                title (str, optional): Заголовок статьи. По умолчанию - пустая строка.
                text (str, optional): Текст статьи. По умолчанию - пустая строка.
        """
        super().__init__()
        self.note_model = NoteModel("sections")
        self.old_title = title
        self.setWindowTitle("Редактирование статьи")
        self.resize(500, 500)
        self.title_line_edit = QLineEdit(title)
        tab_widget = QTabWidget()
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(text)
        self.view_text_edit = QTextEdit()
        self.view_text_edit.setMarkdown(text)
        self.view_text_edit.setReadOnly(True)
        tab_widget.addTab(self.text_edit, "Редактирование")
        tab_widget.addTab(self.view_text_edit, "Предпросмотр")

        font = QFont()
        font.setPointSize(14)
        self.text_edit.setFont(font)
        self.title_line_edit.setFont(font)
        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.update_article)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Заголовок статьи:"))
        layout.addWidget(self.title_line_edit)
        layout.addWidget(QLabel("Текст статьи:"))
        layout.addWidget(tab_widget)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def update_article(self) -> None:
        """
            Сохраняет статью.

            Если заголовок или текст статьи пустые, выводит предупреждение через QMessageBox.
        """
        title = self.title_line_edit.text().strip()
        text = self.text_edit.toPlainText().strip()
        if not title or not text:
            QMessageBox.warning(self, "Внимание", "Поля заголовка и текста не должны быть пустыми.")
            return
        if self.note_model.update_article_data(self.old_title, title, text):
            self.accept()
            QMessageBox.information(self, "Обновлено", "Данная запись успешно обновлена")
        else:
            QMessageBox.error(self, "Внимание", "Ошибка обновления данных в БД.")

