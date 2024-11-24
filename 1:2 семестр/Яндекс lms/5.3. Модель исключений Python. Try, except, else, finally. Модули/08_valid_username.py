class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    elif sum((letter.lower() not in "qwertyuiopasdfghjklzxcvbnm1234567890_") for letter in name):
        raise BadCharacterError
    elif name[0].isdigit():
        raise StartsWithDigitError
    return name


print(username_validation("45_user"))
