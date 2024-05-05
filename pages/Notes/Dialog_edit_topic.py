from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QFont

import sys

from .Model_notes import NoteModel

class EditTopicDialog(QDialog):
    """Диалоговое окно для редактирования заголовка раздела"""
    def __init__(self, title=""):
        """
                  Инициализация диалогового окна для редактирования статьи.

                  :arguments:
                      title (str, optional): Заголовок статьи. По умолчанию - пустая строка.
              """
        super().__init__()
        self.note_model = NoteModel("sections")
        self.old_title = title
        self.setWindowTitle("Редактирование")
        font = QFont()
        font.setPointSize(14)
        self.title_line_edit = QLineEdit(title)
        self.title_line_edit.setFont(font)
        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_article)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Заголовок:"))
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
            QMessageBox.warning(self, "Внимание", "Поле заголовка не должны быть пустым.")
            return
        if self.note_model.update_topic_data(self.old_title, title):
            self.accept()
            QMessageBox.information(self, "Обновлено", "Данные заголовка успешно обновлены")
        else:
            QMessageBox.error(self, "Внимание", "Ошибка обновления данных БД.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = EditTopicDialog("Default Title")
    dialog.exec()
    sys.exit(app.exec())