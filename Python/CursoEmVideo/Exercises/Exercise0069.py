print('-'*50)
print(' '*14, 'CADASTRE UMA PESSOA')
print('-'*50)
contador18 = 0
sexof = 0
sexom = 0


idade = int(input('IDADE: '))
while idade < 0 or idade > 130:
    print('Resposta inválida.')
    idade = int(input('IDADE: '))
if idade < 18:
    contador18 += 1

sexo = str(input('SEXO [ M ] ou [ F ]: ')).strip() .upper() .split() [0]
while sexo != 'F' and sexo != 'M':
    print('Resposta inválida.')
    sexo = str(input('SEXO [ M ] ou [ F ]: ')).strip() .upper() .split() [0]
if sexo == 'F':
    sexof += 1
if sexo == 'M':
    sexom += 1

resposta = str(input('Quer continuar? [ S ] ou [ N ]: ')).upper() .strip() .split() [0]
while resposta != 'S' and resposta != 'N':
    print('Resposta inválida.')        
    resposta = str(input('Quer continuar? [ S ] ou [ N ]: ')).strip() .upper() [0]
    
#CADASTRAR MAIS PESSOAS:

while resposta == 'S':
    print('-'*50)
    print(' '*14, 'CADASTRE UMA PESSOA')
    print('-'*50)
    
    idade = int(input('IDADE: '))
    while idade < 0 or idade > 130:
        print('Resposta inválida.')
        idade = int(input('IDADE: '))
    if idade < 18:
        contador18 += 1
    
    sexo = str(input('SEXO [ M ] ou [ F ]: ')).strip() .upper() .split()[0]
    while sexo != 'F' and sexo != 'M':
        print('Resposta inválida.')
        sexo = str(input('SEXO [ M ] ou [ F ]: ')).strip() .upper() .split()[0]
    if sexo == 'F':
        sexof += 1
    if sexo == 'M':
        sexom += 1
    
    resposta = str(input('Quer continuar? [ S ] ou [ N ]: ')).upper() .strip() .split()[0]
    while resposta != 'S' and resposta != 'N':
        print('Resposta inválida.')        
        resposta = str(input('Quer continuar? [ S ] ou [ N ]: ')).strip() .upper() [0]
print('Há {} pessoas com menos de 18 anos.'.format(contador18))      
print('Há {} mulheres e {} homens.'.format(sexof, sexom))