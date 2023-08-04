km = float(input('Quantos km foram percorridos? '))
dia = int(input('Quantos dias o carro foi usado? '))
preco_km = 0.15
preco_dia = 60
preco_total = (preco_km * km) + (preco_dia * dia)
print ('O total do aluguel é: R${:.2f}'.format(preco_total))
