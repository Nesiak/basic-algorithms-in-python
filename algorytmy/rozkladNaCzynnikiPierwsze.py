def rozkladNaCzynnikiPierwsze():
    liczba = int(input("> "))
    i = 2
    e = liczba ** 2
    
    while i <= e:
        while liczba % i == 0:
            liczba = liczba / i
            e = liczba ** 2
            print(i)    
        i += 1
