def Fibonacci_sequence():
    a = 0
    b = 1
    n = int(input("Długość ciągu: "))
    
    for i in range(n):
        print(b)
        b += a
        a = b - a
