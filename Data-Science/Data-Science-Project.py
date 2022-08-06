import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def part1_EDA():
    data = pd.read_csv("MSA2022-Phase2-ProjectV2\Data-Science\weather-data.csv")
    data_average = data[["tmpc", "dwpc", "relh", "sknt", "gust", "peak_wind_drct"]].mean()
    data_std = data[["tmpc", "dwpc", "relh", "sknt", "gust", "peak_wind_drct"]].std()
    data_quantile = data[["tmpc", "dwpc", "relh", "sknt", "gust", "peak_wind_drct"]].quantile()
    #plt.matshow(data.corr())
    #plt.show()
    print("Weather Data")
    print(data)
    print()
    data.plot()
    print("Mean for Each Column")
    print(data_average)
    print()
    print("Standard Deviation for Each Column")
    print(data_std)
    print()
    print("Percentile (25%-75%) for Each Column")
    print(data_quantile)
    print()
    corr = data.corr()
    sns.heatmap(corr, 
        xticklabels=corr.columns,
        yticklabels=corr.columns)
    plt.show()
    data.plot.scatter("tmpc", "dwpc")
    plt.scatter(data.tmpc, data.dwpc)
    plt.show()

def main():
    part1_EDA()

if __name__ == '__main__':
    main()
