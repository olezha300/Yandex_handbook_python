class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if (b ** 2 - 4 * a * c) < 0 or (a == 0 and c != 0):
        raise NoSolutionsError
    elif a == 0 and c == 0:
        raise InfiniteSolutionsError
    return ((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a, (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a)


print(find_roots(1, 2, 1))
