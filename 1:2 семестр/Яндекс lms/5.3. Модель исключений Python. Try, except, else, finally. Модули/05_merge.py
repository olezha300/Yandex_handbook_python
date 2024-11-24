def isiteration(x):
    try:
        iter(x)
    except TypeError:
        return False
    return True


def merge(a, b):
    if not (isiteration(a) and isiteration(b)):
        raise StopIteration
    elif not (
        all(isinstance(i, type(a[0])) for i in a)
        and all(isinstance(i, type(a[0])) for i in b)
    ):
        raise TypeError
    elif not (list(a) == sorted(list(a)) and list(b) == sorted(list(b))):
        raise ValueError
    return tuple(sorted(a + b))
