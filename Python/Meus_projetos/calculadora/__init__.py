import Adicao
import Subtracao
import Multiplicacao
import Divisao

######################### imports ##########################

numero_soma = []
numero_subtracao = []


while True:

    print("Que operacao deseja fazer? Soma, Subtração, divisão, multiplicação:")
    operacao = input("").upper()
    if operacao == 'SOMA':
        while True:
            numero_soma.append(int(input("Digite um número: ")))
            continuar = str(input("Deseja continuar? Digite Sim ou Não: ")).upper()
            if continuar == "SIM":
                continue
            else:
                break
        resultado_adicao = Adicao.adicao(*numero_soma)
    if operacao == 'SUBTRACAO':
        while True:
            numero_subtracao.append(int(input("Digite um número: ")))
            continuar = str(input("Deseja continuar? Digite Sim ou Não: ")).upper()
            if continuar == "SIM":
                continue
            else:
                break
        resultado_subtracao = Subtracao.subtracao(*numero_subtracao)
    continuar_operacoes = input("Deseja continuar os calculos?").upper()
    if continuar_operacoes == "SIM":
        continue
    else:
        break

resultado = (resultado_subtracao) + (resultado_adicao)
        
print (resultado)
print("Até mais")