def Snake_2(N, M):
    width = len(str(N * M))
    for i in range(1, N + 1):
        for j in range(M):
            if not j % 2 and j != M - 1:
                print(str(i + 2 * N * (j // 2)).rjust(width, ' '), end=' ')
            elif not j % 2 and j == M - 1:
                print(str(i + 2 * N * (j // 2)).rjust(width, ' '))
            elif j % 2 and j != M - 1:
                print(str(2 * N * (j // 2 + 1) - (i - 1)).rjust(width, ' '), end=' ')
            else:
                print(str(2 * N * (j // 2 + 1) - (i - 1)).rjust(width, ' '))


if __name__ == "__main__":
    Snake_2(int(input()), int(input()))