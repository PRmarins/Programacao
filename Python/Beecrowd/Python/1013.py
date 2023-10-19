var = str(input()).strip().split()

tamanho = len(var)

lista = []

i = 0

while i < tamanho:
    lista.append(var[i])
    i+=1

new_list = [int(valor) for valor in lista]

print(f"{max(new_list)} eh o maior")