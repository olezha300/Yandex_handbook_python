def P(number):
    new_number = 0
    old_number = number
    if number > 0:
        while old_number:
            new_number *= 10
            new_number += old_number % 10
            old_number //= 10
        if new_number == number:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    P(int(input()))