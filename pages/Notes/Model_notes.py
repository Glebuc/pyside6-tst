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
