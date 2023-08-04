Num = int(input(''))
N = Num
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador5 = 0
contador2 = 0
contador1 = 0
while N >= 100:
    C = N - 100
    N = C
    contador100 += 1
while N >= 50:
    C = N - 50
    N = C
    contador50 += 1
while N >= 20:
    C = N - 20
    N = C
    contador20 += 1
while N >= 10:
    C = N -10
    N = C
    contador10 += 1
while N >= 5:
    C = N - 5
    N = C
    contador5 += 1
while N >= 2:
    C = N - 2
    N = C
    contador2 += 1
while N >= 1:
    C = N - 1
    N = C
    contador1 += 1    
print(Num)
print('{} nota(s) de R$ 100,00'.format(contador100))
print('{} nota(s) de R$ 50,00'.format(contador50))
print('{} nota(s) de R$ 20,00'.format(contador20))
print('{} nota(s) de R$ 10,00'.format(contador10))
print('{} nota(s) de R$ 5,00'.format(contador5))
print('{} nota(s) de R$ 2,00'.format(contador2))
print('{} nota(s) de R$ 1,00'.format(contador1))