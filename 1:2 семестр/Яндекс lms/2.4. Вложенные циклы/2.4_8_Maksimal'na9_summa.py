def Det_sad(children):
    name = ''
    s = 0
    for i in range(children):
        temp_name = input()
        temp_s = sum(map(int, input()))
        if temp_s >= s:
            name = temp_name
            s = temp_s
    print(name)


if __name__ == "__main__":
    Det_sad(int(input()))