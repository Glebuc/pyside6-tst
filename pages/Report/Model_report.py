from datetime import datetime

from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QComboBox, QMessageBox


from ..BaseModel import BaseModel


class ReportModel(BaseModel):
    """Модель для страницы отчетов и манипулирования табличными значением"""
    def __init__(self, table_name):
        super().__init__(table_name)

    def insert_report(self, title_report: str, report_data: bytes) -> bool:
        """
        Вставляет новый отчет в таблицу report.

        :param title_report: Заголовок отчета.
        :param report_data: Данные отчета в виде байтов.
        :return: True, если вставка прошла успешно, False в противном случае.
        """
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO report (forming_report, title_report, report)
            VALUES (:forming_report, :title_report, :report)
        """)

        forming_report = datetime.now()
        query.bindValue(":forming_report", forming_report)
        query.bindValue(":title_report", title_report)
        query.bindValue(":report", report_data)

        if not query.exec():
            print(query.lastQuery())
            print(f"Ошибка при вставке данных: {query.lastError().text()}")
            return False

        return True

    def delete_report(self, id_report: int) -> bool:
        """
        Удаляет отчет из таблицы report по идентификатору.

        :param id_report: Идентификатор отчета.
        :return: True, если удаление прошло успешно, False в противном случае.
        """
        query = QSqlQuery()
        query.prepare("DELETE FROM report WHERE id_report = :id_report")
        query.bindValue(":id_report", id_report)

        if not query.exec():
            print(query.lastQuery())
            print(f"Ошибка при удалении данных: {query.lastError().text()}")
            return False

        return True

    def delete_all_report(self):
        query = QSqlQuery()
        query.prepare(self.TRUNCATE_DATA_REPORT)