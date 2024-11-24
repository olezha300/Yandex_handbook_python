from sys import stdin

summ = []
lines = [line.rstrip("\n") for line in stdin]
for line in lines:
    list_of_numbres = [int(x) for x in line.split()]
    summ.extend(list_of_numbres)
print(sum(summ))

'''
from sys import stdin

print(sum(map(int, std.read().split())))
'''