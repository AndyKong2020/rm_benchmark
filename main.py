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
        process = data_analyzer.ResultsProcessor(dataset.label_dict, results.label_dict)
        result_error_dict = process.result_error()
        analyzer = data_analyzer.DataAnalyzer(result_error_dict)
        print(analyzer.picture_avg(), analyzer.target_avg())


if __name__ == '__main__':
    main()
