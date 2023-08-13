coordenadas = input("").split()

coordenada_X = float(coordenadas[0])
coordenada_Y = float(coordenadas[1])

quadrante = "Origem"

if coordenada_X == 0 and coordenada_Y == 0:
    quadrante = "Origem"

if coordenada_X > 0 and coordenada_Y == 0 or coordenada_X < 0 and coordenada_Y == 0:
    quadrante = "Eixo X"
    
if coordenada_X == 0 and coordenada_Y < 0 or coordenada_X == 0 and coordenada_Y > 0:
    quadrante = "Eixo Y"

if coordenada_X > 0 and coordenada_Y > 0:
    quadrante = "Q1"
    
if coordenada_X < 0 and coordenada_Y > 0:
    quadrante = "Q2"

if coordenada_X < 0 and coordenada_Y < 0:
    quadrante = "Q3"

if coordenada_X > 0 and coordenada_Y < 0:
    quadrante = "Q4"
    
print (quadrante)