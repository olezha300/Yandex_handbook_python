def Azbuka(N):
    if N > 0:
        for i in range(N):
            s = input()
            if s[0] not in "абв":
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    Azbuka(int(input()))