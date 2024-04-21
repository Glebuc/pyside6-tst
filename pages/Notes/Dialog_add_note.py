from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton

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
        label = QLabel("Введите текст статьи (используйте Markdown):", self)
        layout.addWidget(label)
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)
        publish_button = QPushButton("Опубликовать", self)
        publish_button.clicked.connect(self.publish_article)
        layout.addWidget(publish_button)


    def get_selected_section(self):
        # Возвращает выбранный раздел
        return self.section_combo.currentText()

    def get_article_text(self):
        # Возвращает текст статьи из QTextEdit
        return self.text_edit.toPlainText()

    def publish_article(self):
        # Вызывается при нажатии кнопки "Опубликовать"
        section = self.get_selected_section()
        text = self.get_article_text()
        print(f"Опубликовать статью в разделе '{section}':\n{text}")

if __name__ == "__main__":
    app = QApplication([])

    # Пример списка разделов
    sections = ["Тесты", "Оптимизация тестов"]

    dialog = MyDialog(sections)
    dialog.exec()

    app.exec()
