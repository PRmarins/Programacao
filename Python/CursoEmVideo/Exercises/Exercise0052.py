print ('='*45)
print ('         10 TERMOS DE UMA PROGRESSÃO')
print ('='*45)
ftermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for pa in range (ftermo, (razao * 10) + ftermo, razao):
    print('{} '.format(pa), end='-> ')
print('FIM')