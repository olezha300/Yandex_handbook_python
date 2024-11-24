def solution(*args, **kwargs):
    spisok = [*args]
    price = spisok[0]
    weight = spisok[1]
    money = spisok[2]
    print(money - price * weight)


def main():
    price = int(input())
    weight = int(input())
    money = int(input())
    solution(price, weight, money)


if __name__ == "__main__":
    main()