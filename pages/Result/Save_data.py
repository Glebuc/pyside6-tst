from PySide6.QtWidgets import QTableView, QFileDialog
from PySide6.QtSql import QSqlQueryModel
from PySide6.QtCore import Qt, QDateTime, QTime
import csv
from loger import Logger

log = Logger.get_instance()

def save_data_to_csv(table_view: QTableView):
    """
        Сохраняет данные из QTableView в файл CSV.

        :argument table_view: QTableView, содержащая данные для сохранения.
        :type table_view: QTableView
    """
    model = table_view.model()

    if not isinstance(model, QSqlQueryModel):
        log.log_error("Модель для QTableView не является QSqlQueryModel.")
        return

    file_dialog = QFileDialog()
    file_dialog.setAcceptMode(QFileDialog.AcceptSave)
    file_dialog.setNameFilter("CSV files (*.csv)")

    if file_dialog.exec_():
        file_path = file_dialog.selectedFiles()[0]
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)

                # Write header
                headers = [model.record().fieldName(i) for i in range(model.record().count())]
                csv_writer.writerow(headers)

                for row in range(model.rowCount()):
                    data = [QDateTime.toString(model.record(row).value(i)) if isinstance(model.record(row).value(i),
                                                                                         QDateTime) else
                            QTime.toString(model.record(row).value(i)) if isinstance(model.record(row).value(i),
                                                                                     QTime) else model.record(
                                row).value(i)
                            for i in range(model.record().count())]
                    csv_writer.writerow(data)

            log.log_info(f"Данные сохранены в файл {file_path}")
        except Exception as e:
            log.log_error(f"Ошибка: {e}")