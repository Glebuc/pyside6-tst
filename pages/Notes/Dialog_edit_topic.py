from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QFont

import sys

from .Model_notes import NoteModel


class EditTopicDialog(QDialog):
    """Диалоговое окно для редактирования заголовка раздела"""

    def __init__(self, title="", language=""):
        """
            Инициализация диалогового окна для редактирования раздела.

            :arguments:
                title (str, optional): Заголовок раздела. По умолчанию - пустая строка.
        """
        super().__init__()

        # Словарь меток на разных языках
        self.labels = {
            "Русский": {
                "window_title": "Редактирование",
                "title_label_text": "Заголовок:",
                "save_button_text": "Сохранить",
                "warning_title": "Внимание",
                "warning_message": "Поле заголовка не должно быть пустым.",
                "info_title": "Обновлено",
                "info_message": "Данные заголовка успешно обновлены",
                "error_title": "Ошибка",
                "error_message": "Ошибка обновления данных в БД."
            },
            "English": {
                "window_title": "Edit",
                "title_label_text": "Title:",
                "save_button_text": "Save",
                "warning_title": "Warning",
                "warning_message": "The title field must not be empty.",
                "info_title": "Updated",
                "info_message": "Title data has been successfully updated",
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

        self.note_model = NoteModel("sections")
        self.old_title = title

        font = QFont()
        font.setPointSize(14)
        self.title_line_edit = QLineEdit(title)
        self.title_line_edit.setFont(font)
        self.save_button = QPushButton(self.labels[self.language]["save_button_text"])
        self.save_button.clicked.connect(self.save_article)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.labels[self.language]["title_label_text"]))
        layout.addWidget(self.title_line_edit)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def save_article(self):
        """
            Обновляет заголовок раздела.

            Если заголовок раздела пустой, выводит предупреждение через QMessageBox.
        """
        title = self.title_line_edit.text().strip()
        if not title:
            QMessageBox.warning(
                self,
                self.labels[self.language]["warning_title"],
                self.labels[self.language]["warning_message"]
            )
            return
        if self.note_model.update_topic_data(self.old_title, title):
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = EditTopicDialog("Default Title")
    dialog.exec()
    sys.exit(app.exec())