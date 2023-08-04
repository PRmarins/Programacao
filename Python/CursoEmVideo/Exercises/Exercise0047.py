from time import sleep

n = int(input('Digite um número para a contagem regresiva: '))
for c in range (n, 0, -1):
    print (c)
    sleep(0.5)