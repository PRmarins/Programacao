from time import sleep
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))
number3 = int(input('Digite outro número: '))
print('Calculando...')
sleep(2)
menornumber = number1
maiornumber = number1
if number2 > maiornumber:
    maiornumber = number2
if number3 > maiornumber:
    maiornumber = number3
if number2 < menornumber:
    menornumber = number2
if number3 < menornumber:
    menornumber = number3
print ('The number {} is the big number.'.format(maiornumber))
print ('The number {} is the little number.'.format(menornumber))
