def solution(*args, **kwargs):
    spisok = [*args]
    price = spisok[0]
    nominal = spisok[1]
    if nominal >= 100:
        print(nominal - price)


def main():
    price = int(input(), 2)
    nominal = int(input())
    solution(price, nominal)


if __name__ == "__main__":
    main()