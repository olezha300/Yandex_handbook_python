from sys import stdin
import json

data = [line.strip() for line in stdin]
D = {line.split(' == ')[0]: line.split(' == ')[1] for line in data[1:]}
with open(data[0], "r", encoding="UTF-8") as file_in:
    records = json.load(file_in)
records.update(D)
if len(data) > 1:
    with open(data[0], "w", encoding="UTF-8") as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2, sort_keys=True)