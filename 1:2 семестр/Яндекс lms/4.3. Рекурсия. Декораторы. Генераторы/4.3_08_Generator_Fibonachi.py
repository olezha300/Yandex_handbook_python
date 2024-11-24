def fibonacci(numbers):
    first_number, second_number = 0, 1
    for _ in range(numbers):
        yield first_number
        first_number, second_number = second_number, first_number + second_number