F, N = input(), int(input())
result, my_list = [], []
with open(F, "r", encoding="UTF-8") as file_in:
    for line in file_in:
        result.append(line.rstrip("\n"))
result = result[::-1]
for i in result[:N]:
    my_list.append(i)
for j in my_list[::-1]:
    print(j)