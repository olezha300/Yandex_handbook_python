def solution(*args, **kwargs):
    a = int(''.join(map(str, args)))
    if a >= 10:
        print(int(a - (2.5 * 38)))


def main():
    sdacha = int(input())
    solution(sdacha)


if __name__ == "__main__":
    main()