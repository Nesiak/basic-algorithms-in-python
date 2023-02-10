def check_location():
    print("Give a and b the equation of the line.\n")
    a = int(input("a > "))
    b = int(input("b > "))
    
    print("Give the x and y coordinates of the point")
    x = int(input("x > "))
    y = int(input("y > "))
    
    if y == a * x + b:
        return True
    else:
        return False
