def main():
    res = []
    for i in range(int(input())):
        res.append(input())
    n = [i + ' - ' + str(res.count(i)) for i in res if res.count(i) > 1]
    if n:
        for j in sorted(n):
            print(j)
    else:
        print("Однофамильцев нет")


if __name__ == "__main__":
    main()