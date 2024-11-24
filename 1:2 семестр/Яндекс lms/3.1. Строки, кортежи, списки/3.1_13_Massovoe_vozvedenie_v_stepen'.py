def main():
    N = int(input())
    result = []
    if N > 0:
        for i in range(N):
            result.append(int(input()))
        P = int(input())
        for j in result:
            print(j ** P)


if __name__ == "__main__":
    main()