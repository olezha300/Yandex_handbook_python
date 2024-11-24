k = 0
while (forest := input()) != "Приехали!":
    if "зайка" in forest:
        k += 1
print(k)