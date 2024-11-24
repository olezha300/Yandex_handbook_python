def main():
    res = sorted(map(int, input().split('; ')))
    result = dict.fromkeys(res)
    for i in res:
        for j in res:
            a, b = i, j
            while b:
                a, b = b, a % b
            if a == 1:
                if result[i]:
                    result[i].add(j)
                else:
                    result[i] = {j}
    for i in result:
        if result[i]:
            print(f'{i} - {", ".join(map(str, sorted(result[i])))}')


if __name__ == "__main__":
    main()