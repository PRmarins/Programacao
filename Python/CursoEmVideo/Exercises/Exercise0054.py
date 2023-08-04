frase = str(input('Digite uma frase ou palavra: ')) .strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso =''
for letras in range (len(junto) - 1, -1, -1):
    inverso += junto[letras]
print(junto, inverso)