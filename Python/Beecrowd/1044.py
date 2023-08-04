numbers = str(input("")).split()

number_1 = int(numbers[0])
number_2 = int(numbers[1])

divisao = 0

if number_1 > number_2:
    divisao = number_1 / number_2
    divisao = int(divisao)
    if divisao * number_2 == number_1:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    divisao = number_2 / number_1
    divisao = int(divisao)
    if divisao * number_1 == number_2:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")