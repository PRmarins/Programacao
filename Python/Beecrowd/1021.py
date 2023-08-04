import math

valorpad = float(input(''))
valor = valorpad * 100
valor = math.trunc(valor)

valor100 = int(0)
valor50 = int(0)
valor20 = int(0)
valor10 = int(0)
valor5 = int(0)
valor2 = int(0)
valor1 = int(0)
contador05 = int(0)
contador025 = int(0)
contador01 = int(0)
contador005 = int(0)
contador001 = int(0)

#Valor maior que 100
if valor >= 10000:
    valor100 = valor // 10000
    valor = valor - 10000 * valor100
        
#valor maior ou igual 50 e menor que 100
if 10000 > valor >= 5000:
    valor50 = valor // 5000
    valor = valor - 5000 * valor50

#valor maior ou igual a 20 e menor que 50
if 5000 > valor >= 2000:
    valor20 = valor // 2000
    valor = valor - 2000 * valor20

#valor maior ou igual 10 e menor que 20
if 2000 > valor >= 1000:
    valor10 = valor // 1000
    valor = valor - 1000 * valor10

#valor maior ou igual a 5 e menor que 10
if 1000 > valor >= 500:
    valor5 = valor // 500
    valor = valor - 500 * valor5

#valor maior ou igual a 2 e menor que 5
if 500 > valor >= 200:
    valor2 = valor // 200
    valor = valor - 200 * valor2

#valor maior ou igual a 1 e menor que 2
if 200 > valor >= 100:
    valor1 = valor // 100
    valor = valor - 100 * valor1

#valor maior ou igual a 0.5 e menor que 1
if 100 > valor >= 50:
    valor = valor - 50
    contador05 = 1
    
#valor maior ou igual a 02 e menor que 05
if 50 > valor >= 25:
    valor -= 25
    contador025 = 1


#valor maior ou igual a 0.1 e menor que 0.2
if 25 > valor >= 10:
    valor -= 10
    contador01 = 1
    if valor > 10:
        valor -= 10
        contador01 += 1

#valor maior ou igual a 0.05 e menor que 0.1
if 10 > valor >= 5:
    valor -= 5
    contador005 = 1

#valor maior ou igual a 0.01 e menor que 0.05
if 5 > valor >= 1:
    valor -= 1
    contador001 = 1
    if valor >= 1:
        valor -= 1
        contador001 += 1
        if valor >= 1:
            valor -= 1
            contador001 += 1
            if valor >= 1:
                valor -= 1
                contador001 += 1
                if valor >= 1:
                    valor -= 1
                    contador001 += 1
                    
valor100 = int(valor100)
valor50 = int(valor50)
valor20 = int(valor20)
valor10 = int(valor10)
valor5 = int(valor5)
valor2 = int(valor2)
valor1 = int(valor1)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(valor100))
print('{} nota(s) de R$ 50.00'.format(valor50))
print('{} nota(s) de R$ 20.00'.format(valor20))
print('{} nota(s) de R$ 10.00'.format(valor10))
print('{} nota(s) de R$ 5.00'.format(valor5))
print('{} nota(s) de R$ 2.00'.format(valor2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(valor1))
print('{} moeda(s) de R$ 0.50'.format(contador05))
print('{} moeda(s) de R$ 0.25'.format(contador025))
print('{} moeda(s) de R$ 0.10'.format(contador01))
print('{} moeda(s) de R$ 0.05'.format(contador005))
print('{} moeda(s) de R$ 0.01'.format(contador001))