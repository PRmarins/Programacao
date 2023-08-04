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