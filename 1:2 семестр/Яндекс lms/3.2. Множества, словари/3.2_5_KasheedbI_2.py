def main():
    N, M = int(input()), int(input())
    res = []
    for i in range(N + M):
        res.append(input())
    q = len([i for i in res if res.count(i) == 1])
    print(q if q > 9 else "Таких нет")
    
    
if __name__ == "__main__":
    main()