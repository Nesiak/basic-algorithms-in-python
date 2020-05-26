a = int(input("Podaj liczbę\n"))
b = int(input("Podaj liczbę\n"))

def pierwsza(x):
    i = 1
    dz = []
    while i<=x:
        if x % i == 0:
            dz.append(i)
        i+=1
    return dz

taba = pierwsza(a)
tabb = pierwsza(b)

licznik = 0

for z in taba:
    for y in tabb:
        if z == y:
            licznik+=1

if licznik == 1:
    print("tak")
else:
    print("nie")