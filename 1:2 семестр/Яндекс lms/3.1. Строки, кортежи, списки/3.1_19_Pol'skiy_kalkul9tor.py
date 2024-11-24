def main():
    spisok = list(input().split())
    result = [int(spisok[0])]
    for i in spisok[1:]:
        if i.isdigit():
            result.append(int(i))
        else:
            a = result.pop()
            exec("result[-1] " + i + "= a")
    print(result[0])


if __name__ == "__main__":
    main()