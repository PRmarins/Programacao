# TAG : Almento de salario

salario = float(input())

if salario <= 400.00 :
    novo_salario = salario + (salario * 0.15)
    incremento = novo_salario - salario
    incremento_porcentagem = "15 %"

elif 400.00 < salario <= 800.00 :
    novo_salario = salario + (salario * 0.12)
    incremento = novo_salario - salario
    incremento_porcentagem = "12 %"

elif 800.00 < salario <= 1200.00 :
    novo_salario = salario + (salario * 0.1)
    incremento = novo_salario - salario
    incremento_porcentagem = "10 %"

elif 1200.00 < salario <= 2000.00 :
    novo_salario = salario + (salario * 0.07)
    incremento = novo_salario - salario
    incremento_porcentagem = "7 %"

elif 2000.00 < salario :
    novo_salario = salario + (salario * 0.04)
    incremento = novo_salario - salario
    incremento_porcentagem = "4 %"

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {incremento:.2f}")
print(f"Em percentual: {incremento_porcentagem}")