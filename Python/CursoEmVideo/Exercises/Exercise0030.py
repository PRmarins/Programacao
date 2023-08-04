number = int(input('Digite um número para saber se é impar ou par: '))
impar_par = number % 2
if impar_par == 0:
    print('O número {} é par.'.format(number))
else:
    print('O número {} é impar.'.format(number))