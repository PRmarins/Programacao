from time import sleep
n = int(input('Digite um número que te mostrarei todos o pares até ele: '))
for numero in range (0, n + 2, 2):
    print (numero)
    sleep(0.5)
print ('Acabou')