def make_matrix(size, value=0):
    lst = []
    if isinstance(size, int):
        for i in range(size):
            lst += [list(int(x) for x in str(value)) * size]
    else:
        for _ in range(size[0]):
            for _ in range(size[1]):
                lst += [value]
    return lst
print(make_matrix((4, 2), 1))