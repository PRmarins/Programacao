tempo = int(input('Quando tempo tem seu carro? '))
if tempo<=3:
    print('O seu carro é novo.')
if 6>=tempo>=4:
    print('Seu carro está ficando velho')
if tempo>6:
    print('Seu carro está velho.')
print('===END===')

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua outra nota: '))
media = nota1 + nota2 / 2
if media<=6:
    if media<4:
        print('Você desaprovou!')
    else:
        print('Você está de recuperação!')

if media>=7:
    if 9<=media:
        print('Você está aprovadissimo!!')
    else:
        print('Você está aprovado!')
