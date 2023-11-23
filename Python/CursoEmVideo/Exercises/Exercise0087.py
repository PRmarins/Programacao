dados = ['amora','vicio','bosta']
dados2 = [4,6,2,10]

conjunto = list()

conjunto.append(dados[:])
conjunto.append(dados2[:])

print(conjunto[0])
print(conjunto[1])
print(conjunto)

for elementos in conjunto:
    for subelementos in elementos:
        print(subelementos)