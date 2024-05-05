from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_modules import *
from PySide6.QtUiTools import QUiLoader

from ..BaseModel import BaseModel


class ResultModel(BaseModel):
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

    def apply_filter(self, table_view: QTableView,  test_data: str, user_data: str,
                     param_test: str, start_date: str, end_date:str) -> None:
        """
            Применяет фильтр к данным и обновляет модель представления таблицы.

            :arguments:
                table_view (QTableView): Представление таблицы, к которому будет применен фильтр.
                test_data (str): Выбранные тесты для фильтрации.
                user_data (str): Выбранные пользователи для фильтрации.
                param_test (str): Выбранные параметры тестов для фильтрации.
                start_date (str): Начальная дата для фильтрации по дате теста.
                end_date (str): Конечная дата для фильтрации по дате теста.

            :returns:
                None

            """
        filters = []
        if test_data != "Все тесты" and test_data != "All tests":
            filters.append(f"test_name = '{test_data}'")
        if user_data != "Все пользователи" and user_data != "All users":
            filters.append(f"user_name = '{user_data}'")
        if param_test:
            filters.append(f"test_param = '{param_test}'")
        if start_date and end_date:
            filters.append(f"start_test BETWEEN '{start_date}' AND '{end_date}'")
        where_clause = " AND ".join(filters)
        if where_clause:
            where_clause = "WHERE " + where_clause
        query = f""" SELECT t.test_name, t.test_param, t.time_test, t.test_result, t.start_test, u.user_name
                       FROM tests as t
                       INNER JOIN users as u ON t.id_user_fk = u.user_id {where_clause}"""
        self.setQuery(query)
        if self.rowCount() == 0:
            # Если строк нет, выводим предупреждение
            QMessageBox.warning(None, "Предупреждение", "Нет данных, удовлетворяющих условиям запроса.")
            self.setQuery(self.ALL_RESULT_SQL)
        else:
            # Если нет ни одного условия, выводим предупреждение
            QMessageBox.information(None, "Данные были изменены", "Данные в таблице  отфильтрованы")
        table_view.setModel(self)


    def filter_data(self, combo_box: QComboBox, table_view: QTableView) -> None:
        """
            Применяет фильтр к данным и обновляет модель представления таблицы на основе выбранной опции в QComboBox.

           :arguments:
                combo_box (QComboBox): Выпадающий список, содержащий опции фильтрации.
                table_view (QTableView): Представление таблицы, которое будет обновлено после применения фильтра.
            :returns:
                None
            """
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

