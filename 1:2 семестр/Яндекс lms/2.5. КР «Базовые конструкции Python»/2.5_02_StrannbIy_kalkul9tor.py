def main():
    a = int(input())
    s = input()
    b = int(input())
    if len(s) % 2 == 0 and s.count(' ') >= 1:
        print(a + b)
    elif len(s) % 2 == 0 and ' ' not in s:
        print(a - b)
    elif len(s) % 2 != 0 and s.count(' ') >= 1:
        print(a * b)
    else:
        print(a // b)


if __name__ == "__main__":
    main()