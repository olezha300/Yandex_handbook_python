from itertools import permutations

my_list = []
for _ in range(int(input())):
    my_list += input().split(', ')
for i in permutations(sorted(my_list), r=3):
    print(' '.join(i))