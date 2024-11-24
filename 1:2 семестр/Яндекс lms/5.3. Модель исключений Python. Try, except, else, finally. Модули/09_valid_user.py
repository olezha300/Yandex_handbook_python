class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    elif all(letter.lower() not in ('йцукенгшщзхъёфывапролджэячсмитьбю') for letter in name):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name


def username_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    elif sum((letter.lower() not in "qwertyuiopasdfghjklzxcvbnm1234567890_") for letter in name):
        raise BadCharacterError
    elif name[0].isdigit():
        raise StartsWithDigitError
    return name


def user_validation(**kwargs):
    for key, value in kwargs.items():
        if (
            key not in ("last_name", "first_name", "username")
            and len(kwargs.keys()) == 3
        ) or len(kwargs.keys()) != 3:
            raise KeyError
        elif not isinstance(value, str):
            raise TypeError
    kwargs["last_name"] = name_validation(kwargs["last_name"])
    kwargs["first_name"] = name_validation(kwargs["first_name"])
    kwargs["username"] = username_validation(kwargs["username"])
    return kwargs
        
        
print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))
