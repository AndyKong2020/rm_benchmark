import time

import data_analyzer
import source_data

path = "testInfo.json"


def table():
    try:
        data = source_data.SourceDataSerial(path)
        dict_data = data.deserialize()
        print(dict_data)
    except:
        data = source_data.SourceDataJson(path)
        dict_data = data.json_to_dict()
        print(dict_data)
        d = source_data.JsonObject(dict_data)
        df = d.measurements_dataframe
        print(df)
        mp = data_analyzer.MeasurementsProcessor(df)
        print(mp.iterations_sum())


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
        print(' picture_avg', analyzer.picture_avg(), '\t',
              'target_avg', analyzer.target_avg(), '\n',
              'picture_median', analyzer.picture_median(), '\t',
              'target_median', analyzer.target_median(), '\n',
              'picture_quantiles', analyzer.picture_quantiles(), '\t',
              'target_quantiles', analyzer.target_quantiles(), '\n',
              'picture_pstdev', analyzer.picture_pstdev(), '\t',
              'target_pstdev', analyzer.target_pstdev(), '\n',
              'picture_pvariance', analyzer.picture_pvariance(), '\t',
              'target_pvariance', analyzer.target_pvariance(), '\n',
              'picture_stdev', analyzer.picture_stdev(), '\t',
              'target_stdev', analyzer.target_stdev(), '\n',
              'picture_variance', analyzer.picture_variance(), '\t',
              'target_variance', analyzer.target_variance(), '\n',
              )


if __name__ == '__main__':
    start = time.time()
    table()
    main()
    end = time.time()
    print(end - start)
