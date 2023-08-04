cato = float(input('Valor do cateto oposto: '))
cata = float(input('Valor do outro adjacente: '))
hipotenusa = ((cato ** 2) + (cata ** 2)) ** 0.5
print('Se o valor de um cateto é {} e do outro é {}, ovalor da ipotenusa será: {:.2f}'.format(cata, cato, hipotenusa))

# Forma importando biblioteca:

import math
cato = float(input('Coloque o valor do cateto oposto: '))
cata = float(input('Coloque o valor do cateto adjacente: '))
hipotenusa = math.hypot(cato, cata)
print('A hipotenusa será: {:.2f}'.format(hipotenusa))