import os
from PySide6.QtCore import QSettings
from typing import Dict

class AppSettings(QSettings):
    """"""
    _instance = None

    @staticmethod
    def get_instance():
        if AppSettings._instance is None:
            AppSettings._instance = AppSettings()
        return AppSettings._instance

    def __init__(self):
        self.config_dir = os.path.join(os.path.expanduser("~"), ".aramid-tst-graph")
        self.config_file = os.path.join(self.config_dir, "config.ini")
        os.makedirs(self.config_dir, exist_ok=True)

        super().__init__(self.config_file, QSettings.IniFormat)

        default_settings = {
            "database/host": "None",
            "database/port": "5432",
            "database/database": "None",
            "database/user": "None",
            "database/password": "None",
            "AppSettings/language": "Russian",
            "AppSettings/theme": "Light",

        }

        self.set_default_settings(default_settings)

    def set_default_settings(self, default_settings: Dict) -> None:
        """
           Устанавливает значения по умолчанию для настроек, если они отсутствуют.

           :argument:
           default_settings (dict): Словарь, содержащий пары ключ-значение для значений по умолчанию.
        """
        for key, value in default_settings.items():
            if not self.contains(key):
                self.setValue(key, value)

    def get_setting(self, key: str) -> str:
        """
            Возвращает значение настройки по указанному ключу.

            :argument:
            key (str): Ключ настройки, значение которой нужно получить.

            :return:
            Значение настройки, соответствующее указанному ключу.
        """
        return self.value(key)

    def set_setting(self, key: str, value: str) -> None:
        """
                   Возвращает значение настройки по указанному ключу.

                   :argument:
                   key (str): Ключ настройки, значение которой нужно получить.
        """
        self.setValue(key, value)

    def get_settings_by_tag(self, tag: str) -> Dict:
        """
        Получает все значения из настроек под определенным тегом.

        :argument:
        tag (str): Тег, который определяет группу настроек.
        :return:
        Словарь со значениями настроек, где ключи - это имена настроек, начинающиеся с указанного тега.
        """
        settings_dict = {}
        all_keys = self.allKeys()

        for key in all_keys:
            if key.startswith(tag):
                settings_dict[key] = self.value(key)

        return settings_dict

if __name__ == '__main__':
    obj = AppSettings()
    print(obj.get_settings_by_tag('database'))