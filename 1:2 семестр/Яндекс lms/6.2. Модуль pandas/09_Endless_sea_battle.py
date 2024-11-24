import pandas as pd

a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
data = pd.read_csv('data.csv')
print(data[(data['x'] >= a) & (data['x'] <= c) & (data['y'] >= d) & (data['y'] <= b)])
