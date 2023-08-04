import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = (int(input('Qual é sua jogada? ')))
print('-=' * 11)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida.')

elif computador == 1:
    if jogador == 0:
        print('Computador vence')        
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganha')
    else:
        print('Jogada inválida.')

elif computador == 2:
    if jogador == 0:
        print('Jogador ganha')
    elif jogador == 1:
        print('Computador ganha')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida.')
