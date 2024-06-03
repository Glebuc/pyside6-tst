from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtGui import QPainter
import random
from datetime import datetime, timedelta


class TestChart(QChart):
    def __init__(self, test_name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Создание осей X и Y
        self.axis_x = QDateTimeAxis()
        self.axis_y = QValueAxis()

        # Настройка оси X
        self.axis_x.setFormat("dd.MM.yyyy")  # Установка формата даты на оси X
        self.axis_x.setTitleText("Дата")  # Установка заголовка для оси X
        self.addAxis(self.axis_x, Qt.AlignBottom)  # Добавление оси X на график

        # Настройка оси Y
        self.axis_y.setTitleText("Результат теста")  # Установка заголовка для оси Y
        self.addAxis(self.axis_y, Qt.AlignLeft)  # Добавление оси Y на график

        # Установка заголовка графика
        self.setTitle(f"Результат теста '{test_name}'")

        # Словарь для хранения серий по их именам
        self.series_dict = {}

    def add_series(self, name, data):
        series = QLineSeries(name=name)
        for date, value in data:
            series.append(date.toMSecsSinceEpoch(), value)

        # Добавление серии данных на график
        self.addSeries(series)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)

        # Сохранение серии в словарь
        self.series_dict[name] = series

    def toggle_series_visibility(self, name):
        """
        Переключает видимость серии данных с указанным именем.

        :param name: Имя серии данных.
        """
        if name in self.series_dict:
            series = self.series_dict[name]
            series.setVisible(not series.isVisible())

    def populate_chart_with_data(self, num_series=15):
        current_date = datetime.now()
        start_date = current_date.replace(day=1)

        # Генерация данных для каждой серии
        for i in range(num_series):
            data = []
            for day in range((current_date - start_date).days + 1):
                date = start_date + timedelta(days=day)
                value = random.randint(0, 100)
                data.append((QDateTime(date), value))

            self.add_series(f"Series {i + 1}", data)

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
