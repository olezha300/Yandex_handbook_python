def main():
    res = []
    for i in range(int(input())):
        res.extend(input().split())
    print('\n'.join(set(res)))


if __name__ == "__main__":
    main()