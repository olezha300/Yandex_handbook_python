def sqrt(N):
    for i in range(N):
        for j in range(N):
            d = str(min(i, j, N - i - 1, N - j - 1) + 1)
            print(d.rjust(len(str((N + 1) // 2)), ' '), end=' ' if j < N - 1 else '\n')


if __name__ == "__main__":
    sqrt(int(input()))