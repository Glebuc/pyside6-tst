from typing import List
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from PySide6.QtUiTools import QUiLoader

from ui_modules import *
from ..BaseModel import BaseModel
from loger import Logger


class NoteModel(BaseModel):
    """Модель для страницы заметок и манипулирования табличными значением"""

    def __init__(self, table_name):
        super().__init__(table_name)
        self.log = Logger.get_instance()
        self.get_data_from_database()

    def get_section_names(self):
        """Возвращает список названий разделов из таблицы 'sections'."""

        query = QSqlQuery("SELECT name FROM sections")
        section_names = []
        while query.next():
            section_names.append(query.value(0))
        return section_names

    def get_data_from_database(self):
        """
        Получает данные из базы данных и формирует словарь в формате {название_раздела: [название_статьи1, название_статьи2, ...]}.

        :return: Словарь данных
        :rtype: dict
        """
        data = {}
        # Получаем данные из таблицы sections
        sections_query = QSqlQuery("SELECT id, name FROM sections")
        while sections_query.next():
            section_id = sections_query.value(0)
            section_name = sections_query.value(1)
            data[section_name] = []

            # Получаем данные из таблицы notes для данного раздела
            notes_query = QSqlQuery()
            notes_query.prepare("SELECT title FROM notes WHERE section_id = :section_id")
            notes_query.bindValue(":section_id", section_id)
            if notes_query.exec():
                while notes_query.next():
                    title = notes_query.value(0)
                    data[section_name].append(title)
        return data

    def add_section(self, name: str) -> bool:
        """Добавляет новый раздел в таблицу 'sections'."""
        query = QSqlQuery()
        query.prepare("INSERT INTO sections (name) VALUES (:name)")
        query.bindValue(":name", name)
        if query.exec():
            return True
        else:
            self.log.log_error("Ошибка при выполнении запроса:"+ query.lastError().text())
            return False

    def get_section_id_by_name(self, section_name: str) -> int:
        """Получает идентификатор раздела по его имени."""
        query = QSqlQuery()
        query.prepare("SELECT id FROM sections WHERE name = :name")
        query.bindValue(":name", section_name)
        if query.exec() and query.next():
            return query.value(0)
        else:
            return None

    def add_note(self, title: str, content: str, section_name: str) -> bool:
        """
        Добавление новой заметки в таблицу 'notes'.

        :param title: Заголовок заметки.
        :type title: str
        :param content: Содержимое заметки.
        :type content: str
        :param section_name: Имя раздела, к которому привязана заметка.
        :type section_name: str
        :return: True, если заметка успешно добавлена, False в противном случае.
        :rtype: bool
        """
        # Получаем section_id по имени раздела
        section_id = self.get_section_id_by_name(section_name)

        if section_id is None:
            self.log.log_errorrint(f"Ошибка: Раздел {section_name} не найден.")
            return False

        query = QSqlQuery()
        query.prepare("INSERT INTO notes (title, content, section_id) VALUES (:title, :content, :section_id)")
        query.bindValue(":title", title)
        query.bindValue(":content", content)
        query.bindValue(":section_id", section_id)

        if query.exec():
            return True
        else:
            self.log.log_error("Ошибка при выполнении запроса:" + query.lastError().text())
            return False
