def Sum_digits(N, s):
    if N > 0:
        while N:
            s += N % 10
            N = N // 10
    print(s)


if __name__ == "__main__":
    Sum_digits(int(input()), 0)