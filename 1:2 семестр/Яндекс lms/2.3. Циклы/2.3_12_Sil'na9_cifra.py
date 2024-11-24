def Max_digit(N):
    mx = 0
    if N > 0:
        while N:
            mx = max(mx, N % 10)
            N //= 10
    print(mx)


if __name__ == "__main__":
    Max_digit(int(input()))