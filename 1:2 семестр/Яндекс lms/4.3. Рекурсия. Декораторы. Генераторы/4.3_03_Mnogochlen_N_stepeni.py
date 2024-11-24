def make_equation(*args, **kwargs):
    if len(args) == 1:
        return str(args[0])
    return f"({make_equation(*args[:-1])}) * x + {args[-1]}"