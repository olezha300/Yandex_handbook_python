def F(N, M):
    k = 0
    lenght = len(str(N * M))
    for i in range(N):
        for j in range(M):
            k += 1
            print(f"{k:>{lenght}}", end=' ')
        print()


if __name__ == "__main__":
    F(int(input()), int(input()))