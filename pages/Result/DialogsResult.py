from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
from .Model_result import users
from .ui_dialog_extension_search import Ui_Dialog as ExtensionSearch



class DialogExtensionSearch(QDialog, ExtensionSearch):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Расширенный поиск")
        self.N_comboBox.addItems(["1","4","7","9"])
        self.np_comboBox.addItems(["1","7","9"])
        self.test_comboBox.addItems(["HPC","HPCG","IMB"])
        self.accept_btn.clicked.connect(self.accept)

    def get_filter_parameters(self):
        test_data = self.test_comboBox.currentText()
        user_data = self.user_comboBox.currentText()
        np_data = self.np_comboBox.currentText()
        N_data = self.N_comboBox.currentText()
        start_date = self.from_dateEdit.date().toString(Qt.ISODate)
        end_date = self.before_dateEdit.date().toString(Qt.ISODate)
        return test_data, user_data, np_data, N_data, start_date, end_date

    def filter_query_model(self, model, test_data, user_data, np_data, N_data, start_date, end_date):
        sql_query = """SELECT t.test_name, t.test_param, t.time_test, t.test_result, t.start_test, u.user_name
    FROM tests as t
    INNER JOIN users as u ON t.id_user_fk = u.user_id WHERE """
        conditions = []
        if test_data:
            conditions.append(f"test_name = '{test_data}'")
        if user_data:
            conditions.append(f"user_name = '{user_data}'")
        if np_data:
            conditions.append(f"np_column = '{np_data}'")
        if N_data:
            conditions.append(f"N_column = '{N_data}'")
        if start_date and end_date:
            conditions.append(f"start_test BETWEEN '{start_date}' AND '{end_date}'")

        if conditions:
            sql_query += " AND ".join(conditions)
            model.setQuery(sql_query)
            if model.rowCount() == 0:
                QMessageBox.warning(None, "Предупреждение", "Нет данных, удовлетворяющих условиям запроса.")
                model.revert()
        else:
            QMessageBox.warning(None, "Предупреждение", "Не указано ни одного условия.")
