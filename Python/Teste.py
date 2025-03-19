import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def quadrado_num(a):
    return a*a

for i in range(10):
    print(quadrado_num(random.choice(lista)))