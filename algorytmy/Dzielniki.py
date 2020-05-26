a = int(input("Podaj liczbę\n"))

i = 1
dz = []

while i<=a:
    if a % i == 0:
        dz.append(i)
    i+=1

for x in dz:
    print(f'Dzielnik liczby {a}: {x}\n')