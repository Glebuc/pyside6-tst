# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *
#
# from . resources_rc import *


import sys
import os
import platform

from PySide6.QtWidgets import QDialog, QFormLayout, QCheckBox, QVBoxLayout, QPushButton, \
    QTableView,QMainWindow, QWidget, QHeaderView
from PySide6.QtGui import QTransform
from PySide6 import QtCore

import doctest

from Application import Application
from ui_modules import *
from widgets import *
from pages import Model_result, Save_data, View_result, Dialog_change_view, DialogsSetting, DialogsResult



os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui


        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Aramid TsT Graph"
        description = "Aramid TsT Graph"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        self.tableView = View_result.CustomTableView()
        widgets.verticalLayout_20.replaceWidget(widgets.resultView, self.tableView)
        self.model = Model_result.DatabaseModel('tests')

        widgets.btn_change_view.clicked.connect(self.open_column_selection_dialog)

        widgets.list_test_result.addItem("Все тесты")
        for i in Model_result.result:
            widgets.list_test_result.addItem(i)
            widgets.list_test_chart.addItem(i)

        widgets.list_test_result.currentIndexChanged.connect(
            lambda: self.model.filter_data(combo_box=widgets.list_test_result, table_view=self.tableView))

        widgets.btn_save_view.clicked.connect(lambda: Save_data.save_data_to_csv(self.tableView))
        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.resultView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_report.clicked.connect(self.button_click)
        widgets.btn_bar.clicked.connect(self.button_click)
        widgets.btn_result.clicked.connect(self.button_click)

        widgets.btn_config_DB.clicked.connect(self.open_dialog_config_db)
        widgets.btn_hot_keys.clicked.connect(self.open_dialog_keyword)
        widgets.btn_extension_search.clicked.connect(self.open_dialog_extension_search)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        self.show()

        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile_light = ":C:\\Users\\Admin\\Desktop\\ДИПЛОМ\\themes\\theme_light.qss"
        themeFile_dark = "C:\\Users\\Admin\\Desktop\\ДИПЛОМ\\themes\\theme_dark.qss"
        if useCustomTheme:
            UIFunctions.theme(self, themeFile_light, True)
            AppFunctions.setThemeHack(self)
        else:
            UIFunctions.theme(self, themeFile_dark, True)
            AppFunctions.setThemeHack(self)
        widgets.stackedWidget.setCurrentWidget(widgets.report_page)

        record = self.model.record()
        column_names = [record.fieldName(i) for i in range(record.count())]

        self.column_selection_dialog = Dialog_change_view.ColumnSelectionDialog(column_names)

        # словарь для хранения состояний флажков
        self.checkbox_dict = {}

    def open_column_selection_dialog(self):
        visible_columns = [self.model.headerData(i, QtCore.Qt.Horizontal) for i in range(self.model.columnCount())]

        if self.column_selection_dialog.exec() == QDialog.Accepted:
            selected_columns = self.column_selection_dialog.get_selected_columns()
            for column_index in range(self.model.columnCount()):
                column_name = self.model.headerData(column_index, QtCore.Qt.Horizontal)
                if selected_columns.get(column_name, False):
                    self.tableView.showColumn(column_index)
                else:
                    self.tableView.hideColumn(column_index)

    def update_table_columns(self, selected_columns):
        for column_index in range(self.model.columnCount()):
            column_name = self.model.headerData(column_index, QtCore.Qt.Horizontal)
            if column_name in selected_columns:
                self.tableView.showColumn(column_index)
            else:
                self.tableView.hideColumn(column_index)

    def open_dialog_config_db(self):
        dialog = DialogsSetting.DialogConfigDB(self)
        dialog.exec()

    def open_dialog_keyword(self):
        dialog = DialogsSetting.DialogKey(self)
        dialog.exec()

    def open_dialog_extension_search(self):
        dialog = DialogsResult.DialogExtensionSearch(self)
        dialog.exec()

    def button_click(self) -> None:
        # GET BUTTON CLICKED
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

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        self.dragPos = p.toPoint()



if __name__ == "__main__":
    app = Application(sys.argv)
    app.setWindowIcon(QIcon(u":/icons/images/icons/aramid.svg"))
    window = MainWindow()
    result = app.exec()
    sys.exit(result)
