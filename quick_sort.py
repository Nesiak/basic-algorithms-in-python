def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        more = [i for i in list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)
print(quick_sort([10,5,2,3]))
