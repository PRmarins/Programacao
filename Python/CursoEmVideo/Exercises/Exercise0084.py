numeros = []

while True:
    i = (input("Digite um número: "))
    while True:
        if i in numeros:
            i = input("O número já se econtra na lista, digite outro: ")
        else:
            break
    numeros.append(i)
    continuar = input("Deseja adicionar outro número? [S/N] ").upper()
    if continuar not in ("S","N"):
        while True:
            continuar = (input("Por favor responder com 'N' ou 'S': ")).upper()
            if continuar in ("S","N"):
                break
        
    
    if continuar == "N":
        break
    

numeros_n = [int(n) for n in numeros]

if  5 in numeros_n:
    tem5 = "Sim"

counter = 0
for i in numeros_n:
    if i == 5:
        counter = +1

numeros_n.sort(reverse=True)

print("A lista em ordem decrecente ficou: ", end = "")

for c in numeros_n:
    print(c, end = "")
    print(",", end = " ")
print(f"\nO número '5' apareceu {counter} vezes." )