from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator
from PySide6.QtSql import QSqlDatabase
from database import db_params
from loger import Logger


log = Logger()

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName(db_params['host'])
        db.setDatabaseName(db_params['database'])
        db.setPort(db_params['port'])
        db.setUserName(db_params['user'])
        db.setPassword(db_params['password'])
        print(db.open())
        if not db.open():
            log.log_error(f"Ошибка установки соединения: {db.lastError().text()}")
            return
        else:
            log.log_info("Соединение с БД установлено")


        self.setup()

    def setup(self):
        self.set_translation()
        return self

    def set_translation(self):
        trans = QTranslator(parent=self)
        # 'translations/en.qm'
        ok = trans.load('')
        if ok:
            log.log_info("Английский перевод загружен")
        else:
            log.log_info("Русский перевод загружен")
        QApplication.installTranslator(trans)
