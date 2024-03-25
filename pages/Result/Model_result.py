from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_modules import *
from PySide6.QtUiTools import QUiLoader
from database import db_params
from ..BaseModel import BaseModel


class DatabaseModel(BaseModel):
    """Модель для страницы результатов и манипулирования табличными значением"""
    def __init__(self, table_name):
        super().__init__(table_name)

        self.displayed_columns = []
        self.visible_columns = []

        # index_test_name = self.record().indexOf("test_name")
        # index_test_param = self.record().indexOf("test_param")
        # index_test_note = self.record().indexOf("test_note")
        # index_test_id = self.record().indexOf("test_id")
        # index_start_test = self.record().indexOf("start_test")
        # index_time_test = self.record().indexOf("time_test")
        # index_user_name = self.record().indexOf("user_name")
        # index_test_result = self.record().indexOf("test_result")
        #
        # # Используем индексы полей для установки новых заголовков столбцов
        # self.setHeaderData(index_test_name, Qt.Horizontal, self.tr("Название теста"))
        # self.setHeaderData(index_test_param, Qt.Horizontal, self.tr("Параметры теста"))
        # self.setHeaderData(index_test_note, Qt.Horizontal, self.tr("Заметка"))
        # self.setHeaderData(index_test_id, Qt.Horizontal, self.tr("ID Теста"))
        # self.setHeaderData(index_start_test, Qt.Horizontal, self.tr("Дата выполнения"))
        # self.setHeaderData(index_time_test, Qt.Horizontal, self.tr("Время выполнения"))
        # self.setHeaderData(index_user_name, Qt.Horizontal, self.tr("Пользователь"))
        # self.setHeaderData(index_test_result, Qt.Horizontal, self.tr("Результат"))

    def filter_data(self, combo_box: QComboBox, table_view: QTableView) -> None:
        selected_option = combo_box.currentText()
        query = QSqlQuery()
        if selected_option == "Все тесты":
            self.setQuery(QSqlQuery(BaseModel.ALL_RESULT_SQL))
        else:
            query.prepare(f"""
                SELECT t.test_name, t.test_param, t.time_test, t.test_result, t.start_test, u.user_name
                FROM tests as t
                INNER JOIN users as u ON t.id_user_fk = u.user_id
                WHERE t.test_name = :selected_option
            """)
            query.bindValue(":selected_option", selected_option)
            query.exec_()
            self.setQuery(query)
        table_view.setModel(self)

