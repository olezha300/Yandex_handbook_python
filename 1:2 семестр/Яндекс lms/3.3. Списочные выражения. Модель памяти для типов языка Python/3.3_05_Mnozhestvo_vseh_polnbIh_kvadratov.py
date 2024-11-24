numbers = [number for number in range(16, 100, 4)]
print({x for x in numbers if x in [i ** 2 for i in range(1, int(max(numbers)))]})