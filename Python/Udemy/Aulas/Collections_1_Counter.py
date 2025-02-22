# TAG : COLLECTIONS , COUNTER

''' Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido 
 com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor 
 a quantidade de ocorrências desse elemento.'''

# Utilizando o Counter : 

from collections import Counter

# Exemplo 1 : Utilizando uma lista :

Lista1 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]

# Utilizando o Counter :

Counter1 = Counter(Lista1)

print(Counter1) # Me da a quantidade em que cada elemento da lista aparece.

# Exemplo 2 : Utilizando uma string :

String1 = 'Python é zica demais'

Counter2 = Counter(String1)

print(Counter2) # Me da a quantidade em que cada letra da string aparece (o espaço vazio também é contado).

# Exemplo 3 : Utilizando uma lista de palavras :

lista2 = ['Python', 'é', 'zica', 'Python', 'é', 'a', 'melhor', 'linguagem', 'de', 'programação']

Counter3 = Counter(lista2)

print(Counter3) # Me da a quantidade em que cada palavra da lista aparece.

print(Counter(lista2)['Python']) # Me da a quantidade em que a palavra 'Python' aparece.

# Encontrando as palavras mais comuns em um texto :

texto = '''Python é uma linguagem de programação de alto nível, interpretada, de script, 
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. 
Foi lançada por Guido van Rossum em 1991. Atualmente possui um modelo de desenvolvimento comunitário,
aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. 
Apresenta uma sintaxe elegante, e tipagem dinâmica, fazendo com que seja uma linguagem 
ideal para prototipagem rápida, bem como para uso em pequenos e grandes projetos.'''

palavras = texto.split()

Counter4 = Counter(palavras)

print(Counter4.most_common(5)) # Me da as 5 palavras mais comuns do texto.
