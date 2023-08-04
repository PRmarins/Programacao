import time
resposta = 0
print('''O que deseja fazer?
[ 1 ] SOMAR
[ 2 ] SUBTRAIR
[ 3 ] MULTIPLICAR
[ 4 ] DIVIDIR
[ 5 ] SAIR''')
resposta=int(input('Resposta: '))
if resposta == 1:
    numero1=int(input('Primeiro numero: '))
    numero2=int(input('Segundo numero: '))
    soma = numero1 + numero2
    print('Pensando...')
    time.sleep(2)
    print (soma)
elif resposta == 2:
    numero1=int(input('Primeiro numero: '))
    numero2=int(input('Segundo numero: '))
    subtracao = numero1 - numero2
    print('Pensando...')
    time.sleep(2)
    print(subtracao)
elif resposta == 3:
    numero1=int(input('Primeiro numero: '))
    numero2=int(input('Segundo numero: '))
    multiplicacao = numero1 * numero2
    print('Pensando...')
    time.sleep(2)
    print(multiplicacao)
elif resposta == 4:
    numero1=int(input('Primeiro numero: '))
    numero2=int(input('Segundo numero: '))
    divisao = numero1 / numero2
    print('Pensando...')
    time.sleep(2)
    print(divisao)
while resposta != 5:
    time.sleep(2)
    print('''O que deseja fazer?
[ 1 ] SOMAR
[ 2 ] SUBTRAIR
[ 3 ] MULTIPLICAR
[ 4 ] DIVIDIR
[ 5 ] SAIR''')
    resposta=int(input('Resposta: '))
    if resposta == 1:
        numero1=int(input('Primeiro numero: '))
        numero2=int(input('Segundo numero: '))
        soma = numero1 + numero2
        print('Pensando...')
        time.sleep(2)
        print (soma)
    elif resposta == 2:
        numero1=int(input('Primeiro numero: '))
        numero2=int(input('Segundo numero: '))
        subtracao = numero1 - numero2
        print('Pensando...')
        time.sleep(2)
        print(subtracao)
    elif resposta == 3:
        numero1=int(input('Primeiro numero: '))
        numero2=int(input('Segundo numero: '))
        multiplicacao = numero1 * numero2
        print('Pensando...')
        time.sleep(2)
        print(multiplicacao)
    elif resposta == 4:
        numero1=int(input('Primeiro numero: '))
        numero2=int(input('Segundo numero: '))
        divisao = numero1 / numero2
        print('Pensando...')
        time.sleep(2)
        print(divisao)
    elif resposta == 5:
        print('Saindo...')