from PySide6.QtWidgets import QTableView, QMessageBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtCore import Qt

from pages.Result import Model_result


class CustomTableView(QTableView):
    def __init__(self, parent=None):
        super(CustomTableView, self).__init__(parent)
        #Model_result.init_db()

        self.setSelectionMode(QTableView.SingleSelection)
        self.verticalHeader().setVisible(False)

        self.model = Model_result.ResultModel('tests')
        self.setModel(self.model)

        header = self.horizontalHeader()
        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)


