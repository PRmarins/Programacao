from random import choice
contador = 0
list = [0,1,2,3,4,5,6,7,8,9,10]
computador = choice(list)
print('Acabei de pensar em um número, tente adivinhar qual:')
numero=int(input('Sua resposta: '))
while numero != computador:
    if numero > computador:
        contador += 1
        numero=int(input('Menos: '))
    if numero < computador:
        contador += 1
        numero=(int(input('Mais: ')))
print('Muito bem você acertou com {} tentativas.'.format(contador))