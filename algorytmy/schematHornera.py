def schematHornera():
    baza = int(input("> "))
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")

    w = 0
    l = [a, b, c]

    for i in l:
        w += baza
        w += int(i)
        
    return w
