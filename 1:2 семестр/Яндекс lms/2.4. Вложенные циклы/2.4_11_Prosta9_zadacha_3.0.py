def p(y):
    return y > 1 and all(y % i != 0 for i in range(2, int(y ** 0.5) + 1))


def f(N):
    count = 0
    for i in range(N):
        x = int(input())
        if p(x):
            count += 1
    print(count)


if __name__ == "__main__":
    f(int(input()))