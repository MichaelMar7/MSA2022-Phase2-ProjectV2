import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
from skforecast.model_selection import grid_search_forecaster
from skforecast.model_selection import backtesting_forecaster

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
    data['valid'] = pd.to_datetime(data['valid'], format = "%Y/%m/%d %H:%M" )
    data.set_index("valid", inplace=True)
    data = data.asfreq(freq ="30M")
    data = data.drop(data.columns[[0, 6, 7]], axis=1)
    data = data.interpolate()
    train, test = data[:-17520], data[-17520:]
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

#@cache
def part3(train, test):
    month = 120
    #print("a")
    train = train.asfreq(freq ="6H")
    test = test.asfreq(freq ="6H")
    model = ForecasterAutoreg(regressor = RandomForestRegressor(random_state=123),lags = 1)
    model.fit(y=train["tmpc"])
    #print("b")
    predictions = model.predict(steps=1)
    #print(predictions.head(5))
    #print("c")
    fig, ax = plt.subplots(figsize=(9, 4))
    #train["tmpc"].plot(ax=ax, label='train', linestyle='dotted')
    #test["tmpc"].plot(ax=ax, label='test', linestyle='dotted')
    predictions.plot(ax=ax, label='predictions')
    ax.legend()
    plt.show()
    #
    """
    lags_grid = [10, 20]

    param_grid = {'n_estimators': [100, 1000],
                'max_depth': [3,5]}

    results_grid = grid_search_forecaster(
        forecaster         = model,
        y                  = train["tmpc"],
        param_grid         = param_grid,
        lags_grid          = lags_grid,
        steps              = 12*month,
        refit              = False,
        metric             = 'mean_squared_error',
        initial_train_size = int(len(train)*0.5),
        #fixed_train_size   = False,
        return_best        = True,
        verbose            = False
    )
    results_grid
    """

def part1_q():
    data = pd.read_csv("MSA2022-Phase2-ProjectV2\Data-Science\weather-data.csv")
    return data

def part2_q(data):
    data.set_index("valid", inplace=True)
    data.index = pd.to_datetime(data.index, format = "%Y/%m/%d %H:%M")
    data = data.asfreq(freq ="6H")
    data = data.drop(data.columns[[0, 5, 6]], axis=1)
    data = data.interpolate()
    return data[:-1460], data[-1460:]

"""
def part1_q2():
    data = pd.read_csv("MSA2022-Phase2-ProjectV2\Data-Science\weather-data.csv")
    return data, data[["tmpc", "dwpc", "relh", "sknt", "gust", "peak_wind_drct"]].mean()

def part2_q2(data, data_average):
    data.set_index("valid", inplace=True)
    data.index = pd.to_datetime(data.index, format = "%Y/%m/%d %H:%M")
    data = data.asfreq(freq ="30T")
    data = data.drop(data.columns[[0, 5, 6]], axis=1)
    for column in data.columns:
        data[column] = data[column].replace(np.nan, data_average[column])
    return data[:-17520], data[-17520:]
"""

def part2_q3(data):
    data.set_index("valid", inplace=True)
    data.index = pd.to_datetime(data.index, format = "%Y/%m/%d %H:%M")
    data = data.asfreq(freq ="30T")
    data = data.drop(data.columns[[0, 5, 6]], axis=1)
    data = data.interpolate()
    #X_train, X_test, Y_train, Y_test = train_test_split(data[["tmpc", "dwpc", "relh", "sknt"]], data.index, test_size=0.2, shuffle=False, random_state=0)
    X_train = data[["tmpc"]].iloc[:-17520]
    X_test = data[["tmpc"]].iloc[-17520:]
    Y_train = data.index[:-17520]
    Y_test = data.index[-17520:]
    return X_train, X_test, Y_train, Y_test

def part3_q3(X_train, X_test, Y_train, Y_test):
    model = linear_model.LinearRegression().fit(X_train, Y_train)
    pred = pd.Series(model.predict(X_test), index=Y_test)
    print(pred)
    fig, ax = plt.subplots(figsize=(9, 4))
    #X_train["tmpc"].plot(ax=ax, label='train', linestyle='dotted')
    #X_test["tmpc"].plot(ax=ax, label='test', linestyle='dotted')
    plt.plot(X_train["tmpc"], label='train', linestyle='dotted')
    plt.plot(X_test["tmpc"], label='test', linestyle='dotted')
    #plt.plot(pred, label='predictions')
    #pred["tmpc"].plot(ax=ax, label='predictions')
    ax.legend()
    plt.show()
    plt.plot(X_train["tmpc"].iloc[:48*30])
    plt.show()

def part3_q(train, test):
    pass

def main():
    data = part1_q()
    #train, test = part2_q(data)
    #print(train.head())
    #data, data_average = part1_q2()
    #train, test = part2_q2(data, data_average)
    #part3(train, test)
    X_train, X_test, Y_train, Y_test = part2_q3(data)
    part3_q3(X_train, X_test, Y_train, Y_test)

if __name__ == '__main__':
    main()
