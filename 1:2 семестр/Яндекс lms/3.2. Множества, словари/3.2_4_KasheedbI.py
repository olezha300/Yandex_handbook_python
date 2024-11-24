def main():
    N, M = int(input()), int(input())
    name_N, name_M = set(), set()
    for i in range(N):
        name_N.add(input())
    for j in range(M):
        name_M.add(input())
    q = len(name_N & name_M)
    print(q if q > 0 else "Таких нет")


if __name__ == "__main__":
    main()