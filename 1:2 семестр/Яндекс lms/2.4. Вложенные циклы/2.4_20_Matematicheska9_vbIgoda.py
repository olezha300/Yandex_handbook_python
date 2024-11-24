def G(num, from_base=10, to_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        n, m = divmod(n, to_base)
        result += alphabet[m]
    return result[::-1]


def F(number):
    max_b, best_base = 0, 0
    for base in range(2, 11):
        if (digits_sum := sum(map(int, G(number, 10, base)))) > max_b:
            best_base = base
            max_b = digits_sum
    print(best_base)


if __name__ == "__main__":
    F(int(input()))