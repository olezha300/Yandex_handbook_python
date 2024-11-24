import pandas as pd


def get_long(data: pd.Series, min_length=5) -> pd.Series:
    return pd.Series(
        [data[value] for value in [word for word in data.index if data[word] >= min_length]],
        index=[word for word in data.index if data[word] >= min_length],
        dtype='int64'
    )


data = pd.Series([3, 5, 6, 6], ["мир", "питон", "привет", "яндекс"])
filtered = get_long(data, min_length=6)
print(data)
print(filtered)
