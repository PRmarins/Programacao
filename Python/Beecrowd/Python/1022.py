testes = int(input())
for e in range (1,testes + 1):
    dados = str(input()).split()

    if len(dados) > 1:
        numeros = []

        sinais = []

        for i in range (0,len(dados)):
            if i % 2 == 0:
                numeros.append(dados[i])
            else:
                sinais.append(dados[i])
        n1 = int(numeros[0])
        d1 = int(numeros[1])
        n2 = int(numeros[2])
        d2 = int(numeros[3])

        s1 = str(sinais[1])

        if s1 == "+":
            numerador = (n1 * d2) + (n2 * d1)
            denominador  = (d1 * d2)
            operacao = ((n1 * d2) + (n2 * d1)) / (d1 * d2)

        elif s1 == "-":
            numerador = (n1 * d2) - (n2*d1)
            denominador = (d1 * d2)
            operacao = ((n1 * d2) - (n2*d1)) / (d1 * d2)

        elif s1 == "*":
            numerador = (n1 * n2)
            denominador = (d2 * d1)
            operacao = (n1 * n2) / (d2 * d1)

        elif s1 == "/":
            numerador = (n1 * d2)
            denominador = (n2 * d1)
            operacao = (n1 * d2) / (n2 * d1)

        if numerador > denominador:
            big = numerador
        else:
            big = denominador

        while True:

            if denominador % big == 0 and numerador % big == 0:
                numeradorN = int(numerador / big)
                denominadorN = int(denominador / big)
                break
            else:
                big = big - 1

        print(f"{numerador}/{denominador} = {numeradorN}/{denominadorN}")