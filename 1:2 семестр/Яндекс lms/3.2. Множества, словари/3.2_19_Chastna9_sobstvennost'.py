def main():
    res = []
    for _ in range(int(input())):
        r = list(map(lambda x: x.rstrip(','), input().split()))
        res.extend(set(r[1:]))
    ans = sorted(a for a in res if res.count(a) == 1)
    for i in ans:
        print(i)


if __name__ == "__main__":
    main()