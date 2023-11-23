N = 1
moradores = list()
consumo = list()

while N != 0:
    N = int(input())
    for i in range (0,N):
        dados = input().split()
        for caracteres in dados:
            moradores.append(dados[0])
            consumo.append(dados[1])
        