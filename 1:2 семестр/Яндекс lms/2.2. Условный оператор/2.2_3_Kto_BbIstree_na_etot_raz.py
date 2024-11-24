def solution(*args, **kwargs):
    spisok = [*args]
    v_sr_Pet9 = spisok[0]
    v_sr_Vas9 = spisok[1]
    v_sr_Tol9 = spisok[2]
    if v_sr_Pet9 > v_sr_Vas9 and v_sr_Pet9 > v_sr_Tol9:
        print("Петя")
    elif v_sr_Tol9 > v_sr_Pet9 and v_sr_Tol9 > v_sr_Vas9:
        print("Толя")
    else:
        print("Вася")


def main():
    v_sr_Pet9 = int(input())
    v_sr_Vas9 = int(input())
    v_sr_Tol9 = int(input())
    solution(v_sr_Pet9, v_sr_Vas9, v_sr_Tol9)


if __name__ == "__main__":
    main()