def Det_sad(children):
    result = ''
    for i in range(children):
        mx_digit = 0
        x = int(input())
        while x:
            mx_digit = max(mx_digit, x % 10)
            x //= 10
        result += str(mx_digit)
    print(result)


if __name__ == "__main__":
    Det_sad(int(input()))