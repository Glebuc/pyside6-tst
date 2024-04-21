import os
from typing import Dict

from PySide6.QtCore import QSettings

class AppSettings:
    def __init__(self):
        self.config_dir = os.path.join(os.path.expanduser("~"), ".aramid-tst-graph")
        self.config_file = os.path.join(self.config_dir, "config.ini")
        os.makedirs(self.config_dir, exist_ok=True)

        self.settings = QSettings(self.config_file, QSettings.IniFormat)

        default_settings = {
            "database/host": "None",
            "database/port": "None",
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
            if not self.settings.contains(key):
                self.settings.setValue(key, value)

    def get_setting(self, key):
        """
            Возвращает значение настройки по указанному ключу.

            :argument:
            key (str): Ключ настройки, значение которой нужно получить.

            :return:
            Значение настройки, соответствующее указанному ключу.
        """
        return self.settings.value(key)

    def set_setting(self, key: str, value: str) -> None:
        """
                   Возвращает значение настройки по указанному ключу.

                   :argument:
                   key (str): Ключ настройки, значение которой нужно получить.
        """
        self.settings.setValue(key, value)