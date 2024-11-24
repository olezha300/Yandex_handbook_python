def count(start, end):
    if start < end:
        for i in range(start, end + 1):
            print(i, end=' ')
    else:
        for i in range(start, end - 1, -1):
            print(i, end=' ')


if __name__ == "__main__":
    count(int(input()), int(input()))