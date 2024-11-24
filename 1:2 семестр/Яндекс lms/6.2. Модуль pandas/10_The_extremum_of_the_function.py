import pandas as pd
import numpy as np


def values(func, start: float, end: float, step: float) -> pd.Series:
    index = np.arange(start, end + step, step)
    return pd.Series([func(x) for x in index], index=index, dtype='float64')


def min_extremum(data: pd.Series) -> float:
    for index in data.index:
        if data[index] == min(data.values):
            return index


def max_extremum(data: pd.Series) -> float:
    for index in data.index:
        if data[index] == max(data.values):
            return index


data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
