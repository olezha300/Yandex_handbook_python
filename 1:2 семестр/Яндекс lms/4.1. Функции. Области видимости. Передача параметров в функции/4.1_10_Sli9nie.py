def merge(a, b):
    c = list(a) + list(b)
    c.sort()
    return tuple(c)