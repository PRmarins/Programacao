CONTINUAR = 'G'
soma = 0
contador = 0
while CONTINUAR not in 'N':
    NUMERO = int(input('Digite um número: '))
    PERGUNTA = str(input('Quer continuar? [S/N]')).strip() .upper()
    CONTINUAR = PERGUNTA[0]
    soma += NUMERO
    contador += 1
    while CONTINUAR not in 'SN':
        CONTINUAR = str(input('Resposta inválida, Digite "S" ou "N":[S/N] ')).strip() .upper()
media = soma / contador
print('Você digitou {} e a média foi {:.2f}.'.format(contador,media))