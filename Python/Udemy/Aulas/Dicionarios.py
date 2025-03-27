#TAG: DICIONARIO , TUPLA

# Dicionarios não aceitam valores duplicados, ordenados (a partir da versao Python 3.7, antes disso eram desordenados) 
# e com valores alteraveis.

dicionario = {'jan': 100, 'fev': 200, 'mar': 300, 'abr': 400}

print(dicionario.keys())
print(dicionario.values())

for i in dicionario:
    print(i)

for i in dicionario:
    print(dicionario[i])

for chave, valor in dicionario.items():
    print(f"chave = {chave}, valor = {valor}")

#TUPLA DO DICIONARIO

print(dicionario.items())

#TRANSFORMAR O DICIONARIO EM UMA TUPLA

dicionario_tupla = tuple(dicionario.items())

print(dicionario_tupla)

#SOMAR VALORES, MINIMOS, MXIMOS  E TAMANHO DO DICIONARIO   *** SO FUNCIONA SE OS VALORES FOREM REAIS OU INTEIROS***

print(max(dicionario.values()))
print(min(dicionario.values()))
print(sum(dicionario.values()))
print(len(dicionario.values()))

# Para escrever o calor da lista, voce usa o get, porem associamos um valor padrao quando colocamos uma virgula
# apos o valor que queremos buscar, caso ele nao exista.

print(dicionario.get('diz', 'Valor não existe')) # assim o caso o valor nao exita, sera exhibido a mensagem "valor nao existe"
print(dicionario.get('jan', 'Valor não existe')) # assim o caso o valor exita, sera exhibido o valor