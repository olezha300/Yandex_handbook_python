from itertools import product, combinations, islice, filterfalse

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
nominals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
nominals.sort()
suit, nominal = input(), input()
nominals.remove(nominal)
all_cards = product(nominals, sorted(suits.values()))
result = filterfalse(lambda x: not(any(suits[suit] in comb for comb in x)), combinations(all_cards, r=3))
for comb in islice(result, 10):
    print(', '.join([f"{x} {y}" for x, y in comb]))