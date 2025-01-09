# TAG : CONJUNTOS , SET , DICIONARIO

# Os conjuntos são chamados de sets na programação
'''
- Não possuem valores duplicados
- Não possuem valores ordenados
- Os Sets não são indexados

Bons para utilizar quando queremos armaZenar itens sem preocupar com ordem,
itens duplicados, chave e valores

São usados para referenciar os Sets as chaves {}

-> Diferença entre Sets e Dicionarios:
    - O Dicionario tem chave e valor
    - O Set tem apenas o valor

'''

Sets = set({1,4,2,1,4,5,2,6,3,3,2,3,4,5,1,2}) # Ele irá mostrar os items em ordem crescente sem se repetir #

print(type(Sets))
print(Sets)
print(len(Sets))