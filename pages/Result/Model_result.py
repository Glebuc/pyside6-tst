from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PySide6.QtWidgets import QTableView, QComboBox, QMessageBox
from PySide6.QtCore import Qt, QDateTime, QDate, QTime

from ..BaseModel import BaseModel


class ResultModel(BaseModel):
    """Модель для страницы результатов и манипулирования табличными значением"""

    LIST_TEST_SQL = """
          SELECT test_name FROM tests GROUP BY test_name;
      """
    LIST_MACHINE_SQL = """
              SELECT machine FROM tests GROUP BY machine;
          """
    LIST_OS_VERSION_SQL = """
                  SELECT version_os FROM tests GROUP BY version_os;
              """
    MAX_DATE_SQL = """
          SELECT MAX(start_test) FROM tests;
      """
    MIN_DATE_SQL = """
          SELECT MIN(start_test) FROM tests;
      """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ResultModel, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, table_name):
        if not self._initialized:
            super().__init__(table_name)  # Вызов __init__ базового класса
            self.displayed_columns = []
            self.visible_columns = []
            self._initialized = True

    def data(self, index, role=Qt.DisplayRole):
        """
          Возвращает данные, отображаемые в ячейке, соответствующие указанному индексу и роли.

          :param index: QModelIndex
              Индекс элемента в модели данных.

          :param role: int
              Роль данных в модели (по умолчанию Qt.DisplayRole).

          :return: QVariant
              Возвращает отформатированное представление данных в соответствии с ролью:
              - Если role == Qt.DisplayRole:
                  - QDateTime преобразуется в строку формата "dd.MM.yyyy HH:mm".
                  - QDate преобразуется в строку формата "dd.MM.yyyy".
                  - QTime преобразуется в строку формата "HH:mm".
              - В остальных случаях возвращает данные, полученные от базового класса.
          """
        if role == Qt.DisplayRole:
            value = super(ResultModel, self).data(index, role)
            if isinstance(value, QDateTime):
                return value.toString("dd.MM.yyyy HH:mm")
            elif isinstance(value, QDate):
                return value.toString("dd.MM.yyyy")
            elif isinstance(value, QTime):
                return value.toString("HH:mm")
        return super(ResultModel, self).data(index, role)

    def select_all_test_parametrs(self):
        """
        Запрос к БД для получения всех параметров из таблицы test_params
        """
        self.setQuery("""""")

    def select_all_data(self) -> None:
        """
        Выборка всех данных из таблицы 'tests' и обновляет модель результатами.

        :return: None
        """
        self.setQuery(self.ALL_RESULT_SQL)

    def delete_all_data(self) -> None:
        """
       Очистка таблицы 'tests' и обновляет модель результатами.

        :return: None
        """
        self.setQuery(self.TRUNCATE_DATA_TEST)

    def insert_data(self, test_name: str, start_test: str, test_param: str, test_result: str,
                    machine: str, version_os: str) -> bool:
        """
        Вставляет новую запись в таблицу 'tests'.

        :param test_name: Название теста.
        :param start_test: Дата и время начала теста.
        :param test_param: Параметры теста.
        :param test_result: Результат теста.
        :param machine: Выч. Система на которой проводился тест.
        :param version_os: Версия операционной системы.
        :return: True, если вставка прошла успешно, False в противном случае.
        """
        query = QSqlQuery()
        query.prepare("""
               INSERT INTO tests (test_name, start_test, test_param, test_result, machine, version_os)
               VALUES (:test_name, :start_test, :test_param, :test_result, :machine, :version_os)
           """)

        query.bindValue(":test_name", test_name)
        query.bindValue(":start_test", start_test)
        query.bindValue(":test_param", test_param)
        query.bindValue(":test_result", test_result)
        query.bindValue(":machine", machine)
        query.bindValue(":version_os", version_os)
        if not query.exec():
            print(query.lastQuery())
            print(f"Ошибка при вставке данных: {query.lastError().text()}")
            return False

        return True

    def apply_filter(self, table_view: QTableView, test_data: str, machine_data: str, version_os_data: str,
                     param_test: str, start_date: str, end_date: str) -> None:
        """
        Применяет фильтр к данным и обновляет модель представления таблицы.

        :arguments:
            table_view (QTableView): Представление таблицы, к которому будет применен фильтр.
            test_data (str): Выбранные тесты для фильтрации.
            machine_data (str): Выбранные машины для фильтрации.
            version_os_data (str): Выбранные версии ОС для фильтрации.
            param_test (str): Выбранные параметры тестов для фильтрации.
            start_date (str): Начальная дата для фильтрации по дате теста.
            end_date (str): Конечная дата для фильтрации по дате теста.

        :returns:
            None
        """
        filters = []

        if test_data and test_data not in ["Все тесты", "All tests"]:
            filters.append(f"test_name = '{test_data}'")
        if machine_data and machine_data not in ["Все машины", "All machines"]:
            filters.append(f"machine = '{machine_data}'")
        if version_os_data and version_os_data not in ["Все версии", "All OS versions"]:
            filters.append(f"version_os = '{version_os_data}'")
        if param_test:
            filters.append(f"test_param = '{param_test}'")
        if start_date and end_date:
            filters.append(f"start_test BETWEEN '{start_date}' AND '{end_date}'")

        where_clause = " AND ".join(filters)
        if where_clause:
            where_clause = "WHERE " + where_clause

        query = f"""
           SELECT  t.test_name AS Название, 
                            t.test_param AS Параметры, 
                            t.time_test AS "Время выполнения", 
                            t.test_result AS Результат, 
                            t.start_test AS "Дата выполнения",
                            t.version_os AS "Версия ОС",
                            t.machine AS "Выч. система"
           FROM tests AS t
           {where_clause}
           """

        self.setQuery(query)
        query_str = QSqlQuery(query)

        if self.rowCount() == 0:
            QMessageBox.warning(None, "Предупреждение", "Нет данных, удовлетворяющих условиям запроса.")
            self.last_query = query_str.lastQuery()
            print(self.last_query)
            self.setQuery(self.ALL_RESULT_SQL)
        else:
            QMessageBox.information(None, "Данные были изменены", "Данные в таблице отфильтрованы")

        table_view.setModel(self)


    def filter_data(self, combo_box: QComboBox, table_view: QTableView, language="Russian") -> None:
        """
            Применяет фильтр к данным и обновляет модель представления таблицы на основе выбранной опции в QComboBox.

           :arguments:
                combo_box (QComboBox): Выпадающий список, содержащий опции фильтрации.
                table_view (QTableView): Представление таблицы, которое будет обновлено после применения фильтра.
            :returns:
                None
            """
        selected_option = combo_box.currentText()
        query = QSqlQuery()
        if selected_option == "Все тесты" or selected_option == "All tests":
            self.setQuery(QSqlQuery(BaseModel.ALL_RESULT_SQL))
        else:
            if language in ["Русский", "Russian"]:
                query.prepare(f"""
                        SELECT
                            t.test_name AS Название, 
                            t.test_param AS Параметры, 
                            t.time_test AS "Время выполнения", 
                            t.test_result AS Результат, 
                            t.start_test AS "Дата выполнения",
                            t.version_os AS "Версия ОС",
                            t.machine AS "Выч. система"
                        FROM tests as t
                        WHERE t.test_name = :selected_option
                    """)
            else:
                query.prepare(f"""
                                   SELECT
                                        t.test_name AS "Name test", 
                                        t.test_param AS "Parametrs", 
                                        t.time_test AS "Execution time", 
                                        t.test_result AS "Result", 
                                        t.start_test AS "Launch date",
                                        t.version_os AS "Vesion OS",
                                        t.machine AS "Machine"
                                   FROM tests as t
                                   WHERE t.test_name = :selected_option
                               """)
            query.bindValue(":selected_option", selected_option)
            query.exec()
            self.setQuery(query)
        table_view.setModel(self)

