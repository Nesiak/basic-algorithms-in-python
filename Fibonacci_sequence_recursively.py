def Fibonacci_sequence(n):
    if n < 3:
        return 1
    
    return Fibonacci_sequence(n - 2) + Fibonacci_sequence(n - 1)

print(Fibonacci_sequence(12))

