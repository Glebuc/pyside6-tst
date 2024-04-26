import logging
from datetime import datetime
import sys
import os

class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def __init__(self):
        self.config_dir = os.path.join(os.path.expanduser("~"), ".aramid-tst-graph")
        self.filename = f"log-{datetime.now().strftime('%Y-%m-%d')}.txt"
        self.log_filepath = os.path.join(self.config_dir, self.filename)
        os.makedirs(self.config_dir, exist_ok=True)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(self.log_filepath, mode='w', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log_info(self, message: str) -> None:
        """
        Записывает информационное сообщение в журнал.

        :param message: Строка с информационным сообщением.
        :return: None
        """
        self.logger.info(message)

    def log_warning(self, message: str) -> None:
        """
        Записывает предупреждающее сообщение в журнал.

        :param message: Строка с предупреждающим сообщением.
        :return: None
        """
        self.logger.warning(message)

    def log_error(self, message: str) -> None:
        """
        Записывает сообщение об ошибке в журнал.

        :param message: Строка с сообщением об ошибке.
        :return: None
        """
        self.logger.error(message)

    def log_exception(self, message: str) -> None:
        """
        Записывает сообщение об исключении в журнал.

        :param message: Строка с сообщением об исключении.
        :return: None
        """
        self.logger.exception(message)


