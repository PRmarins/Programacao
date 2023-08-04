pessoapesomaior = 0
pessoapesomenor = 0
for pessoas in range (1, 6):
    peso = float(input('Qual o peso da {}® pessoa? '.format(pessoas)))
    if pessoas == 1:
        pessoapesomaior = peso
        pessoapesomenor = peso
    else:
        if peso > pessoapesomaior:
            pessoapesomaior = peso
        elif peso < pessoapesomenor:
            pessoapesomenor = peso
print ('A pessoa menos pesada pesa {:.2f}Kg.'.format(pessoapesomenor))
print ('A pessoa mais pesada pesa {:.2f}Kg.'.format(pessoapesomaior))