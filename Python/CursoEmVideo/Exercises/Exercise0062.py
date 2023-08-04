print ('='*45)
print ('         10 TERMOS DE UMA PROGRESSÃO')
print ('='*45)
ftermo=int(input('Primeiro termo: '))
razao=int(input('Razão: '))
contador=1
while contador <= 10:
    contador += 1
    print(' {} ->'.format(ftermo),end='')
    ftermo += razao
print(' fim')