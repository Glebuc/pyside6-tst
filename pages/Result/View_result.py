from datetime import datetime

from PySide6.QtCore import Qt, QDateTime, QDate, QTime
from PySide6.QtWidgets import QDialog, QVBoxLayout, QMainWindow, QWidget, QTextEdit, QApplication, QTableView, QHeaderView, QApplication, QMessageBox

from pages.Result import Model_result


class CustomTableView(QTableView):
    """Класс для отображения таблицы на странице Result"""
    def __init__(self, parent=None):
        super(CustomTableView, self).__init__(parent)

        self.setSelectionMode(QTableView.SingleSelection)
        self.verticalHeader().setVisible(False)

        self.model_result = Model_result.ResultModel('tests')
        self.setModel(self.model_result)

        header = self.horizontalHeader()
        for i in range(self.model_result.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        self.doubleClicked.connect(self.show_full_content)

    def set_model(self, model):
        """
               Устанавливает модель данных для таблицы.

               :param model: Модель данных для установки.
               :type model: QAbstractItemModel
        """
        self.setModel()

    def show_full_content(self, index):
        """
               Отображает полное содержимое ячейки таблицы при двойном щелчке.

               :param index: Индекс ячейки, на которую был сделан двойной щелчок.
               :type index: QModelIndex
        """
        model = self.model()  # Получаем текущую модель данных из QTableView

        if index.isValid() and model:
            row = index.row()
            column = index.column()
            model_index = model.index(row, column)
            data = model.data(model_index, Qt.DisplayRole)

            if isinstance(data, QDateTime):
                data = data.toString("dd.MM.yyyy HH:mm")

            elif not isinstance(data, str):
                data = str(data)

            self.display_full_content_dialog(data)

    def display_full_content_dialog(self, content):
        """
               Отображает диалоговое окно предпросмотра данных с заданным содержимым.

               :param content: Содержимое данных для отображения в диалоговом окне.
               :type content: str
        """
        dialog = PreviewWindow(self, content)
        dialog.show()


class PreviewWindow(QMainWindow):
    """
        Класс для предпросмотра текстовых данных в диалоговом окне.
    """
    def __init__(self, parent=None, content=''):
        """
                Инициализация диалогового окна предпросмотра.

                :param parent: Родительское окно (по умолчанию None).
                :param content: Содержимое данных для отображения в окне.
                :type content: str
        """
        super(PreviewWindow, self).__init__(parent)
        self.setWindowTitle("Предпросмотр данных")
        self.resize(600, 400)

        layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        formatted_content = content.replace('\\n', '\n')
        text_edit.setPlainText(formatted_content)

        text_edit.setStyleSheet("QTextEdit { color: black; }")

        layout.addWidget(text_edit)