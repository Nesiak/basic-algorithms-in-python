#sprawdzenie czy suma cyfr w 10 jest równa sumie cyfr w 2
a = int(input("> "))
liczba = []
l = list(str(a))
suma = 0

for x in l:
    suma += int(x)

while a != 0:
    if a % 2 == 0:
        liczba.append(0)
        a = a // 2
    elif a % 2 == 1:
        liczba.append(1)
        a = a // 2

liczba.reverse()
sumab = 0

for x in liczba:
    sumab += x

if suma == sumab:
    print("tak")
else:
    print("nie")