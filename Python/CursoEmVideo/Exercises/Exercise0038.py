from time import sleep

fnumber = int(input('Digite um número: '))
snumber = int(input('Digite outro número: '))
print('Analisando...')
sleep (2)
if fnumber > snumber:
    print('O primeiro número é o maior.')
if fnumber < snumber:
    print('O segundo número é o maior.')
if fnumber == snumber:
    print('Não existe número maior, os dois tem o mesmo valor.')