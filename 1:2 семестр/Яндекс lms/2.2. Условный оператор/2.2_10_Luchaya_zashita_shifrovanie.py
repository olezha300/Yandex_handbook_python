def solution(*args, **kwargs):
    spisok = [*args]
    n = spisok[0]
    summa_1 = n % 10 + n // 10 % 10
    summa_2 = n // 100 + n // 10 % 10
    if summa_1 > summa_2:
        print(str(summa_1) + str(summa_2))
    else:
        print(str(summa_2) + str(summa_1))
    

def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()