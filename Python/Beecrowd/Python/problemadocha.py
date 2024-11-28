branco = "chá branco"
verde  = "chá verde"
preto  = "chá preto"
ervas  = "chá de ervas"

tipo_de_cha = str(input())

competidores = str(input(""))

competidores = list(competidores)

respostas_corretas = 0

for i in competidores:
    if i == tipo_de_cha:
        respostas_corretas += 1
print(respostas_corretas)
