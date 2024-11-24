def main():
    N = int(input())
    result = []
    if N > 0:
        for i in range(N):
            result.append(input())
        search = input()
        for j in result:
            if search.lower() in j.lower():
                print(j)


if __name__ == "__main__":
    main()