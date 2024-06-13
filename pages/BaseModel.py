from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from typing import Optional, Dict, Tuple, Union, List
import json

from loger import Logger

from SettingApp import AppSettings

setting = AppSettings.get_instance()
setting.get_setting("AppSettings/language")



class BaseModel(QSqlQueryModel):
    """Базовая модель, данная модель является родительской для всех других моделей.
     И занимается инициализированием окружения для БД"""
    TESTS_SQL = """
        CREATE TABLE IF NOT EXISTS tests (
        test_note text NULL,
        test_id serial4 NOT NULL,
        start_test timestamp NULL,
        time_test time NULL,
        test_param jsonb NULL,
        test_result text NULL,
        machine varchar NULL,
        version_os varchar NULL,
        CONSTRAINT tests_pk PRIMARY KEY (test_id)
    );
        """
    REPORT_SQL = """
        CREATE TABLE IF NOT EXISTS report (
    	id_report serial4 NOT NULL,
    	forming_report timestamp NOT NULL,
    	title_report varchar NOT NULL,
    	report bytea NOT NULL,
    	CONSTRAINT report_pk PRIMARY KEY (id_report)
    );
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
                FOR EACH ROW EXECUTE PROCEDURE add_new_params();
            END IF;
    END;
    $$
    """

    if setting.get_setting("AppSettings/language") == "Russian":
        ALL_RESULT_SQL = """
                SELECT 
                    t.test_name AS "Название", 
                    t.test_param AS "Параметры", 
                    t.time_test AS "Время выполнения", 
                    t.test_result AS Результат, 
                    t.start_test AS "Дата выполнения",
                    t.version_os AS "Версия ОС",
                    t.machine AS "Выч.система"
                FROM tests AS t
        """
    elif setting.get_setting("AppSettings/language") == "English":
        ALL_RESULT_SQL = """
                    SELECT 
                        t.test_name AS "Name test", 
                        t.test_param AS "Parametrs", 
                        t.time_test AS "Execution time", 
                        t.test_result AS "Result", 
                        t.start_test AS "Launch date",
                        t.version_os AS "Vesion OS",
                        t.machine AS "Machine"
                    FROM tests AS t
                """
    LIST_JSON_PARAM_SQL = """
        SELECT jsonb_object_keys(test_param) as keys
        FROM tests group by keys;
    """

    TRUNCATE_DATA_TEST = """
        TRUNCATE TABLE tests;
    """

    TRUNCATE_DATA_REPORT = """
        TRUNCATE TABLE report;
    """

    def __init__(self, table_name):
        super().__init__()
        self.log = Logger.get_instance()
        self.check_and_create_tables()
        self.load_tests_from_json_file("Test_info.json")
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
        init_db = {
            'tests': self.TESTS_SQL,
            'report': self.REPORT_SQL,
            'sections': self.SECTION_SQL,
            'notes': self.NOTE_SQL,
            'test_params': self.TEST_PARAMS,
            'add_new_params_function':self.FUNCTIONS_PARAMS,
            'add_new_params_trigger':self.TRIGGER_PARAMS
        }

        query = QSqlQuery()
        for table_name, sql_query in init_db.items():
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

    def load_tests_from_json_file(self, file_path: str):
        """
        Загружает данные из JSON-файла и записывает их в таблицы базы данных, если они еще не добавлены.

        :param file_path: Путь к JSON-файлу, содержащему информацию о HPC-тестах.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
            self.init_notes(json_data)
        except Exception as e:
            self.log.log_error(f"Ошибка при загрузке JSON-файла: {str(e)}")

    def init_notes(self, json_data: Dict):
        """
               Загружает данные из JSON и записывает их в таблицы базы данных, если они еще не добавлены.

               :param json_data: Данные JSON, содержащие информацию о HPC-тестах.
               """
        query = QSqlQuery()

        # Проверка существующих разделов
        existing_sections = set()
        if query.exec("SELECT name FROM sections"):
            while query.next():
                existing_sections.add(query.value(0))
        else:
            self.log.log_error("Ошибка выполнения запроса: " + query.lastError().text())
            return

        # Добавление раздела "HPC-тесты"
        if "HPC-тесты" not in existing_sections:
            query.prepare("INSERT INTO sections (name) VALUES (:name)")
            query.bindValue(":name", "HPC-тесты")
            if not query.exec():
                self.log.log_error("Ошибка выполнения запроса: " + query.lastError().text())
                return

        # Получение ID раздела "HPC-тесты"
        query.prepare("SELECT id FROM sections WHERE name = :name")
        query.bindValue(":name", "HPC-тесты")
        if not query.exec() or not query.next():
            self.log.log_error("Ошибка выполнения запроса: " + query.lastError().text())
            return
        section_id = query.value(0)

        # Проверка существующих заметок
        existing_notes = set()
        query.prepare("SELECT title FROM notes WHERE section_id = :section_id")
        query.bindValue(":section_id", section_id)
        if query.exec():
            while query.next():
                existing_notes.add(query.value(0))
        else:
            self.log.log_error("Ошибка выполнения запроса: " + query.lastError().text())
            return

        # Вставка новых заметок
        for title, content in json_data.get("HPC-тесты", {}).items():
            if title not in existing_notes:
                query.prepare("INSERT INTO notes (title, content, section_id) VALUES (:title, :content, :section_id)")
                query.bindValue(":title", title)
                query.bindValue(":content", content)
                query.bindValue(":section_id", section_id)
                if not query.exec():
                    self.log.log_error("Ошибка выполнения запроса: " + query.lastError().text())
                    return


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
