numeros = (input("")).split()

numeros = [int(c) for c in numeros]

for v in sorted(numeros):
    print (v)

print ("")

for v in numeros:
    print(v)