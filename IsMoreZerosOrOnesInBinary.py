def check():
    """checking whether there are more 0's or 1's in the binary notation"""
    a = int(input("> "))
    number = []

    while a != 0:
        if a % 2 == 0:
            number.append(0)
            a = a // 2
        elif a % 2 == 1:
            number.append(1)
            a = a // 2

    number.reverse()

    counter1 = 0
    counter0 = 0

    for x in number:
        if x == 1:
            counter1+=1
        else:
            counter0+=1

    if counter1 > counter0:
        print("More One's.")
    elif counter0 > counter1:
        print("More 0's.")
    else:
        print("Same number.")
