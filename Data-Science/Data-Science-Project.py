import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

def part1_EDA():
    #rawData = part1_EDA_Data()
    df = pd.read_csv("MSA2022-Phase2-ProjectV2\Data-Science\weather-data.csv")
    #df.replace("", None)
    df2 = df["tmpc"].mean()
    print(df)
    print(df2)

def main():
    part1_EDA()

if __name__ == '__main__':
    main()
