def F(N, M):
    k = 1
    lenght = len(str(N * M))
    for i in range(N):
        for j in range(M):
            print(f"{k + N * j}".rjust(lenght), end=' ')
        k += 1
        print()


if __name__ == "__main__":
    F(int(input()), int(input()))