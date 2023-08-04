conta = 0
soma = 0
for numbers in range (1, 7):
    number = int(input('Digite um valor: '))
    if number % 2 == 0:
        soma = soma + number
        conta = conta + 1
print('Você digitou {} números pares e a soma destes é {}'.format(conta, soma))
