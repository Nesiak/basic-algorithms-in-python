#liczba superpierwsza - liczba jest pierwsza i suma jej liczb jest pierwsza

a = int(input("Podaj liczbę\n"))

i = 1
licznik = 0

while i<=a:
    if a % i == 0:
        licznik+=1
    i+=1

if licznik == 2:
    liczba = list(str(a))
    suma = 0
    
    for x in liczba:
        x = int(x)
        suma+=x
        licz = 0
        
        z = 1
        while z<=suma:
            if suma % z == 0:
                licz+=1
            z+=1
    if licz == 2:
        print("tak")
    else:
        print("nie")
else:
    print("nie")