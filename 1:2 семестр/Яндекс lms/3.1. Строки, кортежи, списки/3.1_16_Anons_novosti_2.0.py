def main():
    L = int(input())
    N = int(input())
    result = []
    if L > 0 and N > 0:
        for i in range(N):
            result.append(input())
        for j in result:
            if L > 3:
                if len(j) >= L - 3:
                    print(j[:L - 3] + "...")
                else:
                    print(j + "..." if L == 4 else j)
                L -= len(j)


if __name__ == "__main__":
    main()