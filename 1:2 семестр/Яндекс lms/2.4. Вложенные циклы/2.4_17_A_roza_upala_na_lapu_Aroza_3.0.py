def Roza(N):
    count = 0
    for i in range(N):
        if (x := input()) == x[::-1]:
            count += 1
    print(count)


if __name__ == "__main__":
    Roza(int(input()))