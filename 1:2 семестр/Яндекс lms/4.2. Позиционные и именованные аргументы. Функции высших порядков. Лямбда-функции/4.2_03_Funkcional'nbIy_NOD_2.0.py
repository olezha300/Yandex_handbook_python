def gcd(*args, **kwargs):
    a = list(args)
    while len(a) > 1:
        while a[1] != a[0]:
            if a[1] > a[0]:
                a[1] -= a[0]
            else:
                a[0] -= a[1]
        a.pop(1)
    return a[0]
print(gcd(36, 48, 156, 100500))