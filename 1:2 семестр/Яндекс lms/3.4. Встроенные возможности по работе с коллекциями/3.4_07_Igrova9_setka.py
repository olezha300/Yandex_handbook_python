from itertools import combinations

names = []
for _ in range(int(input())):
    names.append(input())
for pairs in combinations(names, r=2):
    print(' - '.join(pairs))