from PySide6.QtWidgets import QDialog, QFormLayout, QVBoxLayout, QPushButton, \
    QTableView,QMainWindow, QWidget, QHeaderView, QMessageBox, QGraphicsScene, QGraphicsView, QTreeWidgetItem
from PySide6.QtGui import QIcon


import sys
from Application import Application
from ui_modules.ui_main import Ui_MainWindow



widgets = None


class SetupUI(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.ui.retranslateUi(self)
        title = "Aramid TsT Graph"
        self.setWindowTitle(title)
        self.show()


if __name__ == "__main__":
    app = Application(sys.argv)
    app.setWindowIcon(QIcon(u":/icons/images/icons/aramid.svg"))
    window = SetupUI(app)
    result = app.exec()
    sys.exit(result)