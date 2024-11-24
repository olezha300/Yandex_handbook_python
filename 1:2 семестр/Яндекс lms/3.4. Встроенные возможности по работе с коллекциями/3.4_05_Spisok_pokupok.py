d = set()
string = input()
while string != "":
    for i in string.split(", "):
        d.add(i)
for index, value in enumerate(sorted(d), 1):
    print(f"{index}. {value}")