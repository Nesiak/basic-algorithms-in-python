from math import *

def F(x):
    return x ** 2 - x - 3

def calculate(p, q, n):
    dl = (q - p) / n
    s = 0
    for i in range(n):
        s += fabs(F(p + dl * i + dl / 2))
        
    return dl * s

