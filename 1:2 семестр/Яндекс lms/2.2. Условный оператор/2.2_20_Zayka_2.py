def solution(*args, **kwargs):
    spisok = [*args]
    s1 = spisok[0]
    s2 = spisok[1]
    s3 = spisok[2]
    if s1 > s2 and s1 > s3:
        mx_s = s1
        if s2 > s3:
            mx_s2 = s2
            mn_s = s3
        else:
            mx_s2 = s3
            mn_s = s2
    elif s2 > s1 and s2 > s3:
        mx_s = s2
        if s3 > s1:
            mx_s2 = s3
            mn_s = s1
        else:
            mx_s2 = s1
            mn_s = s3
    else:
        mx_s = s3
        if s2 > s1:
            mx_s2 = s2
            mn_s = s1
        else:
            mx_s2 = s1
            mn_s = s2
    if "зайка" in mn_s:
        print(mn_s, len(mn_s))
    elif "зайка" in mx_s2:
        print(mx_s2, len(mx_s2))
    else:
        print(mx_s, len(mx_s))


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    solution(s1, s2, s3)


if __name__ == "__main__":
    main()