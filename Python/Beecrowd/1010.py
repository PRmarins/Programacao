valores = str(input("")).split()
valores2 = str(input("")).split()

codigo1 = int(valores[0])
numeropecas1 = int(valores[1])
valorpeca1 = float(valores[2])

codigo2 = int(valores2[0])
numeropecas2 = int(valores2[1])
valorpeca2 = float(valores2[2])

total = (numeropecas1*valorpeca1) + (valorpeca2*numeropecas2)

print(f"VALOR A PAGAR: R$ {total:.2f}")