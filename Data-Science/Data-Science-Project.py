import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

def part1():
    data = pd.read_csv("MSA2022-Phase2-ProjectV2\Data-Science\weather-data.csv")
    print(data.head())
    print()

    data_average = data[["tmpc", "dwpc", "relh", "sknt", "gust", "peak_wind_drct"]].mean()
    data_std = data[["tmpc", "dwpc", "relh", "sknt", "gust", "peak_wind_drct"]].std()
    data_quantile = data[["tmpc", "dwpc", "relh", "sknt", "gust", "peak_wind_drct"]].quantile()

    print("Weather Data")
    print(data)
    print()

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

    data.plot.line("valid", "tmpc")
    plt.ylabel("Environmental Temperature")
    plt.xlabel("Date and Time")
    plt.plot(data.valid, data.tmpc)
    plt.show()
    return data

def part1_quick():
    data = pd.read_csv("MSA2022-Phase2-ProjectV2\Data-Science\weather-data.csv")
    return data

def part2(data):
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    print(x,y)

def main():
    data = part1_quick()
    part2(data)

if __name__ == '__main__':
    main()
