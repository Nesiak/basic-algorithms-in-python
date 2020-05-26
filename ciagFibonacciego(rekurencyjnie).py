def ciagFib(n):
    if n < 3:
        return 1
    
    return ciagFib(n - 2) + ciagFib(n - 1)

print(ciagFib(12))

