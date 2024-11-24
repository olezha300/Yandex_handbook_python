def table_multiplication(size):
    if size > 0:
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                print(i * j, end=' ')
            print()


if __name__ == "__main__":
    table_multiplication(int(input()))