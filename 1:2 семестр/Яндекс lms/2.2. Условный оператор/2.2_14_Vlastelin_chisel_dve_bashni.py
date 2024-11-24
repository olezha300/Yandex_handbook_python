def solution(*args, **kwargs):
    spisok = [*args]
    n = spisok[0]
    if 100 <= n <= 999:
        digit_1 = n // 100
        digit_2 = n // 10 % 10
        digit_3 = n % 10
        mx = max(digit_1, digit_2, digit_3)
        mn = min(digit_1, digit_2, digit_3)
        sr = digit_1 + digit_2 + digit_3 - mx - mn
        if mn == 0:
            print(f"{sr}{mn} {mx}{sr}")
        else:
            print(f"{mn}{sr} {mx}{sr}")

def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()