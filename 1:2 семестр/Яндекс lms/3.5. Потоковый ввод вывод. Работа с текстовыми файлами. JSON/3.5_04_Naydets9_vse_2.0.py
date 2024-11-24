from sys import stdin

lines = [line.rstrip("\n") for line in stdin]
main_word = lines.pop()
for line in lines:
    if main_word.lower() in line.lower():
        print(line)