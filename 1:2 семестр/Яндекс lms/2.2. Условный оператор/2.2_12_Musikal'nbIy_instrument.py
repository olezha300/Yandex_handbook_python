def solution(*args, **kwargs):
    spisok = [*args]
    a = spisok[0]
    b = spisok[1]
    c = spisok[2]
    if a < b + c and b < a + c and c < a + b:
        print("YES")
    else:
        print("NO")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == "__main__":
    main()