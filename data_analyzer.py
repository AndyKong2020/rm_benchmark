# 作者:明月清风我
# 时间:2022/7/15 21:17
import statistics

import numpy as np
from shapely.geometry import Polygon


class MeasurementsProcessor(object):
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def iterations_sum(self):
        return sum(self.dataframe["iterations"])

    def elapsed_per_op_avg(self):
        pass


class ResultsProcessor(object):
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
        # print(self.dataset, self.results)

    def result_error(self):
        self.result_not_found = 0
        detect_num_error = {}
        detect_coord_error = {}
        magic_num = [-1]

        def cal_area_2poly(data1, data2):
            poly1 = Polygon(data1).convex_hull
            poly2 = Polygon(data2).convex_hull
            if not poly1.intersects(poly2):
                inter_area = 0
            else:
                inter_area = poly1.intersection(poly2).area
            return inter_area

        def intersection_divide_set(data1, data2):
            set_area = cal_area_2poly(data1, data2)
            proportion = set_area / (Polygon(data1).convex_hull.area +
                                     Polygon(data2).convex_hull.area - set_area)
            return proportion

        def distance(data1, data2):
            return ((sum(data1[0][:]) / 4 - sum(data2[0][:]) / 4) ** 2 +
                    (sum(data1[1][:]) / 4 - sum(data2[1][:]) / 4) ** 2) ** 0.5

        for dataset_path_key in self.dataset.keys():
            dataset_path = self.dataset[dataset_path_key]
            results_path = self.results.get(dataset_path_key)
            # print(dataset_path, results_path)
            if results_path is None:
                self.result_not_found += 1
                # print(self.result_not_found, 'rnf')
                continue
            with open(dataset_path, "r") as file:
                dataset_coords = file.readlines()
                for index in range(len(dataset_coords)):
                    dataset_coords[index] = [list(map(float, dataset_coords[index].split()[1:3])),
                                             list(map(float, dataset_coords[index].split()[3:5])),
                                             list(map(float, dataset_coords[index].split()[5:7])),
                                             list(map(float, dataset_coords[index].split()[7:9]))]
            with open(results_path, "r") as file:
                results_coords = file.readlines()
                for index in range(len(results_coords)):
                    results_coords[index] = [list(map(float, results_coords[index].split()[1:3])),
                                             list(map(float, results_coords[index].split()[3:5])),
                                             list(map(float, results_coords[index].split()[5:7])),
                                             list(map(float, results_coords[index].split()[7:9]))]
            detect_num_error[dataset_path_key] = len(results_coords) - len(dataset_coords)
            detect_coord_error[dataset_path_key] = []
            # print(type(results_coords[0][0][0]))
            inf = [[list(map(float, ['inf', 'inf'])),
                    list(map(float, ['inf', 'inf'])),
                    list(map(float, ['inf', 'inf'])),
                    list(map(float, ['inf', 'inf']))]]
            # print('flag1')
            if (dataset_coords == inf) and (results_coords == inf):
                # print('flag2')
                detect_coord_error[dataset_path_key].append(1.0)
                # print('continue')
                continue
            elif (dataset_coords == inf) and (results_coords != inf):
                detect_coord_error[dataset_path_key].append(0.0)
                continue
            elif (dataset_coords != inf) and (results_coords == inf):
                detect_coord_error[dataset_path_key].append(0.0)
                continue
            compare_array = np.zeros([len(results_coords), len(dataset_coords)])
            # print(compare_array, len(results_coords), len(dataset_coords))
            for row in range(len(results_coords)):
                for column in range(len(dataset_coords)):
                    compare_array[row, column] = intersection_divide_set(results_coords[row], dataset_coords[column])
            match = []
            # flag = 0
            # print(compare_array, 'a')
            while compare_array.max() != magic_num[0]:
                max_index_tuple = divmod(np.argmax(compare_array), compare_array.shape[1])
                # print(max_index_tuple)
                match.append(max_index_tuple)
                compare_array[max_index_tuple[0], :] = magic_num[0]
                compare_array[:, max_index_tuple[1]] = magic_num[0]
                # flag += 1
                # print(flag)
                # print(compare_array)
            for index_tuple in match:
                # print(dataset_coords[index_tuple[1]])
                cover_rate = intersection_divide_set(results_coords[index_tuple[0]], dataset_coords[index_tuple[1]])
                detect_coord_error[dataset_path_key].append(cover_rate)
        # print(detect_coord_error)
        return detect_coord_error


class DataAnalyzer(object):
    def __init__(self, compare_dict):
        # print(compare_dict)
        self.compare_dict = compare_dict
        self.accuracy_per_target = []
        self.accuracy_per_picture = []
        # print(self.compare_dict.values())
        for value in self.compare_dict.values():
            self.accuracy_per_picture.append(statistics.mean(value))
            self.accuracy_per_target += value

    def target_avg(self):
        return statistics.mean(self.accuracy_per_target)

    def picture_avg(self):
        return statistics.mean(self.accuracy_per_picture)

    def target_median(self):
        return statistics.median(self.accuracy_per_target)

    def picture_median(self):
        return statistics.median(self.accuracy_per_picture)

    def target_quantiles(self):
        return statistics.quantiles(self.accuracy_per_target)

    def picture_quantiles(self):
        return statistics.quantiles(self.accuracy_per_picture)

    def target_pstdev(self):
        return statistics.pstdev(self.accuracy_per_target)

    def picture_pstdev(self):
        return statistics.pstdev(self.accuracy_per_picture)

    def target_pvariance(self):
        return statistics.pvariance(self.accuracy_per_target)

    def picture_pvariance(self):
        return statistics.pvariance(self.accuracy_per_picture)

    def target_stdev(self):
        return statistics.stdev(self.accuracy_per_target)

    def picture_stdev(self):
        return statistics.stdev(self.accuracy_per_picture)

    def target_variance(self):
        return statistics.variance(self.accuracy_per_target)

    def picture_variance(self):
        return statistics.variance(self.accuracy_per_picture)
