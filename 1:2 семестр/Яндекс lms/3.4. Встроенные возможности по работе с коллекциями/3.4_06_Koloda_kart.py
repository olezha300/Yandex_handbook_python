from itertools import product

nominal = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "валет", "дама", "король", "туз"]
suit = ["пик", "треф", "бубен", "червей"]
suit.remove(input())
for i in product(nominal, suit):
    print(' '.join(i))