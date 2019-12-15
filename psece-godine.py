
x = int(input("Ljudske godina: "))
while x >= 0:
    if 0 <= x <= 2:
        x = x * 10.5
    elif x > 2:
        x = 21 + (x - 2) * 4
    print("Pseće godine: " + " " + str(x))
    break
else:
    print("Krivi unos")


