def main():
    res = {}
    while x := input().split():
        for i in x:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
    for j in res:
        print(j, res[j])


if __name__ == "__main__":
    main()