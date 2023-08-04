print ('='*45)
print ('         TERMOS DE UMA PROGRESSÃO')
print ('='*45)
ftermo = int(input('Diga o primeiro termo da PA: '))
razao = int(input('Razao: '))
contador = 1
mais = 10
total = 0
termo = ftermo
while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo),end='')
        contador += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos mais deseja ver? '))
print('Progressão finalizada com {} termos.'.format(total))