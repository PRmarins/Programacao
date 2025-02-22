# TAG : tempo de jogo com minutos

dados = input().split()

hora_inicio = int(dados[0])
minuto_inicio = int(dados[1])

hora_termino = int(dados[2])
minuto_termino = int(dados[3])

if hora_inicio == hora_termino:
    if minuto_inicio < minuto_termino:
        hora_jogo = hora_termino - hora_inicio
        minuto_jogo = minuto_termino - minuto_inicio
    elif minuto_inicio > minuto_termino:
        hora_jogo = 23
        minuto_jogo = 60 - minuto_inicio + minuto_termino
    elif minuto_inicio == minuto_termino:
        hora_jogo = 24
        minuto_jogo = 0

elif hora_inicio < hora_termino:
    if minuto_inicio < minuto_termino:
        hora_jogo = hora_termino - hora_inicio
        minuto_jogo = minuto_termino - minuto_inicio
    elif minuto_inicio > minuto_termino:
        hora_jogo = hora_termino - hora_inicio - 1
        minuto_jogo = 60 - minuto_inicio + minuto_termino
    elif minuto_inicio == minuto_termino :
        hora_jogo = hora_termino - hora_inicio
        minuto_jogo = 0

elif hora_inicio > hora_termino:
    if minuto_inicio < minuto_termino:
        hora_jogo = 24 - hora_inicio + hora_termino
        minuto_jogo = minuto_termino - minuto_inicio
    elif minuto_inicio > minuto_termino:
        hora_jogo = 24 - hora_inicio + hora_termino - 1
        minuto_jogo = 60 - minuto_inicio + minuto_termino
    elif minuto_inicio == minuto_termino :
        hora_jogo = 24 - hora_inicio + hora_termino
        minuto_jogo = 0

print(f"O JOGO DUROU {hora_jogo} HORA(S) E {minuto_jogo} MINUTO(S)")