# 作者:明月清风我
# 时间:2022/7/15 20:10
import json
from pandas import DataFrame
from pathlib import Path


class SourceData(object):
    def __init__(self, path):
        self.path = path


class SourceDataLabel(SourceData):

    def __init__(self, path):
        super().__init__(path)
        self.path = path
        self.label_dict = {}

        label = Path(self.path)
        for each in label.iterdir():
            self.label_dict[each.name] = each


class SourceDataSerial(SourceData):
    def deserialize(self):
        raise FileExistsError


class SourceDataJson(SourceData):
    def json_to_dict(self):
        with open(self.path, "r") as file:
            result = json.load(file)["results"][0]
        return result


class JsonObject(object):
    measurements_dataframe = DataFrame()

    def __init__(self, data):
        self.measurements = None
        for i in data:
            self.__dict__[i] = data[i]
        self.measurements_dataframe = DataFrame(self.measurements)

