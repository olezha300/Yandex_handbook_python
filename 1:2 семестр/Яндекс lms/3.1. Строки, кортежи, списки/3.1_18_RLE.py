def main():
    s = input()
    symbol, count = s[0], 1
    if len(s) >= 1:
        for i in s[1:]:
            if i == symbol:
                count += 1
            else:
                print(symbol, count)
                symbol, count = i, 1
        print(symbol, count)


if __name__ == "__main__":
    main()