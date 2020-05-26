def liczbaPierwsza(liczba):
    i = 1
    licznik = 0
    
    while i <= liczba:
        if liczba % i == 0:
            licznik += 1
        i += 1
        
    if licznik == 2:
        return True
    else:
        return False