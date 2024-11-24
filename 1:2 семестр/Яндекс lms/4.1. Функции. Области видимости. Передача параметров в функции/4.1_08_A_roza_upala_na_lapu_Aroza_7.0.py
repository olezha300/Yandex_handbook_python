def is_palindrome(x):
    return str(x) == str(x)[::-1] if isinstance(x, int) else x == x[::-1]