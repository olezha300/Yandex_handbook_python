from itertools import product, combinations, islice, filterfalse, dropwhile

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
nominals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
nominals.sort()
suit, nominal, combination = input(), input(), input()
combination = tuple(tuple(c for c in x.split()) for x in combination.split(', '))
nominals.remove(nominal)
all_cards = product(nominals, sorted(suits.values()))
result = dropwhile(lambda s: s != combination, 
                   filterfalse(lambda x: not(any(suits[suit] in comb for comb in x)), 
                                                           combinations(all_cards, r=3)))
comb = list(result)[1]
print(', '.join([f"{x} {y}" for x, y in comb]))