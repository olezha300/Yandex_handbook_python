def solution(*args, **kwargs):
    a = ''.join(args)
    for i in range(3):
        print(a)


def main():
    infa = input()
    solution(infa)


if __name__ == "__main__":
    main()