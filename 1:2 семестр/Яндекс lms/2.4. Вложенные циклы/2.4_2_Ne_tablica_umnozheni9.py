def Not_table_multiplication(size):
    if size > 0:
        for j in range(1, size + 1):
            for i in range(1, size + 1):
                print(i, '*', j, '=', i * j)


if __name__ == "__main__":
    Not_table_multiplication(int(input()))