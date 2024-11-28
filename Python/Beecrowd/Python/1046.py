horas = input().split()

horas = [int(itens) for itens in horas]

if horas[1] < horas[0]:
    total_horas = 0
    horas_primeiro_dia = 24 - horas[0]
    horas_segundo_dia  = horas [1]
    total_horas = horas_primeiro_dia + horas_segundo_dia

elif horas[0] == horas[1]:
    total_horas = 24

else:
    total_horas = horas[1] - horas[0]

print(f"O JOGO DUROU {total_horas} HORA(S)")