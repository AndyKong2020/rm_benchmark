import json
import numpy as np
import pandas as pd
import source_data
import data_analyzer

path = "testInfo.json"


def main():
    try:
        data = source_data.SourceDataSerial(path)
        dict_data = data.deserialize()
        print(dict_data)
    except:
        data = source_data.SourceDataJson(path)
        dict_data = data.json_to_dict()
        print(dict_data)
        d = source_data.DataObject(dict_data)
        print(d.measurements_panel())
        df = d.measurements_panel()
        mp = data_analyzer.MeasurementsProcessor(df)
        print(mp.iterations_sum())


if __name__ == '__main__':
    main()
