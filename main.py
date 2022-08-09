import json
import numpy as np
import pandas as pd
import source_data
import data_analyzer

path = "labels"


def main():
    try:
        data = source_data.SourceDataSerial(path)
        dict_data = data.deserialize()
        print(dict_data)
    except:
        s = source_data.SourceDataDataset(path)
        print(s.dataset_dict)


if __name__ == '__main__':
    main()
