from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Диалоговое окно")

        layout = QVBoxLayout(self)

        # Label
        label = QLabel("Введите название раздела:", self)
        layout.addWidget(label)

        # LineEdit
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)

        # Кнопка подтверждения
        button = QPushButton("Подтвердить", self)
        button.clicked.connect(self.accept)
        layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication([])
    dialog = MyDialog()
    dialog.exec()
