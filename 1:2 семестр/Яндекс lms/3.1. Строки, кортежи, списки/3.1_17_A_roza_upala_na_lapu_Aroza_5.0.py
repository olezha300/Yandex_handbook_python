def main():
    s = ''.join(input().lower().split())
    print("YES" if s == s[::-1] else "NO")


if __name__ == "__main__":
    main()