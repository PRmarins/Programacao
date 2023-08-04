print('Diga seu sexo:')
print('''[M] Masculino
[F] Feminino''')
sexo=str(input('')).strip() .upper()[0]
while sexo not in 'MmFf':
    print('''Resposta inválida.
Qual o seu sexo?''')
    sexo=str(input('')).strip() .upper()[0]
idade=int(input('Qual a sua idade?'))
