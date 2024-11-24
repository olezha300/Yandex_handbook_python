from itertools import count

list_of_numbers = [float(x) for x in input().split()]
for value in count(list_of_numbers[0], list_of_numbers[2]):
    if value <= list_of_numbers[1]:
        print(f"{round(value, 2):.2f}")
    else:
        break