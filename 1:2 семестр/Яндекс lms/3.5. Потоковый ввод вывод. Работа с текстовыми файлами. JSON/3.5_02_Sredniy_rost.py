from sys import stdin

difference = []
lines = [line.rstrip("\n").split() for line in stdin]
for line in lines:
    growth = [int(numbers) for numbers in line[1:]]
    difference.append(growth[-1] - growth[0])
print(round(sum(difference) / len(difference)))