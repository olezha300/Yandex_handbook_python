def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(f"({a} ^ {b}) mod ({a} + {c}) = {(a ** b) % (a + c)}")


if __name__ == "__main__":
    main()