def Zayka_5(N):
    count = 0
    if N > 0:
        for i in range(N):
            k = i
            while (forest := input()) != "ВСЁ":
                if "зайка" == forest and k == i:
                    count += 1
                    k = -1
    print(count)


if __name__ == "__main__":
    Zayka_5(int(input()))