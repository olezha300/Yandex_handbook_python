def solution(*args, **kwargs):
    spisok = [*args]
    n = spisok[0]
    m = spisok[1]
    k1 = spisok[2]
    k2 = spisok[3]
    x = n * (m - k2) // (k1 - k2)
    print(x, n - x)


def main():
    n = int(input())
    m = int(input())
    k1 = int(input())
    k2 = int(input())
    solution(n, m, k1, k2)


if __name__ == "__main__":
    main()