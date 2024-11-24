numbers = {15, 49, 36}
print({digit: [i for i in range(1, digit + 1) if not digit % i] for digit in numbers})