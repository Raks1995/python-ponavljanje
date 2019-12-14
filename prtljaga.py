while True:
    x = float(input("Unesite kilažu(kg): "))
    nadoplata = "Nadoplata iznosi:" + " " + str(round((x - 15) * 50)) + " " + "kn"
    if x < 0:
        print("Nedopušten unos")
    elif x > 50:
        print("Nedopušten unos")
    elif x <= 15:
        print("Nema nadoplate")
        break
    elif 15 < x < 50:
        print(nadoplata)
        break
