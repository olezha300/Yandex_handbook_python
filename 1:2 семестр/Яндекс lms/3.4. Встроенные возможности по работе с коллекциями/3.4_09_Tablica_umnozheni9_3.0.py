from itertools import product

number = int(input())
list_of_numbers = [int(numbers) for numbers in range(1, number + 1)]
for index, i in enumerate(product(list_of_numbers, list_of_numbers), 1):
    print(i[0] * i[1], end=' ')
    if index % number == 0:
        print()