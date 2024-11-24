def Zayka_6():
    k = 0
    if (N := int(input())) > 0:
        for _ in range(N):
            k += (forest := input()).count("зайка")
    print(k)


if __name__ == "__main__":
    Zayka_6()