def search(list, x):
    l = 0
    r = len(list)

    while l <= r:
        mid = l + int((r-l)/2)
        if list[mid] == x:
            return mid
        elif list[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
list = [32, 45, 8, 3, 12, 9]
print(search(list, 9))
