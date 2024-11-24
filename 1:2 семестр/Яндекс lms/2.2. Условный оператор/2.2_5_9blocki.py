def solution(*args, **kwargs):
    spisok = [*args]
    N = spisok[0]
    M = spisok[1]
    if N > 0:
        Pet9 = 6 + N
        Vas9 = 12 + M
        if Pet9 > Vas9:
            print("Петя")
        else:
            print("Вася")


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == "__main__":
    main()