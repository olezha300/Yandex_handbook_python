def solution(*args, **kwargs):
    spisok = [*args]
    elf = spisok[0]
    gnoms = spisok[1]
    people = spisok[2]
    if 10 <= elf <= 99 and 10 <= gnoms <= 99 and 10 <= people <= 99:
        if str(elf)[0] == str(gnoms)[0] and str(elf)[0] == str(people)[0] and str(gnoms)[0] == str(people)[0]:
            print(str(elf)[0])
        elif str(elf)[1] == str(gnoms)[1] and str(elf)[1] == str(people)[1] and str(gnoms)[1] == str(people)[1]:
            print(str(elf)[1])
        elif str(elf)[2] == str(gnoms)[2] and str(elf)[2] == str(people)[2] and str(gnoms)[2] == str(people)[2]:
            print(str(elf)[2])


def main():
    elf = int(input())
    gnoms = int(input())
    people = int(input())
    solution(elf, gnoms, people)


if __name__ == "__main__":
    main()