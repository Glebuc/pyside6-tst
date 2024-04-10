from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout
from PySide6.QtSql import QSqlQueryModel, QSqlQuery
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QMessageBox
from .ui_dialog_extension_search import Ui_Dialog as ExtensionSearch
from pages.BaseModel import BaseModel



class DialogExtensionSearch(QDialog, ExtensionSearch):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        model = BaseModel('tests')
        users = model.execute_sql(model.LIST_USER_SQL)
        tests = model.execute_sql(model.LIST_TEST_SQL)
        min_date = model.execute_sql(model.MIN_DATE_SQL)
        max_date = model.execute_sql(model.MAX_DATE_SQL)
        self.setWindowTitle("Расширенный поиск")
        self.test_comboBox.addItems(tests)
        self.user_comboBox.addItems(users)
        self.before_dateEdit.setDate(max_date[0].date())
        self.from_dateEdit.setDate(min_date[0].date())
        self.accept_btn.clicked.connect(self.accept)
        self.test_comboBox.activated.connect(self.update_test_params)

    def update_test_params(self):
        """
            Обновляет параметры тестов в combobox на основе выбранного теста.

            Если выбранный тест - "Все тесты", функция не выполняет никаких действий.

            :returns:
                None

            Note:
                После выполнения запроса, в случае возникновения ошибки,
                сообщение об ошибке выводится в стандартный вывод.

            """
        test_name = self.test_comboBox.currentText()
        if test_name == "Все тесты":
            return None
        self.parametrs_tests.clear()
        query = QSqlQuery()
        query.prepare("SELECT test_param FROM tests WHERE test_name=:test_name GROUP BY test_param")
        query.bindValue(":test_name", test_name)
        if query.exec():
            while query.next():
                test_param = query.value(0)
                self.parametrs_tests.addItem(test_param)
        else:
            error_text = query.lastError().text()
            QMessageBox("Ошибка запроса:", error_text)

    def get_filter_parameters(self):
        """
        Получает параметры для фильтрации.

        :returns:
            tuple: :
                - test_data (str): Выбранное значение из combobox с тестами.
                - user_data (str): Выбранное значение из combobox с пользователями.
                - param_test (str): Выбранное значение из combobox с параметрами тестов.
                - start_date (str): Начальная дата фильтрации в формате строки ISODate (гггг-мм-дд).
                - end_date (str): Конечная дата фильтрации в формате строки ISODate (гггг-мм-дд).
        """
        test_data = self.test_comboBox.currentText()
        user_data = self.user_comboBox.currentText()
        param_test = self.parametrs_tests.currentText()
        start_date = self.from_dateEdit.date().toString(Qt.ISODate)
        end_date = self.before_dateEdit.date().toString(Qt.ISODate)
        return test_data, user_data, param_test, start_date, end_date


