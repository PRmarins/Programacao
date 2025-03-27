salario = float(input())

if salario <= 2000:
    print('Isento')

elif 2000 < salario >= 3000:
    imposto = (salario - 2000) * 8/100
    print (f"{imposto:.2f}")

elif 3000 < salario <= 4500:
    imposto = (((salario - 2000) * 8/100) + (salario - 3000 * 18/100))
    print(f'{imposto:.2f}')

else:
    imposto = ((salario - 2000) * 8/100) + ((salario - 3000) * 18/100) + ((salario - 4500) * 28/100)
    print(f'{imposto:.2f}')
