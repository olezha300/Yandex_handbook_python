def solution(*args, **kwargs):
    spisok = [*args]
    x = spisok[0]
    y = spisok[1]
    r = 10
    if x ** 2 + y ** 2 > r ** 2:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    elif y >= 0 and x >= 0 and (x ** 2 + y ** 2 <= 25):
        print("Опасность! Покиньте зону как можно скорее!")
    elif (x - 5) * (x + 7) <= 4 * y and y < 0:
        print("Опасность! Покиньте зону как можно скорее!")
    elif x <= 0 and y >= 0 and y <= 1.6 * x + 11 and y <= 5:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")


def main():
    x = float(input())
    y = float(input())
    solution(x, y)


if __name__ == "__main__":
    main()