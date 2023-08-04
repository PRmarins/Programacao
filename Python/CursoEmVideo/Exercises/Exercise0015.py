num = float(input('Digite um número: '))
num_int = int(num)
print('O valor digitado é {} e sua parte inteira é {}'.format(num, num_int))

# Forma de fazer ensinada pelo professor: 
import math
num_1 = float(input('Digite um número: '))
print('O valor digitado é {} e sua parte inteira é {}'.format(num_1, math.trunc(num_1)))
