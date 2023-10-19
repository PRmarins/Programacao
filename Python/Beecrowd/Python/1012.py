variaveis = str(input()).strip().split()

A = float(variaveis[0])
B = float(variaveis[1])
C = float(variaveis[2])

pi = 3.14159

# Triangulo #
Atriangulo = (A * C) / 2

# Circulo #
Acirculo = pi * (C ** 2)

# Trapezio #
Atrapezio = (A + B) * C / 2

# Quadrado #
Aquadrado = B * B

# Retangulo #
Aretangulo = A * B

print(f"TRIANGULO: {Atriangulo:.3f}")
print(f"CIRCULO: {Acirculo:.3f}")
print(f"TRAPEZIO: {Atrapezio:.3f}")
print(f"QUADRADO: {Aquadrado:.3f}")
print(f"RETANGULO: {Aretangulo:.3f}")