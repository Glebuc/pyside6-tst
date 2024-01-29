# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *
#
# from . resources_rc import *


import sys
import os
import platform


from PySide6.QtWidgets import QHeaderView, QMainWindow, QApplication

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ui_modules import *
from widgets import *
from database import Model_result

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
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

        Model_result.init_db()

        self.model = Model_result.DatabaseModel('tests')
        widgets.tableView.setModel(self.model.get_model())
        header = widgets.tableView.horizontalHeader()
        for i in range(widgets.tableView.model().columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        # widgets.tableView.hideColumn(0)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
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
        themeFile = "themes/theme_light.qss"
        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)
        widgets.stackedWidget.setCurrentWidget(widgets.home)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def button_click(self) -> None:
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        print(btn)
        # SHOW HOME PAGE
        if btnName == "btn_report":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            # UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_bar":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            # UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_result":
            widgets.stackedWidget.setCurrentWidget(widgets.result_page)  # SET PAGE
            # UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        self.dragPos = p.toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(u":/icons/images/icons/aramid.svg"))
    window = MainWindow()
    sys.exit(app.exec())
