numeros = ('ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESEIS','DEZESETE','DEZOITO','DEZENOVE','VINTE')
usuario = int(input('Digite um número para mostra - lo por extenso: '))

while 20 < usuario or usuario < 0:
    print('Resposta inválida.')
    usuario = int(input('Digite um numero para mostrá - lo como ele é por extenso: '))
    
print(f'Você digitou o número {numeros[usuario]}.')