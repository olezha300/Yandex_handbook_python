from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    password: str,
    min_length: int = 8,
    possible_chars: str = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890",
    at_least_one: bool = str.isdigit,
) -> str:
    if not isinstance(password, str):
        raise TypeError
    elif len(password) < min_length:
        raise MinLengthError
    elif any(symbol not in possible_chars for symbol in password):
        raise PossibleCharError
    elif not any(map(at_least_one, password)):
        raise NeedCharError
    return sha256(password.encode()).hexdigest()


print(password_validation("Hello12345"))
