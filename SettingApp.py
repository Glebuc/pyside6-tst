import os
from PySide6.QtCore import QSettings
from typing import Dict
from loger import Logger
# from cryptography.fernet import Fernet

class AppSettings(QSettings):
    """
    Класс для работы с настройками приложения.

    Унаследован от QSettings для работы с файлами настроек.

     .. code-block:: python

           setting = AppSettings.get_instance()
           setting.get_setting(param)
    """
    _instance = None

    @staticmethod
    def get_instance():
        """
        Получить единственный экземпляр класса AppSettings.

        :return:
        Уникальный экземпляр класса AppSettings.
        """
        if AppSettings._instance is None:
            AppSettings._instance = AppSettings()
        return AppSettings._instance

    def __init__(self):
        """
        Инициализация класса AppSettings.

        Создает папку и файл конфигурации, устанавливает настройки по умолчанию.
        """
        self.config_dir = os.path.join(os.path.expanduser("~"), ".aramid-tst-graph")
        self.config_file = os.path.join(self.config_dir, "config.ini")
        os.makedirs(self.config_dir, exist_ok=True)
        self.log = Logger.get_instance()

        super().__init__(self.config_file, QSettings.IniFormat)

        default_settings = {
            "database/host": "None",
            "database/port": "5432",
            "database/database": "None",
            "database/user": "None",
            "database/password": "None",
            "database/salt": "f549eebfba38656a649719c910f054f229e5fc93",
            "AppSettings/language": "Russian",
            "AppSettings/theme": "Light",

        }

        self.set_default_settings(default_settings)

    def set_default_settings(self, default_settings: Dict) -> None:
        """
        Установить значения по умолчанию для настроек, если они отсутствуют.

        :param default_settings: Словарь с парами ключ-значение для значений по умолчанию.
        :return: None
        """
        for key, value in default_settings.items():
            if not self.contains(key):
                self.setValue(key, value)
        self.log.log_info("Установлены настройки по умолчанию")

    def get_setting(self, key: str) -> str:
        """
        Получить значение настройки по указанному ключу.

        :param key: Ключ настройки, значение которой нужно получить.
        :return: Значение настройки, соответствующее указанному ключу.
        """
        return self.value(key)

    def set_setting(self, key: str, value: str) -> None:
        """
        Установить значение настройки по указанному ключу.

        :param key: Ключ настройки, значение которой нужно установить.
        :param value: Новое значение настройки.
        :return: None
        """
        self.setValue(key, value)
        self.log.log_info(f"Добавлены новая настройка в файл конфигурации: {key}={value}")

    def set_setting_application(self, new_settings: Dict) -> None:
        """
        Устанавливает новые значения для настроек приложения.

        :param:
            new_settings (Dict): Словарь, содержащий новые значения настроек в формате {ключ: значение}.

        :return:
            None
        """
        for key, value in new_settings.items():
            self.setValue(f"AppSettings/{key}", value)
            self.log.log_info(f"Обновлены настройки в файле конифгурации - {new_settings}")

    def set_setting_database(self, new_settings: Dict) -> None:
        """
        Устанавливает новые значения для настроек приложения.

        :param:
            new_settings (Dict): Словарь, содержащий новые значения настроек в формате {ключ: значение}.

        :return:
            None
        """
        for key, value in new_settings.items():
            self.setValue(f"database/{key}", value)
            self.log.log_info(f"Обновлены настройки базы данных - {new_settings}")

    def get_settings_by_tag(self, tag: str) -> Dict:
        """
        Получить все значения из настроек под определенным тегом.

        :param tag: Тег, который определяет группу настроек.
        :return: Словарь со значениями настроек, где ключи - это имена настроек, начинающиеся с указанного тега.
        """
        settings_dict = {}
        all_keys = self.allKeys()

        for key in all_keys:
            if key.startswith(tag):
                settings_dict[key] = self.value(key)

        return settings_dict

    # def generate_key(self) -> bytes:
    #     """
    #     Генерирует ключ для использования в шифровании методом Fernet.
    #
    #     :returns:
    #         bytes: Сгенерированный ключ.
    #     """
    #     return Fernet.generate_key()
    #
    # def encrypt_string(self, text: str, key: bytes) -> bytes:
    #     """
    #     Шифрует строку с использованием ключа методом Fernet.
    #
    #     :argument:
    #         text (str): Строка для шифрования.
    #         key (bytes): Ключ для шифрования.
    #
    #     :returns:
    #         bytes: Зашифрованная строка.
    #     """
    #     cipher_suite = Fernet(key)
    #     encrypted_text = cipher_suite.encrypt(text.encode())
    #     return encrypted_text
    #
    # def decrypt_string(self, encrypted_text, key):
    #     """
    #     Дешифрует строку, зашифрованную методом Fernet.
    #
    #     :argument:
    #         encrypted_text (bytes): Зашифрованная строка.
    #         key (bytes): Ключ для дешифрования.
    #
    #     :returns:
    #         str: Расшифрованная строка.
    #     """
    #     cipher_suite = Fernet(key)
    #     decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    #     return decrypted_text


if __name__ == '__main__':
    obj = AppSettings()
    print(print(obj.generate_key()))
