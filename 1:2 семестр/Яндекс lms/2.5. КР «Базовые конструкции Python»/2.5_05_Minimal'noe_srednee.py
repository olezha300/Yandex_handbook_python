def main():
    N = int(input())
    res = []
    res_1 = []
    for i in range(N):
        while (x := input()) != "end":
            res.append(int(x))
        res_1.append(round(sum(res) / len(res), 2))
        res.clear()
    print(f"{min(res_1):.2f}")


if __name__ == "__main__":
    main()