# TAG : CONJUNTOS , SET , SETS

# Os conjuntos são chamados de sets na programação
'''
- Não possuem valores duplicados
- Não possuem valores ordenados
- Os Sets não são indexados

Bons para utilizar quando queremos armaZenar itens sem preocupar com ordem,
itens duplicados, chave e valores

São usados para referenciar os Sets as chaves {}

-> Diferença entre Sets e Dicionarios:
    - O Dicionario tem chave e valor
    - O Set tem apenas o valor

'''

Sets = set({1, 4, 2, 1, 4, 5, 2, 6, 3, 3, 2, 3, 4, 5, 1, 2})  # Ele irá mostrar os itens em ordem crescente sem se repetir

print(type(Sets))  # <class 'set'>
print(Sets)        # A ordem dos elementos pode variar
print(len(Sets))   # 6

# Adicionando elementos em um conjunto:
Sets.add(7)
Sets.add(10000)

print(Sets)        # A ordem dos elementos pode variar

# Removendo elementos de um conjunto:

# Forma 1

Sets.remove(4)  # Ele elimina o elemento com esse valor, se o elemento não existir, irá dar erro

print(Sets)        # A ordem dos elementos pode variar

# Forma 2

Sets.discard(5)  # Ele elimina o elemento com esse valor, se o elemento não existir, não irá dar erro

print(Sets)        # A ordem dos elementos pode variar

# Copiando um conjunto para outro:

Sets2 = Sets.copy()

print(Sets2)        # A ordem dos elementos pode variar

# Limpando um conjunto:

Sets2.clear()

print(Sets2)

# unindo 2 conuntos:

# Forma 1

Conjunto1 = {1, 3, 5, 7, 9}
Conjunto2 = {2, 4, 6, 8, 10}

Conjunto3 = Conjunto1.union(Conjunto2)

print(Conjunto3)

# Forma 2

Conjunto4 = Conjunto1 | Conjunto2

print(Conjunto4)

# Verificando se um conjunto é subconjunto de outro:

Conjunto1 = {1, 3, 5, 7, 9}
Conjunto2 = {2, 4, 6, 8, 10}

Conjunto3 = {1, 3, 5}

print(Conjunto3.issubset(Conjunto1))  # True
print(Conjunto3.issubset(Conjunto2))  # False