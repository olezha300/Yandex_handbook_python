def Gonki(N):
    if N > 0:
        for i in range(N):
            for j in range(3 + i, 0, -1):
                print(f"До старта {j} секунд(ы)")
            print(f"Старт {i + 1}!!!")


if __name__ == "__main__":
    Gonki(int(input()))