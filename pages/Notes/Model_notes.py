from typing import List

from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from PySide6.QtUiTools import QUiLoader

from ui_modules import *
from database import db_params
from ..BaseModel import BaseModel


class NoteModel(BaseModel):
    """Модель для страницы заметок и манипулирования табличными значением"""

    def __init__(self, table_name):
        super().__init__(table_name)

    def get_section_names(self):
        """Возвращает список названий разделов из таблицы 'sections'."""

        query = QSqlQuery("SELECT name FROM sections")
        section_names = []
        while query.next():
            section_names.append(query.value(0))
        return section_names


    def add_section(self, name: str) -> bool:
        """Добавляет новый раздел в таблицу 'sections'."""
        query = QSqlQuery()
        query.prepare("INSERT INTO sections (name) VALUES (:name)")
        query.bindValue(":name", name)
        if query.exec():
            return True
        else:
            print("Ошибка при выполнении запроса:", query.lastError().text())
            return False