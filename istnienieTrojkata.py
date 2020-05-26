def istnienieTrojkata(a, b, c):
    if a > b and a > c:
        if a < b + c:
            return True
    
    if b > a and b > c:
        if b < a + c:
            return True
    
    if c > a and c > b:
        if c < a + b:
            return True
    
    if a == b and b == c:
        return True
    
    return False