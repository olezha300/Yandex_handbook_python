def main():
    if (s := input()) == s[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()