import time
import random

itens = ('Pedra', 'Papel', 'Tesoura')
print ('Olá, sou a máquina, gostaria de jogar um jogo?')
resposta1 = str(input('Responda "sim" ou "não": '))
if resposta1 == 'sim' or resposta1 == 'Sim' or resposta1 == 'SIM':
    time.sleep (1)
    print('OK, vamos ver se você consegue me vencer...')
    time.sleep (1)
    print('É um jogo simples que você já conhece, pedra papel e tesoura.')
    time.sleep (3)
    print('Vamos começar...')
    time.sleep(2)
    print(" ============ [ 0 ] PEDRA   ============")
    print(' ============ [ 1 ] PAPEL   ============')
    print(' ============ [ 2 ] TESOURA ============')
    escolha = int(input('Sua escolha: '))
    escolhaMaquina = random.choice (itens)
    print('JO')
    time.sleep (1)
    print('KEN')
    time.sleep (1)
    print('POO...')
    if escolha == 0:
        print('você escolheu PEDRA e eu escolhi {}.'.format(escolhaMaquina))
        print('Hummm...')
        time.sleep(1)
        if escolhaMaquina == 'Papel':
            print('Parece que você perdeu...')
        elif escolhaMaquina == 'Tesoura':
            print('Parece que você ganhou...')
        elif escolhaMaquina == 'Pedra':
            print('Pensamos igual, ninguém ganhou.')
    elif escolha == 1:
        print('Você escolheu PAPEL e eu escolhi {}.'.format(escolhaMaquina))
        print('Hummm...')
        time.sleep (1)
        if escolhaMaquina == 'Pedra':
            print('Parece que você ganhou...')
        elif escolhaMaquina == 'Papel':
            print('Pensamos igual, ninguém ganhou.')
        elif escolhaMaquina == 'Tesoura':
            print('Parece que você perdeu...')
    elif escolha == 2:
        print('Você escolheu TESOURA e eu escolhi {}.'.format(escolhaMaquina))
        print('Hummm...')
        time.sleep (1)
        if escolhaMaquina == 'Tesoura':
            print('Pensamos igual, ninguém ganhou.')
        elif escolhaMaquina == 'Pedra':
            print('Parece que você perdeu...')
        elif escolhaMaquina == 'Papel':
            print('Parece que você ganhou...')
else:
    print('Tudo bem, até mais.')