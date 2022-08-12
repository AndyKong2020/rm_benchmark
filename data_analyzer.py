# 作者:明月清风我
# 时间:2022/7/15 21:17
import pandas as pd
from pandas import Series, DataFrame
from pathlib import Path
import numpy as np
from shapely.geometry import Polygon

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
        def cal_area_2poly(data1, data2):
            poly1 = Polygon(data1).convex_hull
            poly2 = Polygon(data2).convex_hull
            if not poly1.intersects(poly2):
                inter_area = 0
            else:
                inter_area = poly1.intersection(poly2).area
            return inter_area
        for dataset_path_key in self.dataset.keys():
            dataset_path = self.dataset.get(dataset_path_key, default=None)
            results_path = self.results.get(dataset_path_key, default=None)
            if results_path is None:
                self.result_not_found += 1
                continue
            with open(dataset_path, "r") as file:
                dataset_coords = file.readlines()
                dataset_coord = []
                dataset_shpe = []
                for index in range(len(dataset_coords)):
                    dataset_coords[index] = [dataset_coords[index].split()[1:3],
                                             dataset_coords[index].split()[3:5],
                                             dataset_coords[index].split()[5:7],
                                             dataset_coords[index].split()[7:9]]

            with open(results_path, "r") as file:
                results_coords = file.readlines()
                results_coord = []
                for index in range(len(results_coords)):
                    results_coords[index] = [results_coords[index].split()[1:3],
                                             results_coords[index].split()[3:5],
                                             results_coords[index].split()[5:7],
                                             results_coords[index].split()[7:9]]
