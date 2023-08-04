import time
from datetime import date

atual = date.today().year
alistamento = 18
nasceu = int(input('Em que ano você nasceu? '))
idade = atual - nasceu
print('Analisando...')
time.sleep (2)
if idade < alistamento:
    faltam = alistamento - idade
    print('''Você ainda vai se alistar, 
faltam {} anos para se alistar.'''.format(faltam))
if idade > alistamento:
    passou = idade - alistamento
    print('Já passou {} anos do tempo de se alistar!'.format(passou))
if idade == alistamento:
    print('Você tem que se alistar esse ano.')