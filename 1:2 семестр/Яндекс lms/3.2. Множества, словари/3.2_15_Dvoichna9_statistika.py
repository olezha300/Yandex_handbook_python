def main():
    numbers = [int(x) for x in input().split()]
    print('[')
    for i in numbers:
        bin_i = bin(i)[2:]
        print('{')
        print(f'"digits": {len(bin_i)},')
        print(f'"units": {bin_i.count("1")},')
        print(f'"zeros": {bin_i.count("0")}')
        print('},')
    print(']')
    

if __name__ == "__main__":
    main()