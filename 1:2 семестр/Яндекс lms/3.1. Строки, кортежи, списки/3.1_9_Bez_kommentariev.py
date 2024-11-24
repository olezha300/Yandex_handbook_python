def No_comm():
    while (s := input()):
        if not s.startswith("#"):
            print(s[:s.find("#") if "#" in s else len(s)])


if __name__ == "__main__":
    No_comm()