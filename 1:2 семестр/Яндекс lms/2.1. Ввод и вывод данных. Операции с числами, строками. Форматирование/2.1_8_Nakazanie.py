def solution(*args, **kwargs):
    spisok = [*args]
    N = spisok[0]
    phrase = spisok[1]
    if N > 0:
        for i in range(N):
            print('Я больше никогда не буду писать "' + phrase + '"!')


def main():
    N = int(input())
    phrase = input()
    solution(N, phrase)


if __name__ == "__main__":
    main()