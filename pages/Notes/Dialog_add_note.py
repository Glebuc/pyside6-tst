from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton, \
    QLineEdit, QMessageBox, QTabWidget, QWidget

from .Model_notes import NoteModel


class DialogAddNote(QMainWindow):
    def __init__(self, language=""):
        super().__init__()

        # Словарь меток на разных языках
        self.labels = {
            "Русский": {
                "window_title": "Добавление записи",
                "select_label_text": "Выберите раздел:",
                "label_title_text": "Введите заголовок статьи:",
                "label_text": "Введите текст статьи:",
                "tab_edit_text": "Редактирование",
                "tab_preview_text": "Предпросмотр",
                "publish_button_text": "Опубликовать",
                "warning_title": "Внимание",
                "warning_message": 'Для "Редактирование" или "Удаление" выделите статью или раздел',
                "info_title": "Информация",
                "info_message": "Статья успешно добавлена",
                "error_title": "Ошибка",
                "error_message": "Ошибка записи. Статья с таким заголовком уже существует",
                "warning_fill_fields": "Заполните все поля перед публикацией"
            },
            "English": {
                "window_title": "Add Note",
                "select_label_text": "Select section:",
                "label_title_text": "Enter article title:",
                "label_text": "Enter article text:",
                "tab_edit_text": "Editing",
                "tab_preview_text": "Preview",
                "publish_button_text": "Publish",
                "warning_title": "Warning",
                "warning_message": 'Please select an article or section for "Editing" or "Deleting"',
                "info_title": "Information",
                "info_message": "Article added successfully",
                "error_title": "Error",
                "error_message": "Writing error. An article with this title already exists",
                "warning_fill_fields": "Please fill in all fields before publishing"
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

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Создание и добавление метки выбора раздела
        select_label = QLabel(self.labels[self.language]["select_label_text"], self)
        layout.addWidget(select_label)

        # Создание и добавление выпадающего списка с разделами
        self.section_combo = QComboBox(self)
        layout.addWidget(self.section_combo)

        # Создание и добавление метки для заголовка статьи
        label_title = QLabel(self.labels[self.language]["label_title_text"], self)
        layout.addWidget(label_title)

        # Создание и добавление поля ввода заголовка
        self.title_edit = QLineEdit(self)
        layout.addWidget(self.title_edit)

        # Заполнение выпадающего списка названиями разделов
        self.section_combo.addItems(NoteModel.get_section_names(self))

        # Создание и добавление метки для текста статьи
        label = QLabel(self.labels[self.language]["label_text"], self)
        layout.addWidget(label)

        # Создание вкладок для редактирования и предпросмотра текста статьи
        tab_widget = QTabWidget()
        self.text_edit = QTextEdit(self)
        self.view_text_edit = QTextEdit(self)
        self.view_text_edit.setReadOnly(True)
        tab_widget.addTab(self.text_edit, self.labels[self.language]["tab_edit_text"])
        tab_widget.addTab(self.view_text_edit, self.labels[self.language]["tab_preview_text"])
        layout.addWidget(tab_widget)

        # Создание и добавление кнопки "Опубликовать"
        publish_button = QPushButton(self.labels[self.language]["publish_button_text"], self)
        publish_button.clicked.connect(self.publish_article)
        layout.addWidget(publish_button)

        # Подключение обработчика изменения текста
        self.text_edit.textChanged.connect(self.current_text_changed)

    def current_text_changed(self):
        """
           Обработчик события изменения текста в текстовом редакторе.

           Извлекает текст из текстового редактора `self.text_edit` и устанавливает его в виджет `self.view_text_edit`,
           который отображает текст в формате Markdown.

           :return: None
        """
        text = self.text_edit.toPlainText()
        self.view_text_edit.setMarkdown(text)

    def get_selected_section(self) -> str:
        """
        Возвращает выбранный раздел из выпадающего списка.

        :return: Строка с выбранным разделом.
        """
        return self.section_combo.currentText().strip()

    def get_article_text(self) -> str:
        """
        Возвращает текст статьи из текстового редактора.

        :return: Строка с текстом статьи.
        """
        text = self.text_edit.toPlainText().strip()
        if text:
            return text

    def get_article_title(self) -> str:
        """
        Возвращает заголовок статьи из текстового ввода пользователя.

        :return: Строка с текстом статьи.
        """
        title = self.title_edit.text().strip()
        if title:
            return title

    def publish_article(self) -> None:
        """
        Публикует статью в выбранном разделе.

        Вызывается при нажатии кнопки "Опубликовать". Получает выбранный раздел, заголовок и текст статьи,
        а затем записывает данные в БД.

        :return: None
        """
        section = self.get_selected_section()
        title = self.get_article_title()
        text = self.get_article_text()

        if section and title and text:
            if self.note_model.add_note(title, text, section):
                self.statusBar().showMessage(self.labels[self.language]["info_message"], 5000)
            else:
                QMessageBox.warning(
                    self,
                    self.labels[self.language]["error_title"],
                    self.labels[self.language]["error_message"]
                )
        else:
            QMessageBox.warning(
                self,
                self.labels[self.language]["warning_title"],
                self.labels[self.language]["warning_fill_fields"]
            )
