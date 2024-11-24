from functools import lru_cache


@lru_cache(maxsize=1000)
def recursive_digit_sum(number):
    if number < 10:
        return number
    return number % 10 + recursive_digit_sum(number // 10)