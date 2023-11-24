numero_usuario = float(input("Numero: "))

####     LIMITAR A 2 CASAS DECIMAIS, PRIMEIRA FORMA     ####

#       ESSE METODO MULTIPLICA O NUMERO POR 100, TRASNFORMA ELE EM INTEIRO PARA ELIMINAR OS DEMAIS DECIAMIS
#  E DEPOIS DIVIDE POR 100 PARA QUE TENHA 2 CASAS DECIMAIS    #

novo_numero = "{:.2f}" .format(int(numero_usuario * 100) / 100)
novo_numero = float(novo_numero)
print(novo_numero)

####     SEGUNDA FORMA      ####

#       ESSE METODO VAI MULTIPLICAR O NUMERO POR 100, EM SEGUIDA VAI TRASNFORMAR O RESULTADO
#  NO NUMERO INTEIRO >= AO NUMERO MÃE E DEPOIS DIVIDE POR 100 USANDO A BIBLIOTECA MATH.FLOOR    #
import math
novo_numero_2 = math.floor(numero_usuario * 100) / 100

print(novo_numero_2)