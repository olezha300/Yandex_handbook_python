def solution(*args, **kwargs):
    spisok = [*args]
    n = spisok[0]
    m = spisok[1]
    if n < 1000 and m < 1000:
        c = (n % 10 + m % 10) % 10
        b = (n // 10 % 10 + m // 10 % 10) % 10
        a = (n // 100 + m // 100) % 10
        number = a * 100 + b * 10 + c
    print(number)

def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == "__main__":
    main()