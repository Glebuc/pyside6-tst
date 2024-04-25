from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtSql import QSqlDatabase
from PySide6.QtCore import QTranslator, QLocale, QEvent, QObject
from loger import Logger
from SettingApp import AppSettings





class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.log = Logger.get_instance()
        self.app_settings = AppSettings.get_instance()
        self.app_connection_to_db()



        self.translator = QTranslator(self)
        self.setup()


    def setup(self, lang=None):
        self.set_translation(lang)
        return self


    def app_connection_to_db(self):
        db_params = {
            "host": self.app_settings.get_setting("database/host"),
            "port": self.app_settings.get_setting("database/port"),
            "database": self.app_settings.get_setting("database/database"),
            "user": self.app_settings.get_setting("database/user"),
            "password": self.app_settings.get_setting("database/password")
        }

        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(db_params['host'])
        db.setDatabaseName(db_params['database'])
        db.setPort(int(db_params['port']))
        db.setUserName(db_params['user'])
        db.setPassword(db_params['password'])

        if not db.open():
            self.log.log_error(f"Ошибка установки соединения: {db.lastError().text()}")
            return False
        else:
            self.log.log_info("Соединение с БД установлено")
            return True

    def set_translation(self, language=None):
        if not language:
            return
        self.remove_translation()
        ok = self.translator.load(language)

        if ok:
            QApplication.installTranslator(self.translator)
            self.log.log_info("Перевод успешно установлен")
        else:
            self.log.log_error("Ошибка при загрузке перевода")

    def remove_translation(self):
        QApplication.removeTranslator(self.translator)

