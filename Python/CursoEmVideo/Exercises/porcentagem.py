from time import sleep

valorinicial = float(input("Valor aplicado/inicial: "))
valorfinal = float(input("Valor atual: "))
ganhos_porcentagem = ((valorfinal * 100) / valorinicial) - valorinicial
perda_porcentagem = ganhos_porcentagem * -1
print("Calculando...")
sleep(1.5)

if valorfinal > valorinicial:
    print (f"A porcentagem de ganhos foi de {ganhos_porcentagem:.2f}%.")

if valorfinal < valorinicial:
    print (f"A porcentagem de perda foi de {perda_porcentagem:.2f}%.")