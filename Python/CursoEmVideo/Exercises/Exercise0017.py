import math

ang = float(input('Digite um ângulo: '))
anggr = math.radians(ang)
seno = math.sin(anggr)
cos = math.cos(anggr)
tang = math.tan(anggr)
print('O seno de {} é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}.'.format(ang, seno, cos, tang))
