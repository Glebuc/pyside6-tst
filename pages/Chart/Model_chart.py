from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_modules import *
from PySide6.QtUiTools import QUiLoader
from database import db_params
from ..BaseModel import BaseModel


class ChartModel(BaseModel):
    SELECT_ALL_PARAMETRS = "select test_param from tests t where test_param is not null and test_name = 'HPCG'  group by test_param;"

    """Модель для страницы результатов и манипулирования табличными значением"""
    def __init__(self, table_name):
        super().__init__(table_name)





