#list the divisors of the given number

a = int(input("Enter the number: "))

i = 1
dividers = []

while i<=a:
    if a % i == 0:
        dividers.append(i)
    i+=1

for x in dividers:
    z = 1
    while z<=x:
        if x % z == 0:
            print(f'Divider {x}: {z}\n')
        z+=1
