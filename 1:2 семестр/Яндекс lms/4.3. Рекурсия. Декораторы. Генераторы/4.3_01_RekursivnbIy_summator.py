from functools import lru_cache


@lru_cache(maxsize=1000)
def recursive_sum(*args, **kwargs):
    if len(args) == 0:
        return 0
    return args[0] + recursive_sum(*args[1:])

print(recursive_sum(7, 1, 3, 2, 10))