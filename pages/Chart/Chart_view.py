from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtGui import QPainter, QMouseEvent
from PySide6.QtSql import QSqlQuery
import random
import json
import array

# from loger import Logger

class TestChart(QChart):
    def __init__(self, test_name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Создание серии данных для графика
        self.series = QLineSeries()

        # Создание осей X и Y
        self.axis_x = QDateTimeAxis()
        self.axis_y = QValueAxis()

        # Настройка оси X
        self.axis_x.setFormat("dd.MM.yyyy")  # Установка формата даты на оси X
        self.axis_x.setTitleText("Date")  # Установка заголовка для оси X
        self.addAxis(self.axis_x, Qt.AlignBottom)  # Добавление оси X на график
        self.series.attachAxis(self.axis_x)  # Привязка серии данных к оси X

        # Настройка оси Y
        self.axis_y.setTitleText("Test Result")  # Установка заголовка для оси Y
        self.addAxis(self.axis_y, Qt.AlignLeft)  # Добавление оси Y на график
        self.series.attachAxis(self.axis_y)  # Привязка серии данных к оси Y

        # Добавление серии данных на график
        self.addSeries(self.series)

        # Установка заголовка графика
        self.setTitle(f"Test Results for '{test_name}'")

        # Загрузка данных из базы данных и отображение на графике
        self.load_test_results(test_name)

    def load_test_results(self, test_name):
        query = QSqlQuery()
        query.prepare("SELECT start_test, test_result FROM tests WHERE test_name = ? ORDER BY start_test;")
        query.addBindValue(test_name)
        if not query.exec():
            print("Failed to execute query")
            return

        # Очищаем существующие данные серии перед загрузкой новых данных
        self.series.clear()

        while query.next():
            start_test = query.value(0)  # Не нужно вызывать toDateTime()
            # Получаем массив данных типа _int4 из PostgreSQL
            test_result_array = query.value(1)

            if isinstance(test_result_array, str):
                # Если данные представлены в виде строки, преобразуем их в список целых чисел
                test_result_list = [int(x) for x in test_result_array.strip('{}').split(',')]
            else:
                # Если данные уже являются массивом целых чисел, не требуется дополнительных преобразований
                test_result_list = test_result_array

            # Добавляем каждое значение из списка в серию данных
            for i, value in enumerate(test_result_list):
                self.series.append(start_test.toMSecsSinceEpoch() + i, value)


    def zoom_in(self):
        """
            Увеличивает масштаб видимости на 1.1 раза.

            :return:
                None
        """
        self.zoom(1.1)

    def zoom_out(self):
        """
            Уменьшает масштаб видимости на 0.9 раза.

            :return:
                None
        """
        self.zoom(0.9)

    def reset(self):
        """
            Сбрасывает вид в его начальное состояние.

            :return:
                None
        """
        self.zoomReset()
