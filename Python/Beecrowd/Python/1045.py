valores = str(input("")).split()

valores[0] = float(valores[0])
valores[1] = float(valores[1])
valores[2] = float(valores[2])

A = 0
B = 0
C = 0

if valores[0] == valores[1] == valores[2]:
    A = valores[0]
    B = A
    C = A
    
if valores[0] > valores[1] and valores[0] > valores[2] and valores[1] > valores[2]:
    A = valores[0]
    B = valores[1]
    C = valores[2]
if valores[0] > valores[1] and valores[0] > valores[2] and valores[2] > valores[1]:
    A = valores[0]
    B = valores[2]
    C = valores[1]

if valores[1] > valores[0] and valores[1] > valores[2] and valores[0] > valores[2]:
    A = valores[1]
    B = valores[0]
    C = valores[2]
if valores[1] > valores[0] and valores[1] > valores[2] and valores[2] > valores[0]:
    A = valores[1]
    B = valores[2]
    C = valores[0]
        
if valores[2] > valores[1] and valores[2] > valores[0] and valores[1] > valores[0]:
    A = valores[2]
    B = valores[1]
    C = valores[0]
if valores[2] > valores[1] and valores[2] > valores[0] and valores[0] > valores[1]:
    A = valores[2]
    B = valores[0]
    C = valores[1]
        
if valores[0] == valores[1] and valores[2] > valores[1]:
    A = valores[2]
    B = valores[1]
    C = B
elif valores[0] == valores[1] and valores[2] < valores[1]:
    A = valores[0]
    B = A
    C = valores[2]
    
if valores[1] == valores[2] and valores[0] > valores[1]:
    A = valores[0]
    B = valores[1]
    C = B
elif valores[1] == valores[2] and valores[0] < valores[1]:
    A = valores[1]
    B = A
    C = valores[0]
if valores[0] == valores[2] and valores[0] < valores[1]:
    A = valores[1]
    B = valores[0]
    C = B
elif valores[0] == valores[2] and valores[0] > valores[1]:
    A = valores[0]
    B = A
    C = valores[1]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if (A**2) == (B**2) + (C**2):
        print("TRIANGULO RETANGULO")
    if (A**2) > (B**2) + (C**2):
        print("TRIANGULO OBTUSANGULO")
    if (A**2) < (B**2) + (C**2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if B == C and B != A or A == B and A != C or A == C and A != B:
        print("TRIANGULO ISOSCELES")