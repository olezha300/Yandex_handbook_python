import json

numbers, statistics = input(), input()
result, answer = [], []
with open(numbers, "r", encoding="UTF-8") as file_in:
    for line in file_in:
        result.append([int(x) for x in line.strip("\n").split()])
for i in result:
    answer.extend(i)
d = {
    "count": len(answer),
    "positive_count": len([int(x) for x in answer if x > 0]),
    "min": min(answer),
    "max": max(answer),
    "sum": sum(answer),
    "average": round(sum(answer) / len(answer), 2)
}
with open(statistics, "w", encoding="UTF-8") as file_out:
    print(json.dumps(d, indent=2, ensure_ascii=False), file=file_out)