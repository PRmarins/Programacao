def divisao (*args):
    dividir = args[0]
    for i in args[1:]:
        dividir /= i
    return dividir
