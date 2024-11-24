# Ломать - не строить 2

class Error(Exception):
    def __repr__(self):
        raise Exception


def func(a, b, c):
    return ''.join(map(str, (a, b, c)))


def main():
    try:
        func(Error)
    except Exception:
        print("Ура! Ошибка!")


if __name__ == "__main__":
    main()
    