def Happy_new_year(count):
    k = 1
    j = 1
    if count > 0:
        while k <= count:
            for i in range(k, k + j):
                if i <= count:
                    print(i, end=' ')
            k += j
            j += 1
            print()


if __name__ == "__main__":
    Happy_new_year(int(input()))