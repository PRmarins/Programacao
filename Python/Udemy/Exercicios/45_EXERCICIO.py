# TAG : FUNCAO 

def quadrado(a):
    return a * a

while True:
    try:
        num: int = int(input("Número para calcular o quadrado: "))
        print(f"O quadrado de {num} = {quadrado(num)}")
        break  # Sai do loop se o número for válido
    except ValueError:
        print("Por favor, insira um número válido.")