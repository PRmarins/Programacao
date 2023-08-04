import time
tupla = ('Python','Armario','Aprender','Java','Churrasqueira','Controle','Remoto','Computador','Carro','Albergue','Picolas','Aviao','Algoritimos','Pesca')

c = 0
for palavras in tupla:
    time.sleep (1)
    print(f'\nA palavra {tupla[c].upper()} possui as vogais:',end = ' ')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print (letras.lower(),end = ' ')
    
    print(' ')
    c += 1