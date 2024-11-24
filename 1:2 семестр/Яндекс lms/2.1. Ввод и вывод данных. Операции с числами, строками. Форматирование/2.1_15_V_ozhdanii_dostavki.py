def solution(*args, **kwargs):
    spisok = [*args]
    hour = spisok[0]
    minuts = spisok[1]
    minuts_dostavka = spisok[2]
    if 0 <= hour < 24 and 0 <= minuts < 60 and 30 <= minuts_dostavka < 10**9:
        new_hour = (((hour * 60) + minuts + minuts_dostavka) // 60) % 24
        new_minuts = ((hour * 60) + minuts + minuts_dostavka) % 60
        print(f"{new_hour:0>2}:{new_minuts:0>2}")


def main():
    hour = int(input())
    minuts = int(input())
    minuts_dostavka = int(input())
    solution(hour, minuts, minuts_dostavka)


if __name__ == "__main__":
    main()