number = int(input('Digite um número inteiro: '))
print('''Digite uma opção:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} Convertido para BINARIO é igual a {}.'.format(number, bin(number) [2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(number, oct(number) [2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(number, hex(number) [2:]))
else:
    print('Opção invalida.')