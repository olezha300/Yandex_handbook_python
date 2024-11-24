# Ломать — не строить

def func(a, b):
    return a + b


def main():
    try:
        func('a', None)
    except ValueError:
        print("Ура! Ошибка!")


if __name__ == "__main__":
    main()
    