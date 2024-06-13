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
        self.setModel()

    def show_full_content(self, index):
        model = self.model()  # Получаем текущую модель данных из QTableView

        if index.isValid() and model:
            row = index.row()
            column = index.column()
            model_index = model.index(row, column)
            data = model.data(model_index, Qt.DisplayRole)

            if isinstance(data, QDateTime):
                data = data.toString(Qt.ISODate)  # Или другой нужный вам формат

                # Конвертация данных в строку, если это необходимо
            elif not isinstance(data, str):
                data = str(data)

            self.display_full_content_dialog(data)

    def display_full_content_dialog(self, content):
        dialog = PreviewWindow(self, content)
        dialog.show()


class PreviewWindow(QMainWindow):
    def __init__(self, parent=None, content=''):
        super(PreviewWindow, self).__init__(parent)
        self.setWindowTitle("Предпросмотр данных")
        self.resize(600, 400)

        layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setPlainText(content)

        text_edit.setStyleSheet("QTextEdit { color: black; }")

        layout.addWidget(text_edit)