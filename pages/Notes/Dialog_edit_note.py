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

    def __init__(self, title="", text="", language=""):
        """
            Инициализация диалогового окна для редактирования статьи.

            :arguments:
                title (str, optional): Заголовок статьи. По умолчанию - пустая строка.
                text (str, optional): Текст статьи. По умолчанию - пустая строка.
        """
        super().__init__()

        # Словарь меток на разных языках
        self.labels = {
            "Русский": {
                "window_title": "Редактирование статьи",
                "title_label_text": "Заголовок статьи:",
                "text_label_text": "Текст статьи:",
                "tab_edit_text": "Редактирование",
                "tab_preview_text": "Предпросмотр",
                "save_button_text": "Сохранить",
                "warning_title": "Внимание",
                "warning_message": "Поля заголовка и текста не должны быть пустыми.",
                "info_title": "Обновлено",
                "info_message": "Данная запись успешно обновлена",
                "error_title": "Ошибка",
                "error_message": "Ошибка обновления данных в БД."
            },
            "English": {
                "window_title": "Edit Note",
                "title_label_text": "Article Title:",
                "text_label_text": "Article Text:",
                "tab_edit_text": "Editing",
                "tab_preview_text": "Preview",
                "save_button_text": "Save",
                "warning_title": "Warning",
                "warning_message": "Title and text fields must not be empty.",
                "info_title": "Updated",
                "info_message": "The record has been successfully updated",
                "error_title": "Error",
                "error_message": "Error updating data in the database."
            }
        }

        # Приведение language к стандартному виду
        if language.lower() in ["русский", "russian"]:
            self.language = "Русский"
        elif language.lower() in ["английский", "english"]:
            self.language = "English"
        else:
            self.language = "Русский"  # Язык по умолчанию

        # Установка заголовка окна
        self.setWindowTitle(self.labels[self.language]["window_title"])
        self.resize(500, 500)

        self.note_model = NoteModel("sections")
        self.old_title = title

        self.title_line_edit = QLineEdit(title)
        tab_widget = QTabWidget()
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(text)
        self.view_text_edit = QTextEdit()
        self.view_text_edit.setMarkdown(text)
        self.view_text_edit.setReadOnly(True)
        tab_widget.addTab(self.text_edit, self.labels[self.language]["tab_edit_text"])
        tab_widget.addTab(self.view_text_edit, self.labels[self.language]["tab_preview_text"])

        font = QFont()
        font.setPointSize(14)
        self.text_edit.setFont(font)
        self.title_line_edit.setFont(font)
        self.save_button = QPushButton(self.labels[self.language]["save_button_text"])
        self.save_button.clicked.connect(self.update_article)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.labels[self.language]["title_label_text"]))
        layout.addWidget(self.title_line_edit)
        layout.addWidget(QLabel(self.labels[self.language]["text_label_text"]))
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
            QMessageBox.warning(
                self,
                self.labels[self.language]["warning_title"],
                self.labels[self.language]["warning_message"]
            )
            return
        if self.note_model.update_article_data(self.old_title, title, text):
            self.accept()
            QMessageBox.information(
                self,
                self.labels[self.language]["info_title"],
                self.labels[self.language]["info_message"]
            )
        else:
            QMessageBox.warning(
                self,
                self.labels[self.language]["error_title"],
                self.labels[self.language]["error_message"]
            )

