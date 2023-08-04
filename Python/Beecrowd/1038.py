dados = str(input("")).split()
item = int(dados[0])
qtd = int(dados[1])

if item == 1:
    item = 4.00
elif item == 2:
    item = 4.50
elif item == 3:
    item = 5.00
elif item == 4:
    item = 2.00
elif item == 5:
    item = 1.50

total = qtd * item

print (f"Total: R$ {total:.2f}")