print('Digite um numero ara calcular seu fatorial: ')
numero=int(input('Numero: '))
fatoriais = numero - 1
fatorial = numero * fatoriais
while fatoriais != 1:
    fatoriais = fatoriais - 1
    fatorial = fatorial * fatoriais
print (fatorial)