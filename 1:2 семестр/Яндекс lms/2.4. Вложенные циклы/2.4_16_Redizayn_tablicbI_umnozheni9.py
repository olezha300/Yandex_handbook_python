def Table_of_multiplication(a, b):
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            if j != a:
                print(f'{(str(i * j) + " " if b % 2 else str(i * j)).center(b)}|', end='')
            else:
                print(f'{(str(i * j) + " " if b % 2 else str(i * j)).center(b)}')
        if i * j != a * a:
            print(f'{"-"* ((b + 1) * a - 1)}')


if __name__ == "__main__":
    Table_of_multiplication(int(input()), int(input()))