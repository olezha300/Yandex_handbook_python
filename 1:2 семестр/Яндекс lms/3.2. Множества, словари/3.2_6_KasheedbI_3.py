def main():
    N, M = int(input()), int(input())
    res = []
    for i in range(N + M):
        if (s := input()) not in res:
            res.append(s)
        else:
            res.remove(s)
    if len(res) > 0:
        for children in sorted(res):
            print(children)
    else:
        print("Таких нет")


if __name__ == "__main__":
    main()