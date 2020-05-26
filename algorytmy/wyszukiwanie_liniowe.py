def wyszukiwanie(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1
lista = [7,32,12,4,5,16,5]
print(wyszukiwanie(lista, 16))