def znajdz_min_index(lista):
    minimum = lista[0]
    min_index = 0
    for i in range(1,len(lista)):
        if minimum > lista[i]:
            minimum = lista[i]
            min_index = i
    return min_index
def sortowanie(lista):
    for i in range(len(lista)):
        temp = lista[i]
        min_index = znajdz_min_index(lista[i:len(lista)])+i
        lista[i] = lista[min_index]
        lista[min_index] = temp
    return lista
lista = [5,9,11,2,1,8]
print('lista przed posortowaniem: ')
print(lista)
print('lista po posortowaniu: ')
print(sortowanie(lista))