#sprawdzenie czy w zapisie binarnym jest więcej 0 czy 1
a = int(input("> "))
liczba = []

while a != 0:
    if a % 2 == 0:
        liczba.append(0)
        a = a // 2
    elif a % 2 == 1:
        liczba.append(1)
        a = a // 2

liczba.reverse()

licz1 = 0
licz0 = 0

for x in liczba:
    if x == 1:
        licz1+=1
    else:
        licz0+=1

if licz1 > licz0:
    print("jedynek więcej")
elif licz0 > licz1:
    print("zer więcej")
else:
    print("tyle samo")