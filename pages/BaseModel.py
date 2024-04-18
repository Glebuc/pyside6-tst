from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_modules import *
from PySide6.QtUiTools import QUiLoader
from database import db_params
from typing import Optional, Dict, Tuple, Union, List

from loger import Logger





class BaseModel(QSqlQueryModel):
    """Базовая модель, данная модель является родительской для всех других моделей"""
    USERS_SQL = """
        CREATE TABLE IF NOT EXISTS users (
    	user_id serial4 NOT NULL,
    	user_name varchar NOT NULL,
    	fio_user varchar NULL,
    	email_user varchar NULL,
    	password_user varchar NULL,
    	CONSTRAINT users_pk PRIMARY KEY (user_id)
    );
        """
    TESTS_SQL = """
        CREATE TABLE IF NOT EXISTS tests (
    	test_name varchar NOT NULL,
    	test_param jsonb NULL,
    	test_note text NULL,
    	test_id serial4 NOT NULL,
    	id_user_fk int4 NULL,
    	start_test timestamp NULL,
    	time_test time NULL,
    	test_result int4[],
    	CONSTRAINT tests_pk PRIMARY KEY (test_id),
    	CONSTRAINT tests_fk FOREIGN KEY (id_user_fk) REFERENCES users(user_id)
    );
        """
    REPORT_SQL = """
        CREATE TABLE IF NOT EXISTS report (
    	id_report serial4 NOT NULL,
    	user_id_fk int4 NULL,
    	forming_report timestamp NOT NULL,
    	title_report varchar NOT NULL,
    	CONSTRAINT report_pk PRIMARY KEY (id_report),
    	CONSTRAINT report_fk FOREIGN KEY (user_id_fk) REFERENCES users(user_id)
    );
        """
    SETTING_SQL = """
    CREATE TABLE IF NOT EXISTS settings (
    	setting_id serial4 NOT NULL,
    	theme varchar NOT NULL,
    	"language" varchar NOT NULL,
    	"scale" int4 NOT NULL DEFAULT 100,
    	user_id_fk int4 NOT NULL,
    	CONSTRAINT settings_pk PRIMARY KEY (setting_id),
    	CONSTRAINT settings_fk FOREIGN KEY (user_id_fk) REFERENCES users(user_id));"""

    LIST_USER_SQL = """
        SELECT user_name FROM users GROUP BY user_name;
    """
    LIST_TEST_SQL = """
        SELECT test_name FROM tests GROUP BY test_name;
    """
    MAX_DATE_SQL = """
        SELECT MAX(start_test) FROM tests;
    """
    MIN_DATE_SQL = """
        SELECT MIN(start_test) FROM tests;
    """
    ALL_RESULT_SQL = """
        SELECT t.test_name, t.test_param, t.time_test, t.test_result, t.start_test, u.user_name
        FROM tests as t
        INNER JOIN users as u ON t.id_user_fk=u.user_id;
    """
    LIST_JSON_PARAM_SQL = """
        SELECT jsonb_object_keys(test_param) as keys
        FROM tests group by keys;
    """

    def __init__(self, table_name):
        super().__init__()
        self.log = Logger.get_instance()
        self.check_and_create_tables()
        self.setQuery(self.ALL_RESULT_SQL)
        if self.lastError().isValid():
            self.log.log_error("Ошибка выполнения запроса:", self.lastError().text())

    def check_and_create_tables(self):

        existing_tables = self.get_existing_tables()
        if not existing_tables:
            return False

        # Создание таблиц при необходимости
        tables_to_create = {
            'users': self.USERS_SQL,
            'tests': self.TESTS_SQL,
            'report': self.REPORT_SQL,
            'settings': self.SETTING_SQL
        }

        query = QSqlQuery()
        for table_name, sql_query in tables_to_create.items():
            if table_name not in existing_tables:
                if not query.exec(sql_query):
                    self.log.log_error("Ошибка выполнения запроса:", query.lastError().text())
                    return False
        return True

    def get_existing_tables(self) -> Union[List[str], None]:
        """
            Получает список существующих таблиц в базе данных.

            Returns:
                list or None: Список имен существующих таблиц в базе данных или None в случае ошибки.

            Description:
                Этот метод выполняет запрос к информационной схеме PostgreSQL
                для получения списка таблиц, существующих в базе данных. Затем он возвращает список имен этих таблиц.
        """
        query = QSqlQuery()
        if query.exec("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"):
            existing_tables = []
            while query.next():
                existing_tables.append(query.value(0))
            return existing_tables
        else:
            self.log.log_error("Ошибка выполнения запроса:", query.lastError().text())
            return None
    def execute_sql(self, sql_query: str, params: Optional[Union[Tuple, Dict]] = None) -> List:
        """
        Выполняет SQL-запрос и возвращает список значений из результата запроса.

        Args:
            sql_query (str): SQL-запрос для выполнения.
            params (tuple or dict, optional): Параметры запроса. По умолчанию None.

        Returns:
            list: Список значений из результата запроса.
        """
        result = []
        query = self.query()
        if params is not None:
            query.prepare(sql_query)
            query.addBindValue(params)
        else:
            query.prepare(sql_query)

        if query.exec():
            while query.next():
                result.append(query.value(0))
        else:
            self.log.log_error("Ошибка выполнения запроса:", query.lastError().text())
        return result
