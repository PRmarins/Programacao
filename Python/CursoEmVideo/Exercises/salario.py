from time import sleep

salario = float(input('Valor total del salario: '))
salariopordia = salario / 30
salarioporhora = salariopordia / 8

sleep (1)

horaextra = str(input('Hiciste hora extra? [si] o [no] ')).upper() .strip()
if horaextra == 'SI':
    sleep (1)
    quantidadehoraextra = int(input('Quantidade de horas extras: '))
    acrecimohoraextra = quantidadehoraextra * salarioporhora
    sleep (1)
else:
    acrecimohoraextra = 0
    sleep (1)

dobleturno = str(input('Hiciste doble turno? [si] o [no] ')).upper() .strip()
if dobleturno == 'SI':
    sleep(1)
    quantidadedobleturno = (int(input('Cuantos doble turno hiciste? ')))
    acrecimodobleturno = salariopordia * quantidadedobleturno
    sleep (1)
else:
    acrecimodobleturno = 0
    sleep (1)

faltas = str(input('Tienes faltas? [si] o [no] ')) .upper() .strip()
if faltas == 'SI':
    sleep (1)
    numerodefaltas = int(input('Cuantas faltas tuviste? '))
    reducaofaltas = 0 - (salariopordia * numerodefaltas)
    sleep (1)
else:
    reducaofaltas = 0
    sleep (1)

inventario = str(input('Hiciste inventario? [si] o [no] ')).strip() .upper()
if inventario == 'SI':
    acrecimoinventario = salariopordia
    sleep(1)
else:
    acrecimoinventario = 0
    sleep(1)
    
feriados = str(input('Trabajaste en feriado? [si] o [no] ')).upper() .strip()
if feriados == 'SI':
    sleep (1)
    quantidadeferiados = int(input('Cuantos feriados tranajaste? '))
    acrecimoferiado = quantidadeferiados * salariopordia
    sleep (1)
else:
    acrecimoferiado = 0
    sleep(1)
    
    
salariototal = salario + acrecimohoraextra + reducaofaltas + acrecimodobleturno + acrecimoferiado + acrecimoinventario

salarionovopordia = salariototal / 30
salarionovoporhora = salarionovopordia / 8

novooriginal = str(input('''Deseas consultar el salario con acrecimos y decrecimos o el original?

[nuevo] o [original] ''')).strip() .upper()
if novooriginal == 'NUEVO':
    consultar = str(input('''Que desea consultar?

    opciones: [salario] o [salario por dia] o [salario por hora]''')).upper() .strip()
    x = 0
    if consultar == 'SALARIO':
            sleep (1)
            print(f'Su salario total del mes es ${salariototal:.2f} pesos.')
    elif consultar == 'SALARIO POR DIA':
            sleep (1)
            print(f'Su salario por dia es ${salarionovopordia:.2f} pesos.')
    elif consultar == 'SALARIO POR HORA':
            sleep (1)
            print(f'Su salario por hora es ${salarionovoporhora:.2f}.')
    else:
        while consultar != 'SALARIO' or 'SALARIO POR DIA' or 'SALARIO POR HORA':
            x += 1
            print('Opcion invalida')
            sleep (1)
            consultar = str(input('''Que desea consultar?

    opciones: [salario] o [salario por dia] o [salario por hora]''')).upper() .strip()
            if consultar == 'SALARIO':
                sleep (1)
                print(f'Su salario total del mes es ${salariototal:.2f} pesos.')
                sleep (1)
                print('Finalizando programa...')
                break
            elif consultar == 'SALARIO POR DIA':
                sleep (1)
                print(f'Su salario por dia es ${salarionovopordia:.2f} pesos.')
                sleep (1)
                print('Finalizando programa...')
                break
            elif consultar == 'SALARIO POR HORA':
                sleep (1)
                print(f'Su salario por hora es ${salarionovoporhora:.2f}.')
                sleep (1)
                print('Finalizando programa...')
                break
            if x == 5:
                print('Maximo de intentos.')
                sleep (1)
                print('Finalizando...')
                break
elif novooriginal == 'ORIGINAL':
    consultar = str(input('''Que desea consultar?

    opciones: [salario] o [salario por dia] o [salario por hora]''')).upper() .strip()
    x = 0
    if consultar == 'SALARIO':
            sleep (1)
            print(f'Su salario total del mes es ${salario:.2f} pesos.')
    elif consultar == 'SALARIO POR DIA':
            sleep (1)
            print(f'Su salario por dia es ${salariopordia:.2f} pesos.')
    elif consultar == 'SALARIO POR HORA':
            sleep (1)
            print(f'Su salario por hora es ${salarioporhora:.2f}.')
    else:
        while consultar != 'SALARIO' or 'SALARIO POR DIA' or 'SALARIO POR HORA':
            x += 1
            print('Opcion invalida')
            sleep (1)
            consultar = str(input('''Que desea consultar?

    opciones: [salario] o [salario por dia] o [salario por hora]''')).upper() .strip()
            if consultar == 'SALARIO':
                sleep (1)
                print(f'Su salario total del mes es ${salariototal:.2f} pesos.')
                sleep (1)
                print('Finalizando programa...')
                break
            elif consultar == 'SALARIO POR DIA':
                sleep (1)
                print(f'Su salario por dia es ${salariopordia:.2f} pesos.')
                sleep (1)
                print('Finalizando programa...')
                break
            elif consultar == 'SALARIO POR HORA':
                sleep (1)
                print(f'Su salario por hora es ${salarioporhora:.2f}.')
                sleep (1)
                print('Finalizando programa...')
                break
            if x == 5:
                print('Maximo de intentos.')
                sleep (1)
                print('Finalizando...')
                break