y = int(input("Broj redaka: "))
brojac = 1

for brojredaka in range(1, y + 1):
    for brojstupaca in range(0, brojredaka):
        print(brojac, end="")
        brojac = brojac + 1
    print()
