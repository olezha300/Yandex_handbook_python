def main():
    res = []
    for i in range(int(input())):
        res.append(input())
    print(len([i for i in res if res.count(i) > 1]))


if __name__ == "__main__":
    main()