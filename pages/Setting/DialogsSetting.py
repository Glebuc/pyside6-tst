from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QMessageBox

import psycopg2

from typing import Dict
from .Dialog_config_db import Ui_Dialog as DialogConfigDB
from .Dialog_keyword import Ui_Dialog as DialogKeyWord
from SettingApp import AppSettings

class DialogConfigDB(QDialog, DialogConfigDB):
    """Диалоговое окно для редактирования конфигурации БД"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Конфигурация базы данных")
        self.setting = AppSettings.get_instance()
        self.check_connect_db_btn.clicked.connect(self.check_connection)
        self.submit_db_param_btn.clicked.connect(self.save_config_db)

    def get_db_param(self) -> Dict:
        """
        Получает параметры для подключения к базе данных из пользовательского ввода и возвращает их в виде словаря.

        :returns:
            dict: Словарь параметров для подключения к базе данных, включая хост, имя базы данных, пароль пользователя,
                  имя пользователя и порт.
        """
        dict_config_db = {}
        dict_config_db['host'] = self.host_db_edit.text()
        dict_config_db['dbname'] = self.name_db_edit.text()
        dict_config_db['password'] = self.password_db_edit.text()
        dict_config_db['user'] = self.user_db_edit.text()
        dict_config_db['port'] = self.port_db_spin.value()
        if dict_config_db['host'] and dict_config_db['dbname'] and dict_config_db['user'] and dict_config_db['port']:
            return dict_config_db
        else:
            QMessageBox.warning(self, "Предупреждение", "Заполните все поля для настройки соединения с БД")

    def check_connection(self) -> None:
        """
            Проверяет соединение с базой данных, используя введенные пользователем параметры подключения.

            Функция получает значения хоста, имени базы данных, пароля, пользователя и порта из соответствующих
            полей QLineEdit. После этого она пытается установить соединение с базой данных PostgreSQL, используя
            полученные параметры. В случае успешного соединения выводит информационное сообщение об этом, а если
            соединение не удалось установить, выводит предупреждение с текстом ошибки.

            :returns:
                None
        """
        dict_db = self.get_db_param()
        if dict_db is None:
            return None

        try:
            connection = psycopg2.connect(
                host=dict_db['host'],
                dbname=dict_db['dbname'],
                user=dict_db['user'],
                password=dict_db['password'],
                port=dict_db['port']
            )
            connection.close()
            QMessageBox.information(self, "Уведомление", "Соединение установлено успешно!")
        except Exception as e:
            QMessageBox.warning(self, "Предупреждение", f"Ошибка при установке соединения: {str(e)}")

    def save_config_db(self) -> None:
        """
        Сохраняет параметры подключения к базе данных в настройках приложения.

        Получает параметры для подключения к базе данных с помощью функции get_db_param() и, если они присутствуют,
        передает их в метод set_setting_database() для сохранения в настройках приложения.

        :returns:
            None
        """
        db_params = self.get_db_param()
        if db_params:
            self.setting.set_setting_database(db_params)


class DialogKey(QDialog, DialogKeyWord):
    """Диалоговое окно для отображения таблицы с 'горячими' клавишами приложения"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Горячие клавиши в приложение")