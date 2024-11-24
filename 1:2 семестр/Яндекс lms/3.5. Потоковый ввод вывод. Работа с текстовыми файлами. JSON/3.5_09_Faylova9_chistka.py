first, second = input(), input()
result = []
with open(first, "r", encoding="UTF-8") as file_in:
    for line in file_in:
        result.append(line.strip().replace("\t", '').split())
result = [i for i in result if i != []]
with open(second, "w", encoding="UTF-8") as file_out:
    for line in result:
        print(' '.join(line), file=file_out)