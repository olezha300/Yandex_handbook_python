def solution(*args, **kwargs):
    spisok = [*args]
    name = spisok[0]
    price = spisok[1]
    weight = spisok[2]
    money = spisok[3]
    print("Чек")
    print(f"{name} - {weight}кг - {price}руб/кг")
    print(f"Итого: {weight * price}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {money - (weight * price)}руб")


def main():
    name = input()
    price = int(input())
    weight = int(input())
    money = int(input())
    solution(name, price, weight, money)


if __name__ == "__main__":
    main()