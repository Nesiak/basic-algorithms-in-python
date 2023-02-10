def fibonacci_sequence():
    a = 0
    b = 1
    n = int(input("Length of sequence: "))
    
    for i in range(n):
        print(b)
        b += a
        a = b - a
