from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QFormLayout, QCheckBox, QVBoxLayout, QPushButton, QTableView, \
    QMainWindow, QWidget, QHeaderView


class ColumnSelectionDialog(QDialog):
    def __init__(self, column_names, parent=None):
        super(ColumnSelectionDialog, self).__init__(parent)

        self.column_names = column_names

        self.setWindowTitle("Column Selection")
        layout = QVBoxLayout(self)

        self.checkboxes = {}
        for column_name in column_names:
            checkbox = QCheckBox(column_name)
            checkbox.setChecked(True)
            layout.addWidget(checkbox)
            self.checkboxes[column_name] = checkbox

        apply_button = QPushButton("Apply", self)
        apply_button.clicked.connect(self.accept)
        layout.addWidget(apply_button)

    def selected_columns(self):
        return [column for column, checkbox in self.checkboxes.items() if checkbox.isChecked()]
