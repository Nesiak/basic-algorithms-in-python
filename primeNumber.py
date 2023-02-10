def prime_number(number):
    """Checks if given number is a prime number. Takes one argument."""
    i = 1
    counter = 0
    
    while i <= number:
        if number % i == 0:
            number += 1
        i += 1
        
    if counter == 2:
        return True
    else:
        return False
