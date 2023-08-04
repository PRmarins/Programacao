from datetime import date

maiordeidade = 0
menordeidade = 0
for pessoas in range (1, 8):
    pessoa = int(input('Digite o ano em que nasceu: '))
    if date.today().year - pessoa >= 18:
        maiordeidade += 1
    else:
        menordeidade += 1
if maiordeidade > 1 and menordeidade > 1:
    print('Há {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maiordeidade, menordeidade))
elif maiordeidade == 1 and menordeidade >1:
    print('Há apenas {} pessoa maior de idade e {} pessoas menores de idade.'.format(maiordeidade, menordeidade))
elif maiordeidade > 1 and menordeidade == 1:
    print('Há {} pessoas maiores de idade e apenas {} pessoa menor de idade'.format(maiordeidade, menordeidade))