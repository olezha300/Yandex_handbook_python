def main():
    a, b = set(), set()
    for i in range(int(input())):
        a.add(input())
    for j in range(int(input())):
        for k in range(int(input())):
            b.add(input())
    res = sorted(a - b)
    if len(res) > 0:
        print('\n'.join(res))
    else:
        print("Готовить нечего")


if __name__ == "__main__":
    main()