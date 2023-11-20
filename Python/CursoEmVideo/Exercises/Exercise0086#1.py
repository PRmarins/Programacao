expressao = input("Digite a sua expressão: ")

fechado = 0
aberto = 0

pfechado = []

analisador = 0

for n in expressao:
    if n == '(':
        analisador = analisador + 1
        aberto = aberto + 1
    elif n == ')':
        fechado = fechado + 1
        analisador = analisador - 1
    if analisador < 0:
        if fechado in pfechado:
            pfechado.append(fechado)
            pfechado.pop()
        else:
            pfechado.append(fechado)
if analisador == 0:
    print("Não foram encontrados erros de parentesis em sua expressão.")
else:
    print("Há algo de errado em sua expressão por volta do/s parentesis fechando/s numero/s",end= ' ')
    for n in pfechado:
        print(f"[{n}]",end = " ")
    print(f"\nSua expressão teve {aberto} parentesis abertos e {fechado} parentesis fechados.")
