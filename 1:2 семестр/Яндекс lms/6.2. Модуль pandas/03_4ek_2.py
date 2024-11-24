import pandas as pd


def cheque(price_list: pd.Series, **kwargs) -> pd.DataFrame:
    data = {"product": sorted(kwargs),
            "price": [price_list[i] for i in sorted(kwargs)],
            "number": [kwargs[i] for i in sorted(kwargs)]}
    data["cost"] = [data["price"][i] * data["number"][i] for i in range(len(sorted(kwargs)))]
    return pd.DataFrame(data)


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
