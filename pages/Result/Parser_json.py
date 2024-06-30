import json
import re
from pprint import pprint

class JSONParser:
    def __init__(self, json_data):
        self.json_data = json_data

    def parse(self):
        try:
            data = json.loads(self.json_data)
        except json.JSONDecodeError:
            print("Error")
            return False

        parsed_tests = []
        try:
            cluster_name = data["parametr"]["hpc"]["cluster_name"]
            version_os = data["parametr"]["hpc"]["version_os"]
            start_test = data["datetime"]
        except KeyError:
            print("Error")
            return False

        for key, value in data.items():
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

