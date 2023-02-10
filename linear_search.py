def linear_search(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1
list = [7,32,12,4,5,16,5]
print(linear_search(list, 16))
