numeros = (int(input('Digite o primeiro número: ')), 
           int(input('Digite o segundo número: ')), 
           int(input('Digite o terceiro número: ')), 
           int(input('Digite o quarto número: ')), 
           int(input('Digite o quinto número: ')))
print ('Os números digitados são: ',end='')
for x in numeros:
    print(f'[{x}] ',end='')
print('\nOs números pares são: ',end='')
for n in numeros:
    if n % 2 == 0:
        print(f'[{n}] ',end='')