s = int(input("Input your number:\n"))
a = bin(s)
binary = ''
for i in range(2,len(a)):
    binary += a[i]
    i+= 1
print(binary)
