 # 作者:明月清风我
# 时间:2022/7/15 20:10
import json
from pandas import Series, DataFrame


class SourceData:
    def __init__(self, path):
        self.path = path


class SourceDataSerial(SourceData):
    def deserialize(self):
        raise FileExistsError


class SourceDataJson(SourceData):
    def json_to_dict(self):
        with open(self.path, "r") as file:
            result = json.load(file)["results"][0]
        return result


class DataObject:
    def __init__(self, data):
        self.measurements = None
        for i in data:
            self.__dict__[i] = data[i]

    def measurements_panel(self):
        return DataFrame(self.measurements)
