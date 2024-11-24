def main():
    result = list(map(int, input().split()))

    def NOD_for_two_numbers(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def NOD_for_many_numbers(numbers):
        ans = numbers[0]
        for i in range(1, len(numbers)):
            ans = NOD_for_two_numbers(ans, numbers[i])
        return ans

    if len(result) == 2:
        print(NOD_for_two_numbers(result[0], result[1]))
    else:
        print(NOD_for_many_numbers(result))


if __name__ == "__main__":
    main()