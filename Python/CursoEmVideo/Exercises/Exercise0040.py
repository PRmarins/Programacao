from time import sleep

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
medianota = (nota1 + nota2) /2
print('Analizando...')
sleep (2)
if medianota < 5:
    print('Você tem média {:.2f}, portanto está reprovado.'.format(medianota))
if medianota >= 5 and medianota <= 6.99:
    print('Você tem média {:.2f}, portanto está em recuperação.'.format(medianota))
if medianota >= 7:
    print('Você tem média {:.2f}, portanto está aprovado.'.format(medianota))