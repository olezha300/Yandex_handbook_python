def solution(*args, **kwargs):
    a = args
    print("Как Вас зовут?")
    print("Привет,", str(a[0]))


def main():
    name = input()
    solution(name)


if __name__ == "__main__":
    main()