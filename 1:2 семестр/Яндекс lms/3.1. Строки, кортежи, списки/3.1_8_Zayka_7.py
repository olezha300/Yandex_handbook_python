def Zayka_7():
    for i in range(int(input())):
        if "зайка" in (forest := input()):
            print(forest.find("зайка") + 1)
        else:
            print("Заек нет =(")


if __name__ == "__main__":
    Zayka_7()