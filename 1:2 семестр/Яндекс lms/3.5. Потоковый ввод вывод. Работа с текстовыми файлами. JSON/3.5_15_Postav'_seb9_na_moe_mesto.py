import json
from sys import stdin

answers = [i.strip() for i in stdin]
with open("scoring.json", "r", encoding="UTF-8") as file_in:
    data = json.load(file_in)
data = [{y["pattern"]: x["points"] // len(x["tests"]) for y in x["tests"]} for x in data]
result, counter = 0, 0
for i in data:
    for j in range(counter, len(i) + counter):
        if answers[j] in i:
            result += i[answers[j]]
        counter += 1
print(result)