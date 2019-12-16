d = input("Krvna grupa donora: ")
r1 = input("Rh faktor donora: ")
p = input("Krvna grupa primatelja: ")
r2 = input("Rh faktor primatelja: ")
x = "Dopušteno"
y = "Nedopušteno"

if d == p and r1 == r2:
    print(x)
elif d == p and r1 == "-" and r2 == "+":
    print(x)
elif d == "0" and p == "a" or p == "b" or p == "c" and r1 == r2:
    print(x)
elif d == "0" and p == "a" or p == "b" or p == "c" and r1 == "-" and r2 == "+":
    print(x)
elif p == "c" and d == "a" or d == "b" and r1 == r2:
    print(x)
elif p == "c" and d == "a" or d == "b" and r1 == "-" and r2 == "+":
    print(x)
else:
    print(y)

