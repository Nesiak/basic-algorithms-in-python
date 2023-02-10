a = int(input("Enter the number\n"))

i = 1
dividers = []

while i<=a:
    if a % i == 0:
        dividers.append(i)
    i+=1

for x in dividers:
    print(f"Divisor of a number {a}: {x}\n")
