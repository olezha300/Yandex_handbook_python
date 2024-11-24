def Orange(orange):
    for i in range(1, orange - 1):
        if i == 1:
            print("А Б В")
        for j in range(1, orange - i):
            print(f"{i} {j} {orange - i - j}")


if __name__ == "__main__":
    Orange(int(input()))