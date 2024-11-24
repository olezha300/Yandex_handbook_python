def solution(*args, **kwargs):
    spisok = [*args]
    god = spisok[0]
    if god % 4 or not god % 100 and god % 400:
        print('NO')
    else:
        print('YES')


def main():
    god = int(input())
    solution(god)


if __name__ == "__main__":
    main()