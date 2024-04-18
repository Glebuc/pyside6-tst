import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis
from PySide6.QtGui import QPainter, QMouseEvent
import random

from loger import Logger

class CustomChart(QChart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.log = Logger.get_instance()

        self.series = QLineSeries()
        self.addSeries(self.series)

        self.axis_x = QValueAxis()
        self.axis_x.setTickCount(10)
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)
        self.legend().hide()

    def save_chart_image(self, graphics_view, file_path):
        """
        Сохраняет график в виде изображения.

        Args:
            graphics_view (QGraphicsView): Объект QGraphicsView, в котором находится график.
            file_path (str): Путь к файлу, в который нужно сохранить изображение.

        Returns:
            bool: True, если сохранение прошло успешно, в противном случае False.
        """
        chart_view = graphics_view
        chart_view.resize(self.size().toSize())  # Размер QGraphicsView соответствует размеру графика
        image = chart_view.grab()

        # Проверяем, удалось ли сохранить изображение
        if image.save(file_path):
            self.log.log_info("График успешно сохранен в" + file_path)
            return True
        else:
            self.log.log_error("Не удалось сохранить график в "+ file_path)
            return False



    def scroll_up(self):
        """
            Прокручивает вид вверх на фиксированное расстояние.

            :return:
                None
        """
        self.scroll(0, -10)

    def scroll_down(self):
        """
            Прокручивает вид вниз на фиксированное расстояние.

            :return:
                None
        """
        self.scroll(0, 10)

    def scroll_left(self):
        """
           Прокручивает вид влево на фиксированное расстояние.

           :return:
               None
        """
        self.scroll(-10, 0)

    def scroll_right(self):
        """
            Прокручивает вид вправо на фиксированное расстояние.

            :return:
                None
        """
        self.scroll(10, 0)

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


    def update_chart(self):
        self.series.clear()
        for x in range(-10, 11):
            y = random.randint(0, 50)
            self.series.append(x, y)

        self.axis_x.setRange(-10, 11)
        self.axis_y.setRange(0, 50)



class ChartView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setMouseTracking(True)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QPainter.Antialiasing)

        self.pan = False
        self.last_pan_point = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.RightButton:
            self.pan = True
            self.last_pan_point = event.pos()

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.RightButton:
            self.pan = False
            self.last_pan_point = None

        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.pan:
            delta = event.pos() - self.last_pan_point
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
            self.last_pan_point = event.pos()

        super().mouseMoveEvent(event)