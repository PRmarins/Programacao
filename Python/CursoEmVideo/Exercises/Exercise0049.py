soma = 0
contador = 0
number = int(input('Digite um número e direi a soma de todos os números impares divisíveis por 3 até ele: '))
for imparcount in range (1, number + 1, 2):
    if imparcount % 3 == 0:
        soma = soma + imparcount
        contador = contador + 1
print('A soma de todos os número impares divisíveis por 3 de zero até {} é {}, no total são {} números.'.format(number, soma, contador))