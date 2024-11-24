def Min_name(N, min_name):
    if N > 0:
        for i in range(N - 1):
            min_name = min(min_name, input())
        print(min_name)


if __name__ == "__main__":
    Min_name(int(input()), input())