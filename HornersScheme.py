def hornera_scheme():
    base = int(input("> "))
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")

    w = 0
    l = [a, b, c]

    for i in l:
        w += base
        w += int(i)
        
    return w
