from time import sleep

number = int(input('Qual sua idade?'))
if  0 < number < 12:
    print('Você é uma criança.')
elif 12 <= number <= 17:
    print('Você é adolescente.')
elif 17 < number <= 35:
    print('Você é um adulto.')
elif 35 < number <= 42:
    print('Você ta chegando no meio da vida.')
elif 42 < number <= 46:
    print('Você está na metade da vida.')
elif 46 < number < 52:
    print('Você ta ficando velho.')
elif 60 < number <= 110 :
    print('Você ta velho')
elif 0 >= number or number > 110:
    print('Huuuum...')
    sleep(2)
    print('Acho que você está mentindo.')
    resposta = str(input('Você realmente tem essa idade?? '))
    if resposta == ('sim') or resposta == ('Sim') or resposta == ('SIM'):
        print('Caramba, nunca conheci alguem com essa idade.')
    if resposta == ('Não') or resposta == ('NÃO') or resposta == ('não') or resposta == ('nao') or resposta == ('não') or resposta == ('Nao') or resposta == ('NAO'):
        resposta2 = int(input('AH bom, que idade então você realmente tem? '))
        if resposta2 < 12:
            print('Você é uma criança.')
        elif resposta2 == 0:
            print('Impossivel meu amigo.')
        elif 12 <= resposta2 <= 17:
            print('Você é adolescente.')
        elif 17 < resposta2 <= 35:
            print('Você é um adulto.')
        elif 35 < resposta2 <= 42:
            print('Você ta chegando no meio da vida.')
        elif 42 < resposta2 <= 46:
            print('Você está na metade da vida.')
        elif 46 < resposta2 < 52:
            print('Você ta ficando velho.')
        else:
            print('Você ta velho')
    else:
        print('Me cansei de conversar. até mais.')