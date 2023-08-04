notas = str(input("")).split()

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

n1 = n1 * 2
n2 = n2 * 3
n3 = n3 * 4

media = (n1 + n2 + n3 + n4) / 10

print (f"Media: {media:.1f}")

if media >= 7:
    print ("Aluno aprovado.")

elif 5 <= media < 7:
    print ("Aluno em exame.")
    nota_exame = float(input(""))
    media = (media + nota_exame) / 2
    print (f"Nota do exame: {nota_exame}")
    if media < 5:
        print (f"Aluno reprovado.\nMedia final: {media:.1f}")
        
    else:
        print (f"Aluno aprovado.\nMedia final: {media:.1f}")
else:
    print ("Aluno reprovado.")