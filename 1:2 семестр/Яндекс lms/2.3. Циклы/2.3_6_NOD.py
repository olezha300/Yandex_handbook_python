def NOD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)


if __name__ == "__main__":
    NOD(int(input()), int(input()))