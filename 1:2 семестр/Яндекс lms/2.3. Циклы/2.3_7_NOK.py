def NOD(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return first_number


def NOK(first_number, second_number):
    print(first_number * second_number // NOD(first_number, second_number))
    
    
if __name__ == "__main__":
    NOK(int(input()), int(input()))