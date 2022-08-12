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
        dataset = source_data.SourceDataLabel("dataset")
        results = source_data.SourceDataLabel("results")
        process = data_analyzer.ResultsAnalyzer(dataset.label_dict, results.label_dict)
        process.result_error()


if __name__ == '__main__':
    main()
