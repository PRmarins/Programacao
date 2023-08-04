print('Qual a distancia da sua viagem em KM?')
distancia = float(input(''))
valormenos200km = distancia * 0.50
valormais200km = distancia * 0.45
if distancia <= 200:
    print('O valor da sua viagem será de R${:.2f}'.format(valormenos200km))
print('O valor da sua viagem será de R${:.2f}'.format(valormais200km))