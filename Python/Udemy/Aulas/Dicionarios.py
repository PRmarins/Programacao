#TAG: DICIONARIO , TUPLA

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