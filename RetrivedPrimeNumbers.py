a = int(input("Enter first number: "))
b = int(input("Enter second number:"))

def prime(x):
    i = 1
    dividers = []
    while i<=x:
        if x % i == 0:
            dividers.append(i)
        i+=1
    return dividers

taba = prime(a)
tabb = prime(b)

counter = 0

for z in taba:
    for y in tabb:
        if z == y:
            counter+=1

if counter == 1:
    print("yes")
else:
    print("no")
