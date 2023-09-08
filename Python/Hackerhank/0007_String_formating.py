def hexa (n):
    return hex(n)

def octal (n):
    return oct(n)

def binar (n):
    return bin(n)


n = int(input(""))

for i in range (1,n + 1):
    print(i,"   ",hexa(i),"   ",octal(i),"   ",binar(i))