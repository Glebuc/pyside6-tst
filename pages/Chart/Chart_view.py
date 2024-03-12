import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis
from PySide6.QtGui import QPainter, QMouseEvent
import random

class CustomChart(QChart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.series = QLineSeries()
        self.addSeries(self.series)

        self.axis_x = QValueAxis()
        self.axis_x.setTickCount(11)
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)
        self.legend().hide()

    def scroll_up(self):
        self.scroll(0, -10)

    def scroll_down(self):
        self.scroll(0, 10)

    def scroll_left(self):
        self.scroll(-10, 0)

    def scroll_right(self):
        self.scroll(10, 0)

    def zoom_in(self):
        self.zoom(1.1)

    def zoom_out(self):
        self.zoom(0.9)

    def reset(self):
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