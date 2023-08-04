from os import uname_result


numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analizando o número {}.'.format(numero))
print('A unidade é {}.'.format(u))
print('A dezena é {}.'.format(d))
print('A centena é {}.'.format(c))
print('O milhar é {}.'.format(m))
