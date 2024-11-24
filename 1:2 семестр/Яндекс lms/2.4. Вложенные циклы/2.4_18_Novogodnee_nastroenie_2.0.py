stroka = ''
lengths = [0]
for j in range(1, (x := int(input())) + 1):
    stroka += str(j) + ' '
    if j in (sum(range(i)) for i in range(j + 2)):
        lengths.append(len(stroka) - 1)
        stroka = ''
lengths.append(len(stroka) - 1)
d = 1
for k in range(1, x + 1):
    if k - 1 in (sum(range(i)) for i in range(k + 2)):
        print(f"{' ' * ((max(lengths) - lengths[d]) // 2)}{k}", end=' ' if k != 1 else '\n')
        d += 1
    else:
        print(k, end='\n' if k in (sum(range(i)) for i in range(k + 2)) else ' ')