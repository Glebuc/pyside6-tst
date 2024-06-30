from datetime import datetime
from typing import List
from PySide6.QtCore import QDateTime
from datetime import datetime
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
import psycopg2



from ..BaseModel import BaseModel


class ReportModel(BaseModel):
    """Модель для страницы отчетов и манипулирования табличными значением"""
    def __init__(self, table_name):
        super().__init__(table_name)

    def insert_report(self, title_report: str, report: bytes) -> bool:
        """
        Вставляет новый отчет в таблицу report.

        :param title_report: Заголовок отчета.
        :param report: Данные отчета в виде байтов.
        :return: True, если вставка прошла успешно, False в противном случае.
        """
        connection = psycopg2.connect(database="postgres", user="postgres", password="admin",
                                      host="localhost", port="5433")
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO report (forming_report, title_report, report)
                VALUES (%s, %s, %s)
            """
            forming_report = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(query, (forming_report, title_report, report))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Ошибка при вставке данных: {error}")
            cursor.close()
            connection.close()
            return False

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
            print(f"Ошибка при удалении данных: {query.lastError().text()}")
            return False

        return True

    def select_all_report(self) -> List:
        """
               Выполняет SQL-запрос для выбора всех отчетов из базы данных и возвращает их в виде списка словарей.

               :return: List[dict]
                   Список словарей с информацией об отчетах. Каждый словарь содержит ключи:
                   - "title": str, заголовок отчета
                   - "date": str, дата формирования отчета в формате "yyyy-MM-dd"
        """
        query = QSqlQuery("SELECT title_report, forming_report FROM sections")
        reports = []
        while query.next():
            report = {
                "title": query.value(0),
                "date": query.value(1).toString("yyyy-MM-dd")  # Преобразование даты в строку
            }
            reports.append(report)
        return reports

    def delete_all_report(self):
        """
               Выполняет SQL-запрос для удаления всех отчетов из базы данных.

               :return: None
        """
        query = QSqlQuery()
        query.prepare(self.TRUNCATE_DATA_REPORT)