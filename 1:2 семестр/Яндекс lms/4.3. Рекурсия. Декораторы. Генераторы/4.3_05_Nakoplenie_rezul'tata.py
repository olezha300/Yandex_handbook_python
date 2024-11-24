def result_accumulator(func):
    my_list = []
    def wrapper(*args, method="accumulate"):
        my_list.append(func(*args))
        if method == "drop":
            new_list = my_list.copy()
            my_list.clear()
            return new_list
        elif method == "accumulate":
            return None
    return wrapper