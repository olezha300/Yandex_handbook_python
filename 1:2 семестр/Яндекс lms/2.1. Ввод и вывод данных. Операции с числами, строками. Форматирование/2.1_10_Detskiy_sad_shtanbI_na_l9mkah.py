def solution(*args, **kwargs):
    spisok = [*args]
    name = spisok[0]
    number_of_sofa = spisok[1]
    print(f"Группа №{number_of_sofa // 100}.")
    print(f"{number_of_sofa % 10}. {name}.")
    print(f"Шкафчик: {number_of_sofa}.")
    print(f"Кроватка: {number_of_sofa // 10 % 10}.")


def main():
    name = input()
    number_of_sofa = int(input())
    solution(name, number_of_sofa)


if __name__ == "__main__":
    main()