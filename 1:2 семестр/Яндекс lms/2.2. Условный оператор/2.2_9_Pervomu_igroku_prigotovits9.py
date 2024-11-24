def solution(*args, **kwargs):
    spisok = [*args]
    name_1 = spisok[0]
    name_2 = spisok[1]
    name_3 = spisok[2]
    print(min(name_1, name_2, name_3))


def main():
    name_1 = input()
    name_2 = input()
    name_3 = input()
    solution(name_1, name_2, name_3)


if __name__ == "__main__":
    main()