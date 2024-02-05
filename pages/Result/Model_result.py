from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView
from ui_modules import *
from PySide6.QtUiTools import QUiLoader
from database import db_params

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
	test_param varchar NULL,
	test_note text NULL,
	test_id serial4 NOT NULL,
	id_user_fk int4 NULL,
	start_test timestamp NULL,
	time_test time NULL,
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
	CONSTRAINT settings_fk FOREIGN KEY (user_id_fk) REFERENCES users(user_id)
);"""

LIST_TEST_SQL = """
    SELECT test_name FROM tests GROUP BY test_name;
"""
ALL_RESULT_SQL = """
    SELECT t.test_name, t.test_param, t.time_test, t.test_result, t.start_test, u.user_name
    FROM tests as t
    INNER JOIN users as u ON t.id_user_fk = u.user_id
"""


def connection_to_db(*args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            db = QSqlDatabase.addDatabase("QPSQL")
            db.setHostName(db_params['host'])
            db.setDatabaseName(db_params['database'])
            db.setPort(db_params['port'])
            db.setUserName(db_params['user'])
            db.setPassword(db_params['password'])
            db.open()
            if not db.open():
                print("Ошибка установки соединения:", db.lastError().text())
                return None
            result = func(*args, **kwargs)
            db.close()
            return result

        return wrapper

    return decorator


def init_db():
    db = QSqlDatabase.addDatabase('QPSQL')
    db.setHostName(db_params['host'])
    db.setDatabaseName(db_params['database'])
    db.setPort(db_params['port'])
    db.setUserName(db_params['user'])
    db.setPassword(db_params['password'])

    def check(func, *args):
        if not func(*args):
            raise ValueError(func.__self__.lastError())

    check(db.open)
    q = QSqlQuery()
    check(q.exec, USERS_SQL)
    check(q.exec, TESTS_SQL)
    check(q.exec, REPORT_SQL)
    check(q.exec, SETTING_SQL)
    db.close()


@connection_to_db()
def execute_postgresql_query(query_string):
    query = QSqlQuery()
    query.prepare(query_string)
    list_query_data = []
    if query.exec():
        while query.next():
            result = query.value(0)
            list_query_data.append(result)
    else:
        print("Ошибка выполнения запроса:", query.lastError().text())
        return None
    return list_query_data


result = execute_postgresql_query(LIST_TEST_SQL)
new_result = execute_postgresql_query(ALL_RESULT_SQL)


class DatabaseModel(QSqlQueryModel):
    def __init__(self, table_name):
        super().__init__()

        self.displayed_columns = []
        self.visible_columns = []

        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(db_params['host'])
        db.setDatabaseName(db_params['database'])
        db.setPort(db_params['port'])
        db.setUserName(db_params['user'])
        db.setPassword(db_params['password'])

        if not db.open():
            print("Ошибка установки соединения:", db.lastError().text())
            return

        self.setQuery(QSqlQuery(ALL_RESULT_SQL))
        if self.lastError().isValid():
            print("Ошибка выполнения запроса:", self.lastError().text())

    def filter_data(self, combo_box, table_view):
        selected_option = combo_box.currentText()
        query = QSqlQuery()

        if selected_option == "Все тесты":
            self.setQuery(QSqlQuery(ALL_RESULT_SQL))
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

    def close_connection(self):
        QSqlDatabase.database().close()
