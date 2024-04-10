from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton

class MyDialog(QDialog):
    def __init__(self, sections):
        super().__init__()

        self.resize(500, 500)
        self.setWindowTitle("Добавление статьи")

        layout = QVBoxLayout(self)

        # QLabel для инструкции выбора раздела
        select_label = QLabel("Выберите раздел:", self)
        layout.addWidget(select_label)

        # ComboBox для выбора раздела
        self.section_combo = QComboBox(self)
        self.section_combo.addItems(sections)
        layout.addWidget(self.section_combo)

        # QLabel для инструкций
        label = QLabel("Введите текст статьи (используйте Markdown):", self)
        layout.addWidget(label)

        # QTextEdit для написания текста статьи
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        # Кнопки подтверждения
        publish_button = QPushButton("Опубликовать", self)
        publish_button.clicked.connect(self.publish_article)
        layout.addWidget(publish_button)

        save_draft_button = QPushButton("Добавить в черновик", self)
        save_draft_button.clicked.connect(self.save_draft)
        layout.addWidget(save_draft_button)

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

    def save_draft(self):
        # Вызывается при нажатии кнопки "Добавить в черновик"
        section = self.get_selected_section()
        text = self.get_article_text()
        print(f"Добавить статью в черновики раздела '{section}':\n{text}")

if __name__ == "__main__":
    app = QApplication([])

    # Пример списка разделов
    sections = ["Тесты", "Оптимизация тестов"]

    dialog = MyDialog(sections)
    dialog.exec()

    app.exec()
