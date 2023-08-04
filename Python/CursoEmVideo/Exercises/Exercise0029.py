import time
print('Qual era a velocidade do veículo?')
velocidade = float(input(''))
print('Analisando...')
time.sleep(2)
multa = 7.00
valor_multa = multa * (velocidade - 80)
if velocidade>=81:
    print('Você foi multado!')
    print('O valor da multa é de R${:.2f}'.format(valor_multa))
if velocidade <= 80:
    print('Você náo foi multado.')
print('A velocidade limite era de 80km/h!')