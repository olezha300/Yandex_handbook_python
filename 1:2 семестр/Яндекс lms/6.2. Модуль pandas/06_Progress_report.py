import pandas as pd


def best(data: pd.DataFrame) -> pd.DataFrame:
    tmp = data.copy()
    return tmp[(tmp['maths'] > 3) & (tmp['physics'] > 3) & (tmp['computer science'] > 3)]


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)
print(journal)
print(filtered)
