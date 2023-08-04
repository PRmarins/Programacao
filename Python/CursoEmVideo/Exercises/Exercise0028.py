import random
from time import sleep
print('============================================')
print('========= VOU PENSAR EM UM NÚMERO ==========')
print('============================================')
numero = random.randrange(10)
print('Em que número pensei?')
answer = int(input(''))
print('Analisando...')
sleep(3)
if numero == answer:
    print('Você acertou, fui derrotado.')
else:
    print('Você errou, eu ganhei.')
print('Eu pensei no número:',numero)