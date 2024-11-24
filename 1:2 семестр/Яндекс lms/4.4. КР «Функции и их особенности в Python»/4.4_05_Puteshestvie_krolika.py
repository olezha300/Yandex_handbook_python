def rabbit(start, finish, length):
    a = [[start]]
    b = []
    for _ in range(length):
        for way in a:
            if way[-1] + 2 not in way:
                b.append(way + [way[-1] + 2])
            if way[-1] + 1 not in way:
                b.append(way + [way[-1] + 1])
            if way[-1] - 2 not in way:
                b.append(way + [way[-1] - 2])
            if way[-1] - 1 not in way:
                b.append(way + [way[-1] - 1])
        a = b
        b = []
    return list(filter(lambda x: x[-1] == finish, a))