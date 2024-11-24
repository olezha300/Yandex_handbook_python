def main():
    mx = -10000
    n = int(input())
    m = int(input())
    p = int(input())
    for i in range(n - 1):
        b = int(input())
        if abs(b - p) < m:
            mx = max(mx, b)
        p = b
    print(mx)


if __name__ == "__main__":
    main()