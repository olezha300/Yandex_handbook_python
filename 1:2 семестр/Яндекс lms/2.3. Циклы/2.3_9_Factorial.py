def Factorial(N):
    if N >= 0 and N == 1:
        return N
    if N >= 0 and N != 1:
        return N * Factorial(N - 1)


if __name__ == "__main__":
    print(Factorial(int(input())))