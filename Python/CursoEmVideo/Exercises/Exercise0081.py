lista = []

for n in range (0,5):
    lista.append(int(input(f"Digite um número: ")))
    
maior_numero = max(lista)
menor_numero = min(lista)

print (f"O maior valor digitado foi {maior_numero} na posição: ",end = " ")

for i, n in enumerate(lista):
    if n == maior_numero:
        print (f"{i+1}...",end = " ")

print (f"\nO menor valor da lista é o {menor_numero} nas posições: ",end = " ")

for i, n in enumerate(lista):
    if n == menor_numero:
        print(f"{i+1}...",end = " ")
