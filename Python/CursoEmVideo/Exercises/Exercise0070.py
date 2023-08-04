print('-'*50)
print(' '*22, 'LOJA')
print('-'*50)
valortotal = 0
itemmaisde1000 = 0
maisbarato = 'none'
menorvalor = 0

produto = str(input('NOME PRODUTO: ')).strip()
valorproduto = float(input('VALOR DO PRODUTO: '))
valortotal += valorproduto
if valorproduto > 1000:
    itemmaisde1000 += 1
continuar = str(input('QUER ADICIONAR MAIS PRODUTOS? [ S ] ou [ N ]: ')).upper() .split() [0]
maisbarato = produto
menorvalor = valorproduto

while continuar == 'S':
    produto = str(input('NOME PRODUTO: ')).strip()
    valorproduto = float(input('VALOR DO PRODUTO: '))
    valortotal += valorproduto
    if valorproduto > 1000:
        itemmaisde1000 += 1
    if menorvalor > valorproduto:
        menorvalor = valorproduto
    continuar = str(input('QUER ADICIONAR MAIS PRODUTOS? [ S ] ou [ N ]: ')).upper() .split() [0]
    
    while continuar not in 'SN':
        print('RESPOSTA INVÁLIDA.')
        continuar = str(input('QUER ADICIONAR MAIS PRODUTOS? [ S ] ou [ N ]: '))
print('O total da compra foi R${:.2f}.'.format(valortotal))
if itemmaisde1000 > 1:
    print('Temos {} produtos acima de mil reais.'.format(itemmaisde1000))
elif itemmaisde1000 == 1:
    print('Temos 1 produto acima de mil reais')
else:
    print('Não temos produtos acima de mil reais.')
print('O produto mais barato foi o {} custando R${:.2f}.'.format(maisbarato,menorvalor))