# TAG : LISTA

counter = 0

lista = []

while counter < 6:
    lista.append(input("DIgite: "))
    counter += 1

tamanho_lista = len(lista)

for i in range (0,tamanho_lista):
    print(lista[i])
    i += 1
