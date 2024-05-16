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

class JSONParser:
    def __init__(self, json_data):
        self.json_data = json_data
        self.parsers = [HPCGParser, HPLParser, IMBParser]

    def parse(self):
        dict_test_data = {}
        try:
            parsed_data = json.loads(self.json_data)
            for test_name, test_data in parsed_data.items():
                if test_name == 'parametr':
                    continue
                if not test_data.get("complete", False):
                    continue
                list_params = [
                    (key, value)
                    for key, value in test_data.get('config', {}).items()
                    if value
                ]
                dict_test_data[test_name] = {
                    "parameters": list_params,
                    "complete": test_data["complete"]
                }
                for parser_cls in self.parsers:
                    if parser_cls.matches(test_name):
                        result_test = test_data.get("result_test", "")
                        parsed_result = parser_cls().parse_result(result_test)
                        dict_test_data[test_name]["parsed_result"] = parsed_result
                        break

            pprint(dict_test_data)
            return dict_test_data
        except json.JSONDecodeError:
            print("JSON parsing error")
            return None

