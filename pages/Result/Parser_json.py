import json
from pprint import pprint

class JSONParser:

    def __init__(self, json_data):
        self.json_data = json_data

    def parse(self):
        dict_test_data = {}
        try:
            parsed_data = json.loads(self.json_data)
            for i in parsed_data:
                if i == 'parametr':
                    continue
                main_data_test = parsed_data[i]
                if main_data_test["complete"] == False:
                    continue
                list_params = []
                for key, value in main_data_test['config'].items():
                    if not value:
                        continue
                    list_params.append((key, value))
                print(i, "--", list_params, main_data_test["complete"])
            return dict_test_data
        except json.JSONDecodeError:
            print("JSON parsing error")