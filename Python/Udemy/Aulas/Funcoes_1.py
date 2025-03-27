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

print(diz_oi()) # Se nota que o segundo print da linha 44 não será 
# executado, pois a função foi encerrada na linha 43.


# Se em um parametro eu der a ele um valor, ele se torna opcional.
# Exemplo: se eu definir uma função com 2 parametros e um deles eu der um valor, 
# a funcção vai poder ser executada sem erro.

def exponencial(numero, expoente = 2): # Quando eu dou um valor para o expoente, ele deixa da necessidade
# de ser exigido um, porém pode dar a ele um valor que será substituido no seu valor definido.
    return numero ** expoente

print(exponencial(4))
print(exponencial(4,3))

# Se eu tiver uma variavel fora da função, a função não vai conseguir acessar ela.
# Para isso eu preciso pedir ela na forma global dentro da função.

total = 0

def incrementa():
    global total # Caso eu não escreva essa linha, a função vai dar erro, pois ela não consegueria acessar
    # a variavel total que esta fora da função.


    total = total + 1
    return total

print(incrementa())

# Se eu quiser acessar uma variavel de fora da função, eu tambem posso passar ela como parametro.
# Assim a função vai conseguir acessar ela.

def incrementa(total):
    return total + 1

print(incrementa(41))
