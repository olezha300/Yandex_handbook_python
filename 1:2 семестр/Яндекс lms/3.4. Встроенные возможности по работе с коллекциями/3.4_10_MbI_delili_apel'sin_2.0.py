from itertools import product

n = int(input())
print("А Б В")
for i in product(range(1, n + 1), range(1, n + 1), range(1, n + 1)):
    if sum(i) == n:
        print(' '.join([str(x) for x in i]))