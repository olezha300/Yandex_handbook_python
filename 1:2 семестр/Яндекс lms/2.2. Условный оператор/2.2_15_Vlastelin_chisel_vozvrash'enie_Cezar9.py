def solution(*args, **kwargs):
    spisok = [*args]
    n1 = spisok[0]
    n2 = spisok[1]
    n1_1 = n1 // 10
    n1_2 = n1 % 10
    n2_1 = n2 // 10
    n2_2 = n2 % 10
    mx = max(n1_1, n1_2, n2_1, n2_2)
    mn = min(n1_1, n1_2, n2_1, n2_2)
    sr = (n1_1 + n1_2 + n2_1 + n2_2 - mn - mx) % 10
    print(f"{mx}{sr}{mn}")


def main():
    n1 = int(input())
    n2 = int(input())
    solution(n1, n2)


if __name__ == "__main__":
    main()