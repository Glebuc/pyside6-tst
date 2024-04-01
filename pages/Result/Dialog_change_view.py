import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QFormLayout, QCheckBox, QVBoxLayout, QPushButton, QTableView, \
    QMainWindow, QWidget, QHeaderView


from utils import get_themes_path


class ColumnSelectionDialog(QDialog):
    def __init__(self, column_names, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Выбор отображаемых столбцов")
        self.column_names = column_names
        self.checkbox_dict = {}
        self.setMinimumSize(250, 200)

        layout = QVBoxLayout(self)

        for column_name in column_names:
            checkbox = QCheckBox(column_name)
            checkbox.setChecked(True)  # Устанавливаем все флажки в состояние "включено" при инициализации
            self.checkbox_dict[column_name] = checkbox
            layout.addWidget(checkbox)

        button = QPushButton("Принять")
        button.clicked.connect(self.accept)
        layout.addWidget(button)

        with open(os.path.abspath(os.path.join(get_themes_path(), 'theme_light.qss')), 'r') as f: # придумать что-то с путями для файлов приложения
            dialog_stylesheet = f.read()
        self.setStyleSheet(dialog_stylesheet)
        self.setMaximumSize(300, 300)

    def get_selected_columns(self):
        selected_columns = {}
        for column_name, checkbox in self.checkbox_dict.items():
            selected_columns[column_name] = checkbox.isChecked()
        return selected_columns

    def restore_checkbox_states(self, checkbox_states):
        for column_name, checked in checkbox_states.items():
            self.checkbox_dict[column_name].setChecked(checked)
