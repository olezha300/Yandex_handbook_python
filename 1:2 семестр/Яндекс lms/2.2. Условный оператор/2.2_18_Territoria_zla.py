def solution(*args, **kwargs):
    spisok = [*args]
    a = spisok[0]
    b = spisok[1]
    c = spisok[2]
    mx = max(a, b, c)
    mn = min(a, b, c)
    sr = a + b + c - mx - mn
    if mx ** 2 == mn ** 2 + sr ** 2:
        print("100%")
    elif mx ** 2 > mn ** 2 + sr ** 2:
        print("велика")
    else:
        print("крайне мала")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == "__main__":
    main()