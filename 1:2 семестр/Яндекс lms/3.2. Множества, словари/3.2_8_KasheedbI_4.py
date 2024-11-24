def main():
    N, res = int(input()), []
    for i in range(N):
        res.extend([input().split()])
    res.sort()
    key, count = input(), 0
    for j in res:
        if key in j[1:]:
            print(j[0])
            count += 1
    if count == 0:
        print("Таких нет")


if __name__ == "__main__":
    main()