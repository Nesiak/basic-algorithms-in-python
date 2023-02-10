def bubble_sort():
"""bubble sort compares pairs of numbers one by one and swaps their order"""
    list = [9,6,7,2,1,4]
    for x in list:
        print(x, end=', ')
    print('')
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if lista[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        for x in list:
            print(x, end=', ')
        print('')


