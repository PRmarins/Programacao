from time import sleep
from sys import exit
Pessoas_pesadas = list()
Pessoas_leves = list()
counter = 0
counter_error = 0
sair = False

while not sair:
    Vnome = input("Nome: ")
    vpeso = float(input("Peso: "))
    counter += 1
    sair = str(input("Deseja adicionar mais dados? ")).strip()
    if sair.lower() in ['n','não','nao']:
        sair = True

    elif sair.lower() in ['s','sim']:
        sair = False
    else:
        counter_error += 1
        while sair.lower() not in ['s','sim','n','nao','não']:
            print("Resposta inválida, favor responder com 'sim' ou 'não: ")
            sair = str(input('Deseja adicionar mais dados? ')).strip()
            if sair.lower() in ['s','sim']:
                break
            elif sair.lower() in ['n','nao','não']:
                sair = True
                break
            counter_error += 1
            if counter_error == 5:
                print("você não forneceu uma resposta valida!")
                sleep(2)
                print("Encerrando programa...")
                sleep(3) 
                exit()
    if counter == 1:
         Pessoas_pesadas.append([[Vnome],[vpeso]])
         Pessoas_leves.append([[Vnome],[vpeso]])
    else:
        if Vnome not in Pessoas_leves:
            for i in Pessoas_leves:
                for ii in i[1]:
                    if ii >= vpeso:
                        Pessoas_leves[0][0].append(Vnome)
                        Pessoas_leves[0][1].append(vpeso)
                        break

        if Vnome not in Pessoas_pesadas:
            for i in Pessoas_pesadas:
                for ii in i[1]:
                    if vpeso >= ii:
                        Pessoas_pesadas[0][0].append(Vnome)
                        Pessoas_pesadas[0][1].append(vpeso)
                        break

print("As pessoas mais pesadas são:")
for i in Pessoas_pesadas:
    print(i[0])
print("As pessoas mais leves são: ")
for i in Pessoas_leves:
    print(i[0])