comida =["Cachorro quente","Batata frita", "Hamburguer","Pizza"]

caracteres = len(comida) - 1

merda = 0

for elementos in comida:
        
    print(elementos,end = " ")
        
    if merda != caracteres:
        print(", ", end = " ")
        merda += 1
        
print("\nAdicionando novo produto na lista em um local específico:")
        
comida.insert(2,"Coquinha gelada")

merda = 0

caracteres = len(comida) - 1

for elementos in comida:
        
    print(elementos,end = " ")
        
    if merda != caracteres:
        print(", ", end = " ")
        merda += 1
        
print("\nAdicionando um item a mais na lista:")

comida.append("Item adicionado")

merda = 0

caracteres = len(comida) - 1

for elementos in comida:
        
    print(elementos,end = " ")
        
    if merda != caracteres:
        print(", ", end = " ")
        merda += 1

print("\nDeletando item expecifico da lista:")

del comida[1]

merda = 0

caracteres = len(comida) - 1

for elementos in comida:
        
    print(elementos,end = " ")
        
    if merda != caracteres:
        print(", ", end = " ")
        merda += 1
        
print("\nEliminando o ultimo elemento:")

comida.pop()

merda = 0

caracteres = len(comida) - 1

for elementos in comida:
        
    print(elementos,end = " ")
        
    if merda != caracteres:
        print(", ", end = " ")
        merda += 1
        
print("\nEliminando um item especifico da lista (nome do item)")

comida.remove("Hamburguer")

caracteres =len(comida) -1

for elementos in comida:
    print(elementos,end = " ")
    
    if merda != caracteres:
        print(", ",end = " ")
        merda += 1