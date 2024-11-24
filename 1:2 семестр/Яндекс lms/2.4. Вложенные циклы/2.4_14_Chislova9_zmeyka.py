def Snake(N, M):
    width = len(str(N * M))
    for i in range(1, N + 1):
        if i % 2:
            for j in range(M * (i - 1) + 1, M * i + 1):
                if j == M * i:
                    print(str(j).rjust(width, ' '))
                else:
                    print(str(j).rjust(width, ' '), end=' ')
        else:
            for j in range(M * i, M * (i - 1), -1):
                if j == M * (i - 1) + 1:
                    print(str(j).rjust(width, ' '))
                else:
                    print(str(j).rjust(width, ' '), end=' ')


if __name__ == "__main__":
    Snake(int(input()), int(input()))