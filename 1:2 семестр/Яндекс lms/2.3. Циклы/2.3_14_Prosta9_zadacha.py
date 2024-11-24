def P(N):
    i = 2
    result = 'YES'
    if N > 1:
        while N % i:
            if i > N ** 0.5:
                break
            i += 1
        else:
            result = 'NO'
    else:
        result = 'NO'
    print(result)


if __name__ == "__main__":
    P(int(input()))