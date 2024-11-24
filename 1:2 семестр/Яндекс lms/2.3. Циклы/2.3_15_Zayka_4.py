def Zayka_4(N):
    count = 0
    if N > 0:
        for i in range(N):
            if "зайка" in input():
                count += 1
    print(count)


if __name__ == "__main__":
    Zayka_4(int(input()))