string = 'мама мыла раму'
print(sorted(string.split(), key=lambda x: (len(x), x)))