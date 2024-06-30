from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView
from PySide6.QtCharts import QChart, QLineSeries, QScatterSeries, QValueAxis, QDateTimeAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PySide6.QtGui import QPainter
from datetime import datetime, timedelta
import random
import sys

class BarChart(QChart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Создаем ось Y
        self.axis_y = QValueAxis()
        self.addAxis(self.axis_y, Qt.AlignLeft)  # Добавляем ось Y слева
        self.axis_y.setTitleText("Значение")

        # Создаем ось X
        self.axis_x = QBarCategoryAxis()
        self.addAxis(self.axis_x, Qt.AlignBottom)  # Добавляем ось X снизу
        self.axis_x.setTitleText("Вычислительные системы")

        # Устанавливаем заголовок графика
        self.setTitle("Максимальные результаты на различных ВВС теста 'HPL'")

        # Создаем серию столбцов
        self.bar_series = QBarSeries()

        # Добавляем столбцы в серию
        categories = ["Aramid Test Cluster 1", "Aramid Test Cluster 2", "Aramid Test Cluster 3"]
        values = [101, 192, 77]
        for category, value in zip(categories, values):
            bar_set = QBarSet(category)  # Создаем QBarSet с указанием категории
            bar_set.append(int(value))
            self.bar_series.append(bar_set)

        # Добавляем серию столбцов на график
        self.addSeries(self.bar_series)

        # Привязываем оси к серии
        self.bar_series.attachAxis(self.axis_x)
        self.bar_series.attachAxis(self.axis_y)

        # Устанавливаем диапазоны осей
        min_value = min(min(values), 0) if values else 0
        max_value = max(values) if values else 10
        self.axis_y.setRange(min_value * 1.1, max_value * 1.1)


class LineChart(QChart):
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
        self.populate_chart_with_data()

    def add_series(self, name, data):
        line_series = QLineSeries(name=name)
        scatter_series = QScatterSeries()
        scatter_series.setMarkerSize(10)  # Размер точек

        for date, value in data:
            line_series.append(date.toMSecsSinceEpoch(), value)
            scatter_series.append(date.toMSecsSinceEpoch(), value)

        # Добавление серии данных на график
        self.addSeries(line_series)
        self.addSeries(scatter_series)
        line_series.attachAxis(self.axis_x)
        line_series.attachAxis(self.axis_y)
        scatter_series.attachAxis(self.axis_x)
        scatter_series.attachAxis(self.axis_y)

        # Удаление маркерной серии из легенды
        markers = self.legend().markers(scatter_series)
        for marker in markers:
            marker.setVisible(False)

        # Сохранение серий в словарь
        self.series_dict[name] = (line_series, scatter_series)

    def toggle_series_visibility(self, name):
        """
        Переключает видимость серии данных с указанным именем.

        :param name: Имя серии данных.
        """
        if name in self.series_dict:
            line_series, scatter_series = self.series_dict[name]
            line_series.setVisible(not line_series.isVisible())
            scatter_series.setVisible(not scatter_series.isVisible())

    def populate_chart_with_data(self):
        current_date = datetime.now()
        start_date = current_date - timedelta(days=90)
        date_intervals = [start_date + timedelta(days=i * 7) for i in range(13)]  # 13 точек, по одной каждую неделю

        base_values = [100, 150, 200]
        series_names = ["Aramid Test Cluster 1", "Aramid Test Cluster 2", "Aramid Test Cluster 3"]
        deviation_percent = 0.01  # 3% deviation

        for series_index, base_value in enumerate(base_values):
            data = []
            for i, date in enumerate(date_intervals):
                if i == 6:  # Introduce a 20% dip at the 7th point
                    value = base_value * 0.8
                else:
                    value = base_value + random.uniform(-1, 1) * base_value * deviation_percent
                data.append((QDateTime(date), value))
            self.add_series(series_names[series_index], data)

        # Обновление диапазонов осей после добавления данных
        self.axis_x.setRange(date_intervals[0], date_intervals[-1])
        self.axis_y.setRange(70, 230)

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