lista = []

for c in range (0,5):
    repetido = True
    numero = int(input("Digite um valor: "))
    if c == 0 or numero >= lista[-1]:
        if len(lista) >= 1:
            while numero in lista:
                print ("Esse valor já foi posto na lista, tente outro: ")
                numero = int(input("Digite um valor: "))
        lista.append(numero)
    else:
        posicao = 0
        
        while posicao < len(lista):
            if numero < lista[posicao]:
                while numero in lista:
                    print ("Esse valor já foi posto na lista, tente outro: ")
                    numero = int(input("Digite um valor: "))
                lista.insert(posicao,numero)
                break
            posicao += 1
print(f"{lista}")     