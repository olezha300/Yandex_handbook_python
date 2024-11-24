def solution(*args, **kwargs):
    spisok = [*args]
    N = spisok[0]
    M = spisok[1]
    if N >= 1 and M >= 1:
        print(N * M // 2)


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == "__main__":
    main()