def secret_replace(text, **kwargs):
    s = ''
    kwargs = {d: (v, 0) for d, v in kwargs.items()}
    for i in text:
        if i in kwargs:
            s += kwargs[i][0][kwargs[i][1] % len(kwargs[i][0])]
            kwargs[i] = kwargs[i][0], kwargs[i][1] + 1
        else:
            s += i
    return s

print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))