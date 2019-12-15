a = 5000000
v = 9000000
godine = 0

while v >= a:
    godine = godine + 1
    a = int(a * 1.06)
    if godine % 4 == 0:
        v = int((v -500000) * 1.05)
    else:
        v = int(v * 1.02)
print("Alfonci će premašiti Velonce za {0} godina, pri broju stanovnika od {1}.".format(godine, a))