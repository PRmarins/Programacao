valores = input("").split()
valores =[float (v) for v in valores]

A = valores[0]
B = valores[1]
C = valores[2]

area = ((A + B) * C) / 2
perimtro = A + B + C

if A + B > C and B + C > A and A + C > B:
    print(f'Perimetro = {perimtro}')
else:
    print(f"Area = {area}")