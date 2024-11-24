def main():
    res = {}
    for i in range(int(input())):
        x, y = map(int, input().strip().split())
        x //= 10
        y //= 10
        if (x, y) in res.keys():
            res[(x, y)] += 1
        else:
            res[(x, y)] = 1
    print(max(res.values()))


if __name__ == "__main__":
    main()