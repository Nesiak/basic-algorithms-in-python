s = int(input("liczba\n"))
a = bin(s)
binara = ''
for i in range(2,len(a)):
    binara += a[i]
    i+= 1
print(binara)
