from itertools import permutations

my_list = []
N = int(input())
for _ in range(N):
    my_list.append(input())
for i in permutations(sorted(my_list), r=N):
    print(', '.join(i))