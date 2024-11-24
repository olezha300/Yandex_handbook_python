def solution(*args, **kwargs):
    spisok = [*args]
    v_Pet9 = spisok[0]
    v_Vas9 = spisok[1]
    if v_Pet9 > v_Vas9:
        print("Петя")
    else:
        print("Вася")


def main():
    v_Pet9 = int(input())
    v_Vas9 = int(input())
    solution(v_Pet9, v_Vas9)


if __name__ == "__main__":
    main()