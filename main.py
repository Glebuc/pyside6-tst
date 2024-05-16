# from . resources_rc import *


import sys
import os


from PySide6.QtWidgets import (QDialog,
                               QFormLayout,
                               QVBoxLayout,
                               QPushButton,
                               QTableView,
                               QMainWindow,
                               QWidget,
                               QHeaderView,
                               QMessageBox,
                               QGraphicsScene,
                               QGraphicsView,
                               QTreeWidgetItem,
                               QFileDialog)
from PySide6.QtGui import QTransform, QIcon, QFont
from PySide6 import QtCore
from PySide6.QtCore import Qt, QResource

from typing import List

from loger import Logger
from Application import Application
from ui_modules import *
from pages import (BaseModel,
                   Model_result,
                   Save_data,
                   View_result,
                   Dialog_change_view,
                   DialogsSetting,
                   DialogsResult,
                   Chart_view,
                   Model_chart,
                   Dialog_add_topic,
                   Dialog_add_note,
                   Model_notes,
                   Controller_setting,
                   Dialog_article_view,
                   Dialog_edit_note,
                   Dialog_edit_topic,
                   Dialog_test_params,
                   Parser_json)
from SettingApp import AppSettings

from utils import get_translate_path, get_themes_path
from ui_modules import Ui_MainWindow



os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

widgets = None


class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.log = Logger.get_instance()
        self.ui.retranslateUi(self)

        title = "Aramid TsT Graph"
        self.setWindowTitle(title)

        # self.controller_setting = Controller_setting.ControllerSettings()

        self.tableView = View_result.CustomTableView()
        widgets.verticalLayout_20.replaceWidget(widgets.resultView, self.tableView)
        self.model_result = Model_result.ResultModel('tests')
        self.model_chart = Model_chart.ChartModel('tests')
        self.note_model = Model_notes.NoteModel('sections')

        widgets.btn_change_view.clicked.connect(self.open_column_selection_dialog)
        self.setting = AppSettings.get_instance()
        self.scene = QGraphicsScene()
        self.view = Chart_view.ChartView(self.scene)
        self.chart = Chart_view.CustomChart()
        self.chart.update_chart()
        self.scene.addItem(self.chart)


        #Обработчики кнопок масштабирования графика
        widgets.zoom_in_chart_btn.clicked.connect(self.chart.zoom_in)
        widgets.zoom_out_chart_btn.clicked.connect(self.chart.zoom_out)
        widgets.reset_chart_btn.clicked.connect(self.chart.reset)

        widgets.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        widgets.graphicsView.setChart(self.chart)


        self.chart.save_chart_image(widgets.graphicsView, "C:\\Users\\Admin\\Desktop\\ДИПЛОМ" )

        widgets.list_test_result.addItem("Все тесты")
        for i in self.model_result.execute_sql(self.model_result.LIST_TEST_SQL):
            widgets.list_test_result.addItem(i)
            widgets.list_test_chart.addItem(i)

        test_name =  widgets.list_test_chart.currentText()


        widgets.list_test_result.currentIndexChanged.connect(
            lambda: self.model_result.filter_data(combo_box=widgets.list_test_result, table_view=self.tableView))

        widgets.list_test_chart.activated.connect(self.set_param_test_for_chart)

        widgets.btn_save_view.clicked.connect(lambda: Save_data.save_data_to_csv(self.tableView))
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))


        widgets.resultView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



        widgets.btn_report.clicked.connect(self.button_click)
        widgets.btn_bar.clicked.connect(self.button_click)
        widgets.btn_result.clicked.connect(self.button_click)
        widgets.btn_note.clicked.connect(self.button_click)

        widgets.btn_config_DB.clicked.connect(self.open_dialog_config_db)
        widgets.btn_hot_keys.clicked.connect(self.open_dialog_keyword)
        widgets.btn_extension_search.clicked.connect(self.open_dialog_extension_search)

        widgets.add_item_note_btn.clicked.connect(self.open_dialog_add_item_topic)
        widgets.add_topic_note_btn.clicked.connect(self.open_dialog_add_topic)


        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        widgets.comboBox_theme.currentTextChanged.connect(self.change_theme)
        widgets.comboBox_language.currentTextChanged.connect(self.change_translation)
        widgets.btn_save_settings.clicked.connect(self.save_settings)
        widgets.treeWidget.itemDoubleClicked.connect(self.get_item_and_parent_text)
        widgets.stackedWidget.setCurrentWidget(widgets.report_page)
        widgets.edit_note_btn.clicked.connect(self.chose_dialog_for_edit)
        widgets.delete_note_btn.clicked.connect(self.delete_notes_or_topic)
        widgets.test_params_btn.clicked.connect(self.dialog_test_params)
        widgets.import_data_btn.clicked.connect(self.parse_json_data)

        font = QFont()
        font.setPointSize(20)
        widgets.treeWidget.setFont(font)


        self.show()
        record = self.model_result.record()
        column_names = [record.fieldName(i) for i in range(record.count())]

        self.column_selection_dialog = Dialog_change_view.ColumnSelectionDialog(column_names)

        # словарь для хранения состояний флажков
        self.checkbox_dict = {}
        self.populate_tree_widget()

    def parse_json_data(self):
        """
            Данная функция передает
        """
        files = self.open_dialog_for_import_data()
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                json_data = f.read()
                parser = Parser_json.JSONParser(json_data)
                parser.parse()

    def open_dialog_for_import_data(self):
        """Открывает файловое диалогое окно для импорта тестов из JSON файлов

            :returns: List[str], возвращает список строк с путями до JSON-файлов
        """
        files, _ = QFileDialog.getOpenFileNames(
            None,
            "Выберите файлы",
            "",  # Фильтры для файлов, здесь оставлено пустым для выбора всех файлов
            "JSON Файлы (*.json)"  # Фильтр для JSON файлов
        )
        print(files)
        return files

    def on_selection_changed(self) -> bool:
        """
            Обработчик изменения выделения в QTreeWidget.

            Проверяет, выбран ли элемент в QTreeWidget. Если элемент выбран, проверяет, является ли он элементом верхнего уровня или дочерним.
            Если ни один элемент не выбран, показывает предупреждение через QMessageBox.

            :returns:
                bool: True, если выбран дочерний элемент. False, если выбран элемент верхнего уровня или ничего не выбрано.
            """
        selected_items = widgets.treeWidget.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            if selected_item.parent() is None:
                self.log.log_info(f"Выбран элемент вверхнего уровня {selected_item.text(0)} для удаления или редактирования")
                return False
            else:
                self.log.log_info(f"Выбран элемент {selected_item.text(0)} для удаления или редактирования")
                return True
        else:
            QMessageBox.warning(self, "Внимание", 'Для "Редактирование" или "Удаление" выделите статью или раздел')
            return None

    def chose_dialog_for_edit(self) -> None:
        """
            Выбирает диалоговое окно для редактирования, в зависимости от выбранного элемента в QTreeWidget.

            Если элемент выбран и возвращается не None из метода on_selection_changed, открывает диалоговое окно для редактирования,
            либо заголовка раздела, либо содержания статьи.

        """
        selection_result = self.on_selection_changed()
        if selection_result is not None:
            selected_items = widgets.treeWidget.selectedItems()
            if selected_items:
                selected_item = selected_items[0]
                if selection_result:
                    self.dialog_edit_content_article(selected_item.text(0), "Вот")
                else:
                    self.dialog_edit_title_topic(selected_item.text(0))


    def delete_notes_or_topic(self) -> None:
        """
            Удаляет выбранную запись или раздел из базы данных в зависимости от выделенного элемента в QTreeWidget.

            Если элемент выбран и возвращается не None из метода on_selection_changed, отображает диалоговое окно с запросом подтверждения удаления.
            При выборе опции "Да", удаляет запись из таблицы 'notes' или раздел из таблицы 'sections' в базе данных.

            """
        selection_result = self.on_selection_changed()
        if selection_result is not None:
            selected_items = widgets.treeWidget.selectedItems()
            if selected_items:
                selected_item = selected_items[0]
                reply = QMessageBox.question(self, 'Удаление', 'Вы уверены, что хотите удалить запись?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    if selection_result:
                        self.note_model.delete_note_data(selected_item.text(0))
                        widgets.treeWidget.clear()
                        self.populate_tree_widget()
                    else:
                        self.note_model.delete_topic_data(selected_item.text(0))
                        widgets.treeWidget.clear()
                        self.populate_tree_widget()
                else:
                    print('Вы выбрали "Нет".')

    def dialog_test_params(self) -> None:
        """

        :return:
        """
        dialog = Dialog_test_params.TestParamsDialog()
        dialog.exec()
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно для просмотра и редактирования параметров")
        else:
            self.log.log_error("Ошибка открытия  диалоговое окно для просмотра и редактирования параметров")

    def dialog_edit_title_topic(self, title) -> None:
        """
            Открывает диалоговое окно для редактирования заголовка раздела.

            :arguments:
                title (str): Заголовок статьи.

        """
        dialog = Dialog_edit_topic.EditTopicDialog(title)
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно для редактирования раздела")
            if dialog.exec() == QDialog.Accepted:
                widgets.treeWidget.clear()
                self.populate_tree_widget()
        else:
            self.log.log_error("Ошибка открытия диалогового окна для редактирования раздела")

    def dialog_edit_content_article(self, title, content):
        dialog = Dialog_edit_note.EditNoteDialog(title, content)
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно для редактирования статьи")
            if dialog.exec() == QDialog.Accepted:
                widgets.treeWidget.clear()
                self.populate_tree_widget()
        else:
            self.log.log_error("Ошибка открытия диалогового окна для редактирования статьи")

    def get_item_and_parent_text(self, item, column):
        """
            Получает текст элемента и его родительского элемента в дереве элементов,
            а затем отображает соответствующую статью в диалоговом окне.

            :argument:
                item (QTreeWidgetItem): Элемент, для которого нужно получить текст.
                column (int): Индекс столбца элемента, содержащего текст.
            :returns:
                None: Если элемент не имеет родительского элемента.
                None: Если не удалось получить данные о статье из базы данных.

        """
        item_text = item.text(column)
        parent_item = item.parent()
        if parent_item:
            parent_text = parent_item.text(column)
            # Получаем данные о статье из базы данных
            article_data = self.note_model.get_article_data(item_text)
            if article_data:
                article_dialog = Dialog_article_view.ArticleDialog(article_data["title"], article_data["content"])
                article_dialog.exec()
        else:
            return None


    def save_settings(self) -> None:
        """
        Сохраняет текущие настройки приложения.

        Получает текущие значения выбранных темы и языка из соответствующих ComboBox'ов и сохраняет их в настройках приложения.
        Если выбранная тема равна "Светлая", она сохраняется как "Light", если равна "Темная", то как "Dark".
        Если выбранный язык равен "Русский", он сохраняется как "Russian", если равен "Английский", то как "English".

        :returns:
            None
        """
        dict_setting = {}
        theme_text = widgets.comboBox_theme.currentText()
        language_text = widgets.comboBox_language.currentText()

        if theme_text == "Светлая":
            dict_setting["theme"] = "Light"
        elif theme_text == "Темная":
            dict_setting["theme"] = "Dark"
        else:
            dict_setting["theme"] = theme_text

        if language_text == "Русский":
            dict_setting["language"] = "Russian"
        elif language_text == "Английский":
            dict_setting["language"] = "English"
        else:
            dict_setting["language"] = language_text

        self.setting.set_setting_application(dict_setting)

    def get_text_from_combo_chart(self) -> str:
        """
        Получает текущее значение из ComboBox.

        :return:
            str: Текущее выбранное значение из ComboBox.
        """
        return widgets.list_test_chart.currentText()

    def populate_tree_widget(self):
        """
        Заполняет QTreeWidget данными из базы данных.

        Получает данные из базы данных с помощью функции get_data_from_database
        и добавляет их в QTreeWidget.
        """
        # Очищаем QTreeWidget перед заполнением новыми данными
        self.ui.treeWidget.clear()

        # Получаем данные из базы данных
        data = self.note_model.get_data_from_database()

        # Создаем элементы QTreeWidgetItem и добавляем их в QTreeWidget
        for section_name, article_titles in data.items():
            section_item = QTreeWidgetItem([section_name])
            self.ui.treeWidget.addTopLevelItem(section_item)

            for title in article_titles:
                article_item = QTreeWidgetItem([title])
                section_item.addChild(article_item)


    def get_param_test(self) -> List:
        """
        Получает параметры теста на основе текущего выбранного значения в ComboBox.

        :return:
            List: Список параметров теста.
        """
        test_name = self.get_text_from_combo_chart()
        parameters_query = self.model_chart.get_test_parameters(test_name)
        list_param = []
        if parameters_query:
            while parameters_query.next():
                param = parameters_query.value(0)
                list_param.append(param)
        return list_param


    def set_param_test_for_chart(self) -> None:
        """
        Устанавливает параметры теста для ComboBox.

        Очищает содержимое ComboBox и затем добавляет новые параметры.
        """
        widgets.list_param_test.clear()
        list_param = self.get_param_test()
        if list_param:
            widgets.list_param_test.addItems(list_param)


    def change_translation(self, text:str) -> None:
        """
        Изменяет язык приложения в зависимости от выбранного текста в ComboBox.

        :param text: Текст текущего выбранного элемента в ComboBox. Должен быть "Русский" или "Английский".
        :return:
            None
        """
        ru_translate = ':/translations/translations/ru.qm'
        en_translate = ':/translations/translations/en.qm'
        if text == "Английский" or text == "English":
            app.setup(en_translate)
            self.ui.retranslateUi(self)
        elif text == "Русский" or text == "Russian":
            app.setup(ru_translate)
            self.ui.retranslateUi(self)

    def change_theme(self, text: str) -> None:
        """
           Изменяет тему интерфейса в зависимости от выбранного текста в ComboBox.

           :argument:
               text (str): Текст текущего выбранного элемента в ComboBox. Должен быть "Светлая" или "Темная".

           :return:
               None
        """
        themeFile_light = ':/themes/themes/theme_light.qss'
        themeFile_dark = ':/themes/themes/theme_dark.qss'
        if text == "Светлая" or text == "Light":
            UIFunctions.theme(self,themeFile_light)
        elif text == "Темная" or text == "Dark":
            UIFunctions.theme(self,themeFile_dark)

    def open_column_selection_dialog(self):
        """
           Открывает диалоговое окно для выбора отображаемых столбцов в таблице.

           Функция извлекает список всех видимых столбцов из модели данных таблицы и отображает диалоговое окно выбора столбцов.
           После нажатия на кнопку "Подтвердить" диалогового окна функция проверяет, какие столбцы были выбраны пользователем, и соответственно
           скрывает или отображает столбцы в таблице.

           :return:
               None
        """
        visible_columns = [self.model_result.headerData(i, QtCore.Qt.Horizontal) for i in range(self.model_result.columnCount())]
        if self.column_selection_dialog.exec() == QDialog.Accepted:
            selected_columns = self.column_selection_dialog.get_selected_columns()
            for column_index in range(self.model_result.columnCount()):
                column_name = self.model_result.headerData(column_index, QtCore.Qt.Horizontal)
                if selected_columns.get(column_name, False):
                    self.tableView.showColumn(column_index)
                else:
                    self.tableView.hideColumn(column_index)

    def open_dialog_add_topic (self) -> None:
        """
            Открывает диалоговое окно для добавления раздела в Заметках.

            :return:
                None
        """
        dialog = Dialog_add_topic.DialogAddTopic()
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно для добавления раздела")
            if dialog.exec() == QDialog.Accepted:
                self.ui.treeWidget.clear()
                self.populate_tree_widget()
        else:
            self.log.log_error("Ошибка открытия диалогового окна для добавления раздела")

    def open_dialog_add_item_topic(self) -> None:
        """
           Открывает диалоговое окно для добавления статьи в Заметках .

            :return:
                None
        """
        dialog = Dialog_add_note.DialogAddNote()
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно для добавления статьи")
            if dialog.exec() == QDialog.Accepted:
                self.ui.treeWidget.clear()
                self.populate_tree_widget()
        else:
            self.log.log_error("Ошибка открытия диалогового окна для добавления статьи")


    def open_dialog_config_db(self) -> None:
        """
            Открывает диалоговое окно для настройки подключения к базе данных.

            :return:
                None
        """
        dialog = DialogsSetting.DialogConfigDB(self)
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно с кофигом БД")
        dialog.exec()


    def open_dialog_keyword(self) -> None:
        """
            Открывает диалоговое окно для отображения горячих клавиш в приложение.

            :return:
                    None
        """
        dialog = DialogsSetting.DialogKey(self)
        if not dialog.isVisible():
            self.log.log_info("Открыто диалоговое окно с горячими клавишами")
        dialog.exec()

    def open_dialog_extension_search(self):
        dialog = DialogsResult.DialogExtensionSearch(self)
        if dialog.exec() == QDialog.Accepted:
            test_data, user_data, param_test, start_date, end_date = dialog.get_filter_parameters()
            self.model_result.apply_filter(self.tableView, test_data, user_data, param_test, start_date, end_date)



    def button_click(self) -> None:
        """
        Обрабатывает событие нажатия на кнопки в боковом меню.

        В зависимости от названия кнопки устанавливает соответствующую страницу в stackedWidget,
        сбрасывает стиль всех кнопок и устанавливает стиль нажатой кнопки.

        :return:
            None
        """
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_report":
            widgets.stackedWidget.setCurrentWidget(widgets.report_page)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())

        if btnName == "btn_bar":
            widgets.stackedWidget.setCurrentWidget(widgets.chart_page)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())

        if btnName == "btn_result":
            widgets.stackedWidget.setCurrentWidget(widgets.result_page)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())

        if btnName == "btn_note":
            widgets.stackedWidget.setCurrentWidget(widgets.note_page)
            UIFunctions.resetStyle(self, btnName)
            UIFunctions.addStyle(btn, UIFunctions.selectMenu())


if __name__ == "__main__":
    app = Application(sys.argv)
    app.setWindowIcon(QIcon(u":/icons/images/icons/aramid.svg"))
    window = MainWindow(app)
    result = app.exec()
    sys.exit(result)
