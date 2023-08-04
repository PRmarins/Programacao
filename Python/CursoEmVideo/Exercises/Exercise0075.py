listadeprecos = ('Lápis', 1.75,
                 'Borracha', 2.00,
                 'Caderno', 15.90,
                 'Estojo', 25.00,
                 'Transferidor', 4.20,
                 'Compasso', 9.99,
                 'Mochila', 120.32,
                 'Canetas', 22.30,
                 'Livros', 34.90)



for x in range (0,len(listadeprecos)):
    #printar os itens
    if x % 2 == 0:
        print(listadeprecos[x], end = ' ')
        inicio = 40
        espacos = len(listadeprecos[x])
        espacopreco = inicio - espacos
        print('*' * espacopreco, end =' ' )
    #printar os preços
    if x % 2 != 0:
        print(f'R$ {listadeprecos[x]:>6.2f}')
    x+=1
 