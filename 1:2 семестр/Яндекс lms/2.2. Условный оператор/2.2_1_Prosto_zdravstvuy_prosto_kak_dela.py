def solution(*args, **kwargs):
    spisok = [*args]
    name = spisok[0]
    answer = spisok[1]
    print("Как Вас зовут?")
    print(f"Здравствуйте, {name}!")
    print("Как дела?")
    if answer == "хорошо":
        print("Я за вас рада!")
    if answer == "плохо":
        print("Всё наладиться!")


def main():
    name = input()
    answer = input()
    solution(name, answer)


if __name__ == "__main__":
    main()