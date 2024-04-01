from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QMessageBox

import psycopg2

from .Dialog_config_db import Ui_Dialog as DialogConfigDB
from .Dialog_keyword import Ui_Dialog as DialogKeyWord


class DialogConfigDB(QDialog, DialogConfigDB):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Конфигурация базы данных")
        self.check_connect_db_btn.clicked.connect(self.check_connection)

    def check_connection(self) -> None:
        """
            Проверяет соединение с базой данных, используя введенные пользователем параметры подключения.

            Функция получает значения хоста, имени базы данных, пароля, пользователя и порта из соответствующих
            полей QLineEdit. После этого она пытается установить соединение с базой данных PostgreSQL, используя
            полученные параметры. В случае успешного соединения выводит информационное сообщение об этом, а если
            соединение не удалось установить, выводит предупреждение с текстом ошибки.

            Returns:
                None
        """
        host = self.host_db_edit.text()
        dbname = self.name_db_edit.text()
        password = self.password_db_edit.text()
        user = self.user_db_edit.text()
        port = self.port_db_spin.value()

        try:
            connection = psycopg2.connect(
                host=host,
                dbname=dbname,
                user=user,
                password=password,
                port=port
            )
            connection.close()
            QMessageBox.information(self, "Уведомление", "Соединение установлено успешно!")
        except Exception as e:
            QMessageBox.warning(self, "Предупреждение", f"Ошибка при установке соединения: {str(e)}")






class DialogKey(QDialog, DialogKeyWord):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Горячие клавиши в приложение")