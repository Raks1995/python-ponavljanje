print("Za izlazak iz programa upisi q")
x = 0
y = 0

while True:
    smjer = input("Upisi smjer: ")
    for smjer in smjer:
        if smjer.lower() == "u":
            y = y + 1
            print("Position = ({0},{1})".format(x, y))
        elif smjer.lower() == "d":
            y = y - 1
            print("Position = ({0},{1})".format(x, y))
        elif smjer.lower() == "l":
            x = x - 1
            print("Position = ({0},{1})".format(x, y))
        elif smjer.lower() == "r":
            x = x + 1
            print("Position = ({0},{1})".format(x, y))
        elif smjer.lower() != "u" and "r" and "l" and "d" and "q":
            print("Ne prepoznajem unos")
    else:
        if smjer.lower() == "q":
            break
print("Final position = ({0},{1})".format(x, y))




