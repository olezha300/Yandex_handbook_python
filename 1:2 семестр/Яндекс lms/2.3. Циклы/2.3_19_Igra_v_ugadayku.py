start = 1
end = 1001
print((start + end) // 2)
while (x := input()) != 'Угадал!':
    if x == 'Меньше':
        end = (start + end) // 2
        print((start + end) // 2)
    elif x == 'Больше':
        start = (start + end) // 2
        print((start + end) // 2)
print('=' * 35)