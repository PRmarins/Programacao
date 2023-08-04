nome = str(input('Diga seu nome:'))
print('Olá, seu nome é: {}'.format(nome))
print('Olá, seu nome é: {:20}'.format(nome))
print('Olá, seu nome é: {:>20}'.format(nome))
print('Olá, seu nome é: {:<20}'.format(nome))
print('Olá, seu nome é: {:^20}'.format(nome))
print('Olá, seu nome é: {:=^20}'.format(nome))
n1 = int(input('Coloque um número:'))
n2 = int(input('Coloque outro número:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# na linha de baixo se coloca na divisao o ".3f" para delimitar quantas casas decimais vão aparecer.
# o "end=''" no final foi para que a linha de baixo seja continuada logo após a linha de cima.

print('A soma é {}, a multiplicação é {}, a divisáo é {:.3f}'.format(s, m, d), end='')
print(', a divisão inteira {} e a potenciação é {}.'.format(di, e))

# o \n é para pular a linha, ao contrario do exemplo anterior (end='')

idade = str(input('Qual sua idade?'))
print('Olá {} , sua \nidade é {} anos'.format(nome, idade))
