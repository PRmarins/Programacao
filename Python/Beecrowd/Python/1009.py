nome = str(input(""))
salario = float(input(""))
valorvenda = float(input(""))

valorreal = salario + ((valorvenda * 15) / 100)

print(f"TOTAL = R$ {valorreal:.2f}")