import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from skforecast.ForecasterAutoreg import ForecasterAutoreg

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
def part2(data):    
    data = data.drop(data.columns[[0, 6, 7]], axis=1)
    train, test = train_test_split(data, test_size=0.2, random_state=0)
    train = train.sort_values("valid")
    test = test.sort_values("valid")
    print(train.head())
    print()
    print(test.head())
    print()
    fig, ax = plt.subplots(figsize=(9, 4))
    train["tmpc"].plot(ax=ax, label='train')
    test["tmpc"].plot(ax=ax, label='test')
    ax.legend()
    plt.show()
    return train, test

def part3(train, test):
    model = RandomForestRegressor(n_estimators=100, random_state=0, n_jobs=6)
    model.fit(X=train, y=train)

def part1_q():
    data = pd.read_csv("MSA2022-Phase2-ProjectV2\Data-Science\weather-data.csv")
    return data

def part2_q(data):
    data = data.drop(data.columns[[0, 6, 7]], axis=1)
    train, test = train_test_split(data, test_size=0.2, random_state=0)
    return train.sort_values("valid"), test.sort_values("valid") 

def part3_q(train, test):
    pass

def main():
    data = part1_q()
    train, test = part2_q(data)
    part3(train, test)

if __name__ == '__main__':
    main()
