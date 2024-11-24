def clear(number):
    result = 0
    if number > 0:
        while number:
            if (number % 10) % 2 == 0:
                number //= 10
            else:
                result *= 10
                result += number % 10
                number //= 10
        print(str(result)[::-1])


if __name__ == "__main__":
    clear(int(input()))