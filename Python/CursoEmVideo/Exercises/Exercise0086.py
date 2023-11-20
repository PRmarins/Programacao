Expressao = input("DIgite a expressão: ")

pilha = []

for n in Expressao:
    if n == '(':
        pilha.append('(')
    
    elif n == ')':
        if len(Expressao) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print("Sua expressão está correta.")
else:
    print("Há algo de errado na sua expressão.")