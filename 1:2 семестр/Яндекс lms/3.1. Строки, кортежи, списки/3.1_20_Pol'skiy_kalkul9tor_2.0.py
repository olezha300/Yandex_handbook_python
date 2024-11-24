def main():
    from math import factorial

    spisok = list(input().split())
    result = [int(spisok[0])]
    for i in spisok[1:]:
        if i.isdigit():
            result.append(int(i))
        elif i == "/":
            a = result.pop()
            result[-1] //= a
        elif i == "~":
            result[-1] = -result[-1]
        elif i == "!":
            result[-1] = factorial(result[-1])
        elif i == "#":
            result.append(result[-1])
        elif i == "@":
            result.append(result.pop(-3))
        else:
            a = result.pop()
            exec("result[-1] " + i + "= a")
    print(result[0])


if __name__ == "__main__":
    main()