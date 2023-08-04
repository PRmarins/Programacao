import random

name1 = input('Digite o primeiro nome: ')
name2 = input('Digite o segundo nome: ')
name3 = input('Digite o terceiro nome: ')
name4 = input('Digite o quarto nnumero: ')

lista = [name1, name2, name3, name4]
random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
