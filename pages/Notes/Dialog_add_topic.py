from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtSql import QSqlQuery
from .Model_notes import NoteModel
from ui_modules import  Ui_MainWindow

class DialogAddTopic(QDialog):
    def __init__(self):
        super().__init__()
        self.note_model = NoteModel("sections")
        self.setWindowTitle("Добавление раздела")
        layout = QVBoxLayout(self)
        label = QLabel("Введите название раздела:", self)
        layout.addWidget(label)
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)
        button = QPushButton("Подтвердить", self)
        button.clicked.connect(self.add_section_to_database)
        layout.addWidget(button)

    def add_section_to_database(self):
        name = self.line_edit.text()
        if name.strip():
            if self.note_model.add_section(name):
                print("Раздел успешно добавлен в базу данных!")
                self.accept()
                return True
            else:
                print("Не удалось добавить раздел в базу данных.")
                return False
        else:
            QMessageBox.warning(self,"Предупреждение","Название раздела не указано.")

