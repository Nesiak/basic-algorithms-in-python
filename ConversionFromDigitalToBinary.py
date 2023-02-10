#switch from binary to decimal
a = int(input("> "))
number = []

while a != 0:
    if a % 2 == 0:
        number.append(0)
        a = a // 2
    elif a % 2 == 1:
        number.append(1)
        a = a // 2

number.reverse()

for x in number:
    print(x,end='')
