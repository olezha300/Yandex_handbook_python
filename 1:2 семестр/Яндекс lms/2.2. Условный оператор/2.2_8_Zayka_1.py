def solution(*args, **kwargs):
    spisok = [*args]
    strocha = spisok[0]
    if "зайка" in strocha:
        print("YES")
    else:
        print("NO")


def main():
    strochka = input()
    solution(strochka)


if __name__ == "__main__":
    main()