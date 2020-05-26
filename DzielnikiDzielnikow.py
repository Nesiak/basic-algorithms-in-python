#wypisz dzielniki dzielników podanej liczby

a = int(input("Podaj liczbę\n"))

i = 1
dz = []

while i<=a:
    if a % i == 0:
        dz.append(i)
    i+=1

for x in dz:
    z = 1
    while z<=x:
        if x % z == 0:
            print(f'Dzielnik {x}: {z}\n')
        z+=1