from time import sleep
resposta = str(input('Você deseja fazer um imprestimo? '))
if resposta == ('SIM') or resposta == ('Sim') or resposta == ('sim'):
    print('Ok, espere um momento...')
    sleep(3)
    imprestimo = float(input('Quando você deseja receber de imprestimo? '))
    salario = float(input('Qual seu salário? '))
    tempo = int(input('Quantos meses você pretende pagar? '))
    print('Calculando...')
    sleep(3)
    valorMensal = imprestimo / tempo
    if valorMensal > ((salario * 30) / 100):
        print('Sinto muinto não podemos concluir seu imprestimo. Até mais.')
    else:
        print('Você terá que pagar R${:.2f} por mes.'.format(valorMensal))
        sleep(2)
        print('Tem certeza que deseja concluir o imprestimo?')
        resposta2 = str(input('Para confirmar digite "S" para negar digite "N".'))
        if resposta2 == ('S'):
            print('Muito bem, você terá seu imprestimo dentro de 48 horas.')
            sleep(1)
            print('Até mais.')
        if resposta2 == ('N'):
            print('Tudo bem, até a próxima.')
if resposta == ('NAO') or resposta == ('Nao') or resposta == ('nao') or resposta == ('NÃO') or resposta == ('Não') or resposta == ('não'):
    print('Ok, até mais.')
elif resposta != ('Nao') and resposta != ('nao') and resposta != ('NÃO') and resposta != ('Não') and resposta != ('não') and resposta != ('SIM') and resposta != ('Sim') and resposta != ('sim'):
    print('Resposta invalida. Até mais.')