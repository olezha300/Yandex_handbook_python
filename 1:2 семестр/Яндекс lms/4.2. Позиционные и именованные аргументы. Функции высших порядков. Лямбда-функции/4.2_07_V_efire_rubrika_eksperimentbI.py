numbers = tuple()
def enter_results(*args, **kwargs):
    global numbers
    numbers += args
    print(numbers)

def get_sum():
    return round(sum(numbers[::2]), 2), round(sum(numbers[1::2]), 2)

def get_average():
    return round(sum(numbers[::2]) / len(numbers[::2]), 2), round(sum(numbers[1::2]) / len(numbers[1::2]), 2)