def News(L, N):
    if L > 0 and N > 0:
        for i in range(N):
            s = input()
            if len(s) > L:
                print(s[:L - 3] + "...")
            else:
                print(s)


if __name__ == "__main__":
    News(int(input()), int(input()))