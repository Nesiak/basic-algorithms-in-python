def affiliation_point_to_Segment():
    Ax = float(input("Ax: "))
    Ay = float(input("Ay: "))

    Bx = float(input("Bx: "))
    By = float(input("By: "))

    Cx = float(input("Cx: "))
    Cy = float(input("Cy: "))


    # formula: (Y - Ya)(Xb - Xa) - (Yb - Ya)(X - Xa) = 0
    # after conversion: Xb * Y + Xa * Ya + X  * Ya - Xa * Y - Xb * Ya - X * Yb
    
    expression = Bx * Cy + Ax * Ay + Cx * Ay - Ax * Cy - Bx * Ay - Cx * By
    if expression == 0:
        return True
    else:
        return False
