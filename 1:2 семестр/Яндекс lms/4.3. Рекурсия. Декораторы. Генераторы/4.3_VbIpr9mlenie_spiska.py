def make_linear(inner_list):
    my_list = []
    for i in inner_list:
        if type(i) is not list:
            my_list.append(i)
        else:
            my_list.extend(make_linear(i))
    return my_list