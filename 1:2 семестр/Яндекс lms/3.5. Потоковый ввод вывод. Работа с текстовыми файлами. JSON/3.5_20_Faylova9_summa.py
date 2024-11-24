with open("numbers.num", "rb", encoding="UTF-8") as file_in:
    data = file_in.read()
print(sum([int.from_bytes(data[i:i + 2], "big") for i in range(0, len(data), 2)]) % 2**16)