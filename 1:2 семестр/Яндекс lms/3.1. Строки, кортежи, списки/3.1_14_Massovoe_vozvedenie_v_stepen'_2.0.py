def main():
    result = list(map(int, input().split()))
    P = int(input())
    for i in result:
        print(i ** P, end=' ')


if __name__ == "__main__":
    main()