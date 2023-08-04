number = int(input('Digite um número para ver sua taboada: '))
for tabuada in range (1, 11):
    multiplicacao = tabuada * number
    print('{} x {} = {}'.format(number, tabuada, multiplicacao))
    