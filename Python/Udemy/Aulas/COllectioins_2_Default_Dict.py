# TAG : Default Dict , Collections

'''Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, 
podendo utilizar um lambda para isso.'''

# Função lambda -> Função anônima que pode ter qualquer número de argumentos, mas só uma expressão.

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario ['Curso'] = 'Python'

print(dicionario)

print(dicionario['Otro'])  # Se eu tentar acessar uma chave que não existe,
#ele cria a chave com o valor default.

print(dicionario) # Agaro a chave outro foi criada com o valor default (0).

