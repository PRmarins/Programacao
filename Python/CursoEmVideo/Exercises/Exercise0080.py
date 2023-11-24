########   ESSA FORMA SO FUNCIONA PARA QUANDO NAO TENHA NUMEROS IGUAIS #######

lista_de_numeros = {(int(input("Digite o primeiro número: "))
                    (int(input("Digite um segundo número: ")))
                    (int(input("Digite um terceiro número: ")))
                    (int(input("Digite o quarto número: ")))
                    (int(input("Digite o quinto número: "))))}
maior_numero = max(lista_de_numeros)
menor_numero = min(lista_de_numeros)
P_maximo = lista_de_numeros.index(maior_numero) + 1
P_minimo = lista_de_numeros.index(menor_numero) + 1
print (f'O maior valor da lista é o valor "{maior_numero}" que se encontra na posição "{P_maximo}" da lista, e o menor valor da lista é o "{menor_numero} que se encontra na posição "{P_minimo}".')