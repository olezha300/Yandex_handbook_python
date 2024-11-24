def solution(*args, **kwargs):
    spisok = [*args]
    name = spisok[0]
    price = spisok[1]
    weight = spisok[2]
    money = spisok[3]
    uslovie = spisok[4]
    x = spisok[5]
    print(f"{'Чек':=^35}")
    for i in range(len(uslovie)):
        print(f"{uslovie[i] : <10}{x[i] : >25}")
    print(f"{'=':=^35}")


def main():
    name = input()
    price = int(input())
    weight = int(input())
    money = int(input())
    uslovie = ["Товар:", "Цена:", "Итого:", "Внесено:", "Сдача:"]
    x = [name, f"{weight}кг * {price}руб/кг", f"{weight * price}руб", f"{money}руб", f"{money - (weight * price)}руб"]
    solution(name, price, weight, money, uslovie, x)


if __name__ == "__main__":
    main()