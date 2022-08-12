# 作者:明月清风我
# 时间:2022/7/15 21:17
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
        # self.dataset_path = dataset_path
        # self.results_path = results_path
        # self.dataset_object = source_data.SourceDataLabel(self.dataset_path)
        # self.results_object = source_data.SourceDataLabel(self.results_path)
        # self.dataset = self.dataset_object.label_dict
        # self.results = self.results_object.label_dict
        self.dataset = dataset_path
        self.results = results_path
        print(self.dataset, self.results)

    def result_error(self):
        self.result_not_found = 0
        detect_num_error = {}
        detect_coord_error = {}

        def cal_area_2poly(data1, data2):
            poly1 = Polygon(data1).convex_hull
            poly2 = Polygon(data2).convex_hull
            if not poly1.intersects(poly2):
                inter_area = 0
            else:
                inter_area = poly1.intersection(poly2).area
            return inter_area

        def distance(data1, data2):
            return ((sum(data1[0][:])/4 - sum(data2[0][:])/4)**2 + (sum(data1[1][:])/4 - sum(data2[1][:])/4)**2)**0.5

        for dataset_path_key in self.dataset.keys():
            dataset_path = self.dataset[dataset_path_key]
            results_path = self.results[dataset_path_key]
            print(dataset_path, results_path)
            if results_path is None:
                self.result_not_found += 1
                print(self.result_not_found, 'rnf')
                continue
            with open(dataset_path, "r") as file:
                dataset_coords = file.readlines()
                index: int
                for index in range(len(dataset_coords)):
                    dataset_coords[index] = [list(map(float, dataset_coords[index].split()[1:3])),
                                             list(map(float, dataset_coords[index].split()[3:5])),
                                             list(map(float, dataset_coords[index].split()[5:7])),
                                             list(map(float, dataset_coords[index].split()[7:9]))]
            with open(results_path, "r") as file:
                results_coords = file.readlines()
                index: int
                for index in range(len(results_coords)):
                    results_coords[index] = [list(map(float, results_coords[index].split()[1:3])),
                                             list(map(float, results_coords[index].split()[3:5])),
                                             list(map(float, results_coords[index].split()[5:7])),
                                             list(map(float, results_coords[index].split()[7:9]))]
            detect_num_error[dataset_path_key] = len(results_coords) - len(dataset_coords)
            compare_array = np.zeros([len(results_coords), len(dataset_coords)])
            print(compare_array, len(results_coords), len(dataset_coords))
            for row in range(len(results_coords)):
                for column in range(len(dataset_coords)):
                    compare_array[row, column] = distance(results_coords[row], dataset_coords[column])
            match = []
            flag = 0
            print(compare_array, 'a')
            while compare_array.min() != 2:
                min_index_tuple = divmod(np.argmax(compare_array), compare_array.shape[1])
                match.append(min_index_tuple)
                compare_array[min_index_tuple[0], :] = 2
                compare_array[:, min_index_tuple[1]] = 2
                flag += 1
                print(flag)
                print(compare_array)
            detect_coord_error[dataset_path_key] = []
            for index_tuple in match:
                cover_rate = cal_area_2poly(results_coords[index_tuple[0]], dataset_coords[index_tuple[1]])/\
                             Polygon(dataset_coords[index_tuple[1]]).convex_hull.area
                detect_coord_error[dataset_path_key].append(cover_rate)
        print(detect_coord_error)