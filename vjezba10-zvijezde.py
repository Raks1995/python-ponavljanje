a = int(input("Broj redaka: "))
brojac = "*"

for brojredaka in range(1, a + 1):
    for brojstupaca in range(1, brojredaka):
        print(brojac, end="")
    print()
