from itertools import product, starmap

N, M = int(input()), int(input())
for i in range(N):
    print(*starmap(lambda x, y: str(x + y).rjust(len(str(N * M))), product([i * M], range(1, M + 1))))