def check():
    """checking if the sum of the digits in 10 is equal to the sum of the digits in 2"""
    a = int(input("> "))
    number = []
    l = list(str(a))
    total = 0

    for x in l:
        total += int(x)

    while a != 0:
        if a % 2 == 0:
            number.append(0)
            a = a // 2
        elif a % 2 == 1:
            number.append(1)
            a = a // 2

    number.reverse()
    totalb = 0

    for x in number:
        totalb += x

    if total == totalb:
        return "yes"
    else:
        return "no"
