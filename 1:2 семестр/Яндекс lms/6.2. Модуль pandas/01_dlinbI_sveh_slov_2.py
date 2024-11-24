import pandas as pd


def length_stats(text: str) -> pd.Series:
    for p in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
        if p in text:
            text = text.replace(p, '')
    text = sorted(set(text.lower().split()))
    return pd.Series([len(word) for word in text], index=text)


print(length_stats('Мама мыла раму'))
