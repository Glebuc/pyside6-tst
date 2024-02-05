from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self.setup()

    def setup(self):
        self.set_translation()
        return self

    def set_translation(self):
        trans = QTranslator(parent=self)
        ok = trans.load('')
        if ok:
            print("Английский перевод загружен")
        else:
            print("Русский перевод загружен")
        QApplication.installTranslator(trans)
