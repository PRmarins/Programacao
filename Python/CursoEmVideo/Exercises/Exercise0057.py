qmulheres = 0
sexo = ['Masculino', 'Feminino']
idadesoma = 0
homemmaisvelho = 0

for pessoas in range (1,5):
    print('='*45)
    print('                   PESSOA {}'.format(pessoas))
    print('='*45)
    nome = str(input('Digite seu nome: '))
    idade = int(input('{}, digite sua idade: '.format(nome)))
    print('[1]  PARA MASCULINO')
    print('[2]  PARA FEMININO')
    sexoo = int(input('Qual o seu sexo? '))
    idadesoma = idadesoma + idade
    if sexoo == 2 and idade < 20:
        qmulheres += 1
    if sexoo == 1:
        homemmaisvelho = idade
        nomehomemmaisvelho = nome
mediaidade = idadesoma / 4
print('A media de idade do grupo é de {} anos.'.format(mediaidade))
if homemmaisvelho != 0:
    print('O homem mais velho é o {} com {} anos.'.format(nomehomemmaisvelho, homemmaisvelho))
if qmulheres == 1:
    print ('Há {} mulher com menos de 20 anos.'.format(qmulheres))
elif qmulheres < 1:
    print ('Há {} mulheres com menos de 20 anos.'.format(qmulheres))