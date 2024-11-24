def same_type(func):
    def wrapper(*args, **kwargs):
        my_type = type(args[0])
        for arg in args[1:]:
            if type(arg) is not my_type:
                print("Обнаружены различные типы данных")
                break
            return func(*args, **kwargs)

    return wrapper