number1 = int(input('Me de um número: '))
number2 = int(input('Me de outro numero: '))
number3 = int(input('Me de outro número: '))
if number1 + number2 > number3 and number2 + number3 > number1 and number1 + number3 > number2:
    print('Estes números podem formar um triângulo.')
    if number1 != number2 and number2 != number3:
        print('É um triângulo é um triângulo escaleno.')
    if number1 == number2 or number2 == number3 or number1 == number3:
        print('Este triângulo é um triângulo isosceles.')
    if number1 == number2 == number3:
        print('Este triangulo é um triângulo equilatero.')
else:
    print('Estes número não podem formar um triângulo.')
