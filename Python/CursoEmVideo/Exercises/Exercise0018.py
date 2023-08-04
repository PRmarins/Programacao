import random


name1 = input('Digite o primeiro nome para o sorteio: ')
name2 = input('Digite o segundo nome para o sorteio: ')
name3 = input('Digite o terceiro nome para o sorteio: ')
name4 = input('Digite o quarto nome para o sorteio: ')
name5 = input('Digite o quinto nome para o sorteio: ')

lista = (name1, name2, name3, name4, name5)

escolhido = random.choice(lista)

print('O escolhido foi {}.'.format(escolhido))
