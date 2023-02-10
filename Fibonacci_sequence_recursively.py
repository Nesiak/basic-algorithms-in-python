def fibonacci_sequence(n):
    if n < 3:
        return 1
    
    return fibonacci_sequence(n - 2) + fibonacci_sequence(n - 1)

print(fibonacci_sequence(12))

