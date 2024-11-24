class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    elif all(letter.lower() not in ('йцукенгшщзхъёфывапролджэячсмитьбю') for letter in name):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name


print(name_validation("иванов"))
