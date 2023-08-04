print('-'*50)
print(' '*14,'SEQUENCIA DE FIBONACCI')
print('-'*50)
termos = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
contador = 3
print('{} -> {} '.format(t1,t2,),end='')
while contador <= termos:
    t3 = t1 + t2
    print('-> {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    contador += 1