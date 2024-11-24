from sys import stdin

result = []
lines = [line.strip("\n") for line in stdin]
for line in lines:
    result.extend([x for x in line.split() if x.lower() == x.lower()[::-1]])
for i in sorted(set(result)):
    print(i)