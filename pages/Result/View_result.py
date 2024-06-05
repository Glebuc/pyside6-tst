from PySide6.QtWidgets import QTableView, QMessageBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtCore import Qt, QRect, QEvent, QPoint
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionButton, QStyle, QTableView, QHeaderView, QApplication

from pages.Result import Model_result

class CheckBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(CheckBoxDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == 0:
            checked = index.model().data(index, Qt.DisplayRole)
            if checked:
                check_state = Qt.Checked
            else:
                check_state = Qt.Unchecked

            check_box_style_option = QStyleOptionButton()
            check_box_style_option.state |= QStyle.State_Enabled
            if check_state == Qt.Checked:
                check_box_style_option.state |= QStyle.State_On
            else:
                check_box_style_option.state |= QStyle.State_Off
            check_box_style_option.rect = self.getCheckBoxRect(option)

            QApplication.style().drawControl(QStyle.CE_CheckBox, check_box_style_option, painter)
        else:
            super(CheckBoxDelegate, self).paint(painter, option, index)

    def editorEvent(self, event, model, option, index):
        if index.column() == 0 and event.type() in (QEvent.MouseButtonRelease, QEvent.MouseButtonDblClick):
            if event.button() == Qt.LeftButton:
                new_value = not model.data(index, Qt.DisplayRole)
                model.setData(index, new_value, Qt.EditRole)
                return True
        return super(CheckBoxDelegate, self).editorEvent(event, model, option, index)

    def getCheckBoxRect(self, option):
        check_box_style_option = QStyleOptionButton()
        check_box_rect = QApplication.style().subElementRect(QStyle.SE_CheckBoxIndicator, check_box_style_option)
        check_box_point = option.rect.center() - QPoint(check_box_rect.width() // 2, check_box_rect.height() // 2)
        return QRect(check_box_point, check_box_rect.size())


class CustomTableView(QTableView):
    """Класс для отображения таблицы на странице Result"""
    def __init__(self, parent=None):
        super(CustomTableView, self).__init__(parent)

        self.setSelectionMode(QTableView.SingleSelection)
        self.verticalHeader().setVisible(False)

        self.model = Model_result.ResultModel('tests')
        self.setModel(self.model)

        header = self.horizontalHeader()
        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        self.setItemDelegateForColumn(-1, CheckBoxDelegate(self))

