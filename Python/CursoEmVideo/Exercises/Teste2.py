trabalho = 140000
receberWU = 160000


aluguel = 83000
afip = 5000
marianaUALA = 11000
agua = 6300
mp = 20000
brub = 1820
celular = 1500
uala = 3290
cartaobbva = 25000
marianamp = 27000

inv = 30000

dividatotal = aluguel + afip + marianaUALA + agua + mp + brub + inv + celular + uala + cartaobbva + marianamp
total_mes = (trabalho + receberWU - aluguel - afip - marianaUALA - agua - mp - brub - inv - marianamp
              - celular - uala - cartaobbva)

print(f"{total_mes} \n{dividatotal}")