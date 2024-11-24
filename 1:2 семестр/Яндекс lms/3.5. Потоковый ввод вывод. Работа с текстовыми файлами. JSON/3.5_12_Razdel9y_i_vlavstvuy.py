from sys import stdin

files = [name.strip() for name in stdin]
result = []
with open(files[0]) as file_in:
    for line in file_in:
        result.append(line.split())
D = dict(zip([1, 2, 3], ['>', '<', '==']))
for n in range(1, len(files)):
    with open(files[n], 'w') as file_out:
        for line in result:
            for i in line:
                if eval('len(list(filter(lambda x: not int(x) % 2, i)))'
                        + D[n] +
                        'len(list(filter(lambda x: int(x) % 2, i)))'):
                    print(i, end=' ', file=file_out)
            print('\n', end='', file=file_out)