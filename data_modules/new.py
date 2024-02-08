from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QDialog, QCheckBox, QPushButton, \
    QWidget
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6 import QtCore


class ColumnSelectionDialog(QDialog):
    def __init__(self, column_names, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Column Selection")
        self.column_names = column_names
        self.checkbox_dict = {}

        layout = QVBoxLayout(self)

        for column_name in column_names:
            checkbox = QCheckBox(column_name)
            checkbox.setChecked(True)  # Устанавливаем все флажки в состояние "включено" при инициализации
            self.checkbox_dict[column_name] = checkbox
            layout.addWidget(checkbox)

        # Добавляем кнопку "OK"
        button = QPushButton("OK")
        button.clicked.connect(self.accept)
        layout.addWidget(button)

    def get_selected_columns(self):
        selected_columns = {}
        for column_name, checkbox in self.checkbox_dict.items():
            selected_columns[column_name] = checkbox.isChecked()
        return selected_columns

    def restore_checkbox_states(self, checkbox_states):
        for column_name, checked in checkbox_states.items():
            self.checkbox_dict[column_name].setChecked(checked)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # Создаем базу данных SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("example.db")
        self.db.open()
        self.checkbox_dict = {}
        # Заполняем базу данных данными
        self.fill_database()

        # Добавляем кнопку для открытия диалогового окна выбора столбцов
        button = QPushButton("Select Columns")
        button.clicked.connect(self.open_column_selection_dialog)

        self.table_view = QTableView()

        # Создаем главное окно
        central_widget = QVBoxLayout()
        central_widget.addWidget(button)
        central_widget.addWidget(self.table_view)
        central_widget.setContentsMargins(5, 5, 5, 5)

        widget = QWidget()
        widget.setLayout(central_widget)
        self.setCentralWidget(widget)
        # Создаем диалоговое окно выбора столбцов

        # Создаем модель запроса и устанавливаем SQL-запрос
        self.model = QSqlQueryModel()
        self.model.setQuery("SELECT * FROM example_table", self.db)


        self.table_view.setModel(self.model)

        # Получаем список названий всех столбцов в модели
        record = self.model.record()
        column_names = [record.fieldName(i) for i in range(record.count())]

        # Создаем диалоговое окно выбора столбцов
        self.column_selection_dialog = ColumnSelectionDialog(column_names)

        # Создаем словарь для хранения состояний флажков
        self.checkbox_dict = {}

    def open_column_selection_dialog(self):
        # Получаем список названий столбцов, которые в данный момент отображаются в QTableView
        visible_columns = [self.model.headerData(i, QtCore.Qt.Horizontal) for i in range(self.model.columnCount())]

        # Открываем диалоговое окно
        if self.column_selection_dialog.exec() == QDialog.Accepted:
            selected_columns = self.column_selection_dialog.get_selected_columns()

            # Проходим по всем столбцам в модели
            for column_index in range(self.model.columnCount()):
                # Получаем название столбца из заголовка
                column_name = self.model.headerData(column_index, QtCore.Qt.Horizontal)

                # Если столбец в списке выбранных столбцов, отображаем его, иначе скрываем
                if selected_columns.get(column_name, False):
                    self.table_view.showColumn(column_index)
                else:
                    self.table_view.hideColumn(column_index)

    def update_table_columns(self, selected_columns):
        # Проходим по всем столбцам модели
        for column_index in range(self.model.columnCount()):
            # Получаем название столбца из заголовка
            column_name = self.model.headerData(column_index, QtCore.Qt.Horizontal)

            # Если столбец в списке выбранных столбцов, отображаем его, иначе скрываем
            if column_name in selected_columns:
                self.table_view.showColumn(column_index)
            else:
                self.table_view.hideColumn(column_index)


    def fill_database(self):
        query = self.db.exec()
        query.prepare("""CREATE TABLE IF NOT EXISTS example_table (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER,
                            city TEXT
                          )""")
        query.exec_()

        # Добавляем несколько строк данных
        data = [
            ("Alice", 25, "New York"),
            ("Bob", 30, "Los Angeles"),
            ("Charlie", 35, "Chicago"),
            ("David", 40, "Houston"),
            ("Eva", 45, "Philadelphia")
        ]

        for row in data:
            query.prepare("INSERT INTO example_table (name, age, city) VALUES (:name, :age, :city)")
            query.bindValue(":name", row[0])
            query.bindValue(":age", row[1])
            query.bindValue(":city", row[2])
            query.exec_()

        print("База данных успешно заполнена данными.")

    # def update_table_columns(self, selected_columns):
    #     # Получаем модель заголовка горизонтального столбца
    #     header_model = self.table_view.horizontalHeader().model()
    #
    #     # Проходим по всем столбцам
    #     for column_index in range(header_model.columnCount()):
    #         # Получаем название столбца из заголовка
    #         column_name = header_model.headerData(column_index, QtCore.Qt.Horizontal)
    #
    #         # Если столбец в списке выбранных столбцов, отображаем его, иначе скрываем
    #         if column_name in selected_columns and selected_columns[column_name]:
    #             self.table_view.showColumn(column_index)
    #         else:
    #             self.table_view.hideColumn(column_index)
    #
    # def open_column_selection_dialog(self):
    #     # Получаем список названий всех столбцов в модели
    #     record = self.model.record()
    #     all_column_names = [record.fieldName(i) for i in range(record.count())]
    #
    #     # Получаем список названий столбцов, которые в данный момент отображаются в QTableView
    #     visible_columns = [self.model.headerData(i, QtCore.Qt.Horizontal) for i in range(self.model.columnCount())]
    #
    #     # Устанавливаем флажки CheckBox в соответствии с отображаемыми столбцами
    #     for column_name, checkbox in self.column_selection_dialog.checkbox_dict.items():
    #         if column_name in visible_columns:
    #             checkbox.setChecked(True)
    #         else:
    #             checkbox.setChecked(False)
    #
    #     # Открываем диалоговое окно
    #     if self.column_selection_dialog.exec() == QDialog.Accepted:
    #         selected_columns = self.column_selection_dialog.get_selected_columns()
    #         self.update_table_columns(selected_columns)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
