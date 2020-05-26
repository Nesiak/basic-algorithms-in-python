def szyfrPrzestawieniowy(tekst):
    tekstTab = []
    
    for i in tekst:
        tekstTab.append(i)
    
    n = len(tekstTab)
    
    for i in range(0, n - 1, 2):
        tmp = tekstTab[i]
        tekstTab[i] = tekstTab[i + 1]
        tekstTab[i + 1] = tmp
    
    napis = ''
    for i in tekstTab:
        napis += i
    return napis
