n = []


def add_word(word):
    global n
    n.append(word)


def get_work():
    global n
    return ", ".join(n) + f". ({len(n)})"