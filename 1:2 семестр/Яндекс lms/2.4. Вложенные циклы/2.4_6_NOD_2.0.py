def NOD(N):
    x1 = int(input())
    for i in range(N - 1):
        x2 = int(input())
        while x1 != x2:
            if x1 > x2:
                x1 -= x2
            else:
                x2 -= x1
    print(x1)


if __name__ == "__main__":
    NOD(int(input()))