lst = []


def modern_print(string):
    if string not in lst:
        print(string)
        lst.append(string)