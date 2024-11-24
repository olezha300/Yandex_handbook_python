d = []
for i in range(int(input())):
    d += (input().split(', '))
for index, value in enumerate(sorted(d), 1):
    print(f"{index}. {value}")