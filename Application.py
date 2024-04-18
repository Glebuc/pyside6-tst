from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtSql import QSqlDatabase
from PySide6.QtCore import QTranslator, QLocale, QEvent, QObject
from database import db_params
from loger import Logger





class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.log = Logger.get_instance()
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(db_params['host'])
        db.setDatabaseName(db_params['database'])
        db.setPort(db_params['port'])
        db.setUserName(db_params['user'])
        db.setPassword(db_params['password'])
        if not db.open():
            self.log.log_error(f"Ошибка установки соединения: {db.lastError().text()}")
            return
        else:
            self.log.log_info("Соединение с БД установлено")
        self.translator = QTranslator(self)
        self.setup()


    def setup(self, lang=None):
        self.set_translation(lang)
        return self

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

