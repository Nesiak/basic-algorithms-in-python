def przynaleznoscPunktuDoOdcinka():
    Ax = float(input("Ax: "))
    Ay = float(input("Ay: "))

    Bx = float(input("Bx: "))
    By = float(input("By: "))


    Cx = float(input("Cx: "))
    Cy = float(input("Cy: "))

    # wzór: (Y - Ya)(Xb - Xa) - (Yb - Ya)(X - Xa) = 0
    # po przekształceniu: Xb * Y + Xa * Ya + X  * Ya - Xa * Y - Xb * Ya - X * Yb
    
    wyrazenie = Bx * Cy + Ax * Ay + Cx * Ay - Ax * Cy - Bx * Ay - Cx * By
    if wyrazenie == 0:
        return True
    else:
        return False
