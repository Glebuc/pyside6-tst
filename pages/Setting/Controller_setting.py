from PySide6.QtWidgets import QApplication
from ui_modules import Ui_MainWindow
from .DialogsSetting import DialogKey
from PySide6.QtWidgets import QMainWindow

class ControllerSettings(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.widgets = Ui_MainWindow()
        self.widgets.setupUi(self)
        self.widgets.btn_hot_keys.clicked.connect(self.open_dialog_keyword)

    def open_dialog_keyword(self) -> None:
        """
        Открывает диалоговое окно для отображения горячих клавиш в приложение.

        :return:
                None
        """
        dialog = DialogKey(self)
        if not dialog.isVisible():
            # Проверяем, что главный цикл событий запущен
            if not QApplication.instance():
                app = QApplication([])
            self.log.log_info("Открыто диалоговое окно с горячими клавишами")
            dialog.exec()
