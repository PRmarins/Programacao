import time
lista = []

resposta = "S"

continuar = False

n = int(input("Digite um valor: "))
if n not in lista:
    lista.append(n)
else:
    print ("Este número já se encontra na lista.")

print ("Deseja adicionar mais valores?")
resposta = str(input('"S" para sim e "N" para não: ')).upper().strip()
time.sleep(1)
if resposta == "S":
    continuar = True
else:
    continuar = False
    
if continuar == True:
    while continuar == True:
        n = int(input("Digite um valor: "))
        if n not in lista:
            lista.append(n)
        else:
            print ("Este número já se encontra na lista.")
        print ("Deseja adicionar mais valores?")
        resposta = str(input('"S" para sim e "N" para não: ')).upper().strip()
        time.sleep(1)
        if resposta == "S":
            continuar = True
        else:
            continuar = False

ordem_crescente = sorted(lista)

print (f"Os valores digitados foram: ", end=" ")

for v in ordem_crescente:
    print ("{}...".format(v),end="")