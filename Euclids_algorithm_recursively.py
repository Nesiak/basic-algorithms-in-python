def euklides(a, b):
    if a != b:
        if a > b:
            tmp1 = a - b
        else:
            tmp1 = a
        
        if b > a:
            tmp2 = b - a
        else:
            tmp2 = b
        
        return euklides(tmp1, tmp2)
    
    return a
