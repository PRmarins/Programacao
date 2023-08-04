salario = float(input('Qual é o valor do seu salário? '))
if salario > 1250.00:
    novosalario = ((salario * 10) / 100) + salario
if salario <= 1250.00:
    novosalario = ((salario * 15) / 100) + salario
print('Seu novo salario será: {:.2f}'.format(novosalario))
