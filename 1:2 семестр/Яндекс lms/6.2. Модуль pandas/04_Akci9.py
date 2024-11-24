import pandas as pd


def cheque(price_list: pd.Series, **kwargs) -> pd.DataFrame:
    data = {"product": sorted(kwargs),
            "price": [price_list[i] for i in sorted(kwargs)],
            "number": [kwargs[i] for i in sorted(kwargs)]}
    data["cost"] = [data["price"][i] * data["number"][i] for i in range(len(sorted(kwargs)))]
    return pd.DataFrame(data)


def discount(cheque: pd.DataFrame) -> pd.DataFrame:
    tmp = cheque.copy()
    for i in range(len(tmp.index)):
        if tmp["number"][i] > 2:
            tmp["cost"][i] *= 0.5
    return tmp


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)
