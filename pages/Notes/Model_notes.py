from typing import List
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel


from ..BaseModel import BaseModel
from loger import Logger
from typing import Dict


class NoteModel(BaseModel):
    """Модель для страницы заметок и манипулирования табличными значением"""

    def __init__(self, table_name):
        super().__init__(table_name)
        self.log = Logger.get_instance()
        self.get_data_from_database()

    def get_section_names(self):
        """
        Возвращает список названий разделов из таблицы 'sections'.

        :return: Список строк с названиями разделов.
        :rtype: list[str]
        """
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
        """
        Добавляет новый раздел в таблицу 'sections'.

        :argument name: Название раздела для добавления.
        :type name: str
        :return: True, если раздел успешно добавлен, False в противном случае.
        :rtype: bool
        """
        query = QSqlQuery()
        query.prepare("INSERT INTO sections (name) VALUES (:name)")
        query.bindValue(":name", name)
        if query.exec():
            return True
        else:
            self.log.log_error("Ошибка при выполнении запроса:" + query.lastError().text())
            return False

    def get_section_id_by_name(self, section_name: str) -> int:
        """
        Получает идентификатор раздела по его имени.

        :argument section_name: Имя раздела, для которого нужно получить идентификатор.
        :type section_name: str
        :return: Идентификатор раздела, если он найден, иначе None.
        :rtype: int or None
        """
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

        :argument title: Заголовок заметки.
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
            self.log.log_error(f"Ошибка: Раздел {section_name} не найден.")
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

    def get_article_data(self, article_title: str) -> Dict:
        """
            Получает данные о статье из базы данных по её заголовку.

            :argument:
                article_title (str): Заголовок статьи, для которой нужно получить данные.

            :returns:
                dict: Словарь с данными о статье, включая заголовок (title) и содержимое (content).
                      Если статья с указанным заголовком не найдена, возвращает пустой словарь.
                      Если произошла ошибка при выполнении запроса к базе данных, возвращает пустой словарь.

        """
        result = {}
        query = QSqlQuery()
        query.prepare("SELECT title, content FROM notes WHERE title = :title")
        query.bindValue(":title", article_title)
        if query.exec():
            if query.next():
                result['title'] = query.value(0)
                result['content'] = query.value(1)
            else:
                self.log.log_error("Статья с таким заголовком не найдена")
        else:
            self.log.log_error("Ошибка при выполнении запроса: "+ query.lastError().text())
        return result

    def update_article_data(self, old_title,  article_title: str, article_content: str) -> None:
        """
           Обновляет содержимое статьи в таблице 'notes'.

           :argument:
               article_title (str): Заголовок статьи, которую необходимо обновить.
               article_content (str): Новое содержимое статьи.

           :returns:
               None
           """
        query = QSqlQuery()
        query.prepare("UPDATE notes SET title = :title, content = :content WHERE title = :old_title")
        query.bindValue(":old_title", old_title)
        query.bindValue(":title", article_title)
        query.bindValue(":content", article_content)
        if query.exec():
            self.log.log_info("Статья успешно обновлена")
            return True
        else:
            self.log.log_error("Ошибка при выполнении запроса на обновление статьи: " + query.lastError().text())
            return False

    def update_topic_data(self, old_topic_title, topic_title: str) -> bool:
        """
        Обновляет название раздела в таблице 'sections'.

        :argument:
            topic_title (str): Новое название раздела.

        :returns:
            bool: True, если запрос выполнен успешно, иначе False.
        """
        query = QSqlQuery()
        query.prepare("UPDATE sections SET name = :name WHERE name = :old_title")
        query.bindValue(":name", topic_title)
        query.bindValue(":old_title", old_topic_title)
        if query.exec():
            self.log.log_info("Название раздела успешно обновлено")
            return True
        else:
            self.log.log_error("Ошибка при выполнении запроса на обновление раздела: " + query.lastError().text())
            return False
