from itertools import cycle

count_of_foods = int(input())
foods = [input() for _ in range(count_of_foods)]
days, count = int(input()), 0
for food in cycle(foods):
    if count < days:
        print(food)
        count += 1
    else:
        break