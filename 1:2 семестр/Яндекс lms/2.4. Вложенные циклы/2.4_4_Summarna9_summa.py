def Summ(N):
    s = 0
    for i in range(N):
        x = int(input())
        while x:
            s += x % 10
            x //= 10
    print(s)


if __name__ == "__main__":
    Summ(int(input()))