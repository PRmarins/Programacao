from multiprocessing.util import LOGGER_NAME


name = str(input('Digite seu nome completo: ')).strip()
name1 = name.split()
fname = name1[0]
lname = name1[len(name1)-1]
print('Seu primeiro nome é {}.'.format(fname))
print('Seu último nome é {}.'.format(lname))