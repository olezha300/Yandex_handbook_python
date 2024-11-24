def main():
    alpha = []
    while (s := input()) != "ФИНИШ":
        alpha.extend(s.lower().split())
    mx, alpha = 0, ''.join(alpha)
    for i in set(alpha):
        mx = max(mx, alpha.count(i))
    print(min([j for j in set(alpha) if alpha.count(j) == mx]))

    
if __name__ == "__main__":
    main()