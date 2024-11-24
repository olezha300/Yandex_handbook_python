def solution(*args, **kwargs):
    spisok = [*args]
    p = spisok[0]
    v = spisok[1]
    t = spisok[2]
    if p > t and p > v:
        first = "Петя"
        if t > v:
            second = "Толя"
            third = "Вася"
        else:
            second = "Вася"
            third = "Толя"
    elif t > p and t > v:
        first = "Толя"
        if p > v:
            second = "Петя"
            third = "Вася"
        else:
            second = "Вася"
            third = "Петя"
    else:
        first = "Вася"
        if t > p:
            second = "Толя"
            third = "Петя"
        else:
            second = "Петя"
            third = "Толя"
    print(f'{"": ^8}{first: ^8}{"": ^8}')
    print(f'{second: ^8}{"": ^8}{"": ^8}')
    print(f'{"": ^8}{"": ^8}{third: ^8}')
    print(f'{"II": ^8}{"I": ^8}{"III": ^8}')

def main():
    p = int(input())
    v = int(input())
    t = int(input())
    solution(p, v, t)


if __name__ == "__main__":
    main()