from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtSql import QSqlQuery
from .Model_notes import NoteModel


class DialogAddTopic(QDialog):
    """
    Диалоговое окно для добавления нового раздела.

    Отображает диалоговое окно, в котором пользователь может ввести название нового раздела
    и при подтверждении сохраняет раздел в базу данных.
    """

    def __init__(self, language=""):
        """
        Инициализация диалогового окна добавления раздела.

        Создает элементы интерфейса (поле ввода, кнопку подтверждения) и настраивает обработчики событий.
        """
        super().__init__()

        # Словарь меток на разных языках
        self.labels = {
            "Русский": {
                "window_title": "Добавление раздела",
                "label_text": "Введите название раздела:",
                "button_text": "Подтвердить"
            },
            "English": {
                "window_title": "Add Section",
                "label_text": "Enter section name:",
                "button_text": "Confirm"
            }
        }

        if language.lower() in ["русский", "russian"]:
            self.language = "Русский"
        elif language.lower() in ["английский", "english"]:
            self.language = "English"
        else:
            self.language = "Русский" 

        self.setWindowTitle(self.labels[self.language]["window_title"])
        layout = QVBoxLayout(self)
        label = QLabel(self.labels[self.language]["label_text"], self)
        layout.addWidget(label)
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)
        button = QPushButton(self.labels[self.language]["button_text"], self)
        button.clicked.connect(self.add_section_to_database)
        layout.addWidget(button)
        self.note_model = NoteModel("sections")



    def add_section_to_database(self) -> bool:
        """
        Добавляет раздел в базу данных.

        При нажатии кнопки "Подтвердить" извлекает текст из поля ввода и добавляет его в базу данных.
        Если раздел успешно добавлен, диалоговое окно закрывается.

        :return:
            bool: Возвращает True, если раздел успешно добавлен, иначе False.
        """
        name = self.line_edit.text()
        if name.strip():
            if self.note_model.add_section(name):
                QMessageBox.information(self, "Информация","Раздел успешно добавлен в базу данных!")
                self.accept()
                return True
            else:
                QMessageBox.warning(self, "Информация","Не удалось добавить раздел в базу данных.\nТакой раздел уже существует")
                return False
        else:
            QMessageBox.warning(self, "Предупреждение", "Название раздела не указано.")
            return False
