import itertools


def multiple_sum(*numbers, div=2):
    mx = 0
    for i in range(1, len(numbers) + 1):
        for combination in itertools.combinations(numbers, i):
            s = sum(combination)
            if s % div == 0 and s > mx:
                mx = s
    return mx