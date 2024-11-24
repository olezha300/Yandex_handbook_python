def solution(*args, **kwargs):
    spisok = [*args]
    red = spisok[0]
    green = spisok[1]
    blue = spisok[2]
    print(red + blue + 1)


def main():
    red = int(input())
    green = int(input())
    blue = int(input())
    solution(red, green, blue)


if __name__ == "__main__":
    main()