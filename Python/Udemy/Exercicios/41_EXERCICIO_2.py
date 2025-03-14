# TAG : LISTA

A = [1, 0, 5, -2, -5, 7]

var = A[0] + A[1] + A[5]

print(var)

A[5] = 100

for i in range (0, len(A)):
    print(A[i])

"""	
Outra forma de escrever os valores:

print(*A, sep=", ")

ou

for i in A:
    print(i)
    
"""	