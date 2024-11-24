import pandas as pd
import string


def length_stats(text: str) -> tuple[pd.Series]:
    for p in string.punctuation:
        if p in text:
            text = text.replace(p, "")
    text_odd = [word for word in sorted(set(text.lower().split())) if len(word) % 2 != 0]
    text_even = [word for word in sorted(set(text.lower().split())) if len(word) % 2 == 0]
    len_of_words = [len(word) for word in sorted(set(text.lower().split()))]
    lst_odd = [i for i in len_of_words if i % 2 != 0]
    lst_even = [i for i in len_of_words if i % 2 == 0]
    if lst_odd == []:
        return pd.Series(lst_odd, index=text_odd, dtype="int64"), pd.Series(lst_even, index=text_even)
    elif lst_even == []:
        return pd.Series(lst_odd, index=text_odd), pd.Series(lst_even, index=text_even, dtype="int64")
    return pd.Series(lst_odd, index=text_odd), pd.Series(lst_even, index=text_even)


odd, even = length_stats("Мама мыла раму")
print(odd)
print(even)
