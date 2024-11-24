from itertools import accumulate

for values in accumulate(map(lambda x: ' ' + x, input().split())):
    print(values[1:])