from typing import List

from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from PySide6.QtUiTools import QUiLoader

from ui_modules import *
from ..BaseModel import BaseModel
from loger import Logger


class ChartModel(BaseModel):
    """Модель для страницы графиков и манипулирования табличными значением"""

    def __init__(self, table_name):
        super().__init__(table_name)
        self.log = Logger.get_instance()

    def check_database_connection(self) -> bool:
        """Проверяет наличие соединения с базой данных"""
        return QSqlDatabase.database().isValid()

    def get_test_parameters(self, test_name: str) -> None:
        """
        Получает параметры теста по его имени

        :param test_name: Имя теста для получения параметров
        :return: QSqlQuery с результатами запроса
        """
        if not self.check_database_connection():
            self.log.log_error("Нет соединения с БД")
            return None

        query = QSqlQuery()
        query.prepare("SELECT test_param FROM tests WHERE test_param IS NOT NULL AND test_name = :test_name GROUP BY test_param;")
        query.bindValue(":test_name", test_name)
        if not query.exec():
            self.log.log_error("Error executing query:"+ query.lastError().text())
            return None
        return query

    def get_data_for_chart(self, test_name, test_param):
        pass








