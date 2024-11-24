def main():
    n = set()
    while (forest := input()) != '':
        a = [x.strip() for x in forest.split()]
        for i in range(len(a)):
            if a[i] == "зайка":
                if i - 1 >= 0:
                    n.add(a[i - 1])
                if i + 1 < len(a):
                    n.add(a[i + 1])
    print(*n, sep='\n')


if __name__ == "__main__":
    main()