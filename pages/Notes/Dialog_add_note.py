from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton, QLineEdit
from .Model_notes import NoteModel

class DialogAddNote(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.setWindowTitle("Добавление статьи")
        layout = QVBoxLayout(self)
        select_label = QLabel("Выберите раздел:", self)
        layout.addWidget(select_label)
        self.section_combo = QComboBox(self)
        layout.addWidget(self.section_combo)
        label_title = QLabel("Введите заголовок статьи:")
        layout.addWidget(label_title)
        self.title_edit = QLineEdit()
        layout.addWidget(self.title_edit)
        self.section_combo.addItems(NoteModel.get_section_names(self))
        label = QLabel("Введите текст статьи:", self)
        layout.addWidget(label)
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)
        publish_button = QPushButton("Опубликовать", self)
        publish_button.clicked.connect(self.publish_article)
        layout.addWidget(publish_button)

    def get_selected_section(self) -> str:
        """
        Возвращает выбранный раздел из выпадающего списка.

        :return: Строка с выбранным разделом.
        """
        return self.section_combo.currentText()

    def get_article_text(self) -> str:
        """
        Возвращает текст статьи из текстового редактора.

        :return: Строка с текстом статьи.
        """
        return self.text_edit.toPlainText()

    def publish_article(self) -> None:
        """
        Публикует статью в выбранном разделе.

        Вызывается при нажатии кнопки "Опубликовать". Получает выбранный раздел и текст статьи,
        а затем записывает данные в БД.

        :return: None
        """
        section = self.get_selected_section()
        text = self.get_article_text()
        print(f"Опубликовать статью в разделе '{section}':\n{text}")

