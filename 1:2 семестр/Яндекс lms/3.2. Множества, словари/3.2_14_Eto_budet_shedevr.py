def main():
    res, d = [], set()
    for i in range(int(input())):
        res.append(input())
    for j in range(int(input())):
        d.add(x := input())
        for k in range(int(input())):
            if input() not in res:
                d.discard(x)
    if len(d) > 0:
        print('\n'.join(sorted(d)))
    else:
        print("Готовить нечего")


if __name__ == "__main__":
    main()  