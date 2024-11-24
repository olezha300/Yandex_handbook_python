def main():
    menu = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
    N = int(input())
    if N > 0:
        for i in range(N):
            print(menu[i % len(menu)])
    print(len(menu))

if __name__ == "__main__":
    main()