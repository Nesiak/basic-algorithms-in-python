def find_min_index(list):
    minimum = list[0]
    min_index = 0
    for i in range(1,len(list)):
        if minimum > list[i]:
            minimum = list[i]
            min_index = i
    return min_index
def sort(list):
    for i in range(len(list)):
        temp = list[i]
        min_index = find_min_index(list[i:len(list)])+i
        list[i] = list[min_index]
        list[min_index] = temp
    return list
lista = [5,9,11,2,1,8]
print('List before sorting: ')
print(lista)
print('List after sorting: ')
print(sort(list))
