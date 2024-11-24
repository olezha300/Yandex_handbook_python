def solution(*args, **kwargs):
    spisok = [*args]
    a = spisok[0]
    b = spisok[1]
    c = spisok[2]
    if a == 0:
        if b == 0:
            if c == 0:
                print("Infinite solutions")
            else:
                print("No solution")
        else:
            print(-c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            print("No solution")
        elif d == 0:
            print(-b / (2 * a))
        else:
            sol1 = (-b - d ** 0.5) / (2 * a)
            sol2 = (-b + d ** 0.5) / (2 * a)
            if sol1 > sol2:
                print(f"{sol2:0.2f} {sol1:0.2f}")
            else:
                print(f"{sol1:0.2f} {sol2:0.2f}")


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    solution(a, b, c)


if __name__ == "__main__":
    main()