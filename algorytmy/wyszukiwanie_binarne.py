def wyszukiwanie(lista, x):
    l = 0
    r = len(lista)

    while l <= r:
        mid = l + int((r-l)/2)
        if lista[mid] == x:
            return mid
        elif lista[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
lista = [32, 45, 8, 3, 12, 9]
print(wyszukiwanie(lista, 9))