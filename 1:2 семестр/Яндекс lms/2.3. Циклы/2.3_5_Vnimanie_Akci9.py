suma = 0
while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
        suma += price
    else:
        suma += price
print(suma)