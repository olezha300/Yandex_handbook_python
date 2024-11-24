def rindex(text):
    for letter in sorted({i for i in text if i.isalpha()}):
        yield letter, text.rindex(letter)