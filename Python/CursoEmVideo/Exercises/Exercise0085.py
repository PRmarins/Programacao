list = []
par_list = []
impar_list = []
#      ADICIONANDO NÚMERO A LISTA E VERIFICANDO SE O NUMERO JA SE ENCONTRA NA LISTA     #
while True:
    num = input("Digite um número: ").split()
    if num in list:
        while True:
            num = input("O número já se encontra na lista, digite outro: ").split()
            if num not in list:
                break
    list.append(num[0])
    
#       PERGUNTANDO SE DESEJA ADICIONAR MAIS NÚMEROS        #

    continue_ = input("Desejá adicionar mais números? [S/N] ").strip().upper()
    
    if continue_ not in ("S","N"):
        
        while continue_ not in ("S", "N"):
            continue_ = input("Resposta inválida, responda com  [S/N]: ").strip().upper()
            if continue_ in ("S", "N"):
                break
    if continue_ == "N":
        break

#       CRIANDO UMA COPIA DA LISTA EM FORMATO INT E PONDO EM ORDEM CRESCENTE        #
n_list = [int(num) for num in list]
n_list.sort()

#       ADICIONANDO OS ELEMENTOS PARES E IMPARES A SUAS RESPECTIVAS LISTAS      #

for n in n_list:
    if n % 2 == 0:
        par_list.append(n)
    else:
        impar_list.append(n)

print (f"A lista em ordem crescente ficou: {n_list}")
print (f"A lista dos números pares ficou {par_list}")
print(f"A lista dos números impares ficou {impar_list}")