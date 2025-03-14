# TAG : LISTA

lista = []

for i in range (0,10):
    lista.append(int(input("Digite um valor: ")))

par_lista = []

for i in lista:
    if i % 2 == 0:
        par_lista.append(i)

if len(par_lista) > 0:
    print(*par_lista, sep=", ")

elif len(par_lista) > 0:
    print(len(par_lista))

else:
    exit()