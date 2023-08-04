numero = 0
soma = 0
contador = -1
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número (999 para parar)'))
print('A soma dos termos digitados deu: {}. Você digitou {} números.'.format(soma,contador))