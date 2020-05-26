def czyPunktNalezyDoProstej():
    print("Podaj a i b równanie prostej")
    a = int(input("> "))
    b = int(input("> "))
    
    print("Podaj współrzędne x i y punktu")
    x = int(input("> "))
    y = int(input("> "))
    
    if y == a * x + b:
        return True
    else:
        return False