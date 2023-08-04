produto=float(input('Digite o preço do produto: '))
print('Como deseja pagar sua compra?')
print('A VISTA PRESSIONE 1')
print('PARCELADO PRESSIONE 2')
resposta=int(input('Digite a resposta: '))
if resposta == 1:
    print('Você deseja pagar em dinheiro, cheque ou cartão?')
    print('DINHEIRO/CHEQUE PRESSIONE 1')
    print('CARTÃO DIGITE 2')
    resposta1=int(input('Digite como deseja pagar:'))
    if resposta1 == 1:
        resposta1 = (resposta1 * 10) / 100
        print('Sua compra vai custar R${:.2f}.'.format(resposta1))
    else:
        resposta1 = (resposta1 * 5) / 100
        print('Sua compra vai custar R${:.2f}.'.format(resposta1))
else:
    print('Deseja parcelar em quantas vezes (máximo 12 vezes)?')
    resposta2=int(input('Digite a quantidade de parcelas que deseja: '))
    if resposta2 == 2:
        parcela2vzs = resposta / 2
        print('Sua Compra será parcelada em 2 parcelas de R${:.2f}.'.format(parcela2vzs))
    elif resposta2 >= 3 and resposta2 <= 12:
        valortotal = produto + (produto * 20) / 100
        parcela3a12vzs = (produto + (produto * 20) / 100) / resposta2
        print('Sua compra será parcelada em {} parcelas de R${:.2f}, o produto final custará R${:.2f}.'.format(resposta2, parcela3a12vzs, valortotal))