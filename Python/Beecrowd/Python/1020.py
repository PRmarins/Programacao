valor = int(input(''))
if 364 >= valor >= 360:
    valor = 359 
if valor >= 365:
    ano = valor // 365
    print('{} ano(s)'.format(ano))
if valor < 365:
    ano = 0
    print('{} ano(s)'.format(ano))
while valor >= 365:
    valor -= 365
if valor >= 30:
    mes = valor // 30
    print('{} mes(es)'.format(mes))
while valor >= 30:
    valor -= 30
if valor < 30:
    print('{} dia(s)'.format(valor))