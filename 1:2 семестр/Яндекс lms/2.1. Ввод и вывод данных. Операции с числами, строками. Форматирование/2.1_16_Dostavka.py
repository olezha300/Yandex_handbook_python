def solution(*args, **kwargs):
    spisok = [*args]
    sklad = spisok[0]
    magazin = spisok[1]
    v_sr = spisok[2]
    direction = abs(sklad - magazin)
    print(f"{direction / v_sr :0.2f}")


def main():
    sklad = int(input())
    magazin = int(input())
    v_sr = int(input())
    solution(sklad, magazin, v_sr)


if __name__ == "__main__":
    main()