import time
from random import randint

print('-'*60)
print(' '*20, 'VAMOS JOGAR UM JOGO')
print('-'*60)

contador = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,100)
    total = computador + jogador
    time.sleep(1)
    escolhajogador = int(input('Você acha que vai ser par [ 0 ] ou impar [ 1 ]? '))
    time.sleep(1)
    if total % 2 == 0:
        if escolhajogador == 0:
            print(' ')
            print('O computador jogou {} e você {}, total de {}, você ganhou vamos jogar novamente.'.format(computador, jogador, total))
            print(' ')
            contador += 1
        else:
            break
    else:
        if escolhajogador == 1:
            print(' ')
            print('O computador jogou {} e você {}, total de {}, você ganhou vamos jogar novamente.'.format(computador, jogador, total))
            print(' ')
            contador += 1
        else:
            break
time.sleep(1)
print('Você errou. Você acertou um total de {} vezes consecutivas.'.format(contador))