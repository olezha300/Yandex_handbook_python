def solution(*args, **kwargs):
    spisok = [*args]
    n = spisok[0]
    if n > 0:
        for i in range(n):
            print("Купи слона!")


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()