# 作者:明月清风我
# 时间:2022/7/15 21:17
import pandas as pd
from pandas import Series, DataFrame
from pathlib import Path

import source_data


class MeasurementsProcessor:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def iterations_sum(self):
        return sum(self.dataframe["iterations"])

    def elapsed_per_op_avg(self):
        pass


class ResultsAnalyzer:
    dataset = {}
    results = {}
    result_not_found = 0

    def __init__(self, dataset_path, results_path):
        self.dataset_path = dataset_path
        self.results_path = results_path
        self.dataset = source_data.SourceDataLabel(dataset_path).label_dict
        self.results = source_data.SourceDataLabel(results_path).label_dict

    def result_error(self):
        self.result_not_found = 0
        for dataset_path_key in self.dataset.keys():
            dataset_path = self.dataset.get(dataset_path_key, default=None)
            results_path = self.results.get(dataset_path_key, default=None)
            if results_path is None:
                self.result_not_found += 1
                continue
            with open(dataset_path, "r") as file:
                pass
