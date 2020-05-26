def szyfrCezara(tekst, alfabet, key):
    wynik = ''
    dlT = len(tekst)
    dlA = len(alfabet)
    
    for i in range(dlT):
        for j in range(dlA):
            if tekst[i] == alfabet[j]:
                wynik += alfabet[(j + key) % dlA]
    
    return wynik
    
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'