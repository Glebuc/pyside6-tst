import json
import re
from pprint import pprint


class BaseTestParser:
    """
        Базовый класс для всех парсеров тестов.

        atributes:
        pattern (str): Регулярное выражение для проверки, подходит ли парсер для имени теста. Должно быть задано в подклассах.

        methods:
        parse_result(result_test):
            Парсит строку результата теста. Должен быть реализован в подклассах.

        matches(test_name):
            Проверяет, подходит ли данный парсер для указанного имени теста.
        """
    pattern = None  # Каждый парсер должен задать свой pattern

    def parse_result(self, result_test):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    def matches(cls, test_name):
        """
            Проверяет, подходит ли данный парсер для указанного имени теста.

            :arguments:
               test_name (str): Имя теста.

            :returns:
               bool: True, если парсер подходит для данного имени теста, иначе False.
        """
        return cls.pattern is not None and re.search(cls.pattern, test_name)

class HPCGParser(BaseTestParser):
    """
        Парсер теста HPCG
    """
    pattern = r"HPCG"

    def parse_result(self, result_test):
        return {"parsed_result": result_test[::-1]}  # Пример парсинга

class HPLParser(BaseTestParser):
    """
           Парсер теста HPL
    """
    pattern = r"HPL"

    def parse_result(self, result_test):
        return {"parsed_result": result_test.upper()}  # Пример парсинга

class IMBParser(BaseTestParser):
    """
        Парсер теста IMB
    """

    pattern = r"IMB"

    def parse_result(self, result_test):
        return {"parsed_result": f"IMB parsed: {result_test}"}  # Пример парсинга


import json

class JSONParser:
    def __init__(self, json_data):
        self.json_data = json.loads(json_data)

    def parse(self):
        parsed_tests = []
        cluster_name = self.json_data["parametr"]["hpc"]["cluster_name"]
        version_os = self.json_data["parametr"]["hpc"]["version_os"]
        start_test = self.json_data["datetime"]

        for key, value in self.json_data.items():
            if key in ["datetime", "parametr"]:
                continue

            if isinstance(value, dict) and value.get("complete") and value.get("result_test", "").strip():
                test_result = {
                    "test_name": key,
                    "result_test": value["result_test"],
                    "config": value["config"],
                    "start_test": start_test,
                    "cluster_name": cluster_name,
                    "version_os": version_os
                }
                parsed_tests.append(test_result)

        return parsed_tests

