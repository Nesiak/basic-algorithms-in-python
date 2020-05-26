def partition(tab, p, r):
    x = tab[p]
    i = p
    j = r
    tmp = None
    
    while True:
        while tab[j] > x:
            j -= 1
        while tab[i] < x:
            i += 1
        if i < j:
            tmp = tab[i]
            tab[i] = tab[j]
            tab[j] = tmp
            
            i += 1
            j -= 1
        else:
            return j

def quickSort(tab, p, r):
    q = None
    if p < r:
        q = partition(tab, p, r)
        quickSort(tab, p, q)
        quickSort(tab, q + 1, r)

    return tab

tab = [1, 2, 3, 1, -4, -3, 14, 11, 12, 13, 7, 8]
print(quickSort(tab, 0, len(tab) - 1))










            
    