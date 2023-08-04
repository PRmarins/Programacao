from time import sleep

print('Olá, eu vou te pedir 3 medidas e vamos ver se essas medidas podem formar um triangulo ou náo. Caso sim, também irei dizer a classificação dele.')
sleep (2)
lado1=int(input('Digite uma medida: '))
lado2=int(input('Digite a segunda medida: '))
lado3=int(input('Digite a terceira medida: '))
print('Analisando...')
sleep (2)
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('Se pode formar um triângulo com essas medidas.')
    if lado1 == lado2 == lado3:
        print('se forma um triângulo equilatero.')
    elif lado1 == lado2 != lado3:
        print('Se forma um triângulo isósceles.')
    else:
        print('Se forma um triângulo escaleno.')
else:
    print('Essas medidas não podem formar um triângulo.')