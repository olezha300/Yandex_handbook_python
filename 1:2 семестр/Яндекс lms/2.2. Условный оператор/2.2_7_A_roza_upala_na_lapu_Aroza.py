def solution(*args, **kwargs):
    spisok = [*args]
    N = spisok[0]
    if N == N[::-1]:
        print("YES")
    else:
        print("NO")


def main():
    N = input()
    solution(N)


if __name__ == "__main__":
    main()