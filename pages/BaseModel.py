from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_modules import *
from PySide6.QtUiTools import QUiLoader
from typing import Optional, Dict, Tuple, Union, List

from loger import Logger

from SettingApp import AppSettings

setting = AppSettings.get_instance()
setting.get_setting("AppSettings/language")



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
    	CONSTRAINT settings_fk FOREIGN KEY (user_id_fk) REFERENCES users(user_id));
    """

    SECTION_SQL = """
    CREATE TABLE IF NOT EXISTS sections (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """

    NOTE_SQL = """
     CREATE TABLE IF NOT EXISTS notes (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL UNIQUE,
        content TEXT NOT NULL,
        section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE
    )
    """

    TEST_PARAMS = """
    CREATE TABLE IF NOT EXISTS test_params (
        param_test varchar NOT NULL,
        param_description VARCHAR,
        CONSTRAINT test_params_pk PRIMARY KEY (param_test)
    );
    """

    FUNCTIONS_PARAMS = """
    CREATE OR REPLACE FUNCTION add_new_params()
    RETURNS TRIGGER AS $$
    BEGIN
        INSERT INTO test_params (param_test)
        SELECT DISTINCT key
        FROM jsonb_each_text(NEW.test_param)
        ON CONFLICT (param_test) DO NOTHING;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """

    TRIGGER_PARAMS = """
    DO
    $$
    BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM pg_trigger
                WHERE tgname = 'add_new_params_trigger' 
                AND tgrelid = 'tests'::regclass
            ) THEN
                CREATE TRIGGER add_new_params_trigger
                AFTER INSERT ON tests
                FOR EACH ROW EXECUTE FUNCTION add_new_params();
            END IF;
    END;
    $$
    """

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
    if setting.get_setting("AppSettings/language") == "Russian":
        ALL_RESULT_SQL = """
            SELECT 
                t.test_name AS Название, 
                t.test_param AS Параметры, 
                t.time_test AS "Время выполнения", 
                t.test_result AS Результат, 
                t.start_test AS "Дата выполнения", 
                u.user_name AS Пользователь
            FROM tests AS t
            INNER JOIN users AS u ON t.id_user_fk = u.user_id;
        """
    elif setting.get_setting("AppSettings/language") == "English":
        ALL_RESULT_SQL = """
                    SELECT 
                        t.test_name AS "Name test", 
                        t.test_param AS "Parametrs", 
                        t.time_test AS "Execution time", 
                        t.test_result AS "Result", 
                        t.start_test AS "Launch date", 
                        u.user_name AS "User"
                    FROM tests AS t
                    INNER JOIN users AS u ON t.id_user_fk = u.user_id;
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
            self.log.log_error("Ошибка выполнения запроса:"+ self.lastError().text())

    def check_and_create_tables(self):
        """
            Проверяет существование таблиц в базе данных и создает их, если необходимо.

            :return: True, если все таблицы успешно созданы или уже существуют, False в случае ошибки.
            :rtype: bool
        """
        existing_tables = self.get_existing_tables()
        if not existing_tables:
            return False

        # Создание таблиц при необходимости
        tables_to_create = {
            'users': self.USERS_SQL,
            'tests': self.TESTS_SQL,
            'report': self.REPORT_SQL,
            'settings': self.SETTING_SQL,
            'sections': self.SECTION_SQL,
            'notes': self.NOTE_SQL,
            'test_params': self.TEST_PARAMS,
            'add_new_params_function':self.FUNCTIONS_PARAMS,
            'add_new_params_trigger':self.TRIGGER_PARAMS
        }

        query = QSqlQuery()
        for table_name, sql_query in tables_to_create.items():
            if table_name not in existing_tables:
                if not query.exec(sql_query):
                    self.log.log_error("Ошибка выполнения запроса:"+ query.lastError().text())
                    return False
            elif table_name == 'add_new_params_function':
                if not query.exec(sql_query):
                    self.log.log_error("Ошибка выполнения запроса:" + query.lastError().text())
                    return False
        return True

    def get_existing_tables(self) -> Union[List[str], None]:
        """
            Получает список существующих таблиц в базе данных.

            :returns:
                list or None: Список имен существующих таблиц в базе данных или None в случае ошибки.

            description:
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
            self.log.log_error("Ошибка выполнения запроса:"+ query.lastError().text())
            return None
    def execute_sql(self, sql_query: str, params: Optional[Union[Tuple, Dict]] = None) -> List:
        """
        Выполняет SQL-запрос и возвращает список значений из результата запроса.

        :argument:
            sql_query (str): SQL-запрос для выполнения.
            params (tuple or dict, optional): Параметры запроса. По умолчанию None.

        :returns:
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
            self.log.log_error("Ошибка выполнения запроса: "+ query.lastError().text())
        return result
