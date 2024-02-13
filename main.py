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
from pages import Model_result, Save_data, View_result, Dialog_change_view

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
        widgets.verticalLayout_20.replaceWidget(widgets.tableView, self.tableView)
        self.model = Model_result.DatabaseModel('tests')

        widgets.pushButton_7.clicked.connect(self.open_column_selection_dialog)

        widgets.list_test.addItem("Все тесты")
        for i in Model_result.result:
            widgets.list_test.addItem(i)

        widgets.list_test.currentIndexChanged.connect(
            lambda: self.model.filter_data(combo_box=widgets.list_test, table_view=self.tableView))

        widgets.pushButton_8.clicked.connect(lambda: Save_data.save_data_to_csv(self.tableView))
        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_report.clicked.connect(self.button_click)
        widgets.btn_bar.clicked.connect(self.button_click)
        widgets.btn_result.clicked.connect(self.button_click)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile_light = "themes/theme_light.qss"
        themeFile_dark = "themes/theme_dark.qss"
        if useCustomTheme:
            UIFunctions.theme(self, themeFile_light, True)
            AppFunctions.setThemeHack(self)
        else:
            UIFunctions.theme(self, themeFile_dark, True)
            AppFunctions.setThemeHack(self)
        widgets.stackedWidget.setCurrentWidget(widgets.home)

        record = self.model.record()
        column_names = [record.fieldName(i) for i in range(record.count())]

        self.column_selection_dialog = Dialog_change_view.ColumnSelectionDialog(column_names)

        # Создаем словарь для хранения состояний флажков
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



    def button_click(self) -> None:
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_report":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())

        # SHOW WIDGETS PAGE
        if btnName == "btn_bar":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())


        # SHOW NEW PAGE
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
