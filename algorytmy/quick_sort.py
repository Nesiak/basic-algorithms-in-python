def quick_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivot = lista[0]
        mniej = [i for i in lista[1:] if i <= pivot]
        wiecej = [i for i in lista[1:] if i > pivot]
        return quick_sort(mniej) + [pivot] + quick_sort(wiecej)
print(quick_sort([10,5,2,3]))
