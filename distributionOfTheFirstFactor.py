def distributionOfTheFirstFactor():
    number = int(input("> "))
    i = 2
    e = number ** 2
    
    while i <= e:
        while number % i == 0:
            number = number / i
            e = number ** 2
            print(i)    
        i += 1
