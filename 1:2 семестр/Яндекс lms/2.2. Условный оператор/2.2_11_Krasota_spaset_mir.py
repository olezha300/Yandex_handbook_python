def solution(*args, **kwargs):
    spisok = [*args]
    n = spisok[0]
    digit_1 = n // 100
    digit_2 = n // 10 % 10
    digit_3 = n % 10
    mn = min(digit_1, digit_2, digit_3)
    mx = max(digit_1, digit_2, digit_3)
    if 100 <= n <= 999 and mn + mx == (digit_1 + digit_2 + digit_3 - mn - mx) * 2:
        print("YES")
    else:
        print("NO")


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()