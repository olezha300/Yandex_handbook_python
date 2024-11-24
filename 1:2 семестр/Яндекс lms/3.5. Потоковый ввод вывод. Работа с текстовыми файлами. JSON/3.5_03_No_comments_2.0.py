from sys import stdin

for line in stdin.readlines():
    if not line.startswith("#"):
        print(line[:line.find("#")])