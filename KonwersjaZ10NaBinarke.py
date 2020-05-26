#zamiana z 10 na 2
a = int(input("> "))
liczba = []

while a != 0:
    if a % 2 == 0:
        liczba.append(0)
        a = a // 2
    elif a % 2 == 1:
        liczba.append(1)
        a = a // 2

liczba.reverse()

for x in liczba:
    print(x,end='')