def sortowaniePrzezWstawianie(tab):
    n = len(tab)
    current = None
    otherIndex = None
    
    for i in range(1, n, 1):
        current = tab[i]
        otherIndex = i
        
        while otherIndex > 0 and current < tab[otherIndex - 1]:
            tab[otherIndex] = tab[otherIndex - 1]
            otherIndex -= 1
            
        tab[otherIndex] = current
        
    return tab

print(sortowaniePrzezWstawianie([1, 2, 3, 1, -2, -5, 15, 13, 17, 11, 10, 12, 11]))