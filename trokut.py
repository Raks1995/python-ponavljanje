print("Program provjerava vrstu trokuta.")

a = int(input("Prva stranica: "))
b = int(input("Druga stranica: "))
c = int(input("Treća stranica: "))

if a == b == c:
    print("Trokut je jednakostraničan")
elif a == b != c or a != b == c or a == c != b:
    print("Trokut je jednakokračan")
elif a != b != c:
    print("Trokut je raznostraničan")







