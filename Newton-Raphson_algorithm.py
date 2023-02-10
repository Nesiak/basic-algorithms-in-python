from math import *

def element(p, E, l):
    a = p
    i = 0
    
    while fabs(a - p / a) > E and i < l:
        a = (a + p / a) / 2
        i += 1
    
    return a
