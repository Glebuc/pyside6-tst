from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QVBoxLayout, QWidget, QHeaderView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, Slot
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
	test_param jsonb NULL,
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



class BaseModel(QSqlQueryModel):
    """Базовая модель, данная модель является родительской для всех других моделей"""
    def __init__(self, table_name):
        super().__init__()
        self.setQuery(ALL_RESULT_SQL)
        if self.lastError().isValid():
            print("Ошибка выполнения запроса:", self.lastError().text())