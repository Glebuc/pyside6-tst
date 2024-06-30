import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsSimpleTextItem
from PySide6.QtCharts import QChart
from PySide6.QtCharts import QScatterSeries, QChartView
from PySide6.QtGui import QPainter, QMouseEvent
from PySide6.QtCore import Qt, QPointF

class HoverPoint(QScatterSeries):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hover_text = QGraphicsSimpleTextItem(parent=self.chart())

    def set_hover_text(self, text):
        if self.points():
            self.hover_text.setText(text)
            self.hover_text.setPos(self.points()[0].x(), self.points()[0].y())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("График с точками")
        self.setGeometry(100, 100, 800, 600)

        chart = QChart()
        chart.setTitle("График с точками")


        series = HoverPoint()
        series.setName("Точки")
        series.setMarkerSize(10)  # Размер маркера точек
        series.setMarkerShape(QScatterSeries.MarkerShapeCircle)  # Форма маркера точек

        chart.addSeries(series)

        # Создаем оси
        chart.createDefaultAxes()

        # Создаем виджет для отображения графика
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chart_view)

        # Обработка событий мыши для отображения информации о точках
        self.chart_view = chart_view
        self.hover_text = series.hover_text
        self.chart_view.setMouseTracking(True)

        # Словарь для хранения дополнительной информации о точках
        self.point_data = {}

        # Добавляем точки на график с дополнительной информацией
        points = [(1, 1, "Точка 1"), (2, 4, "Точка 2"), (3, 9, "Точка 3"), (4, 16, "Точка 4"), (5, 25, "Точка 5")]
        for index, point in enumerate(points):
            series.append(point[0], point[1])
            self.point_data[index] = point[2]

    def mousePressEvent(self, event: QMouseEvent):
        pos = self.chart_view.mapToScene(event.pos())
        item = self.chart_view.chart().scene().itemAt(pos, self.chart_view.transform())
        if isinstance(item, QScatterSeries):
            index = item.points()[0].x()
            point_data = self.point_data.get(index)
            if point_data:
                self.hover_text.setText(point_data)
                self.hover_text.setPos(item.points()[0].x(), item.points()[0].y())
                self.hover_text.show()
        else:
            self.hover_text.hide()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        pos = self.chart_view.mapToScene(event.pos())
        item = self.chart_view.chart().scene().itemAt(pos, self.chart_view.transform())
        if isinstance(item, QScatterSeries):
            index = item.points()[0].x()
            point_data = self.point_data.get(index)
            if point_data:
                self.hover_text.setText(point_data)
                self.hover_text.setPos(item.points()[0].x(), item.points()[0].y())
                self.hover_text.show()
        else:
            self.hover_text.hide()
        super().mouseMoveEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())