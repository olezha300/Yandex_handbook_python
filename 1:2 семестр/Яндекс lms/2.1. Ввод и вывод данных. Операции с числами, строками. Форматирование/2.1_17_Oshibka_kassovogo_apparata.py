def solution(*args, **kwargs):
    spisok = [*args]
    main_sum = spisok[0]
    last_sum = spisok[1]
    print(main_sum + last_sum)


def main():
    main_sum = int(input())
    last_sum = int(input(), 2)
    solution(main_sum, last_sum)


if __name__ == "__main__":
    main()