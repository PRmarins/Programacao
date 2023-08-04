import random
sorteio = (random.randint(0,99),random.randint(0,99),random.randint(0,99),random.randint(0,99),random.randint(0,99))
print(f'Os valores sorteados foram: ',end='')
for n in sorteio:
    print(f'{n} ',end='')
print(f'\nO maior valor sorteado é: {max(sorteio)}.')
print(f'O menor valor sorteado é: {min(sorteio)}.')