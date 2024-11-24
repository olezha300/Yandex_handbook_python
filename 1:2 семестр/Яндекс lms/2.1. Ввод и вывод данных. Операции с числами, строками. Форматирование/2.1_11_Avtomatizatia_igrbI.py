def solution(*args, **kwargs):
    n = int(''.join(map(str, args)))
    if 1000 <= n <= 9999:
        a = str(n // 1000)
        b = str(n // 100 % 10)
        c = str(n // 10 % 10)
        d = str(n % 10)
        print(b + a + d + c)


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()