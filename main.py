# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *
#from PySide6.QtCharts import *
#
# from . resources_rc import *


import sys
import os
import platform

from PySide6.QtWidgets import QDialog, QFormLayout, QCheckBox, QVBoxLayout, QPushButton, \
    QTableView,QMainWindow, QWidget, QHeaderView, QMessageBox, QGraphicsScene
from PySide6.QtGui import QTransform
from PySide6 import QtCore
from PySide6.QtCore import Qt

import doctest

from datetime import datetime
from loger import Logger
from Application import Application
from ui_modules import *
from widgets import *
from pages import BaseModel, Model_result, Save_data, View_result, Dialog_change_view, DialogsSetting, DialogsResult,\
                            Chart_view



os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.log = Logger()


        Settings.ENABLE_CUSTOM_TITLE_BAR = False


        title = "Aramid TsT Graph"
        self.setWindowTitle(title)

        self.tableView = View_result.CustomTableView()
        widgets.verticalLayout_20.replaceWidget(widgets.resultView, self.tableView)
        self.model = Model_result.DatabaseModel('tests')

        widgets.btn_change_view.clicked.connect(self.open_column_selection_dialog)

        self.scene = QGraphicsScene()
        self.view = Chart_view.ChartView(self.scene)
        self.chart = Chart_view.CustomChart()
        self.chart.update_chart()
        self.scene.addItem(self.chart)
        widgets.up_chart_btn.clicked.connect(self.chart.scroll_up)
        widgets.down_chart_btn.clicked.connect(self.chart.scroll_down)
        widgets.left_chart_btn.clicked.connect(self.chart.scroll_left)
        widgets.right_chart_btn.clicked.connect(self.chart.scroll_right)
        widgets.zoom_in_chart_btn.clicked.connect(self.chart.zoom_in)
        widgets.zoom_out_chart_btn.clicked.connect(self.chart.zoom_out)
        widgets.reset_chart_btn.clicked.connect(self.chart.reset)


        widgets.graphicsView.setChart(self.chart)

        widgets.list_test_result.addItem("Все тесты")
        for i in self.model.execute_sql(BaseModel.LIST_TEST_SQL):
            widgets.list_test_result.addItem(i)
            widgets.list_test_chart.addItem(i)

        widgets.list_test_result.currentIndexChanged.connect(
            lambda: self.model.filter_data(combo_box=widgets.list_test_result, table_view=self.tableView))

        widgets.btn_save_view.clicked.connect(lambda: Save_data.save_data_to_csv(self.tableView))
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        UIFunctions.uiDefinitions(self)

        widgets.resultView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



        widgets.btn_report.clicked.connect(self.button_click)
        widgets.btn_bar.clicked.connect(self.button_click)
        widgets.btn_result.clicked.connect(self.button_click)

        widgets.btn_config_DB.clicked.connect(self.open_dialog_config_db)
        widgets.btn_hot_keys.clicked.connect(self.open_dialog_keyword)
        widgets.btn_extension_search.clicked.connect(self.open_dialog_extension_search)


        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        self.show()


        useCustomTheme = True
        themeFile_light = "themes\\theme_light.qss"
        themeFile_dark = "themes\\theme_dark.qss"
        if useCustomTheme:
            UIFunctions.theme(self, themeFile_light, True)
            AppFunctions.setThemeHack(self)
            self.log.log_info("Установлена светлая тема".strip())
        else:
            UIFunctions.theme(self, themeFile_dark, True)
            AppFunctions.setThemeHack(self)
            self.log.log_info("Установлена темная тема")
        widgets.stackedWidget.setCurrentWidget(widgets.report_page)

        record = self.model.record()
        column_names = [record.fieldName(i) for i in range(record.count())]

        self.column_selection_dialog = Dialog_change_view.ColumnSelectionDialog(column_names)

        # словарь для хранения состояний флажков
        self.checkbox_dict = {}


    def open_column_selection_dialog(self):
        """
           Открывает диалоговое окно для выбора отображаемых столбцов в таблице.

           Функция извлекает список всех видимых столбцов из модели данных таблицы и отображает диалоговое окно выбора столбцов.
           После нажатия на кнопку "Подтвердить" диалогового окна функция проверяет, какие столбцы были выбраны пользователем, и соответственно
           скрывает или отображает столбцы в таблице.

           Returns:
               None
           """
        visible_columns = [self.model.headerData(i, QtCore.Qt.Horizontal) for i in range(self.model.columnCount())]
        if self.column_selection_dialog.exec() == QDialog.Accepted:
            selected_columns = self.column_selection_dialog.get_selected_columns()
            for column_index in range(self.model.columnCount()):
                column_name = self.model.headerData(column_index, QtCore.Qt.Horizontal)
                if selected_columns.get(column_name, False):
                    self.tableView.showColumn(column_index)
                else:
                    self.tableView.hideColumn(column_index)

    def open_dialog_config_db(self) -> None:
        """
            Открывает диалоговое окно для настройки подключения к базе данных.

            Returns:
                None
        """
        dialog = DialogsSetting.DialogConfigDB(self)
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно с кофигом БД")
        dialog.exec()


    def open_dialog_keyword(self) -> None:
        """
            Открывает диалоговое окно для отображения горячих клавиш в приложение.

            Returns:
                    None
        """
        dialog = DialogsSetting.DialogKey(self)
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно с горячими клавишами")
        dialog.exec()

    def open_dialog_extension_search(self):
        dialog = DialogsResult.DialogExtensionSearch(self)
        if dialog.exec() == QDialog.Accepted:
            test_data,user_data,np_data,N_data, start_date, end_date = dialog.get_filter_parameters()
            self.apply_filter(test_data, start_date, end_date, user_data)

    def apply_filter(self, test_data, start_date, end_date, user_data):
        #Перенести эту функцию в модель данных страницы результатов
        filters = []
        if test_data:
            filters.append(f"test_name = '{test_data}'")
        if user_data:
            filters.append(f"user_name = '{user_data}'")
        if start_date and end_date:
            filters.append(f"start_test BETWEEN '{start_date}' AND '{end_date}'")
        where_clause = " AND ".join(filters)
        if where_clause:
            where_clause = "WHERE " + where_clause
        query = f""" SELECT t.test_name, t.test_param, t.time_test, t.test_result, t.start_test, u.user_name
                    FROM tests as t
                    INNER JOIN users as u ON t.id_user_fk = u.user_id {where_clause}"""
        print(query)
        self.model.setQuery(query)
        if self.model.rowCount() == 0:
            # Если строк нет, выводим предупреждение
            QMessageBox.warning(None, "Предупреждение", "Нет данных, удовлетворяющих условиям запроса.")
            # Оставляем модель предыдущей
            self.model.setQuery(self.model.ALL_RESULT_SQL)
        else:
            # Если нет ни одного условия, выводим предупреждение
            QMessageBox.information(None, "Данные были изменены", "Данные в таблице  отфильтрованы")
        self.tableView.setModel(self.model)

    def button_click(self) -> None:
        """
        Обрабатывает событие нажатия на кнопки в боковом меню.

        В зависимости от названия кнопки устанавливает соответствующую страницу в stackedWidget,
        сбрасывает стиль всех кнопок и устанавливает стиль нажатой кнопки.

        Returns:
            None
        """
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_report":
            widgets.stackedWidget.setCurrentWidget(widgets.report_page)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())

        if btnName == "btn_bar":
            widgets.stackedWidget.setCurrentWidget(widgets.chart_page)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())


        if btnName == "btn_result":
            widgets.stackedWidget.setCurrentWidget(widgets.result_page)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())


if __name__ == "__main__":
    app = Application(sys.argv)
    app.setWindowIcon(QIcon(u":/icons/images/icons/aramid.svg"))
    window = MainWindow()
    # window.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinMaxButtonsHint)
    result = app.exec()
    sys.exit(result)
