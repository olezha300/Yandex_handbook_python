alphabet = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ь": "",
    "Ъ": "",
}
x, y = "", ""
with open("cyrillic.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        x += line

for i in x:
    if i.upper() in alphabet:
        y += (
            alphabet[i.upper()].lower().capitalize()
            if i == i.upper()
            else alphabet[i.upper()].lower()
        )
    else:
        y += i

with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    print(y, file=file_out)