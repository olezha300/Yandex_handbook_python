def P(number):
    i = 2
    while number > 1:
        if number % i == 0:
            print(i, end=' ')
            number //= i
            if number > 1:
                print("*", end=' ')
        else:
            i += 1


if __name__ == "__main__":
    P(int(input()))