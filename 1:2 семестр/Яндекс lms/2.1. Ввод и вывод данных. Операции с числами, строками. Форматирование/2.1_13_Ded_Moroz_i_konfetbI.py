def solution(*args, **kwargs):
    spisok = [*args]
    children = spisok[0]
    candy = spisok[1]
    print(candy // children)
    print(candy % children)


def main():
    children = int(input())
    candy = int(input())
    solution(children, candy)


if __name__ == "__main__":
    main()