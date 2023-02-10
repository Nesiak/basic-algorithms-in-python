#
def check():
    """super prime number - a number is prime and the sum of its numbers is prime"""
    a = int(input("Enter a number: "))

    i = 1
    counter = 0

    while i<=a:
        if a % i == 0:
            counter+=1
        i+=1

    if counter == 2:
        number = list(str(a))
        total = 0

        for x in number:
            x = int(x)
            total+=x
            count = 0

            z = 1
            while z<=total:
                if total % z == 0:
                    count+=1
                z+=1
        if count == 2:
            print("yes")
        else:
            print("no")
    else:
        print("no")
check()