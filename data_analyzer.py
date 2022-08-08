# 作者:明月清风我
# 时间:2022/7/15 21:17
import pandas as pd
from pandas import Series, DataFrame
from source_data import DataObject


class MeasurementsProcessor:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def iterations_sum(self):
        return sum(self.dataframe["iterations"])

    def elapsed_per_op_avg(self):
        pass