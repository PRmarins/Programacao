# TAG : FUNCAO

# Função é um bloco de código que só é executado quando chamado.
# Pode receber parâmetros e retornar valores.
# É definida pela palavra def.

def inicio ():
    print("Hello world")

inicio()

# Evita que eu tenha que fazer novamente o codigo, posso simplesmente chamar a função.

# Função com parâmetros
def soma (a, b):
    print(a + b)

soma(2, 3)

# Função com retorno e parâmetros
def soma (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    return a / b

print(soma(2, 3))
print(subtracao(2, 3))
print(multiplicacao(2, 3))
print(divisao(2, 3))


# Em uma função tudo que esta deopois do return, não é executado:

def diz_oi ():
    print('Estou sendo executado antes do retorno')
    return 'Oi'
    print('Estou sendo executado depois do retorno')

print(diz_oi()) # Se nota que o segundo print da linha 44 não será executado, pois a função foi encerrada na linha 43.
