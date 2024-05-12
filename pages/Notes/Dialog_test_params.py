from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QDialog, QPushButton, QMessageBox, QStyledItemDelegate
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt


class ReadOnlyDelegate(QStyledItemDelegate):
    """
        Класс делегата для создания ячеек только для чтения в QTableView.

        Этот делегат используется для предотвращения редактирования определенных ячеек в QTableView.

        Атрибуты:
            parent (QObject): Родительский объект этого делегата.

        methods:
            createEditor(parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
                Создает и возвращает виджет редактора для элемента, указанного данным индексом.
                В этой реализации всегда возвращает None, чтобы предотвратить редактирование.
        """
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index) -> None:
        """
               Создает и возвращает виджет редактора для элемента, указанного данным индексом.
                Всегда возвращает None, чтобы предотвратить редактирование.

               :arguments:
                   parent (QWidget): Родительский виджет редактора.
                   option (QStyleOptionViewItem): Стилевые параметры для элемента представления.
                   index (QModelIndex): Индекс модели для элемента.

               :returns:
                   None для блокировки редактирование.
               """
        return None



class TestParamsDialog(QDialog):
    """
        Диалоговое окно для редактирования параметров тестов.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Параметры тестов")
        layout = QVBoxLayout(self)
        self.model = QSqlTableModel()
        self.model.setTable("test_params")
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "Параметр теста")
        self.model.setHeaderData(1, Qt.Horizontal, "Описание параметра")

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setStretchLastSection(True)

        delegate = ReadOnlyDelegate(self.table_view)
        self.table_view.setItemDelegateForColumn(0, delegate)

        layout.addWidget(self.table_view)
        save_button = QPushButton("Сохранить изменения")
        save_button.clicked.connect(self.save_changes)
        layout.addWidget(save_button)

    def save_changes(self) -> None:
        """
            Сохраняет изменения в базе данных.
            :arguments:
                None
            :returns:
                None
        """
        if not self.model.submitAll():
            QMessageBox.warning(self, "Ошибка", "Ошибка сохранения изменений в БД.")
            return
        QMessageBox.information(self, "Успех", "Измененеия сохранены в БД.")