

from ui_modules import Settings
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QSizeGrip
from PySide6.QtCore import QFile, QTextStream, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup



class UIFunctions():

    def toggleMenu(self, enable: bool) -> None:
        """
        Переключает видимость бокового меню.

        :argument enable: Флаг, указывающий, следует ли показать меню (True) или скрыть (False).
        :type enable: bool
        """
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleLeftBox(self, enable):
        """
           Переключает видимость левой дополнительной панели.

           :argument enable: Флаг, указывающий, нужно ли включить панель (True) или выключить (False).
           :type enable: bool
        """
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            # color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

        UIFunctions.start_box_animation(self, width, "left")


    def start_box_animation(self, left_box_width, direction):
        """
            Запускает анимацию изменения ширины дополнительных боковых панелей.

            :argument left_box_width: Текущая ширина левой дополнительной панели.
            :type left_box_width: int
            :argument direction: Направление анимации. "left" для левой панели
            :type direction: str
            """
        left_width = 0

        if left_box_width == 0 and direction == "left":
            left_width = Settings.LEFT_BOX_WIDTH
        else:
            left_width = 0

        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)


        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.start()

    def selectStandardMenu(self, widget):
        """
        Выделяет стандартное меню на панели верхнего меню.

        :argument widget: Имя объекта кнопки, которую следует выделить.
        :type widget: str
        """
        for w in self.ui.topMenu.findChildren('QPushButton'):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def theme(self, file):
        """
            Применяет тему стилей к пользовательскому интерфейсу из файла QSS.

            :argument:
                file (str): Путь к файлу QSS, содержащему стили.

            :returns:
                None

            :raise:
                FileNotFoundError: Если файл QSS не найден.
                IOError: Если возникает ошибка при чтении файла QSS.
            """
        qss_file = QFile(file)
        if not qss_file.open(QFile.ReadOnly | QFile.Text):
            raise FileNotFoundError(f"Файл QSS не найден: {file}")

        try:
            stream = QTextStream(qss_file)
            self.ui.styleSheet.setStyleSheet(stream.readAll())
        except IOError as e:
            self.log.log_error(f"Ошибка при чтении файла QSS: {e}")
            raise e
        finally:
            qss_file.close()

    def setStyle(self, widget, style):
        """
        Применяет стиль к виджету.

        :argument widget: Виджет, к которому нужно применить стиль.
        :type widget: QWidget
        :argument style: Строка с CSS-стилями для применения к виджету.
        :type style: str
        """
        widget.setStyleSheet(style)

    def resetStyle(self, selectedBtnName):
        """
        Сбрасывает стиль всех кнопок в верхнем меню, кроме выбранной кнопки.

        :argument selectedBtnName: Имя выбранной кнопки, стиль которой не нужно сбрасывать.
        :type selectedBtnName: str
        """
        for btn in self.ui.topMenu.findChildren(QPushButton):
            if btn.objectName() != selectedBtnName:
                btn.setStyleSheet("")

    @staticmethod
    def selectMenu() -> str:
        """
        Возвращает строку со стилем для выделения пункта меню.

        :return: Строка со стилем для выделения пункта меню.
        :rtype: str
        """
        return "background-color: rgb(70, 70, 70)"

    @staticmethod
    def addStyle(widget, new_style: str) -> None:
        """
        Добавляет новый стиль к существующему стилю виджета.

        :argument widget: Виджет, к которому нужно добавить стиль.
        :type widget: QWidget
        :argument new_style: Новый стиль, который нужно добавить к существующему стилю виджета.
        :type new_style: str
        """
        current_style = widget.styleSheet()
        widget.setStyleSheet(current_style + new_style)

