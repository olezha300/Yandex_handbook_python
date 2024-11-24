def Clear():
    while (s := input()):
        if not s.endswith("@@@"):
            if s.startswith("##"):
                print(s[2:])
            else:
                print(s)


if __name__ == "__main__":
    Clear()