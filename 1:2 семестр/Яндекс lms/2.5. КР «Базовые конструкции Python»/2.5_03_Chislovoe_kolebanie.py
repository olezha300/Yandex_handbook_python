def main():
    N = int(input())
    M = int(input())
    D = int(input())
    res = []
    for i in range(N, M + 1, D):
        res.append(str(i))
    for j in range(M, N - 1, -D):
        res.append(str(j))
    print(' - '.join(res))


if __name__ == "__main__":
    main()